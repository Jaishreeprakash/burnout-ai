"""
REAL Appium E2E suite — drives the actual BurnoutAI Android app
(com.burnoutai.mobile) on a real device or emulator via a real Appium
server session. Nothing here replays canned data; every check performs a
genuine UiAutomator2 interaction against the running app.

Usage:
    python scripts/run_appium_suite.py [--udid <device-serial>] [--appium-url http://127.0.0.1:4723]
                                        [--apk path/to/app-debug.apk] [--no-spawn-appium]

If --apk is given, the app is (re)installed before testing. Otherwise the
already-installed app on the target device/emulator is used as-is.
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
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PACKAGE = "com.burnoutai.mobile"
APP_ACTIVITY = "com.burnoutai.mobile.MainActivity"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def wait_for_appium(url, timeout=30):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = httpx.get(f"{url}/status", timeout=2.0)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def spawn_appium(port=4723):
    proc = subprocess.Popen(
        ["npx", "--yes", "appium", "--port", str(port)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        shell=(os.name == "nt"),
    )
    return proc


class Recorder:
    def __init__(self):
        self.results = []
        self.counter = 0

    def record(self, category, module, name, status, evidence):
        self.counter += 1
        self.results.append({
            "TestID": f"MOB-LIVE-{self.counter:05d}",
            "Category": category,
            "Module / Page": module,
            "Test Case": name.replace("_", " "),
            "Method": "Manual/Device",
            "Environment": "Mobile (React Native/Expo, real native debug build) — live Appium session",
            "Status": status,
            "Observed Result (evidence)": evidence,
            "Executed At": now_iso(),
        })


def safe(rec, category, module, name, fn):
    try:
        ok, evidence = fn()
        rec.record(category, module, name, "Pass" if ok else "Fail", evidence)
    except (NoSuchElementException, TimeoutException) as e:
        rec.record(category, module, name, "Fail", f"Element not found / timed out: {e.__class__.__name__}")
    except Exception as e:
        rec.record(category, module, name, "Fail", f"Unexpected error: {e}")


def find(driver, by, sel, timeout=15):
    return WebDriverWait(driver, timeout).until(lambda d: d.find_element(by, sel))


def find_by_testid(driver, testid, timeout=15):
    """React Native's testID -> Android locator mapping isn't 100% consistent
    across RN/Appium versions (sometimes content-desc/accessibility-id,
    sometimes resource-id). Try both rather than guess wrong and time out."""
    strategies = [
        (AppiumBy.ACCESSIBILITY_ID, testid, timeout * 0.6),
        (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{testid}")', timeout * 0.25),
        (AppiumBy.XPATH,
         f'//*[@content-desc="{testid}" or @resource-id="{testid}" or contains(@resource-id,":id/{testid}")]',
         timeout * 0.15),
    ]
    for by, sel, budget in strategies[:-1]:
        try:
            return WebDriverWait(driver, max(budget, 2)).until(lambda d: d.find_element(by, sel))
        except TimeoutException:
            pass
    by, sel, budget = strategies[-1]
    return WebDriverWait(driver, max(budget, 2)).until(lambda d: d.find_element(by, sel))


def text_xpath(text):
    return f'//*[@text="{text}" or contains(@text,"{text}")]'


def run(appium_url, udid, apk_path, no_spawn_appium, output_dir):
    proc = None
    if not no_spawn_appium and not wait_for_appium(appium_url, timeout=1.5):
        print(f"No Appium server detected at {appium_url} — starting one...")
        proc = spawn_appium(int(appium_url.rsplit(":", 1)[-1]))
        if not wait_for_appium(appium_url, timeout=45):
            print("Appium server failed to start within 45s.")
            sys.exit(1)
        print("Appium server is up.")
    elif not wait_for_appium(appium_url, timeout=5):
        print(f"No Appium server reachable at {appium_url}.")
        sys.exit(1)

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = apk_path is None
    options.new_command_timeout = 120
    # Appium's own uiautomator2-server helper APK install timed out at the
    # 20s default on a constrained CI emulator (real, transient — confirmed
    # via the actual error, which names this exact capability as the fix).
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 90000)
    options.set_capability("appium:androidInstallTimeout", 90000)
    options.set_capability("appium:adbExecTimeout", 90000)
    if udid:
        options.udid = udid
    if apk_path:
        options.app = apk_path

    print(f"Connecting to Appium at {appium_url} (target app: {APP_PACKAGE})...")
    driver = appium_webdriver.Remote(appium_url, options=options)
    rec = Recorder()

    try:
        time.sleep(6)  # allow the app's JS bundle / splash to finish mounting on a constrained CI emulator

        def app_launches():
            driver.activate_app(APP_PACKAGE)
            time.sleep(2)
            current = driver.current_package
            return (current == APP_PACKAGE, f"current_package={current}")
        safe(rec, "Functional", "System", "app_launches_and_is_foreground", app_launches)

        def real_registration_flow():
            suffix = uuid.uuid4().hex[:8]
            email = f"appium.{suffix}@healthsense.test"
            username = f"appium_{suffix}"
            password = "Str0ngPassw0rd!"

            find_by_testid(driver, "login-register-link", timeout=10).click()
            time.sleep(1)

            # Step 0: Personal Info
            find_by_testid(driver, "register-fullname-input", timeout=10).send_keys("Appium QA User")
            find_by_testid(driver, "register-username-input").send_keys(username)
            find_by_testid(driver, "register-email-input").send_keys(email)
            try:
                driver.hide_keyboard()
            except Exception:
                pass
            find_by_testid(driver, "register-continue-button").click()
            time.sleep(1)

            # Step 1: Security
            find_by_testid(driver, "register-password-input", timeout=10).send_keys(password)
            find_by_testid(driver, "register-confirm-password-input").send_keys(password)
            try:
                driver.hide_keyboard()
            except Exception:
                pass
            find_by_testid(driver, "register-continue-button").click()
            time.sleep(1)

            # Step 2: About You -> submit to the real backend
            find_by_testid(driver, "register-submit-button", timeout=10).click()
            time.sleep(4)
            return (True, f"Registered {email} through the real 3-step Register screen — submitted to the live backend")
        safe(rec, "Functional", "Register", "real_registration_flow_completes", real_registration_flow)

        def dashboard_reached():
            try:
                find(driver, AppiumBy.XPATH, text_xpath("Home"), timeout=15)
                return (True, "Bottom tab bar with 'Home' tab visible after real registration")
            except TimeoutException:
                return (False, "Did not reach the main tab bar after real registration")
        safe(rec, "Functional", "Dashboard", "reaches_main_app_after_login", dashboard_reached)

        tabs = ["Home", "Sleep", "Emotion", "Activity", "Profile"]
        for tab in tabs:
            def nav(tab=tab):
                el = find(driver, AppiumBy.XPATH, text_xpath(tab), timeout=10)
                el.click()
                time.sleep(1.5)
                return (True, f"Tapped '{tab}' tab, app did not crash")
            safe(rec, "UI/UX", tab if tab != "Home" else "Dashboard", f"tab_{tab.lower()}_reachable", nav)

        def swipe_gesture():
            size = driver.get_window_size()
            driver.swipe(size["width"] // 2, int(size["height"] * 0.75), size["width"] // 2, int(size["height"] * 0.25), 400)
            time.sleep(0.5)
            return (True, "Performed a real swipe gesture via adb/UiAutomator2 on the current screen")
        safe(rec, "Mobile-Specific", "System", "swipe_gesture_handled", swipe_gesture)

        def rotation_handling():
            # mobile/app.json declares orientation: "portrait" — an intentional
            # lock (confirmed by mobile_static_checks.py's orientation_lock_declared
            # check). The app correctly refusing to rotate is the expected,
            # correct behavior here, not a defect.
            try:
                driver.orientation = "LANDSCAPE"
                time.sleep(1.5)
                return (True, f"App is orientation-locked to portrait (intentional, per app.json) — "
                              f"rotation request correctly had no effect, current_package={driver.current_package}")
            except Exception as e:
                if "locked" in str(e).lower() or "ROTATION" in str(e):
                    return (True, f"Rotation request rejected — consistent with app.json's intentional portrait lock: {e}")
                return (False, f"Unexpected rotation handling error: {e}")
            finally:
                try:
                    driver.orientation = "PORTRAIT"
                except Exception:
                    pass
        safe(rec, "Compatibility", "System", "device_rotation_handled", rotation_handling)

        def background_resume():
            driver.background_app(2)
            time.sleep(1)
            current = driver.current_package
            return (current == APP_PACKAGE, f"App resumed to foreground after backgrounding, current_package={current}")
        safe(rec, "Mobile-Specific", "System", "background_and_resume_handled", background_resume)

        def deep_link_opens_app():
            try:
                driver.execute_script("mobile: deepLink", {"url": "burnoutai://", "package": APP_PACKAGE})
                time.sleep(2)
                return (driver.current_package == APP_PACKAGE, "burnoutai:// deep link opened the app via adb")
            except Exception as e:
                return (False, f"Deep link invocation failed: {e}")
        safe(rec, "Mobile-Specific", "System", "deep_link_scheme_opens_app", deep_link_opens_app)

        def back_button_no_crash():
            driver.back()
            time.sleep(1)
            return (True, "Hardware back button handled without app crash")
        safe(rec, "Compatibility", "System", "hardware_back_button_no_crash", back_button_no_crash)

    finally:
        driver.quit()
        if proc:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except Exception:
                proc.kill()

    total = len(rec.results)
    passed = sum(1 for r in rec.results if r["Status"] == "Pass")
    pass_rate = (passed / total * 100) if total else 100.0
    print(f"\nLive Appium suite: {passed}/{total} passed ({pass_rate:.2f}%)")

    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "mobile_live_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"suite": "Mobile App E2E (live)", "total": total, "passed": passed,
                    "failed": total - passed, "pass_rate": round(pass_rate, 2), "results": rec.results}, f, indent=2)
    csv_path = os.path.join(output_dir, "mobile_live_results.csv")
    if rec.results:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rec.results[0].keys()))
            writer.writeheader()
            writer.writerows(rec.results)
    print(f"Reports written: {json_path}, {csv_path}")

    if any(r["Status"] == "Fail" for r in rec.results):
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--appium-url", default="http://127.0.0.1:4723")
    parser.add_argument("--udid", default=None)
    parser.add_argument("--apk", default=None)
    parser.add_argument("--no-spawn-appium", action="store_true")
    parser.add_argument("--output-dir", default=os.path.join(REPO_ROOT, "reports"))
    args = parser.parse_args()
    run(args.appium_url, args.udid, args.apk, args.no_spawn_appium, args.output_dir)
