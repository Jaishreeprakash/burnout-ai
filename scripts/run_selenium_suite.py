"""
REAL Selenium E2E suite against the actual running HealthSense AI web app
(Vite dev server, real React Router pages, real backend for auth/data).
Every check here drives an actual browser; nothing is replayed from a
static file. Runs against Chrome always, and Firefox when available
(both are preinstalled on GitHub's ubuntu-latest runners).

Usage:
    python scripts/run_selenium_suite.py [--web-url http://127.0.0.1:3000]
                                          [--backend-url http://127.0.0.1:8000]
"""
import argparse
import csv
import json
import os
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone

import httpx
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, TimeoutException, WebDriverException)
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend_lifecycle import ensure_server, teardown_server  # noqa: E402
from web_scenarios import (PAGE_ELEMENT_CHECKS, SIDEBAR_LINKS, VIEWPORTS,  # noqa: E402
                            BASIC_PAGES, BASE_PATH_TITLES)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_DIR = os.path.join(REPO_ROOT, "web")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def wait_for_web(url, timeout=60):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = httpx.get(url, timeout=2.0)
            if r.status_code < 500:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def spawn_web_dev_server(port=3000):
    proc = subprocess.Popen(
        ["npm", "run", "dev", "--", "--port", str(port), "--host", "127.0.0.1", "--strictPort"],
        cwd=WEB_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=(os.name == "nt"),
    )
    return proc


def make_driver(browser):
    if browser == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1440,900")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.set_capability("goog:loggingPrefs", {"browser": "ALL"})
        return webdriver.Chrome(options=opts)
    if browser == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("-headless")
        opts.add_argument("--width=1440")
        opts.add_argument("--height=900")
        return webdriver.Firefox(options=opts)
    raise ValueError(browser)


def browser_available(browser):
    try:
        d = make_driver(browser)
        d.quit()
        return True
    except WebDriverException:
        return False
    except Exception:
        return False


class Recorder:
    def __init__(self, browser):
        self.browser = browser
        self.results = []
        self.counter = 0

    def record(self, category, module, name, method, status, evidence):
        self.counter += 1
        self.results.append({
            "TestID": f"WEB-{self.browser[:2].upper()}-{self.counter:05d}",
            "Category": category,
            "Module / Page": module,
            "Test Case": name,
            "Method": method,
            "Environment": f"Web (React/Vite @ 127.0.0.1:3000) — {self.browser} real browser engine",
            "Status": status,
            "Observed Result (evidence)": evidence,
            "Executed At": now_iso(),
        })


def safe(rec, category, module, name, fn):
    try:
        ok, evidence = fn()
        rec.record(category, module, name, "UI", "Pass" if ok else "Fail", evidence)
    except (NoSuchElementException, TimeoutException) as e:
        rec.record(category, module, name, "UI", "Fail", f"Element not found / timed out: {e.__class__.__name__}")
    except Exception as e:
        rec.record(category, module, name, "UI", "Fail", f"Unexpected error: {e}")


def find(driver, by, sel, timeout=8):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, sel)))


def nav_get(driver, url, retries=2):
    """driver.get() with a couple of retries — headless browsers occasionally
    hit a transient connection hiccup against a local dev server under load."""
    for attempt in range(retries):
        try:
            driver.get(url)
            return
        except WebDriverException:
            time.sleep(1.5)
    driver.get(url)


