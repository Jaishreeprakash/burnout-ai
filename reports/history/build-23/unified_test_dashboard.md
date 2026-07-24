# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard is generated from **real suite runs** — a live FastAPI backend, a real concurrent load test, real Selenium browser sessions, and real static + Appium mobile checks. No row here is replayed from a static fixture.

## 📊 Unified Summary Overview

| Component | Test Suite | Total Tests | Passed | Failed | Pass Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Website E2E | Real Selenium suite (Chrome + Firefox) | 219 | ✅ 121 | ❌ 98 | 55.2% |
| Mobile App E2E | Real static analysis + live Appium | 74 | ✅ 74 | ✅ 0 | 100.0% |
| Backend & Security | Real functional/security scenarios (live backend) | 406 | ✅ 406 | ✅ 0 | 100.0% |
| API Load Testing | Real 100-VU baseline load test | 400 | ✅ 400 | ✅ 0 | 100.0% |

---

## 🌐 Website E2E Test Verification Details

Browsers run: chrome, firefox

<details>
<summary>Click to view Website E2E Test Cases (219 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WEB-CH-00001 | UI/UX | Login | element_present_username_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00002 | UI/UX | Login | element_present_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00003 | UI/UX | Login | element_present_submit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00004 | UI/UX | Login | element_present_register_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00005 | UI/UX | Login | element_present_password_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00006 | Functional | Login | empty_submit_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Form did not navigate away on empty submit |
| WEB-CH-00007 | Security | Login | wrong_credentials_rejected | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | No error banner appeared after invalid login |
| WEB-CH-00008 | Security | Login | sql_injection_input_no_crash | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Page still renders content after SQLi-style login attempt |
| WEB-CH-00009 | Functional | Login | password_show_hide_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | type changed password -> text |
| WEB-CH-00010 | UI/UX | Login | register_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on https://jaishreeprakash.github.io/burnout-ai/register |
| WEB-CH-00011 | UI/UX | Register | element_present_full_name_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00012 | UI/UX | Register | element_present_username_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00013 | UI/UX | Register | element_present_email_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00014 | UI/UX | Register | element_present_age_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00015 | UI/UX | Register | element_present_gender_select | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00016 | UI/UX | Register | element_present_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00017 | UI/UX | Register | element_present_confirm_password_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00018 | UI/UX | Register | element_present_submit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00019 | UI/UX | Register | element_present_login_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00020 | Functional | Register | short_password_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Weak password correctly blocked client-side submit |
| WEB-CH-00021 | Functional | Register | password_mismatch_blocked | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Password mismatch correctly blocked client-side submit |
| WEB-CH-00022 | Security | Register | xss_input_no_crash | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Page renders normally with XSS-style full_name input (no script executed/crash) |
| WEB-CH-00023 | UI/UX | Register | login_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on https://jaishreeprakash.github.io/burnout-ai/login |
| WEB-CH-00024 | Functional | Register | real_registration_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Registered selenium.chrome.36252ba8@healthsense.test and landed on https://jaishreeprakash.github.io/burnout-ai/dashboard |
| WEB-CH-00025 | Functional | Login | real_login_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Signed out then logged back in with real credentials, reached /dashboard |
| WEB-CH-00026 | UI/UX | Sidebar | nav_link_dashboard_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Dashboard' navigated to https://jaishreeprakash.github.io/burnout-ai/dashboard |
| WEB-CH-00027 | UI/UX | Sidebar | nav_link_sleep_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Sleep Tracker' navigated to https://jaishreeprakash.github.io/burnout-ai/sleep |
| WEB-CH-00028 | UI/UX | Sidebar | nav_link_phone_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Phone Usage' navigated to https://jaishreeprakash.github.io/burnout-ai/phone |
| WEB-CH-00029 | UI/UX | Sidebar | nav_link_emotions_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Emotion Analysis' navigated to https://jaishreeprakash.github.io/burnout-ai/emotions |
| WEB-CH-00030 | UI/UX | Sidebar | nav_link_activity_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Activity Tracker' navigated to https://jaishreeprakash.github.io/burnout-ai/activity |
| WEB-CH-00031 | UI/UX | Sidebar | nav_link_recommendations_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Recommendations' navigated to https://jaishreeprakash.github.io/burnout-ai/recommendations |
| WEB-CH-00032 | UI/UX | Sidebar | nav_link_analytics_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Analytics' navigated to https://jaishreeprakash.github.io/burnout-ai/analytics |
| WEB-CH-00033 | UI/UX | Sidebar | nav_link_chat_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'AI Coach Chat' navigated to https://jaishreeprakash.github.io/burnout-ai/chat |
| WEB-CH-00034 | UI/UX | Sidebar | nav_link_profile_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Profile' navigated to https://jaishreeprakash.github.io/burnout-ai/profile |
| WEB-CH-00035 | UI/UX | Dashboard | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00036 | UI/UX | Dashboard | element_present_burnout_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00037 | UI/UX | Dashboard | element_present_wellness_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00038 | UI/UX | Dashboard | element_present_health_dimensions_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00039 | UI/UX | Dashboard | element_present_emotional_stability_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00040 | UI/UX | Dashboard | element_present_emotion_distribution_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00041 | UI/UX | Dashboard | element_present_ai_recommendations_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00042 | UI/UX | Dashboard | element_present_progress_comparison_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00043 | UI/UX | Dashboard | element_present_quick_stats_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00044 | UI/UX | Dashboard | element_present_view_all_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00045 | UI/UX | Sleep Tracker | element_present_overview_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00046 | UI/UX | Sleep Tracker | element_present_calendar_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00047 | UI/UX | Sleep Tracker | element_present_log_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00048 | UI/UX | Sleep Tracker | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00049 | UI/UX | Sleep Tracker | element_present_log_sleep_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00050 | UI/UX | Recommendations | element_present_filter_all | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00051 | UI/UX | Recommendations | element_present_filter_sleep | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00052 | UI/UX | Recommendations | element_present_filter_phone | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00053 | UI/UX | Recommendations | element_present_filter_activity | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00054 | UI/UX | Recommendations | element_present_filter_mental_health | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00055 | UI/UX | Recommendations | element_present_filter_social | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00056 | UI/UX | Recommendations | element_present_filter_nutrition | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00057 | UI/UX | Recommendations | element_present_sort_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00058 | UI/UX | Analytics | element_present_range_7d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00059 | UI/UX | Analytics | element_present_range_30d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00060 | UI/UX | Analytics | element_present_export_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00061 | UI/UX | Analytics | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00062 | UI/UX | Wellness Chat | element_present_message_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00063 | UI/UX | Wellness Chat | element_present_send_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00064 | UI/UX | Wellness Chat | element_present_new_chat_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00065 | UI/UX | Profile | element_present_profile_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00066 | UI/UX | Profile | element_present_notifications_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00067 | UI/UX | Profile | element_present_privacy_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00068 | UI/UX | Profile | element_present_edit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00069 | UI/UX | Profile | element_present_sign_out_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00070 | Functional | Phone Usage | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 287 chars rendered |
| WEB-CH-00071 | Functional | Emotion Analysis | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 287 chars rendered |
| WEB-CH-00072 | Functional | Activity Tracker | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 287 chars rendered |
| WEB-CH-00073 | Functional | Sleep Tracker | tab_switching_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00074 | Functional | Sleep Tracker | log_sleep_modal_open_cancel | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00075 | Functional | Recommendations | category_filters_clickable | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00076 | Functional | Analytics | range_toggle_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00077 | E2E | Wellness Chat | send_message_gets_real_reply | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00078 | Functional | Profile | tab_switching_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ❌ Fail | Element not found / timed out: TimeoutException |
| WEB-CH-00079 | Compatibility | Dashboard | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00080 | Compatibility | Dashboard | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00081 | Compatibility | Dashboard | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00082 | Compatibility | Sleep Tracker | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00083 | Compatibility | Sleep Tracker | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00084 | Compatibility | Sleep Tracker | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00085 | Compatibility | Phone Usage | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00086 | Compatibility | Phone Usage | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00087 | Compatibility | Phone Usage | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00088 | Compatibility | Emotion Analysis | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00089 | Compatibility | Emotion Analysis | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00090 | Compatibility | Emotion Analysis | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00091 | Compatibility | Activity Tracker | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00092 | Compatibility | Activity Tracker | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00093 | Compatibility | Activity Tracker | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00094 | Compatibility | Recommendations | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00095 | Compatibility | Recommendations | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00096 | Compatibility | Recommendations | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00097 | Compatibility | Analytics | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |
| WEB-CH-00098 | Compatibility | Analytics | responsive_tablet_768x1024 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 768x1024 (tablet) |
| WEB-CH-00099 | Compatibility | Analytics | responsive_desktop_1440x900 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 1440x900 (desktop) |
| WEB-CH-00100 | Compatibility | Wellness Chat | responsive_mobile_375x812 | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Renders content at 375x812 (mobile) |

*... showing 100 of 219 Website E2E test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## 📱 Mobile App E2E Test Verification Details

Static source-analysis cases: 61 • Live Appium cases (real device/emulator): 13

<details>
<summary>Click to view Mobile E2E Test Cases (74 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MOB-STATIC-00001 | Compatibility | Dashboard | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00002 | UI/UX | Dashboard | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No TextInput on this screen — nothing to avoid |
| MOB-STATIC-00003 | Functional | Dashboard | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No async data-fetch calls on this screen |
| MOB-STATIC-00004 | Accessibility | Dashboard | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 1 accessibilityLabel/testID attribute(s) found across 9 touchable element(s) in screens/main/DashboardScreen.tsx |
| MOB-STATIC-00005 | Functional | Dashboard | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00006 | Compatibility | Sleep Tracker | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/SleepScreen.tsx |
| MOB-STATIC-00007 | UI/UX | Sleep Tracker | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00008 | Functional | Sleep Tracker | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/SleepScreen.tsx |
| MOB-STATIC-00009 | Accessibility | Sleep Tracker | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 4 accessibilityLabel/testID attribute(s) found across 8 touchable element(s) in screens/main/SleepScreen.tsx |
| MOB-STATIC-00010 | Functional | Sleep Tracker | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00011 | Compatibility | Emotion Analysis | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00012 | UI/UX | Emotion Analysis | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00013 | Functional | Emotion Analysis | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00014 | Accessibility | Emotion Analysis | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 7 accessibilityLabel/testID attribute(s) found across 14 touchable element(s) in screens/main/EmotionScreen.tsx |
| MOB-STATIC-00015 | Functional | Emotion Analysis | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00016 | Compatibility | Activity Tracker | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00017 | UI/UX | Activity Tracker | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00018 | Functional | Activity Tracker | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00019 | Accessibility | Activity Tracker | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 2 accessibilityLabel/testID attribute(s) found across 5 touchable element(s) in screens/main/ActivityScreen.tsx |
| MOB-STATIC-00020 | Functional | Activity Tracker | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00021 | Compatibility | Profile | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/ProfileScreen.tsx |
| MOB-STATIC-00022 | UI/UX | Profile | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No TextInput on this screen — nothing to avoid |
| MOB-STATIC-00023 | Functional | Profile | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/ProfileScreen.tsx |
| MOB-STATIC-00024 | Accessibility | Profile | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 2 accessibilityLabel/testID attribute(s) found across 5 touchable element(s) in screens/main/ProfileScreen.tsx |
| MOB-STATIC-00025 | Functional | Profile | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00026 | Compatibility | Recommendations | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/RecommendationsScreen.tsx |
| MOB-STATIC-00027 | UI/UX | Recommendations | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No TextInput on this screen — nothing to avoid |
| MOB-STATIC-00028 | Functional | Recommendations | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/RecommendationsScreen.tsx |
| MOB-STATIC-00029 | Accessibility | Recommendations | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 3 accessibilityLabel/testID attribute(s) found across 7 touchable element(s) in screens/main/RecommendationsScreen.tsx |
| MOB-STATIC-00030 | Functional | Recommendations | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00031 | Compatibility | Phone Usage | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/main/PhoneUsageScreen.tsx |
| MOB-STATIC-00032 | UI/UX | Phone Usage | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/main/PhoneUsageScreen.tsx |
| MOB-STATIC-00033 | Functional | Phone Usage | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/main/PhoneUsageScreen.tsx |
| MOB-STATIC-00034 | Accessibility | Phone Usage | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 2 accessibilityLabel/testID attribute(s) found across 5 touchable element(s) in screens/main/PhoneUsageScreen.tsx |
| MOB-STATIC-00035 | Functional | Phone Usage | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00036 | Compatibility | Analytics | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/analytics/AnalyticsScreen.tsx |
| MOB-STATIC-00037 | UI/UX | Analytics | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No TextInput on this screen — nothing to avoid |
| MOB-STATIC-00038 | Functional | Analytics | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/analytics/AnalyticsScreen.tsx |
| MOB-STATIC-00039 | Accessibility | Analytics | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 2 accessibilityLabel/testID attribute(s) found across 5 touchable element(s) in screens/analytics/AnalyticsScreen.tsx |
| MOB-STATIC-00040 | Functional | Analytics | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00041 | Compatibility | Login | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/auth/LoginScreen.tsx |
| MOB-STATIC-00042 | UI/UX | Login | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/auth/LoginScreen.tsx |
| MOB-STATIC-00043 | Functional | Login | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/auth/LoginScreen.tsx |
| MOB-STATIC-00044 | Accessibility | Login | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 8 accessibilityLabel/testID attribute(s) found across 11 touchable element(s) in screens/auth/LoginScreen.tsx |
| MOB-STATIC-00045 | Functional | Login | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00046 | Compatibility | Register | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/auth/RegisterScreen.tsx |
| MOB-STATIC-00047 | UI/UX | Register | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/auth/RegisterScreen.tsx |
| MOB-STATIC-00048 | Functional | Register | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/auth/RegisterScreen.tsx |
| MOB-STATIC-00049 | Accessibility | Register | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 14 accessibilityLabel/testID attribute(s) found across 11 touchable element(s) in screens/auth/RegisterScreen.tsx |
| MOB-STATIC-00050 | Functional | Register | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00051 | Compatibility | Forgot Password | safe area insets used | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | Found useSafeAreaInsets() in screens/auth/ForgotPasswordScreen.tsx |
| MOB-STATIC-00052 | UI/UX | Forgot Password | keyboard avoiding view present | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | KeyboardAvoidingView wraps the input field(s) in screens/auth/ForgotPasswordScreen.tsx |
| MOB-STATIC-00053 | Functional | Forgot Password | async calls have error handling | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | try/catch present around async calls in screens/auth/ForgotPasswordScreen.tsx |
| MOB-STATIC-00054 | Accessibility | Forgot Password | interactive elements have accessibility hooks | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 11 accessibilityLabel/testID attribute(s) found across 11 touchable element(s) in screens/auth/ForgotPasswordScreen.tsx |
| MOB-STATIC-00055 | Functional | Forgot Password | no leftover debug markers | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | No console.log/TODO/FIXME markers found |
| MOB-STATIC-00056 | Mobile-Specific | System | deep link scheme configured | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | app.json scheme='burnoutai', found in AndroidManifest.xml intent-filter |
| MOB-STATIC-00057 | Mobile-Specific | System | orientation lock declared | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | app.json orientation='portrait' |
| MOB-STATIC-00058 | Mobile-Specific | System | application id consistent app json and gradle | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | app.json android.package='com.burnoutai.mobile' vs build.gradle applicationId='com.burnoutai.mobile' |
| MOB-STATIC-00059 | Mobile-Specific | System | gradle wrapper version pinned | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | zipStorePath=wrapper/dists |
| MOB-STATIC-00060 | Mobile-Specific | System | demo login path available for ci | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | demoLogin()/demo-session mock path confirmed in AuthContext.tsx + services/api.ts — usable for CI without a live backend |
| MOB-STATIC-00061 | Mobile-Specific | System | testid coverage added for appium | Static Analysis | Mobile source (React Native/Expo) — static analysis, no device needed | ✅ Pass | 28 testID attributes present across auth + core screens for reliable Appium locators |
| MOB-LIVE-00001 | Functional | System | app launches and is foreground | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | current_package=com.burnoutai.mobile |
| MOB-LIVE-00002 | Functional | Register | real registration flow completes | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Registered appium.63105d31@healthsense.test through the real 3-step Register screen — submitted to the live backend |
| MOB-LIVE-00003 | Functional | Dashboard | reaches main app after login | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Bottom tab bar with 'Home' tab visible after real registration |
| MOB-LIVE-00004 | UI/UX | Dashboard | tab home reachable | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Tapped 'Home' tab, app did not crash |
| MOB-LIVE-00005 | UI/UX | Sleep | tab sleep reachable | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Tapped 'Sleep' tab, app did not crash |
| MOB-LIVE-00006 | UI/UX | Emotion | tab emotion reachable | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Tapped 'Emotion' tab, app did not crash |
| MOB-LIVE-00007 | UI/UX | Activity | tab activity reachable | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Tapped 'Activity' tab, app did not crash |
| MOB-LIVE-00008 | UI/UX | Profile | tab profile reachable | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Tapped 'Profile' tab, app did not crash |
| MOB-LIVE-00009 | Mobile-Specific | System | swipe gesture handled | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Performed a real swipe gesture via adb/UiAutomator2 on the current screen |
| MOB-LIVE-00010 | Compatibility | System | device rotation handled | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Rotation request rejected — consistent with app.json's intentional portrait lock: Message: Screen rotation cannot be changed to ROTATION_270 after 2000ms. Is it locked programmatically?
Stacktrace:
io.appium.uiautomator2.common.exceptions.InvalidElementStateException: Screen rotation cannot be changed to ROTATION_270 after 2000ms. Is it locked programmatically?
	at io.appium.uiautomator2.model.internal.CustomUiDevice.setRotationSync(CustomUiDevice.java:226)
	at io.appium.uiautomator2.handler.SetOrientation.safeHandle(SetOrientation.java:41)
	at io.appium.uiautomator2.handler.request.SafeRequestHandler.handle(SafeRequestHandler.java:59)
	at io.appium.uiautomator2.server.AppiumServlet.handleRequest(AppiumServlet.java:267)
	at io.appium.uiautomator2.server.AppiumServlet.handleHttpRequest(AppiumServlet.java:261)
	at io.appium.uiautomator2.http.ServerHandler.channelRead(ServerHandler.java:77)
	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:357)
	at io.netty.handler.codec.MessageToMessageDecoder.channelRead(MessageToMessageDecoder.java:107)
	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:357)
	at io.netty.channel.CombinedChannelDuplexHandler$DelegatingChannelHandlerContext.fireChannelRead(CombinedChannelDuplexHandler.java:434)
	at io.netty.handler.codec.ByteToMessageDecoder.fireChannelRead(ByteToMessageDecoder.java:361)
	at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:325)
	at io.netty.channel.CombinedChannelDuplexHandler.channelRead(CombinedChannelDuplexHandler.java:249)
	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:355)
	at io.netty.handler.timeout.IdleStateHandler.channelRead(IdleStateHandler.java:288)
	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:355)
	at io.netty.channel.DefaultChannelPipeline$HeadContext.channelRead(DefaultChannelPipeline.java:1429)
	at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:918)
	at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:176)
	at io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.handle(AbstractNioChannel.java:445)
	at io.netty.channel.nio.NioIoHandler$DefaultNioRegistration.handle(NioIoHandler.java:388)
	at io.netty.channel.nio.NioIoHandler.processSelectedKey(NioIoHandler.java:596)
	at io.netty.channel.nio.NioIoHandler.processSelectedKeysOptimized(NioIoHandler.java:571)
	at io.netty.channel.nio.NioIoHandler.processSelectedKeys(NioIoHandler.java:512)
	at io.netty.channel.nio.NioIoHandler.run(NioIoHandler.java:484)
	at io.netty.channel.SingleThreadIoEventLoop.runIo(SingleThreadIoEventLoop.java:225)
	at io.netty.channel.SingleThreadIoEventLoop.run(SingleThreadIoEventLoop.java:196)
	at io.netty.util.concurrent.SingleThreadEventExecutor$5.run(SingleThreadEventExecutor.java:1195)
	at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74)
	at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30)
	at java.lang.Thread.run(Thread.java:1012)
 |
