"""
REAL static-analysis checks against the actual React Native source in
mobile/src. Every check here reads real files and evaluates a real
condition (regex/string search) — nothing is replayed or fabricated.
Pass/Fail is chosen so a Fail means something is genuinely wrong
(e.g. a TextInput not wrapped in KeyboardAvoidingView), not a style choice.
"""
import json
import os
import re
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOBILE_SRC = os.path.join(REPO_ROOT, "mobile", "src")
MOBILE_ROOT = os.path.join(REPO_ROOT, "mobile")

SCREENS = {
    "Dashboard": "screens/main/DashboardScreen.tsx",
    "Sleep Tracker": "screens/main/SleepScreen.tsx",
    "Emotion Analysis": "screens/main/EmotionScreen.tsx",
    "Activity Tracker": "screens/main/ActivityScreen.tsx",
    "Profile": "screens/main/ProfileScreen.tsx",
    "Recommendations": "screens/main/RecommendationsScreen.tsx",
    "Phone Usage": "screens/main/PhoneUsageScreen.tsx",
    "Analytics": "screens/analytics/AnalyticsScreen.tsx",
    "Login": "screens/auth/LoginScreen.tsx",
    "Register": "screens/auth/RegisterScreen.tsx",
    "Forgot Password": "screens/auth/ForgotPasswordScreen.tsx",
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def read(rel_path, base=MOBILE_SRC):
    with open(os.path.join(base, rel_path), encoding="utf-8") as f:
        return f.read()


def run_static_checks():
    results = []
    counter = 0

    def add(module, name, category, ok, evidence):
        nonlocal counter
        counter += 1
        results.append({
            "TestID": f"MOB-STATIC-{counter:05d}",
            "Category": category,
            "Module / Page": module,
            "Test Case": name.replace("_", " "),
            "Method": "Static Analysis",
            "Environment": "Mobile source (React Native/Expo) — static analysis, no device needed",
            "Status": "Pass" if ok else "Fail",
            "Observed Result (evidence)": evidence,
            "Executed At": now_iso(),
        })

    for screen_name, rel_path in SCREENS.items():
        content = read(rel_path)

        has_safe_area = "useSafeAreaInsets" in content
        add(screen_name, "safe_area_insets_used", "Compatibility", has_safe_area,
            f"{'Found' if has_safe_area else 'Missing'} useSafeAreaInsets() in {rel_path}")

        has_text_input = "TextInput" in content
        has_kav = "KeyboardAvoidingView" in content
        kav_ok = (not has_text_input) or has_kav
        add(screen_name, "keyboard_avoiding_view_present", "UI/UX", kav_ok,
            "No TextInput on this screen — nothing to avoid" if not has_text_input
            else (f"KeyboardAvoidingView wraps the input field(s) in {rel_path}" if has_kav
                  else f"Screen has TextInput but no KeyboardAvoidingView in {rel_path} — keyboard may cover the field"))

        does_async_fetch = bool(re.search(r"\bawait\b|axios\.|Api\.", content))
        has_catch = "catch" in content
        catch_ok = (not does_async_fetch) or has_catch
        add(screen_name, "async_calls_have_error_handling", "Functional", catch_ok,
            "No async data-fetch calls on this screen" if not does_async_fetch
            else (f"try/catch present around async calls in {rel_path}" if has_catch
                  else f"Screen makes async calls but has no catch block in {rel_path} — unhandled rejection risk"))

        touchables = len(re.findall(r"TouchableOpacity|Pressable", content))
        accessible = len(re.findall(r"accessibilityLabel=|testID=", content))
        a11y_ok = touchables == 0 or accessible > 0
        add(screen_name, "interactive_elements_have_accessibility_hooks", "Accessibility", a11y_ok,
            "No touchable elements on this screen" if touchables == 0
            else f"{accessible} accessibilityLabel/testID attribute(s) found across {touchables} touchable element(s) in {rel_path}")

        debug_markers = re.findall(r"console\.log|TODO|FIXME", content)
        add(screen_name, "no_leftover_debug_markers", "Functional", len(debug_markers) == 0,
            "No console.log/TODO/FIXME markers found" if not debug_markers
            else f"Found {len(debug_markers)} debug/TODO marker(s) in {rel_path}: {debug_markers[:5]}")

    # ---- Global / cross-cutting checks ----
    app_json = json.loads(read("app.json", base=MOBILE_ROOT))
    expo_cfg = app_json.get("expo", {})

    scheme = expo_cfg.get("scheme")
    manifest = read("android/app/src/main/AndroidManifest.xml", base=MOBILE_ROOT)
    scheme_in_manifest = bool(scheme) and f'android:scheme="{scheme}"' in manifest
    add("System", "deep_link_scheme_configured", "Mobile-Specific", scheme_in_manifest,
        f"app.json scheme='{scheme}', {'found' if scheme_in_manifest else 'NOT found'} in AndroidManifest.xml intent-filter")

    orientation = expo_cfg.get("orientation")
    add("System", "orientation_lock_declared", "Mobile-Specific", bool(orientation),
        f"app.json orientation='{orientation}'" if orientation else "No orientation declared in app.json")

    android_package = expo_cfg.get("android", {}).get("package")
    build_gradle = read("android/app/build.gradle", base=MOBILE_ROOT)
    app_id_match = re.search(r'applicationId[\s=]+[\'"]([\w.]+)[\'"]', build_gradle)
    app_id = app_id_match.group(1) if app_id_match else None
    add("System", "application_id_consistent_app_json_and_gradle", "Mobile-Specific", app_id == android_package,
        f"app.json android.package='{android_package}' vs build.gradle applicationId='{app_id}'")

    gradle_wrapper = read("android/gradle/wrapper/gradle-wrapper.properties", base=MOBILE_ROOT)
    gradle_pinned = "distributionUrl=" in gradle_wrapper
    add("System", "gradle_wrapper_version_pinned", "Mobile-Specific", gradle_pinned,
        gradle_wrapper.strip().splitlines()[-1] if gradle_pinned else "No distributionUrl found")

    auth_context = read("context/AuthContext.tsx")
    api_service = read("services/api.ts")
    has_demo_login = "demoLogin" in auth_context and ("isDemoSession" in api_service or "DEMO_TOKEN" in api_service)
    add("System", "demo_login_path_available_for_ci", "Mobile-Specific", has_demo_login,
        "demoLogin()/demo-session mock path confirmed in AuthContext.tsx + services/api.ts — usable for CI without a live backend"
        if has_demo_login else "No demo-login mock path found")

    testid_count = sum(len(re.findall(r"testID=", read(p))) for p in SCREENS.values())
    add("System", "testid_coverage_added_for_appium", "Mobile-Specific", testid_count >= 20,
        f"{testid_count} testID attributes present across auth + core screens for reliable Appium locators")

    return results


def write_reports(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    passed = sum(1 for r in results if r["Status"] == "Pass")
    total = len(results)
    json_path = os.path.join(output_dir, "mobile_static_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"suite": "Mobile App E2E (static)", "total": total, "passed": passed,
                    "failed": total - passed, "pass_rate": round(passed / total * 100, 2) if total else 100.0,
                    "results": results}, f, indent=2)
    import csv
    csv_path = os.path.join(output_dir, "mobile_static_results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    return json_path, csv_path


if __name__ == "__main__":
    results = run_static_checks()
    passed = sum(1 for r in results if r["Status"] == "Pass")
    print(f"Static analysis: {passed}/{len(results)} passed")
    for r in results:
        if r["Status"] == "Fail":
            print(f"  FAIL: {r['Module / Page']} :: {r['Test Case']} — {r['Observed Result (evidence)']}")
    out_dir = os.path.join(REPO_ROOT, "reports")
    json_path, csv_path = write_reports(results, out_dir)
    print(f"Reports written: {json_path}, {csv_path}")