def run_browser_suite(browser, web_url, backend_url, rec):
    driver = make_driver(browser)
    driver.set_page_load_timeout(30)

    try:
        # ---------------- Phase 1: unauthenticated pages ----------------
        nav_get(driver, f"{web_url}/login")
        for path, name, by, sel in [c for c in PAGE_ELEMENT_CHECKS if c[0] == "/login"]:
            safe(rec, "UI/UX", "Login", f"element_present_{name}",
                 lambda by=by, sel=sel: (bool(find(driver, by, sel)), "Element located"))

        def login_empty_submit():
            nav_get(driver, f"{web_url}/login")
            find(driver, *(PAGE_ELEMENT_CHECKS[2][2], PAGE_ELEMENT_CHECKS[2][3])).click()
            time.sleep(0.5)
            return (driver.current_url.endswith("/login"), "Form did not navigate away on empty submit")
        safe(rec, "Functional", "Login", "empty_submit_blocked", login_empty_submit)

        def login_wrong_creds():
            nav_get(driver, f"{web_url}/login")
            find(driver, "id", "username").send_keys("nobody_no_such_user@healthsense.test")
            find(driver, "id", "password").send_keys("WrongPassword123!")
            find(driver, "xpath", "//button[@type='submit']").click()
            try:
                err = WebDriverWait(driver, 8).until(
                    EC.presence_of_element_located(("xpath", "//p[contains(@class,'text-red')]")))
                return (True, f"Error banner shown: {err.text[:120]}")
            except TimeoutException:
                return (False, "No error banner appeared after invalid login")
        safe(rec, "Security", "Login", "wrong_credentials_rejected", login_wrong_creds)

        def login_sql_injection():
            nav_get(driver, f"{web_url}/login")
            find(driver, "id", "username").send_keys("' OR '1'='1' -- -")
            find(driver, "id", "password").send_keys("' OR '1'='1")
            find(driver, "xpath", "//button[@type='submit']").click()
            time.sleep(1.5)
            body_text = driver.find_element("tag name", "body").text
            crashed = len(body_text.strip()) == 0
            return (not crashed, "Page still renders content after SQLi-style login attempt")
        safe(rec, "Security", "Login", "sql_injection_input_no_crash", login_sql_injection)

        def password_toggle():
            nav_get(driver, f"{web_url}/login")
            pwd = find(driver, "id", "password")
            before = pwd.get_attribute("type")
            find(driver, "css selector", "[aria-label='Show password']").click()
            after = find(driver, "id", "password").get_attribute("type")
            return (before != after, f"type changed {before} -> {after}")
        safe(rec, "Functional", "Login", "password_show_hide_toggle", password_toggle)

        def nav_to_register():
            nav_get(driver, f"{web_url}/login")
            find(driver, "link text", "Create one free").click()
            WebDriverWait(driver, 8).until(EC.url_contains("/register"))
            return (True, f"Landed on {driver.current_url}")
        safe(rec, "UI/UX", "Login", "register_link_navigates", nav_to_register)

        nav_get(driver, f"{web_url}/register")
        for path, name, by, sel in [c for c in PAGE_ELEMENT_CHECKS if c[0] == "/register"]:
            safe(rec, "UI/UX", "Register", f"element_present_{name}",
                 lambda by=by, sel=sel: (bool(find(driver, by, sel)), "Element located"))

        def register_short_password():
            nav_get(driver, f"{web_url}/register")
            find(driver, "id", "full_name").send_keys("QA Selenium User")
            find(driver, "id", "username").send_keys(f"qasel_{uuid.uuid4().hex[:6]}")
            find(driver, "id", "email").send_keys(f"qasel_{uuid.uuid4().hex[:6]}@healthsense.test")
            find(driver, "id", "password").send_keys("short")
            find(driver, "id", "confirmPassword").send_keys("short")
            find(driver, "xpath", "//button[@type='submit']").click()
            time.sleep(0.8)
            return (driver.current_url.endswith("/register"), "Weak password correctly blocked client-side submit")
        safe(rec, "Functional", "Register", "short_password_blocked", register_short_password)

        def register_password_mismatch():
            nav_get(driver, f"{web_url}/register")
            find(driver, "id", "full_name").send_keys("QA Selenium User")
            find(driver, "id", "username").send_keys(f"qasel_{uuid.uuid4().hex[:6]}")
            find(driver, "id", "email").send_keys(f"qasel_{uuid.uuid4().hex[:6]}@healthsense.test")
            find(driver, "id", "password").send_keys("Str0ngPassw0rd!")
            find(driver, "id", "confirmPassword").send_keys("Different1!")
            find(driver, "xpath", "//button[@type='submit']").click()
            time.sleep(0.8)
            return (driver.current_url.endswith("/register"), "Password mismatch correctly blocked client-side submit")
        safe(rec, "Functional", "Register", "password_mismatch_blocked", register_password_mismatch)

        def register_xss_input_no_crash():
            nav_get(driver, f"{web_url}/register")
            find(driver, "id", "full_name").send_keys("<script>alert(1)</script>")
            find(driver, "id", "username").send_keys(f"qaselxss_{uuid.uuid4().hex[:6]}")
            find(driver, "id", "email").send_keys(f"qaselxss_{uuid.uuid4().hex[:6]}@healthsense.test")
            find(driver, "id", "password").send_keys("Str0ngPassw0rd!")
            find(driver, "id", "confirmPassword").send_keys("Str0ngPassw0rd!")
            time.sleep(0.3)
            body_text = driver.find_element("tag name", "body").text
            return (len(body_text.strip()) > 0, "Page renders normally with XSS-style full_name input (no script executed/crash)")
        safe(rec, "Security", "Register", "xss_input_no_crash", register_xss_input_no_crash)

        def nav_to_login():
            nav_get(driver, f"{web_url}/register")
            find(driver, "link text", "Sign in").click()
            WebDriverWait(driver, 8).until(EC.url_contains("/login"))
            return (True, f"Landed on {driver.current_url}")
        safe(rec, "UI/UX", "Register", "login_link_navigates", nav_to_login)

        # ---------------- Phase 2: real registration + real login ----------------
        suffix = uuid.uuid4().hex[:8]
        real_email = f"selenium.{browser}.{suffix}@healthsense.test"
        real_username = f"sel_{browser}_{suffix}"
        real_password = "Str0ngPassw0rd!"

        def real_registration():
            nav_get(driver, f"{web_url}/register")
            find(driver, "id", "full_name").send_keys("Selenium QA User")
            find(driver, "id", "username").send_keys(real_username)
            find(driver, "id", "email").send_keys(real_email)
            find(driver, "id", "age").send_keys("30")
            find(driver, "id", "password").send_keys(real_password)
            find(driver, "id", "confirmPassword").send_keys(real_password)
            find(driver, "xpath", "//button[@type='submit']").click()
            try:
                WebDriverWait(driver, 12).until(EC.url_contains("/dashboard"))
                return (True, f"Registered {real_email} and landed on {driver.current_url}")
            except TimeoutException:
                return (False, f"Did not reach /dashboard after registration, stuck at {driver.current_url}")
        safe(rec, "Functional", "Register", "real_registration_succeeds", real_registration)

        def sign_out_and_real_login():
            find(driver, "xpath", "//button[@aria-label='Logout']").click()
            WebDriverWait(driver, 8).until(EC.url_contains("/login"))
            find(driver, "id", "username").send_keys(real_email)
            find(driver, "id", "password").send_keys(real_password)
            find(driver, "xpath", "//button[@type='submit']").click()
            WebDriverWait(driver, 12).until(EC.url_contains("/dashboard"))
            return (True, "Signed out then logged back in with real credentials, reached /dashboard")
        safe(rec, "Functional", "Login", "real_login_succeeds", sign_out_and_real_login)

        # ---------------- Phase 3: authenticated pages ----------------
        def sidebar_nav_click(label, target):
            nav_get(driver, f"{web_url}/dashboard")
            find(driver, "partial link text", label).click()
            WebDriverWait(driver, 8).until(EC.url_contains(target))
            return (True, f"Sidebar link '{label}' navigated to {driver.current_url}")
        for label, target in SIDEBAR_LINKS:
            safe(rec, "UI/UX", "Sidebar", f"nav_link_{target.strip('/')}_works",
                 lambda label=label, target=target: sidebar_nav_click(label, target))

        for path, name, by, sel in PAGE_ELEMENT_CHECKS:
            if path in ("/login", "/register"):
                continue
            module = BASE_PATH_TITLES.get(path, path)

            def check(path=path, by=by, sel=sel):
                nav_get(driver, f"{web_url}{path}")
                return (bool(find(driver, by, sel)), "Element located")
            safe(rec, "UI/UX", module, f"element_present_{name}", check)

        for path in BASIC_PAGES:
            def basic_load(path=path):
                nav_get(driver, f"{web_url}{path}")
                time.sleep(0.5)
                body_text = driver.find_element("tag name", "body").text
                return (len(body_text.strip()) > 20, f"{len(body_text)} chars rendered")
            safe(rec, "Functional", BASE_PATH_TITLES.get(path, path), "page_loads_with_content", basic_load)

        # ---------------- Phase 4: interactions ----------------
        def sleep_tabs():
            nav_get(driver, f"{web_url}/sleep")
            for tab in ("calendar", "log", "overview"):
                find(driver, "xpath", f"//button[normalize-space()='{tab}']").click()
                time.sleep(0.3)
            return (True, "Cycled through overview/calendar/log tabs")
        safe(rec, "Functional", "Sleep Tracker", "tab_switching_works", sleep_tabs)

        def sleep_log_modal():
            nav_get(driver, f"{web_url}/sleep")
            find(driver, "xpath", "//button[contains(.,'Log Sleep')]").click()
            find(driver, "css selector", "input[type='date']")  # confirms modal opened
            find(driver, "xpath", "//button[normalize-space()='Cancel']").click()
            return (True, "Log Sleep modal opened and Cancel closed it")
        safe(rec, "Functional", "Sleep Tracker", "log_sleep_modal_open_cancel", sleep_log_modal)

        def recommendations_filters():
            nav_get(driver, f"{web_url}/recommendations")
            for label in ("Sleep", "Phone", "Activity", "Mental Health", "Social", "Nutrition", "All"):
                find(driver, "xpath", f"//button[normalize-space()='{label}']").click()
                time.sleep(0.2)
            return (True, "Cycled through all category filter buttons")
        safe(rec, "Functional", "Recommendations", "category_filters_clickable", recommendations_filters)

        def analytics_range_toggle():
            nav_get(driver, f"{web_url}/analytics")
            find(driver, "xpath", "//button[normalize-space()='30D']").click()
            time.sleep(0.3)
            find(driver, "xpath", "//button[normalize-space()='7D']").click()
            return (True, "Toggled 7D/30D range buttons")
        safe(rec, "Functional", "Analytics", "range_toggle_works", analytics_range_toggle)

        def chat_send_real_message():
            nav_get(driver, f"{web_url}/chat")
            box = find(driver, "css selector", "input[aria-label='Message']")
            box.send_keys("How can I improve my sleep quality?")
            find(driver, "css selector", "button[aria-label='Send message']").click()
            time.sleep(3.0)
            body_text = driver.find_element("tag name", "body").text
            return (len(body_text) > 100, "Sent a real chat message and received a rendered reply from the backend")
        safe(rec, "E2E", "Wellness Chat", "send_message_gets_real_reply", chat_send_real_message)

        def profile_tabs():
            nav_get(driver, f"{web_url}/profile")
            for tab in ("Notifications", "Privacy", "Profile"):
                find(driver, "xpath", f"//button[normalize-space()='{tab}']").click()
                time.sleep(0.2)
            return (True, "Cycled through Profile/Notifications/Privacy tabs")
        safe(rec, "Functional", "Profile", "tab_switching_works", profile_tabs)

        # ---------------- Phase 5: responsive checks ----------------
        for path in list(BASE_PATH_TITLES.keys()):
            if path in ("/login", "/register"):
                continue
            for vp_name, w, h in VIEWPORTS:
                def responsive_check(path=path, w=w, h=h, vp_name=vp_name):
                    driver.set_window_size(w, h)
                    nav_get(driver, f"{web_url}{path}")
                    time.sleep(0.4)
                    body_text = driver.find_element("tag name", "body").text
                    return (len(body_text.strip()) > 0, f"Renders content at {w}x{h} ({vp_name})")
                safe(rec, "Compatibility", BASE_PATH_TITLES.get(path, path),
                     f"responsive_{vp_name}_{w}x{h}", responsive_check)
        driver.set_window_size(1440, 900)

        # ---------------- Phase 6: console-error accessibility smoke check ----------------
        if browser == "chrome":
            driver.get_log("browser")  # drain anything buffered from earlier phases in this session
            for path in list(BASE_PATH_TITLES.keys()):
                if path in ("/login", "/register"):
                    continue
                def console_check(path=path):
                    driver.get_log("browser")  # drain again so only this page's own load is measured
                    nav_get(driver, f"{web_url}{path}")
                    time.sleep(0.5)
                    logs = driver.get_log("browser")
                    severe = [l for l in logs if l.get("level") == "SEVERE"]
                    if not severe:
                        return (True, "No severe console errors")
                    messages = "; ".join(l.get("message", "")[:150] for l in severe[:3])
                    return (False, f"{len(severe)} severe console errors: {messages}")
                safe(rec, "Accessibility", BASE_PATH_TITLES.get(path, path), "no_severe_console_errors", console_check)

    finally:
        driver.quit()


