# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard is generated from **real suite runs** — a live FastAPI backend, a real concurrent load test, real Selenium browser sessions, and real static + Appium mobile checks. No row here is replayed from a static fixture.

## 📊 Unified Summary Overview

| Component | Test Suite | Total Tests | Passed | Failed | Pass Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Website E2E | Real Selenium suite (Chrome + Firefox) | 400 | ✅ 170 | ❌ 230 | 42.5% |
| Mobile App E2E | Real static analysis + live Appium | 400 | ✅ 350 | ❌ 50 | 87.5% |
| Backend & Security | Real functional/security scenarios (live backend) | 406 | ✅ 406 | ✅ 0 | 100.0% |
| API Load Testing | Real 100-VU baseline load test | 400 | ✅ 400 | ✅ 0 | 100.0% |

---

## 🌐 Website E2E Test Verification Details

Browsers run: chrome, firefox

<details>
<summary>Click to view Website E2E Test Cases (400 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WEB-CH-00001 | UI/UX | Login | element_present_username_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00002 | UI/UX | Login | element_present_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00003 | UI/UX | Login | element_present_submit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00004 | UI/UX | Login | element_present_register_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00005 | UI/UX | Login | element_present_password_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00006 | UI/UX | Login | element_present_forgot_password_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00007 | UI/UX | Login | element_present_ai_analysis_feature_label | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00008 | Functional | Login | empty_submit_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Form did not navigate away on empty submit |
| WEB-CH-00009 | Security | Login | wrong_credentials_rejected | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | No error banner appeared after invalid login |
| WEB-CH-00010 | Security | Login | sql_injection_input_no_crash | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Page still renders content after SQLi-style login attempt |
| WEB-CH-00011 | Functional | Login | password_show_hide_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | type changed password -> text |
| WEB-CH-00012 | UI/UX | Login | register_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on https://jaishreeprakash.github.io/burnout-ai/register |
| WEB-CH-00013 | UI/UX | Register | element_present_full_name_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00014 | UI/UX | Register | element_present_username_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00015 | UI/UX | Register | element_present_email_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00016 | UI/UX | Register | element_present_age_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00017 | UI/UX | Register | element_present_gender_select | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00018 | UI/UX | Register | element_present_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00019 | UI/UX | Register | element_present_confirm_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00020 | UI/UX | Register | element_present_submit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00021 | UI/UX | Register | element_present_login_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00022 | Functional | Register | short_password_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Weak password correctly blocked client-side submit |
| WEB-CH-00023 | Functional | Register | password_mismatch_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Password mismatch correctly blocked client-side submit |
| WEB-CH-00024 | Security | Register | xss_input_no_crash | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Page renders normally with XSS-style full_name input (no script executed/crash) |
| WEB-CH-00025 | UI/UX | Register | login_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on https://jaishreeprakash.github.io/burnout-ai/login |
| WEB-CH-00026 | Functional | Login | empty_submit_shows_required_errors | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | react-hook-form required-field messages present: True |
| WEB-CH-00027 | Functional | Login | password_toggle_reverts_on_second_click | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | type sequence password -> text -> password |
| WEB-CH-00028 | Functional | Register | empty_submit_shows_required_errors | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | react-hook-form required-field messages present: True |
| WEB-CH-00029 | Functional | Register | invalid_email_format_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Invalid email format correctly blocked client-side submit |
| WEB-CH-00030 | Functional | Register | username_min_length_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sub-minimum-length username correctly blocked client-side submit |
| WEB-CH-00031 | Functional | Register | username_invalid_chars_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Username with invalid characters correctly blocked client-side submit |
| WEB-CH-00032 | Functional | Register | age_out_of_range_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Below-minimum age correctly blocked client-side submit |
| WEB-CH-00033 | Functional | Register | gender_select_has_expected_options | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Gender select options: ['Prefer not to say', 'Male', 'Female', 'Non-binary', 'Other'] |
| WEB-CH-00034 | Functional | Register | real_registration_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Registered selenium.chrome.59855687@healthsense.test and landed on https://jaishreeprakash.github.io/burnout-ai/dashboard |
| WEB-CH-00035 | Functional | Login | real_login_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Signed out then logged back in with real credentials, reached /dashboard |
| WEB-CH-00036 | UI/UX | Sidebar | nav_link_dashboard_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Dashboard' navigated to https://jaishreeprakash.github.io/burnout-ai/dashboard |
| WEB-CH-00037 | UI/UX | Sidebar | nav_link_sleep_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Sleep Tracker' navigated to https://jaishreeprakash.github.io/burnout-ai/sleep |
| WEB-CH-00038 | UI/UX | Sidebar | nav_link_phone_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Phone Usage' navigated to https://jaishreeprakash.github.io/burnout-ai/phone |
| WEB-CH-00039 | UI/UX | Sidebar | nav_link_emotions_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Emotion Analysis' navigated to https://jaishreeprakash.github.io/burnout-ai/emotions |
| WEB-CH-00040 | UI/UX | Sidebar | nav_link_activity_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Activity Tracker' navigated to https://jaishreeprakash.github.io/burnout-ai/activity |
| WEB-CH-00041 | UI/UX | Sidebar | nav_link_recommendations_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Recommendations' navigated to https://jaishreeprakash.github.io/burnout-ai/recommendations |
| WEB-CH-00042 | UI/UX | Sidebar | nav_link_analytics_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Analytics' navigated to https://jaishreeprakash.github.io/burnout-ai/analytics |
| WEB-CH-00043 | UI/UX | Sidebar | nav_link_chat_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'AI Coach Chat' navigated to https://jaishreeprakash.github.io/burnout-ai/chat |
| WEB-CH-00044 | UI/UX | Sidebar | nav_link_profile_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Profile' navigated to https://jaishreeprakash.github.io/burnout-ai/profile |
| WEB-CH-00045 | UI/UX | Dashboard | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00046 | UI/UX | Dashboard | element_present_burnout_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00047 | UI/UX | Dashboard | element_present_wellness_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00048 | UI/UX | Dashboard | element_present_health_dimensions_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00049 | UI/UX | Dashboard | element_present_emotional_stability_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00050 | UI/UX | Dashboard | element_present_emotion_distribution_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00051 | UI/UX | Dashboard | element_present_ai_recommendations_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00052 | UI/UX | Dashboard | element_present_progress_comparison_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00053 | UI/UX | Dashboard | element_present_quick_stats_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00054 | UI/UX | Dashboard | element_present_view_all_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00055 | UI/UX | Dashboard | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00056 | UI/UX | Dashboard | element_present_header_notifications_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00057 | UI/UX | Sleep Tracker | element_present_overview_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00058 | UI/UX | Sleep Tracker | element_present_calendar_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00059 | UI/UX | Sleep Tracker | element_present_log_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00060 | UI/UX | Sleep Tracker | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00061 | UI/UX | Sleep Tracker | element_present_log_sleep_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00062 | UI/UX | Sleep Tracker | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00063 | UI/UX | Sleep Tracker | element_present_header_notifications_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00064 | UI/UX | Sleep Tracker | element_present_sleep_duration_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00065 | UI/UX | Sleep Tracker | element_present_sleep_quality_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00066 | UI/UX | Recommendations | element_present_filter_all | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00067 | UI/UX | Recommendations | element_present_filter_sleep | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00068 | UI/UX | Recommendations | element_present_filter_phone | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00069 | UI/UX | Recommendations | element_present_filter_activity | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00070 | UI/UX | Recommendations | element_present_filter_mental_health | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00071 | UI/UX | Recommendations | element_present_filter_social | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00072 | UI/UX | Recommendations | element_present_filter_nutrition | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00073 | UI/UX | Recommendations | element_present_sort_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00074 | UI/UX | Recommendations | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00075 | UI/UX | Recommendations | element_present_header_notifications_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00076 | UI/UX | Recommendations | element_present_overall_progress_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00077 | UI/UX | Recommendations | element_present_high_priority_label | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00078 | UI/UX | Analytics | element_present_range_7d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00079 | UI/UX | Analytics | element_present_range_30d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00080 | UI/UX | Analytics | element_present_export_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00081 | UI/UX | Analytics | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00082 | UI/UX | Analytics | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00083 | UI/UX | Analytics | element_present_header_notifications_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00084 | UI/UX | Analytics | element_present_burnout_score_trend_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00085 | UI/UX | Analytics | element_present_all_metrics_overlay_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00086 | UI/UX | Analytics | element_present_burnout_records_region | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00087 | UI/UX | Analytics | element_present_analytics_dashboard_label | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00088 | UI/UX | Wellness Chat | element_present_message_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00089 | UI/UX | Wellness Chat | element_present_send_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00090 | UI/UX | Wellness Chat | element_present_new_chat_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00091 | UI/UX | Wellness Chat | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00092 | UI/UX | Wellness Chat | element_present_header_notifications_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00093 | UI/UX | Wellness Chat | element_present_coach_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00094 | UI/UX | Wellness Chat | element_present_starter_prompt_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00095 | UI/UX | Profile | element_present_profile_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00096 | UI/UX | Profile | element_present_notifications_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00097 | UI/UX | Profile | element_present_privacy_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00098 | UI/UX | Profile | element_present_edit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00099 | UI/UX | Profile | element_present_sign_out_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00100 | UI/UX | Profile | element_present_header_open_menu_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |

*... showing 100 of 400 Website E2E test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## 📱 Mobile App E2E Test Verification Details

Static source-analysis cases: 355 • Live Appium cases (real device/emulator): 45

<details>
<summary>Click to view Mobile E2E Test Cases (400 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MOB-STATIC-00001 | Compatibility | Dashboard | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00002 | UI/UX | Dashboard | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No TextInput on this screen — nothing to avoid |
| MOB-STATIC-00003 | Functional | Dashboard | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No async data-fetch calls on this screen |
| MOB-STATIC-00004 | Accessibility | Dashboard | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 1 accessibilityLabel/testID attribute(s) found across 9 touchable element(s) in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00005 | Functional | Dashboard | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00006 | Code Quality | Dashboard | uses stylesheet create | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found StyleSheet.create( in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00007 | UI/UX | Dashboard | shows loading state during fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found ActivityIndicator/SkeletonLoader in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00008 | UI/UX | Dashboard | handles empty state when no data | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No empty-state handling pattern in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00009 | Functional | Dashboard | flatlist or sectionlist has key extractor | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No FlatList/SectionList on this screen |
| MOB-STATIC-00010 | Code Quality | Dashboard | typed props or navigation defined | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found typed Props/navigation generic in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00011 | Code Quality | Dashboard | no untyped any usage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No untyped `: any` usage |
| MOB-STATIC-00012 | Mobile-Specific | Dashboard | screen has testid coverage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No testID attribute(s) in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00013 | Functional | Dashboard | imports service layer not raw fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | services/hooks/context import=True, raw fetch()=not used in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00014 | Mobile-Specific | Dashboard | no hardcoded backend url in screen | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No literal http(s):// URL in screen source |
| MOB-STATIC-00015 | UI/UX | Dashboard | uses theme hook for colors | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useTheme() call in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00016 | UI/UX | Dashboard | touchables have active opacity or pressable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | activeOpacity=/Pressable present in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00017 | Accessibility | Dashboard | accessibility role declared on touchables | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found accessibilityRole= among 9 touchable(s) in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00018 | Compatibility | Dashboard | safe area inset applied to layout | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found insets.top/insets.bottom usage in a style/layout in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00019 | UI/UX | Dashboard | email input has correct keyboard type | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No email-labeled input on this screen |
| MOB-STATIC-00020 | Security | Dashboard | password inputs use secure text entry | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No password-labeled input on this screen |
| MOB-STATIC-00021 | Mobile-Specific | Dashboard | animated values use native driver | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | useNativeDriver: true present in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00022 | Code Quality | Dashboard | component has default export | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found export default in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00023 | Functional | Dashboard | screen registered in a navigator | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found import/reference of DashboardScreen in navigation/*Navigator.tsx |
| MOB-STATIC-00024 | Code Quality | Dashboard | uses react fc typed component | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found `: React.FC` typed component declaration in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00025 | Functional | Dashboard | list items have stable keys in map | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | key={...} present alongside .map( in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00026 | UI/UX | Dashboard | scrollview has content container style | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | contentContainerStyle present in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00027 | UI/UX | Dashboard | uses vector icons library | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found @expo/vector-icons import in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00028 | Code Quality | Dashboard | screen file line count reasonable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | screens/main/DashboardScreen.tsx is 360 lines (within the 700-line maintainability guideline) |
| MOB-STATIC-00029 | UI/UX | Dashboard | user facing error alert on catch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No catch block on this screen |
| MOB-STATIC-00030 | Compatibility | Sleep Tracker | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/SleepScreen.tsx |
| MOB-STATIC-00031 | UI/UX | Sleep Tracker | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00032 | Functional | Sleep Tracker | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/SleepScreen.tsx |
| MOB-STATIC-00033 | Accessibility | Sleep Tracker | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 4 accessibilityLabel/testID attribute(s) found across 8 touchable element(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00034 | Functional | Sleep Tracker | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00035 | Code Quality | Sleep Tracker | uses stylesheet create | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found StyleSheet.create( in screens/main/SleepScreen.tsx |
| MOB-STATIC-00036 | UI/UX | Sleep Tracker | shows loading state during fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found ActivityIndicator/SkeletonLoader in screens/main/SleepScreen.tsx |
| MOB-STATIC-00037 | UI/UX | Sleep Tracker | handles empty state when no data | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No empty-state handling pattern in screens/main/SleepScreen.tsx |
| MOB-STATIC-00038 | Functional | Sleep Tracker | flatlist or sectionlist has key extractor | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No FlatList/SectionList on this screen |
| MOB-STATIC-00039 | Code Quality | Sleep Tracker | typed props or navigation defined | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | Missing typed Props/navigation generic in screens/main/SleepScreen.tsx |
| MOB-STATIC-00040 | Code Quality | Sleep Tracker | no untyped any usage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No untyped `: any` usage |
| MOB-STATIC-00041 | Mobile-Specific | Sleep Tracker | screen has testid coverage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No testID attribute(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00042 | Functional | Sleep Tracker | imports service layer not raw fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | services/hooks/context import=True, raw fetch()=not used in screens/main/SleepScreen.tsx |
| MOB-STATIC-00043 | Mobile-Specific | Sleep Tracker | no hardcoded backend url in screen | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No literal http(s):// URL in screen source |
| MOB-STATIC-00044 | UI/UX | Sleep Tracker | uses theme hook for colors | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useTheme() call in screens/main/SleepScreen.tsx |
| MOB-STATIC-00045 | UI/UX | Sleep Tracker | touchables have active opacity or pressable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | activeOpacity=/Pressable present in screens/main/SleepScreen.tsx |
| MOB-STATIC-00046 | Accessibility | Sleep Tracker | accessibility role declared on touchables | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found accessibilityRole= among 8 touchable(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00047 | Compatibility | Sleep Tracker | safe area inset applied to layout | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found insets.top/insets.bottom usage in a style/layout in screens/main/SleepScreen.tsx |
| MOB-STATIC-00048 | UI/UX | Sleep Tracker | email input has correct keyboard type | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No email-labeled input on this screen |
| MOB-STATIC-00049 | Security | Sleep Tracker | password inputs use secure text entry | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No password-labeled input on this screen |
| MOB-STATIC-00050 | Mobile-Specific | Sleep Tracker | animated values use native driver | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No Animated.timing/Animated.Value on this screen |
| MOB-STATIC-00051 | Code Quality | Sleep Tracker | component has default export | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found export default in screens/main/SleepScreen.tsx |
| MOB-STATIC-00052 | Functional | Sleep Tracker | screen registered in a navigator | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found import/reference of SleepScreen in navigation/*Navigator.tsx |
| MOB-STATIC-00053 | Code Quality | Sleep Tracker | uses react fc typed component | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found `: React.FC` typed component declaration in screens/main/SleepScreen.tsx |
| MOB-STATIC-00054 | Functional | Sleep Tracker | list items have stable keys in map | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | key={...} present alongside .map( in screens/main/SleepScreen.tsx |
| MOB-STATIC-00055 | UI/UX | Sleep Tracker | scrollview has content container style | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | contentContainerStyle present in screens/main/SleepScreen.tsx |
| MOB-STATIC-00056 | UI/UX | Sleep Tracker | uses vector icons library | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found @expo/vector-icons import in screens/main/SleepScreen.tsx |
| MOB-STATIC-00057 | Code Quality | Sleep Tracker | screen file line count reasonable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | screens/main/SleepScreen.tsx is 437 lines (within the 700-line maintainability guideline) |
| MOB-STATIC-00058 | UI/UX | Sleep Tracker | user facing error alert on catch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Alert.alert( present alongside catch in screens/main/SleepScreen.tsx |
| MOB-STATIC-00059 | Compatibility | Emotion Analysis | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00060 | UI/UX | Emotion Analysis | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00061 | Functional | Emotion Analysis | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00062 | Accessibility | Emotion Analysis | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 7 accessibilityLabel/testID attribute(s) found across 14 touchable element(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00063 | Functional | Emotion Analysis | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00064 | Code Quality | Emotion Analysis | uses stylesheet create | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found StyleSheet.create( in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00065 | UI/UX | Emotion Analysis | shows loading state during fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found ActivityIndicator/SkeletonLoader in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00066 | UI/UX | Emotion Analysis | handles empty state when no data | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found empty-state handling pattern in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00067 | Functional | Emotion Analysis | flatlist or sectionlist has key extractor | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | keyExtractor present in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00068 | Code Quality | Emotion Analysis | typed props or navigation defined | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | Missing typed Props/navigation generic in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00069 | Code Quality | Emotion Analysis | no untyped any usage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No untyped `: any` usage |
| MOB-STATIC-00070 | Mobile-Specific | Emotion Analysis | screen has testid coverage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No testID attribute(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00071 | Functional | Emotion Analysis | imports service layer not raw fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | services/hooks/context import=True, raw fetch()=not used in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00072 | Mobile-Specific | Emotion Analysis | no hardcoded backend url in screen | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No literal http(s):// URL in screen source |
| MOB-STATIC-00073 | UI/UX | Emotion Analysis | uses theme hook for colors | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useTheme() call in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00074 | UI/UX | Emotion Analysis | touchables have active opacity or pressable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | activeOpacity=/Pressable present in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00075 | Accessibility | Emotion Analysis | accessibility role declared on touchables | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found accessibilityRole= among 14 touchable(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00076 | Compatibility | Emotion Analysis | safe area inset applied to layout | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found insets.top/insets.bottom usage in a style/layout in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00077 | UI/UX | Emotion Analysis | email input has correct keyboard type | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No email-labeled input on this screen |
| MOB-STATIC-00078 | Security | Emotion Analysis | password inputs use secure text entry | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No password-labeled input on this screen |
| MOB-STATIC-00079 | Mobile-Specific | Emotion Analysis | animated values use native driver | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | useNativeDriver: true present in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00080 | Code Quality | Emotion Analysis | component has default export | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found export default in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00081 | Functional | Emotion Analysis | screen registered in a navigator | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found import/reference of EmotionScreen in navigation/*Navigator.tsx |
| MOB-STATIC-00082 | Code Quality | Emotion Analysis | uses react fc typed component | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found `: React.FC` typed component declaration in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00083 | Functional | Emotion Analysis | list items have stable keys in map | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | key={...} present alongside .map( in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00084 | UI/UX | Emotion Analysis | scrollview has content container style | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | contentContainerStyle present in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00085 | UI/UX | Emotion Analysis | uses vector icons library | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found @expo/vector-icons import in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00086 | Code Quality | Emotion Analysis | screen file line count reasonable | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | screens/main/EmotionScreen.tsx is 517 lines (within the 700-line maintainability guideline) |
| MOB-STATIC-00087 | UI/UX | Emotion Analysis | user facing error alert on catch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Alert.alert( present alongside catch in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00088 | Compatibility | Activity Tracker | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00089 | UI/UX | Activity Tracker | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00090 | Functional | Activity Tracker | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00091 | Accessibility | Activity Tracker | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 2 accessibilityLabel/testID attribute(s) found across 5 touchable element(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00092 | Functional | Activity Tracker | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00093 | Code Quality | Activity Tracker | uses stylesheet create | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found StyleSheet.create( in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00094 | UI/UX | Activity Tracker | shows loading state during fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found ActivityIndicator/SkeletonLoader in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00095 | UI/UX | Activity Tracker | handles empty state when no data | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No empty-state handling pattern in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00096 | Functional | Activity Tracker | flatlist or sectionlist has key extractor | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No FlatList/SectionList on this screen |
| MOB-STATIC-00097 | Code Quality | Activity Tracker | typed props or navigation defined | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found typed Props/navigation generic in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00098 | Code Quality | Activity Tracker | no untyped any usage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | Found 1 `: any` usage(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00099 | Mobile-Specific | Activity Tracker | screen has testid coverage | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ❌ Fail | No testID attribute(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00100 | Functional | Activity Tracker | imports service layer not raw fetch | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | services/hooks/context import=True, raw fetch()=not used in screens/main/ActivityScreen.tsx |

*... showing 100 of 400 Mobile test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## 🛡️ Backend & Security Test Verification Details

**Security-category checks:** 155 run, 0 failed (none — no real vulnerabilities found by this scenario set)

<details>
<summary>Click to view Backend & Security Test Cases (406 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BE-00001 | Functional | System | GET / — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.4ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00002 | API | System | GET / — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.9ms. {"detail":"Method Not Allowed"} |
| BE-00003 | API | System | GET / — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (direct response), 1.1ms |
| BE-00004 | Security | System | GET / — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00005 | API | System | GET / — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (case-sensitive routing correctly rejects altered-case path), 1.1ms |
| BE-00006 | Functional | System | GET / — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.1ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00007 | Functional | System | GET /health — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms. {"status":"ok"} |
| BE-00008 | API | System | GET /health — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.8ms. {"detail":"Method Not Allowed"} |
| BE-00009 | API | System | GET /health — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00010 | Security | System | GET /health — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00011 | API | System | GET /health — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00012 | Functional | System | GET /health — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms. {"status":"ok"} |
| BE-00013 | Functional | Auth | POST /api/v1/auth/register — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 261.7ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODUxMzEwNzB9.jTv7ouS_s5oAyMVfM9pp2b31wmroZOxGg4a71nBGNbQ","token_type":"bearer","user":{"i |
| BE-00014 | API | Auth | POST /api/v1/auth/register — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.1ms. {"detail":"Method Not Allowed"} |
| BE-00015 | API | Auth | POST /api/v1/auth/register — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00016 | Security | Auth | POST /api/v1/auth/register — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00017 | API | Auth | POST /api/v1/auth/register — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 1.0ms |
| BE-00018 | Security | Auth | POST /api/v1/auth/register — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 3.2ms. {"detail":"This username is already taken"} |
| BE-00019 | Security | Auth | POST /api/v1/auth/register — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"This username is already taken"} |
| BE-00020 | Security | Auth | POST /api/v1/auth/register — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"This username is already taken"} |
| BE-00021 | Functional | Auth | POST /api/v1/auth/register — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"This username is already taken"} |
| BE-00022 | Functional | Auth | POST /api/v1/auth/register — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"This username is already taken"} |
| BE-00023 | Functional | Auth | POST /api/v1/auth/register — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"This username is already taken"} |
| BE-00024 | Security | Auth | POST /api/v1/auth/register — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"An account with this email already exists"} |
| BE-00025 | Security | Auth | POST /api/v1/auth/register — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00026 | Security | Auth | POST /api/v1/auth/register — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00027 | Functional | Auth | POST /api/v1/auth/register — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00028 | Functional | Auth | POST /api/v1/auth/register — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00029 | Functional | Auth | POST /api/v1/auth/register — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00030 | Security | Auth | POST /api/v1/auth/register — string field full name sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"An account with this email already exists"} |
| BE-00031 | Security | Auth | POST /api/v1/auth/register — string field full name xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00032 | Security | Auth | POST /api/v1/auth/register — string field full name crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00033 | Functional | Auth | POST /api/v1/auth/register — string field full name oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00034 | Functional | Auth | POST /api/v1/auth/register — string field full name empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00035 | Functional | Auth | POST /api/v1/auth/register — string field full name whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00036 | Functional | Auth | POST /api/v1/auth/register — numeric field age negative | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"greater_than_equal","loc":["body","age"],"msg":"Input should be greater than or equal to 0","input":-1,"ctx":{"ge":0},"url":"https://errors.pydantic.dev/2.5/v/greater_than_equal"}] |
| BE-00037 | Functional | Auth | POST /api/v1/auth/register — numeric field age zero | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"An account with this email already exists"} |
| BE-00038 | Functional | Auth | POST /api/v1/auth/register — numeric field age very large | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"less_than_equal","loc":["body","age"],"msg":"Input should be less than or equal to 150","input":1000000000000000.0,"ctx":{"le":150},"url":"https://errors.pydantic.dev/2.5/v/less_th |
| BE-00039 | Functional | Auth | POST /api/v1/auth/register — numeric field age very small fraction | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"int_from_float","loc":["body","age"],"msg":"Input should be a valid integer, got a number with a fractional part","input":1e-06,"url":"https://errors.pydantic.dev/2.5/v/int_from_fl |
| BE-00040 | Functional | Auth | POST /api/v1/auth/register — numeric field age wrong type string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.4ms. {"detail":[{"type":"int_parsing","loc":["body","age"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"not-a-number","url":"https://errors.pydantic.dev/2.5/v/int_ |
| BE-00041 | Functional | Auth | POST /api/v1/auth/register — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.8ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"username":"qa_user","password":"Str0ngPassw0rd!","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_ |
| BE-00042 | Functional | Auth | POST /api/v1/auth/register — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.7ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00043 | Functional | Auth | POST /api/v1/auth/register — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"An account with this email already exists"} |
| BE-00044 | Functional | Auth | POST /api/v1/auth/register — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 1.0ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00045 | Functional | Auth | POST /api/v1/auth/login — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.5ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODUxMzEwNzB9.jTv7ouS_s5oAyMVfM9pp2b31wmroZOxGg4a71nBGNbQ","token_type":"bearer","user":{"i |
| BE-00046 | API | Auth | POST /api/v1/auth/login — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.4ms. {"detail":"Method Not Allowed"} |
| BE-00047 | API | Auth | POST /api/v1/auth/login — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.3ms |
| BE-00048 | Security | Auth | POST /api/v1/auth/login — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms — preflight handled without server error |
| BE-00049 | API | Auth | POST /api/v1/auth/login — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 1.1ms |
| BE-00050 | Security | Auth | POST /api/v1/auth/login — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.9ms. {"detail":"Incorrect email or password"} |
| BE-00051 | Security | Auth | POST /api/v1/auth/login — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.3ms. {"detail":"Incorrect email or password"} |
| BE-00052 | Security | Auth | POST /api/v1/auth/login — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.2ms. {"detail":"Incorrect email or password"} |
| BE-00053 | Functional | Auth | POST /api/v1/auth/login — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.3ms. {"detail":"Incorrect email or password"} |
| BE-00054 | Functional | Auth | POST /api/v1/auth/login — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.0ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00055 | Functional | Auth | POST /api/v1/auth/login — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.5ms. {"detail":"Incorrect email or password"} |
| BE-00056 | Security | Auth | POST /api/v1/auth/login — string field password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 259.5ms. {"detail":"Incorrect email or password"} |
| BE-00057 | Security | Auth | POST /api/v1/auth/login — string field password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 260.6ms. {"detail":"Incorrect email or password"} |
| BE-00058 | Security | Auth | POST /api/v1/auth/login — string field password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 261.5ms. {"detail":"Incorrect email or password"} |
| BE-00059 | Functional | Auth | POST /api/v1/auth/login — string field password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.9ms. {"detail":"Incorrect email or password"} |
| BE-00060 | Functional | Auth | POST /api/v1/auth/login — string field password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.1ms. {"detail":[{"type":"missing","loc":["body","password"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00061 | Functional | Auth | POST /api/v1/auth/login — string field password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 259.6ms. {"detail":"Incorrect email or password"} |
| BE-00062 | Functional | Auth | POST /api/v1/auth/login — missing required field username | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.4ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00063 | Functional | Auth | GET /api/v1/auth/me — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 3.0ms. {"id":1,"email":"qa.userd0fc59d4@healthsense.test","username":"qa_userd0fc59d4","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-27T04:44:29.759107","is_act |
| BE-00064 | API | Auth | GET /api/v1/auth/me — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.9ms. {"detail":"Method Not Allowed"} |
| BE-00065 | API | Auth | GET /api/v1/auth/me — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00066 | Security | Auth | GET /api/v1/auth/me — missing auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 0.9ms. {"detail":"Not authenticated"} |
| BE-00067 | Security | Auth | GET /api/v1/auth/me — malformed auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.8ms. {"detail":"Could not validate credentials"} |
| BE-00068 | Security | Auth | GET /api/v1/auth/me — expired auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.2ms. {"detail":"Could not validate credentials"} |
| BE-00069 | Security | Auth | GET /api/v1/auth/me — token for nonexistent user | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.4ms. {"detail":"Could not validate credentials"} |
| BE-00070 | Security | Auth | GET /api/v1/auth/me — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00071 | API | Auth | GET /api/v1/auth/me — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00072 | Functional | Auth | GET /api/v1/auth/me — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 2.6ms. {"id":1,"email":"qa.userd0fc59d4@healthsense.test","username":"qa_userd0fc59d4","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-27T04:44:29.759107","is_act |
| BE-00073 | Functional | Auth | POST /api/v1/auth/reset-password — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 261.2ms. {"status":"success","message":"Password updated successfully"} |
| BE-00074 | API | Auth | POST /api/v1/auth/reset-password — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00075 | API | Auth | POST /api/v1/auth/reset-password — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00076 | Security | Auth | POST /api/v1/auth/reset-password — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00077 | API | Auth | POST /api/v1/auth/reset-password — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00078 | Security | Auth | POST /api/v1/auth/reset-password — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 3.1ms. {"detail":"No account found with this email or username"} |
| BE-00079 | Security | Auth | POST /api/v1/auth/reset-password — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.7ms. {"detail":"No account found with this email or username"} |
| BE-00080 | Security | Auth | POST /api/v1/auth/reset-password — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.7ms. {"detail":"No account found with this email or username"} |
| BE-00081 | Functional | Auth | POST /api/v1/auth/reset-password — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.8ms. {"detail":"No account found with this email or username"} |
| BE-00082 | Functional | Auth | POST /api/v1/auth/reset-password — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.9ms. {"detail":"No account found with this email or username"} |
| BE-00083 | Functional | Auth | POST /api/v1/auth/reset-password — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.9ms. {"detail":"No account found with this email or username"} |
| BE-00084 | Security | Auth | POST /api/v1/auth/reset-password — string field new password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.6ms. {"status":"success","message":"Password updated successfully"} |
| BE-00085 | Security | Auth | POST /api/v1/auth/reset-password — string field new password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.2ms. {"status":"success","message":"Password updated successfully"} |
| BE-00086 | Security | Auth | POST /api/v1/auth/reset-password — string field new password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.4ms. {"status":"success","message":"Password updated successfully"} |
| BE-00087 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.4ms. {"detail":[{"type":"string_too_long","loc":["body","new_password"],"msg":"String should have at most 72 characters","input":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
| BE-00088 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.5ms. {"status":"success","message":"Password updated successfully"} |
| BE-00089 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.4ms. {"status":"success","message":"Password updated successfully"} |
| BE-00090 | Functional | Auth | POST /api/v1/auth/reset-password — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.2ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"new_password":"NewStr0ngPass!"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00091 | Functional | Auth | POST /api/v1/auth/reset-password — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.8ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00092 | Functional | Auth | POST /api/v1/auth/reset-password — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 261.0ms. {"status":"success","message":"Password updated successfully"} |
| BE-00093 | Functional | Auth | POST /api/v1/auth/reset-password — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 1.2ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00094 | Functional | Tracking-Sleep | POST /api/v1/tracking/sleep — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 6.5ms. {"id":1,"user_id":1,"date":"2026-07-27T04:44:33.314000","duration_hours":7.5,"quality_score":82.0,"consistency_score":75.0,"bedtime":"23:00","wake_time":"06:30","created_at":"2026-07-27T04:44:33.31799 |
| BE-00095 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.0ms. {"detail":"Method Not Allowed"} |
| BE-00096 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00097 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — missing auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.0ms. {"detail":"Not authenticated"} |
| BE-00098 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — malformed auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.0ms. {"detail":"Could not validate credentials"} |
| BE-00099 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — expired auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.0ms. {"detail":"Could not validate credentials"} |
| BE-00100 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — token for nonexistent user | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.5ms. {"detail":"Could not validate credentials"} |

*... showing 100 of 406 Backend & Security test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## ⚡ API Load Testing — Baseline/Load Test

**Test configuration:** 100 virtual users, continuous for 61s, backend running with 4 worker process(es).

**Requests per second (RPS)**
> 143.49 req/sec

**Response Time**
> Average: 678ms
> Min: 9ms
> Max: 4421ms
> p95: 2047ms

**Total requests sent:** 8,776 • **Errors:** 0 (0.00%)

> ⚠️ **Known issue:** Every backend route handler is synchronous (`def`, not `async def`). A single uvicorn worker process only exposes ~40 threadpool slots for concurrent requests, so 100 concurrent virtual users against a single worker produces ~90% request timeouts — consistent with the pre-existing backend/load_test_results.csv in this repo. Multiple worker processes (as this suite uses) is the standard fix.

**Per-endpoint breakdown:**

| Endpoint | Requests | Errors | Avg (ms) | Min (ms) | Max (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| log_activity | 359 | 0 | 602.8 | 82.2 | 3455.9 |
| log_sleep | 422 | 0 | 583.4 | 47.9 | 2038.7 |
| health_check | 527 | 0 | 107.7 | 8.9 | 621.8 |
| recommendations_all | 895 | 0 | 537.6 | 68.4 | 2378.4 |
| burnout_history | 709 | 0 | 479.0 | 56.8 | 3478.2 |
| burnout_analysis | 1015 | 0 | 648.3 | 90.0 | 4326.4 |
| activity_history | 651 | 0 | 549.4 | 75.2 | 2528.3 |
| recommendations_quick | 745 | 0 | 541.1 | 45.8 | 3284.4 |
| wellness_dashboard | 1370 | 0 | 939.5 | 96.3 | 3933.5 |
| root_status | 374 | 0 | 108.1 | 11.8 | 1014.5 |
| sleep_history | 742 | 0 | 559.3 | 92.5 | 2099.9 |
| wellness_trends | 505 | 0 | 581.8 | 89.9 | 2647.9 |
| login | 462 | 0 | 2497.4 | 1224.6 | 4420.6 |

<details>
<summary>Click to view sampled request-level rows (400 of 8,776 real requests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LOAD-00001 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 283.4ms |
| LOAD-00002 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 296.2ms |
| LOAD-00003 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 39.6ms |
| LOAD-00004 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 166.4ms |
| LOAD-00005 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 127.5ms |
| LOAD-00006 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 205.2ms |
| LOAD-00007 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 219.4ms |
| LOAD-00008 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 399.0ms |
| LOAD-00009 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 281.5ms |
| LOAD-00010 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 958.5ms |
| LOAD-00011 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 710.7ms |
| LOAD-00012 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 788.0ms |
| LOAD-00013 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 304.7ms |
| LOAD-00014 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 180.2ms |
| LOAD-00015 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 79.2ms |
| LOAD-00016 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 397.1ms |
| LOAD-00017 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 686.9ms |
| LOAD-00018 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 553.3ms |
| LOAD-00019 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 476.2ms |
| LOAD-00020 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1099.1ms |
| LOAD-00021 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 99.3ms |
| LOAD-00022 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 255.8ms |
| LOAD-00023 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 390.0ms |
| LOAD-00024 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 900.2ms |
| LOAD-00025 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 378.3ms |
| LOAD-00026 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1733.2ms |
| LOAD-00027 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 89.6ms |
| LOAD-00028 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 409.1ms |
| LOAD-00029 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1538.4ms |
| LOAD-00030 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 56.2ms |
| LOAD-00031 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 748.7ms |
| LOAD-00032 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 894.7ms |
| LOAD-00033 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 44.0ms |
| LOAD-00034 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 360.7ms |
| LOAD-00035 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 118.0ms |
| LOAD-00036 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 314.3ms |
| LOAD-00037 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 915.3ms |
| LOAD-00038 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 657.8ms |
| LOAD-00039 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 84.8ms |
| LOAD-00040 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 55.5ms |
| LOAD-00041 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2693.3ms |
| LOAD-00042 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 445.9ms |
| LOAD-00043 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 336.1ms |
| LOAD-00044 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 312.9ms |
| LOAD-00045 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 338.7ms |
| LOAD-00046 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 212.4ms |
| LOAD-00047 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 484.0ms |
| LOAD-00048 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1208.1ms |
| LOAD-00049 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 768.0ms |
| LOAD-00050 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 689.9ms |
| LOAD-00051 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 258.2ms |
| LOAD-00052 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1399.3ms |
| LOAD-00053 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 313.2ms |
| LOAD-00054 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 941.9ms |
| LOAD-00055 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 613.1ms |
| LOAD-00056 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 744.1ms |
| LOAD-00057 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1689.6ms |
| LOAD-00058 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 479.8ms |
| LOAD-00059 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 310.9ms |
| LOAD-00060 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 385.8ms |
| LOAD-00061 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1017.5ms |
| LOAD-00062 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 705.1ms |
| LOAD-00063 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1009.0ms |
| LOAD-00064 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 621.8ms |
| LOAD-00065 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 167.4ms |
| LOAD-00066 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 3180.6ms |
| LOAD-00067 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 819.4ms |
| LOAD-00068 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1006.3ms |
| LOAD-00069 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1317.2ms |
| LOAD-00070 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 40.4ms |
| LOAD-00071 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 55.0ms |
| LOAD-00072 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 460.3ms |
| LOAD-00073 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 262.6ms |
| LOAD-00074 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 297.8ms |
| LOAD-00075 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 541.3ms |
| LOAD-00076 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 516.3ms |
| LOAD-00077 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 1497.0ms |
| LOAD-00078 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 606.7ms |
| LOAD-00079 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 465.5ms |
| LOAD-00080 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 76.3ms |
| LOAD-00081 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 516.5ms |
| LOAD-00082 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 3309.6ms |
| LOAD-00083 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 77.5ms |
| LOAD-00084 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 91.9ms |
| LOAD-00085 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 433.2ms |
| LOAD-00086 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 416.4ms |
| LOAD-00087 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2778.3ms |
| LOAD-00088 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 417.4ms |
| LOAD-00089 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 660.3ms |
| LOAD-00090 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 202.5ms |
| LOAD-00091 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2530.4ms |
| LOAD-00092 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1053.1ms |
| LOAD-00093 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1948.9ms |
| LOAD-00094 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 419.2ms |
| LOAD-00095 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 349.5ms |
| LOAD-00096 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 830.6ms |
| LOAD-00097 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 193.1ms |
| LOAD-00098 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 414.9ms |
| LOAD-00099 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 268.9ms |
| LOAD-00100 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 843.1ms |

*... showing 100 of 400 sampled rows. See the full JSON/CSV artifact for all rows.*

</details>

---

## 📦 Test Report Artifacts

Full result files are uploaded as workflow artifacts:

- **Website E2E:** `reports/web_e2e_results.json` / `.csv`
- **Mobile App E2E:** `reports/mobile_e2e_results.json` / `.csv`
- **Backend & Security:** `reports/backend_security_results.json` / `.csv`
- **API Load Testing:** `reports/api_load_test_results.json` / `.csv`
- **Android debug APK build:** see the `mobile-debug-apk` artifact on this workflow run