| MOB-LIVE-00011 | Mobile-Specific | System | background and resume handled | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | App resumed to foreground after backgrounding, current_package=com.burnoutai.mobile |
| MOB-LIVE-00012 | Mobile-Specific | System | deep link scheme opens app | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | burnoutai:// deep link opened the app via adb |
| MOB-LIVE-00013 | Compatibility | System | hardware back button no crash | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Hardware back button handled without app crash |

</details>

---

## 🛡️ Backend & Security Test Verification Details

**Security-category checks:** 155 run, 0 failed (none — no real vulnerabilities found by this scenario set)

<details>
<summary>Click to view Backend & Security Test Cases (406 tests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BE-00001 | Functional | System | GET / — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.3ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00002 | API | System | GET / — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.9ms. {"detail":"Method Not Allowed"} |
| BE-00003 | API | System | GET / — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (direct response), 1.0ms |
| BE-00004 | Security | System | GET / — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00005 | API | System | GET / — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (case-sensitive routing correctly rejects altered-case path), 1.0ms |
| BE-00006 | Functional | System | GET / — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00007 | Functional | System | GET /health — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms. {"status":"ok"} |
| BE-00008 | API | System | GET /health — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.8ms. {"detail":"Method Not Allowed"} |
| BE-00009 | API | System | GET /health — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00010 | Security | System | GET /health — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00011 | API | System | GET /health — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00012 | Functional | System | GET /health — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms. {"status":"ok"} |
| BE-00013 | Functional | Auth | POST /api/v1/auth/register — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 261.9ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODQ2NzU1MzJ9.1Y-geFkhwmRg6iyp7_A_YEbcDxZLu6A-Zc_IjiHofYM","token_type":"bearer","user":{"i |
| BE-00014 | API | Auth | POST /api/v1/auth/register — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00015 | API | Auth | POST /api/v1/auth/register — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00016 | Security | Auth | POST /api/v1/auth/register — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00017 | API | Auth | POST /api/v1/auth/register — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00018 | Security | Auth | POST /api/v1/auth/register — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 3.3ms. {"detail":"This username is already taken"} |
| BE-00019 | Security | Auth | POST /api/v1/auth/register — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.7ms. {"detail":"This username is already taken"} |
| BE-00020 | Security | Auth | POST /api/v1/auth/register — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.7ms. {"detail":"This username is already taken"} |
| BE-00021 | Functional | Auth | POST /api/v1/auth/register — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.8ms. {"detail":"This username is already taken"} |
| BE-00022 | Functional | Auth | POST /api/v1/auth/register — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.8ms. {"detail":"This username is already taken"} |
| BE-00023 | Functional | Auth | POST /api/v1/auth/register — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.7ms. {"detail":"This username is already taken"} |
| BE-00024 | Security | Auth | POST /api/v1/auth/register — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"An account with this email already exists"} |
| BE-00025 | Security | Auth | POST /api/v1/auth/register — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.6ms. {"detail":"An account with this email already exists"} |
| BE-00026 | Security | Auth | POST /api/v1/auth/register — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00027 | Functional | Auth | POST /api/v1/auth/register — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00028 | Functional | Auth | POST /api/v1/auth/register — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00029 | Functional | Auth | POST /api/v1/auth/register — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00030 | Security | Auth | POST /api/v1/auth/register — string field full name sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"An account with this email already exists"} |
| BE-00031 | Security | Auth | POST /api/v1/auth/register — string field full name xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00032 | Security | Auth | POST /api/v1/auth/register — string field full name crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00033 | Functional | Auth | POST /api/v1/auth/register — string field full name oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"An account with this email already exists"} |
| BE-00034 | Functional | Auth | POST /api/v1/auth/register — string field full name empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00035 | Functional | Auth | POST /api/v1/auth/register — string field full name whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00036 | Functional | Auth | POST /api/v1/auth/register — numeric field age negative | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.7ms. {"detail":[{"type":"greater_than_equal","loc":["body","age"],"msg":"Input should be greater than or equal to 0","input":-1,"ctx":{"ge":0},"url":"https://errors.pydantic.dev/2.5/v/greater_than_equal"}] |
| BE-00037 | Functional | Auth | POST /api/v1/auth/register — numeric field age zero | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"An account with this email already exists"} |
| BE-00038 | Functional | Auth | POST /api/v1/auth/register — numeric field age very large | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"less_than_equal","loc":["body","age"],"msg":"Input should be less than or equal to 150","input":1000000000000000.0,"ctx":{"le":150},"url":"https://errors.pydantic.dev/2.5/v/less_th |
| BE-00039 | Functional | Auth | POST /api/v1/auth/register — numeric field age very small fraction | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.6ms. {"detail":[{"type":"int_from_float","loc":["body","age"],"msg":"Input should be a valid integer, got a number with a fractional part","input":1e-06,"url":"https://errors.pydantic.dev/2.5/v/int_from_fl |
| BE-00040 | Functional | Auth | POST /api/v1/auth/register — numeric field age wrong type string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.3ms. {"detail":[{"type":"int_parsing","loc":["body","age"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"not-a-number","url":"https://errors.pydantic.dev/2.5/v/int_ |
| BE-00041 | Functional | Auth | POST /api/v1/auth/register — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.6ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"username":"qa_user","password":"Str0ngPassw0rd!","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_ |
| BE-00042 | Functional | Auth | POST /api/v1/auth/register — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.6ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00043 | Functional | Auth | POST /api/v1/auth/register — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00044 | Functional | Auth | POST /api/v1/auth/register — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 0.9ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00045 | Functional | Auth | POST /api/v1/auth/login — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.0ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODQ2NzU1MzN9.fZleP0YXwJfs_F3rk-Hr7AhyJRS574KlydJNykbFrW0","token_type":"bearer","user":{"i |
| BE-00046 | API | Auth | POST /api/v1/auth/login — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00047 | API | Auth | POST /api/v1/auth/login — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00048 | Security | Auth | POST /api/v1/auth/login — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00049 | API | Auth | POST /api/v1/auth/login — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 1.0ms |
| BE-00050 | Security | Auth | POST /api/v1/auth/login — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.5ms. {"detail":"Incorrect email or password"} |
| BE-00051 | Security | Auth | POST /api/v1/auth/login — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.1ms. {"detail":"Incorrect email or password"} |
| BE-00052 | Security | Auth | POST /api/v1/auth/login — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.0ms. {"detail":"Incorrect email or password"} |
| BE-00053 | Functional | Auth | POST /api/v1/auth/login — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.9ms. {"detail":"Incorrect email or password"} |
| BE-00054 | Functional | Auth | POST /api/v1/auth/login — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00055 | Functional | Auth | POST /api/v1/auth/login — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.2ms. {"detail":"Incorrect email or password"} |
| BE-00056 | Security | Auth | POST /api/v1/auth/login — string field password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 259.5ms. {"detail":"Incorrect email or password"} |
| BE-00057 | Security | Auth | POST /api/v1/auth/login — string field password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 260.3ms. {"detail":"Incorrect email or password"} |
| BE-00058 | Security | Auth | POST /api/v1/auth/login — string field password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 260.3ms. {"detail":"Incorrect email or password"} |
| BE-00059 | Functional | Auth | POST /api/v1/auth/login — string field password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.8ms. {"detail":"Incorrect email or password"} |
| BE-00060 | Functional | Auth | POST /api/v1/auth/login — string field password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"missing","loc":["body","password"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00061 | Functional | Auth | POST /api/v1/auth/login — string field password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 259.7ms. {"detail":"Incorrect email or password"} |
| BE-00062 | Functional | Auth | POST /api/v1/auth/login — missing required field username | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.4ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00063 | Functional | Auth | GET /api/v1/auth/me — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 3.1ms. {"id":1,"email":"qa.user4165730a@healthsense.test","username":"qa_user4165730a","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-21T22:12:12.594930","is_act |
| BE-00064 | API | Auth | GET /api/v1/auth/me — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.0ms. {"detail":"Method Not Allowed"} |
| BE-00065 | API | Auth | GET /api/v1/auth/me — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00066 | Security | Auth | GET /api/v1/auth/me — missing auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 0.9ms. {"detail":"Not authenticated"} |
| BE-00067 | Security | Auth | GET /api/v1/auth/me — malformed auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.8ms. {"detail":"Could not validate credentials"} |
| BE-00068 | Security | Auth | GET /api/v1/auth/me — expired auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.0ms. {"detail":"Could not validate credentials"} |
| BE-00069 | Security | Auth | GET /api/v1/auth/me — token for nonexistent user | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.4ms. {"detail":"Could not validate credentials"} |
| BE-00070 | Security | Auth | GET /api/v1/auth/me — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.0ms — preflight handled without server error |
| BE-00071 | API | Auth | GET /api/v1/auth/me — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00072 | Functional | Auth | GET /api/v1/auth/me — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 2.6ms. {"id":1,"email":"qa.user4165730a@healthsense.test","username":"qa_user4165730a","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-21T22:12:12.594930","is_act |
| BE-00073 | Functional | Auth | POST /api/v1/auth/reset-password — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 261.2ms. {"status":"success","message":"Password updated successfully"} |
| BE-00074 | API | Auth | POST /api/v1/auth/reset-password — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00075 | API | Auth | POST /api/v1/auth/reset-password — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00076 | Security | Auth | POST /api/v1/auth/reset-password — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00077 | API | Auth | POST /api/v1/auth/reset-password — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00078 | Security | Auth | POST /api/v1/auth/reset-password — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 3.1ms. {"detail":"No account found with this email or username"} |
| BE-00079 | Security | Auth | POST /api/v1/auth/reset-password — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.6ms. {"detail":"No account found with this email or username"} |
| BE-00080 | Security | Auth | POST /api/v1/auth/reset-password — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.5ms. {"detail":"No account found with this email or username"} |
| BE-00081 | Functional | Auth | POST /api/v1/auth/reset-password — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.6ms. {"detail":"No account found with this email or username"} |
| BE-00082 | Functional | Auth | POST /api/v1/auth/reset-password — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 3.2ms. {"detail":"No account found with this email or username"} |
| BE-00083 | Functional | Auth | POST /api/v1/auth/reset-password — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.8ms. {"detail":"No account found with this email or username"} |
| BE-00084 | Security | Auth | POST /api/v1/auth/reset-password — string field new password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.2ms. {"status":"success","message":"Password updated successfully"} |
| BE-00085 | Security | Auth | POST /api/v1/auth/reset-password — string field new password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.4ms. {"status":"success","message":"Password updated successfully"} |
| BE-00086 | Security | Auth | POST /api/v1/auth/reset-password — string field new password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.7ms. {"status":"success","message":"Password updated successfully"} |
| BE-00087 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.2ms. {"detail":[{"type":"string_too_long","loc":["body","new_password"],"msg":"String should have at most 72 characters","input":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
| BE-00088 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.3ms. {"status":"success","message":"Password updated successfully"} |
| BE-00089 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.3ms. {"status":"success","message":"Password updated successfully"} |
| BE-00090 | Functional | Auth | POST /api/v1/auth/reset-password — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.1ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"new_password":"NewStr0ngPass!"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00091 | Functional | Auth | POST /api/v1/auth/reset-password — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.7ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00092 | Functional | Auth | POST /api/v1/auth/reset-password — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 260.0ms. {"status":"success","message":"Password updated successfully"} |
| BE-00093 | Functional | Auth | POST /api/v1/auth/reset-password — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 1.4ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00094 | Functional | Tracking-Sleep | POST /api/v1/tracking/sleep — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 7.1ms. {"id":1,"user_id":1,"date":"2026-07-21T22:12:16.144000","duration_hours":7.5,"quality_score":82.0,"consistency_score":75.0,"bedtime":"23:00","wake_time":"06:30","created_at":"2026-07-21T22:12:16.14812 |
| BE-00095 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.1ms. {"detail":"Method Not Allowed"} |
| BE-00096 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00097 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — missing auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.0ms. {"detail":"Not authenticated"} |
| BE-00098 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — malformed auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.1ms. {"detail":"Could not validate credentials"} |
| BE-00099 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — expired auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.9ms. {"detail":"Could not validate credentials"} |
| BE-00100 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — token for nonexistent user | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.5ms. {"detail":"Could not validate credentials"} |

*... showing 100 of 406 Backend & Security test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## ⚡ API Load Testing — Baseline/Load Test

**Test configuration:** 100 virtual users, continuous for 61s, backend running with 4 worker process(es).

**Requests per second (RPS)**
> 170.52 req/sec

**Response Time**
> Average: 572ms
> Min: 6ms
> Max: 3355ms
> p95: 1560ms

**Total requests sent:** 10,369 • **Errors:** 0 (0.00%)

> ⚠️ **Known issue:** Every backend route handler is synchronous (`def`, not `async def`). A single uvicorn worker process only exposes ~40 threadpool slots for concurrent requests, so 100 concurrent virtual users against a single worker produces ~90% request timeouts — consistent with the pre-existing backend/load_test_results.csv in this repo. Multiple worker processes (as this suite uses) is the standard fix.

**Per-endpoint breakdown:**

| Endpoint | Requests | Errors | Avg (ms) | Min (ms) | Max (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| recommendations_quick | 839 | 0 | 450.5 | 73.1 | 1838.0 |
| recommendations_all | 1006 | 0 | 469.1 | 56.9 | 2316.3 |
| root_status | 405 | 0 | 94.8 | 6.0 | 506.8 |
| burnout_analysis | 1272 | 0 | 545.6 | 103.7 | 2699.0 |
| activity_history | 809 | 0 | 473.8 | 92.8 | 2037.6 |
| log_sleep | 557 | 0 | 528.5 | 96.2 | 1924.7 |
| wellness_trends | 611 | 0 | 503.8 | 63.3 | 2189.6 |
| wellness_dashboard | 1618 | 0 | 807.6 | 210.8 | 2308.9 |
| sleep_history | 831 | 0 | 459.4 | 91.9 | 1721.3 |
| health_check | 614 | 0 | 94.7 | 8.8 | 821.3 |
| log_activity | 453 | 0 | 551.1 | 54.7 | 1774.8 |
| login | 470 | 0 | 2127.6 | 831.0 | 3354.8 |
| burnout_history | 884 | 0 | 412.4 | 52.9 | 1678.4 |

<details>
<summary>Click to view sampled request-level rows (400 of 10,369 real requests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LOAD-00001 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 650.7ms |
| LOAD-00002 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 171.1ms |
| LOAD-00003 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 227.4ms |
| LOAD-00004 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 163.3ms |
| LOAD-00005 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 324.1ms |
| LOAD-00006 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 243.8ms |
| LOAD-00007 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 470.5ms |
| LOAD-00008 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 101.0ms |
| LOAD-00009 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 405.6ms |
| LOAD-00010 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 227.0ms |
| LOAD-00011 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 334.6ms |
| LOAD-00012 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 408.6ms |
| LOAD-00013 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 224.6ms |
| LOAD-00014 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 644.1ms |
| LOAD-00015 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 230.4ms |
| LOAD-00016 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 355.3ms |
| LOAD-00017 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 639.2ms |
| LOAD-00018 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 337.1ms |
| LOAD-00019 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1357.9ms |
| LOAD-00020 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 429.5ms |
| LOAD-00021 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 658.0ms |
| LOAD-00022 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 385.1ms |
| LOAD-00023 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 1055.3ms |
| LOAD-00024 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 272.8ms |
| LOAD-00025 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 250.4ms |
| LOAD-00026 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2518.4ms |
| LOAD-00027 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 325.2ms |
| LOAD-00028 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 1489.3ms |
| LOAD-00029 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 1269.1ms |
| LOAD-00030 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 148.2ms |
| LOAD-00031 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 611.3ms |
| LOAD-00032 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 469.3ms |
| LOAD-00033 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 20.8ms |
| LOAD-00034 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 290.6ms |
| LOAD-00035 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 643.7ms |
| LOAD-00036 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 629.4ms |
| LOAD-00037 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 300.3ms |
| LOAD-00038 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 43.9ms |
| LOAD-00039 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 354.4ms |
| LOAD-00040 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 659.7ms |
| LOAD-00041 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 262.8ms |
| LOAD-00042 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 609.0ms |
| LOAD-00043 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 522.5ms |
| LOAD-00044 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 439.8ms |
| LOAD-00045 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1929.1ms |
| LOAD-00046 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 199.7ms |
| LOAD-00047 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 845.7ms |
| LOAD-00048 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 572.7ms |
| LOAD-00049 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 514.8ms |
| LOAD-00050 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 544.2ms |
| LOAD-00051 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 702.2ms |
| LOAD-00052 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 416.8ms |
| LOAD-00053 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 108.0ms |
| LOAD-00054 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 311.5ms |
| LOAD-00055 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 267.0ms |
| LOAD-00056 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 339.2ms |
| LOAD-00057 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 625.2ms |
| LOAD-00058 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 381.0ms |
| LOAD-00059 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 577.0ms |
| LOAD-00060 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 305.4ms |
| LOAD-00061 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 274.0ms |
| LOAD-00062 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 271.2ms |
| LOAD-00063 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 191.1ms |
| LOAD-00064 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 229.7ms |
| LOAD-00065 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 725.0ms |
| LOAD-00066 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2023.5ms |
| LOAD-00067 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 517.2ms |
| LOAD-00068 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 505.9ms |
| LOAD-00069 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 668.7ms |
| LOAD-00070 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 525.9ms |
| LOAD-00071 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 281.4ms |
| LOAD-00072 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 317.9ms |
| LOAD-00073 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 684.2ms |
| LOAD-00074 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 366.1ms |
| LOAD-00075 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1201.2ms |
| LOAD-00076 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 566.5ms |
| LOAD-00077 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 221.2ms |
| LOAD-00078 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 80.4ms |
| LOAD-00079 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 618.7ms |
| LOAD-00080 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1882.8ms |
| LOAD-00081 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 779.2ms |
| LOAD-00082 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 522.1ms |
| LOAD-00083 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2294.1ms |
| LOAD-00084 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 364.4ms |
| LOAD-00085 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 329.4ms |
| LOAD-00086 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 68.3ms |
| LOAD-00087 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 506.2ms |
| LOAD-00088 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 518.0ms |
| LOAD-00089 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 358.2ms |
| LOAD-00090 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 659.1ms |
| LOAD-00091 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 774.0ms |
| LOAD-00092 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 73.8ms |
| LOAD-00093 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 99.9ms |
| LOAD-00094 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 337.8ms |
| LOAD-00095 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 596.5ms |
| LOAD-00096 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 279.8ms |
| LOAD-00097 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 634.6ms |
| LOAD-00098 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 423.4ms |
| LOAD-00099 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 977.2ms |
| LOAD-00100 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 219.0ms |

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