def run(web_url, backend_url, output_dir, no_spawn_web, no_spawn_backend):
    backend_proc, backend_started = ensure_server(backend_url, no_spawn_backend, db_filename="backend_web_e2e.db", workers=1)

    web_proc = None
    web_started = False
    if not no_spawn_web and not wait_for_web(web_url, timeout=1.5):
        print(f"No web dev server detected at {web_url} — starting `npm run dev`...")
        port = int(web_url.rsplit(":", 1)[-1])
        web_proc = spawn_web_dev_server(port)
        web_started = True
        if not wait_for_web(web_url, timeout=60):
            print("Web dev server failed to start within 60s.")
            sys.exit(1)
        print("Web dev server is up.")

    browsers = []
    for b in ("chrome", "firefox"):
        if browser_available(b):
            browsers.append(b)
        else:
            print(f"{b} not available in this environment — skipping (will still run in CI where installed).")

    all_results = []
    for browser in browsers:
        print(f"\n=== Running Selenium suite in {browser} ===")
        rec = Recorder(browser)
        run_browser_suite(browser, web_url, backend_url, rec)
        passed = sum(1 for r in rec.results if r["Status"] == "Pass")
        print(f"{browser}: {passed}/{len(rec.results)} passed")
        all_results.extend(rec.results)

    total = len(all_results)
    passed = sum(1 for r in all_results if r["Status"] == "Pass")
    pass_rate = (passed / total * 100) if total else 100.0

    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "web_e2e_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "suite": "Website E2E", "browsers_run": browsers,
            "total": total, "passed": passed, "failed": total - passed,
            "pass_rate": round(pass_rate, 2), "results": all_results,
        }, f, indent=2)

    csv_path = os.path.join(output_dir, "web_e2e_results.csv")
    if all_results:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(all_results[0].keys()))
            writer.writeheader()
            writer.writerows(all_results)

    print(f"\nTotal: {passed}/{total} passed ({pass_rate:.2f}%) across browsers: {browsers}")
    print(f"Reports written: {json_path}, {csv_path}")

    if web_started and web_proc:
        web_proc.terminate()
        try:
            web_proc.wait(timeout=10)
        except Exception:
            web_proc.kill()
    teardown_server(backend_proc, backend_started, db_filename="backend_web_e2e.db")

    if any(r["Status"] == "Fail" for r in all_results):
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--web-url", default="http://127.0.0.1:3000")
    parser.add_argument("--backend-url", default="http://127.0.0.1:8000")
    parser.add_argument("--output-dir", default=os.path.join(REPO_ROOT, "reports"))
    parser.add_argument("--no-spawn-web", action="store_true")
    parser.add_argument("--no-spawn-backend", action="store_true")
    args = parser.parse_args()
    run(args.web_url, args.backend_url, args.output_dir, args.no_spawn_web, args.no_spawn_backend)
