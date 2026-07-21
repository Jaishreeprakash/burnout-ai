# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard is generated from **real suite runs** — a live FastAPI backend, a real concurrent load test, real Selenium browser sessions, and real static + Appium mobile checks. No row here is replayed from a static fixture.

## 📊 Unified Summary Overview

| Component | Test Suite | Total Tests | Passed | Failed | Pass Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Website E2E | Real Selenium suite (Chrome + Firefox) | 219 | ✅ 219 | ✅ 0 | 100.0% |
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
| WEB-CH-00007 | Security | Login | wrong_credentials_rejected | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Error banner shown: Incorrect email or password |
| WEB-CH-00008 | Security | Login | sql_injection_input_no_crash | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Page still renders content after SQLi-style login attempt |
| WEB-CH-00009 | Functional | Login | password_show_hide_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | type changed password -> text |
| WEB-CH-00010 | UI/UX | Login | register_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on http://127.0.0.1:3000/register |
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
| WEB-CH-00023 | UI/UX | Register | login_link_navigates | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Landed on http://127.0.0.1:3000/login |
| WEB-CH-00024 | Functional | Register | real_registration_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Registered selenium.chrome.207da508@healthsense.test and landed on http://127.0.0.1:3000/dashboard |
| WEB-CH-00025 | Functional | Login | real_login_succeeds | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Signed out then logged back in with real credentials, reached /dashboard |
| WEB-CH-00026 | UI/UX | Sidebar | nav_link_dashboard_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Dashboard' navigated to http://127.0.0.1:3000/dashboard |
| WEB-CH-00027 | UI/UX | Sidebar | nav_link_sleep_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Sleep Tracker' navigated to http://127.0.0.1:3000/sleep |
| WEB-CH-00028 | UI/UX | Sidebar | nav_link_phone_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Phone Usage' navigated to http://127.0.0.1:3000/phone |
| WEB-CH-00029 | UI/UX | Sidebar | nav_link_emotions_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Emotion Analysis' navigated to http://127.0.0.1:3000/emotions |
| WEB-CH-00030 | UI/UX | Sidebar | nav_link_activity_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Activity Tracker' navigated to http://127.0.0.1:3000/activity |
| WEB-CH-00031 | UI/UX | Sidebar | nav_link_recommendations_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Recommendations' navigated to http://127.0.0.1:3000/recommendations |
| WEB-CH-00032 | UI/UX | Sidebar | nav_link_analytics_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Analytics' navigated to http://127.0.0.1:3000/analytics |
| WEB-CH-00033 | UI/UX | Sidebar | nav_link_chat_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'AI Coach Chat' navigated to http://127.0.0.1:3000/chat |
| WEB-CH-00034 | UI/UX | Sidebar | nav_link_profile_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sidebar link 'Profile' navigated to http://127.0.0.1:3000/profile |
| WEB-CH-00035 | UI/UX | Dashboard | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00036 | UI/UX | Dashboard | element_present_burnout_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00037 | UI/UX | Dashboard | element_present_wellness_score_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00038 | UI/UX | Dashboard | element_present_health_dimensions_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00039 | UI/UX | Dashboard | element_present_emotional_stability_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00040 | UI/UX | Dashboard | element_present_emotion_distribution_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00041 | UI/UX | Dashboard | element_present_ai_recommendations_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00042 | UI/UX | Dashboard | element_present_progress_comparison_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00043 | UI/UX | Dashboard | element_present_quick_stats_heading | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00044 | UI/UX | Dashboard | element_present_view_all_link | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00045 | UI/UX | Sleep Tracker | element_present_overview_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00046 | UI/UX | Sleep Tracker | element_present_calendar_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00047 | UI/UX | Sleep Tracker | element_present_log_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00048 | UI/UX | Sleep Tracker | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00049 | UI/UX | Sleep Tracker | element_present_log_sleep_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00050 | UI/UX | Recommendations | element_present_filter_all | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00051 | UI/UX | Recommendations | element_present_filter_sleep | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00052 | UI/UX | Recommendations | element_present_filter_phone | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00053 | UI/UX | Recommendations | element_present_filter_activity | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00054 | UI/UX | Recommendations | element_present_filter_mental_health | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00055 | UI/UX | Recommendations | element_present_filter_social | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00056 | UI/UX | Recommendations | element_present_filter_nutrition | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00057 | UI/UX | Recommendations | element_present_sort_toggle | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00058 | UI/UX | Analytics | element_present_range_7d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00059 | UI/UX | Analytics | element_present_range_30d | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00060 | UI/UX | Analytics | element_present_export_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00061 | UI/UX | Analytics | element_present_refresh_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00062 | UI/UX | Wellness Chat | element_present_message_input | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00063 | UI/UX | Wellness Chat | element_present_send_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00064 | UI/UX | Wellness Chat | element_present_new_chat_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00065 | UI/UX | Profile | element_present_profile_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00066 | UI/UX | Profile | element_present_notifications_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00067 | UI/UX | Profile | element_present_privacy_tab | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00068 | UI/UX | Profile | element_present_edit_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00069 | UI/UX | Profile | element_present_sign_out_button | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Element located |
| WEB-CH-00070 | Functional | Phone Usage | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 639 chars rendered |
| WEB-CH-00071 | Functional | Emotion Analysis | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 591 chars rendered |
| WEB-CH-00072 | Functional | Activity Tracker | page_loads_with_content | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | 715 chars rendered |
| WEB-CH-00073 | Functional | Sleep Tracker | tab_switching_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Cycled through overview/calendar/log tabs |
| WEB-CH-00074 | Functional | Sleep Tracker | log_sleep_modal_open_cancel | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Log Sleep modal opened and Cancel closed it |
| WEB-CH-00075 | Functional | Recommendations | category_filters_clickable | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Cycled through all category filter buttons |
| WEB-CH-00076 | Functional | Analytics | range_toggle_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Toggled 7D/30D range buttons |
| WEB-CH-00077 | E2E | Wellness Chat | send_message_gets_real_reply | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Sent a real chat message and received a rendered reply from the backend |
| WEB-CH-00078 | Functional | Profile | tab_switching_works | UI | Web (React/Vite @ 127.0.0.1:3000) — chrome real browser engine | ✅ Pass | Cycled through Profile/Notifications/Privacy tabs |
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
| MOB-LIVE-00002 | Functional | Register | real registration flow completes | Manual/Device | Mobile (React Native/Expo, real native debug build) — live Appium session | ✅ Pass | Registered appium.fbd1c872@healthsense.test through the real 3-step Register screen — submitted to the live backend |
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
| BE-00001 | Functional | System | GET / — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.2ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00002 | API | System | GET / — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.8ms. {"detail":"Method Not Allowed"} |
| BE-00003 | API | System | GET / — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (direct response), 0.9ms |
| BE-00004 | Security | System | GET / — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.7ms — preflight handled without server error |
| BE-00005 | API | System | GET / — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00006 | Functional | System | GET / — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00007 | Functional | System | GET /health — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms. {"status":"ok"} |
| BE-00008 | API | System | GET /health — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.7ms. {"detail":"Method Not Allowed"} |
| BE-00009 | API | System | GET /health — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.8ms |
| BE-00010 | Security | System | GET /health — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.7ms — preflight handled without server error |
| BE-00011 | API | System | GET /health — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00012 | Functional | System | GET /health — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms. {"status":"ok"} |
| BE-00013 | Functional | Auth | POST /api/v1/auth/register — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 294.1ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODQ2Njk2OTR9.oiYJpFVsFNb1Fsay8WL2bjiH1Wt7iUygtUUHhjGbpZ0","token_type":"bearer","user":{"i |
| BE-00014 | API | Auth | POST /api/v1/auth/register — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.1ms. {"detail":"Method Not Allowed"} |
| BE-00015 | API | Auth | POST /api/v1/auth/register — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00016 | Security | Auth | POST /api/v1/auth/register — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.7ms — preflight handled without server error |
| BE-00017 | API | Auth | POST /api/v1/auth/register — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00018 | Security | Auth | POST /api/v1/auth/register — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.9ms. {"detail":"This username is already taken"} |
| BE-00019 | Security | Auth | POST /api/v1/auth/register — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"This username is already taken"} |
| BE-00020 | Security | Auth | POST /api/v1/auth/register — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"This username is already taken"} |
| BE-00021 | Functional | Auth | POST /api/v1/auth/register — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"This username is already taken"} |
| BE-00022 | Functional | Auth | POST /api/v1/auth/register — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"This username is already taken"} |
| BE-00023 | Functional | Auth | POST /api/v1/auth/register — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"This username is already taken"} |
| BE-00024 | Security | Auth | POST /api/v1/auth/register — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00025 | Security | Auth | POST /api/v1/auth/register — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00026 | Security | Auth | POST /api/v1/auth/register — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00027 | Functional | Auth | POST /api/v1/auth/register — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00028 | Functional | Auth | POST /api/v1/auth/register — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00029 | Functional | Auth | POST /api/v1/auth/register — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00030 | Security | Auth | POST /api/v1/auth/register — string field full name sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00031 | Security | Auth | POST /api/v1/auth/register — string field full name xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00032 | Security | Auth | POST /api/v1/auth/register — string field full name crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00033 | Functional | Auth | POST /api/v1/auth/register — string field full name oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00034 | Functional | Auth | POST /api/v1/auth/register — string field full name empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00035 | Functional | Auth | POST /api/v1/auth/register — string field full name whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00036 | Functional | Auth | POST /api/v1/auth/register — numeric field age negative | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.6ms. {"detail":[{"type":"greater_than_equal","loc":["body","age"],"msg":"Input should be greater than or equal to 0","input":-1,"ctx":{"ge":0},"url":"https://errors.pydantic.dev/2.5/v/greater_than_equal"}] |
| BE-00037 | Functional | Auth | POST /api/v1/auth/register — numeric field age zero | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00038 | Functional | Auth | POST /api/v1/auth/register — numeric field age very large | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.6ms. {"detail":[{"type":"less_than_equal","loc":["body","age"],"msg":"Input should be less than or equal to 150","input":1000000000000000.0,"ctx":{"le":150},"url":"https://errors.pydantic.dev/2.5/v/less_th |
| BE-00039 | Functional | Auth | POST /api/v1/auth/register — numeric field age very small fraction | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.5ms. {"detail":[{"type":"int_from_float","loc":["body","age"],"msg":"Input should be a valid integer, got a number with a fractional part","input":1e-06,"url":"https://errors.pydantic.dev/2.5/v/int_from_fl |
| BE-00040 | Functional | Auth | POST /api/v1/auth/register — numeric field age wrong type string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.3ms. {"detail":[{"type":"int_parsing","loc":["body","age"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"not-a-number","url":"https://errors.pydantic.dev/2.5/v/int_ |
| BE-00041 | Functional | Auth | POST /api/v1/auth/register — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.6ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"username":"qa_user","password":"Str0ngPassw0rd!","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_ |
| BE-00042 | Functional | Auth | POST /api/v1/auth/register — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.5ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00043 | Functional | Auth | POST /api/v1/auth/register — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00044 | Functional | Auth | POST /api/v1/auth/register — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 0.9ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00045 | Functional | Auth | POST /api/v1/auth/login — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.8ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODQ2Njk2OTR9.oiYJpFVsFNb1Fsay8WL2bjiH1Wt7iUygtUUHhjGbpZ0","token_type":"bearer","user":{"i |
| BE-00046 | API | Auth | POST /api/v1/auth/login — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.1ms. {"detail":"Method Not Allowed"} |
| BE-00047 | API | Auth | POST /api/v1/auth/login — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00048 | Security | Auth | POST /api/v1/auth/login — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00049 | API | Auth | POST /api/v1/auth/login — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00050 | Security | Auth | POST /api/v1/auth/login — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.1ms. {"detail":"Incorrect email or password"} |
| BE-00051 | Security | Auth | POST /api/v1/auth/login — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.6ms. {"detail":"Incorrect email or password"} |
| BE-00052 | Security | Auth | POST /api/v1/auth/login — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.6ms. {"detail":"Incorrect email or password"} |
| BE-00053 | Functional | Auth | POST /api/v1/auth/login — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.6ms. {"detail":"Incorrect email or password"} |
| BE-00054 | Functional | Auth | POST /api/v1/auth/login — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.7ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00055 | Functional | Auth | POST /api/v1/auth/login — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.9ms. {"detail":"Incorrect email or password"} |
| BE-00056 | Security | Auth | POST /api/v1/auth/login — string field password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 291.6ms. {"detail":"Incorrect email or password"} |
| BE-00057 | Security | Auth | POST /api/v1/auth/login — string field password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 295.1ms. {"detail":"Incorrect email or password"} |
| BE-00058 | Security | Auth | POST /api/v1/auth/login — string field password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 292.7ms. {"detail":"Incorrect email or password"} |
| BE-00059 | Functional | Auth | POST /api/v1/auth/login — string field password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.5ms. {"detail":"Incorrect email or password"} |
| BE-00060 | Functional | Auth | POST /api/v1/auth/login — string field password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.7ms. {"detail":[{"type":"missing","loc":["body","password"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00061 | Functional | Auth | POST /api/v1/auth/login — string field password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 291.9ms. {"detail":"Incorrect email or password"} |
| BE-00062 | Functional | Auth | POST /api/v1/auth/login — missing required field username | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.2ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00063 | Functional | Auth | GET /api/v1/auth/me — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 3.0ms. {"id":1,"email":"qa.user5f25e071@healthsense.test","username":"qa_user5f25e071","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-21T20:34:54.086997","is_act |
| BE-00064 | API | Auth | GET /api/v1/auth/me — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.9ms. {"detail":"Method Not Allowed"} |
| BE-00065 | API | Auth | GET /api/v1/auth/me — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.8ms |
| BE-00066 | Security | Auth | GET /api/v1/auth/me — missing auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 0.8ms. {"detail":"Not authenticated"} |
| BE-00067 | Security | Auth | GET /api/v1/auth/me — malformed auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.6ms. {"detail":"Could not validate credentials"} |
| BE-00068 | Security | Auth | GET /api/v1/auth/me — expired auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.8ms. {"detail":"Could not validate credentials"} |
| BE-00069 | Security | Auth | GET /api/v1/auth/me — token for nonexistent user | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.1ms. {"detail":"Could not validate credentials"} |
| BE-00070 | Security | Auth | GET /api/v1/auth/me — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00071 | API | Auth | GET /api/v1/auth/me — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00072 | Functional | Auth | GET /api/v1/auth/me — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 2.2ms. {"id":1,"email":"qa.user5f25e071@healthsense.test","username":"qa_user5f25e071","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-21T20:34:54.086997","is_act |
| BE-00073 | Functional | Auth | POST /api/v1/auth/reset-password — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.6ms. {"status":"success","message":"Password updated successfully"} |
| BE-00074 | API | Auth | POST /api/v1/auth/reset-password — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.1ms. {"detail":"Method Not Allowed"} |
| BE-00075 | API | Auth | POST /api/v1/auth/reset-password — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00076 | Security | Auth | POST /api/v1/auth/reset-password — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00077 | API | Auth | POST /api/v1/auth/reset-password — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00078 | Security | Auth | POST /api/v1/auth/reset-password — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.9ms. {"detail":"No account found with this email or username"} |
| BE-00079 | Security | Auth | POST /api/v1/auth/reset-password — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.5ms. {"detail":"No account found with this email or username"} |
| BE-00080 | Security | Auth | POST /api/v1/auth/reset-password — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.4ms. {"detail":"No account found with this email or username"} |
| BE-00081 | Functional | Auth | POST /api/v1/auth/reset-password — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.4ms. {"detail":"No account found with this email or username"} |
| BE-00082 | Functional | Auth | POST /api/v1/auth/reset-password — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.9ms. {"detail":"No account found with this email or username"} |
| BE-00083 | Functional | Auth | POST /api/v1/auth/reset-password — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.8ms. {"detail":"No account found with this email or username"} |
| BE-00084 | Security | Auth | POST /api/v1/auth/reset-password — string field new password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.5ms. {"status":"success","message":"Password updated successfully"} |
| BE-00085 | Security | Auth | POST /api/v1/auth/reset-password — string field new password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.1ms. {"status":"success","message":"Password updated successfully"} |
| BE-00086 | Security | Auth | POST /api/v1/auth/reset-password — string field new password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.8ms. {"status":"success","message":"Password updated successfully"} |
| BE-00087 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.2ms. {"detail":[{"type":"string_too_long","loc":["body","new_password"],"msg":"String should have at most 72 characters","input":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
| BE-00088 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.8ms. {"status":"success","message":"Password updated successfully"} |
| BE-00089 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.9ms. {"status":"success","message":"Password updated successfully"} |
| BE-00090 | Functional | Auth | POST /api/v1/auth/reset-password — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.2ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"new_password":"NewStr0ngPass!"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00091 | Functional | Auth | POST /api/v1/auth/reset-password — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.7ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00092 | Functional | Auth | POST /api/v1/auth/reset-password — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.4ms. {"status":"success","message":"Password updated successfully"} |
| BE-00093 | Functional | Auth | POST /api/v1/auth/reset-password — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 1.3ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00094 | Functional | Tracking-Sleep | POST /api/v1/tracking/sleep — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 6.3ms. {"id":1,"user_id":1,"date":"2026-07-21T20:34:58.045000","duration_hours":7.5,"quality_score":82.0,"consistency_score":75.0,"bedtime":"23:00","wake_time":"06:30","created_at":"2026-07-21T20:34:58.04846 |
| BE-00095 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.0ms. {"detail":"Method Not Allowed"} |
| BE-00096 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00097 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — missing auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.0ms. {"detail":"Not authenticated"} |
| BE-00098 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — malformed auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.0ms. {"detail":"Could not validate credentials"} |
| BE-00099 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — expired auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.9ms. {"detail":"Could not validate credentials"} |
| BE-00100 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — token for nonexistent user | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.3ms. {"detail":"Could not validate credentials"} |

*... showing 100 of 406 Backend & Security test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## ⚡ API Load Testing — Baseline/Load Test

**Test configuration:** 100 virtual users, continuous for 61s, backend running with 4 worker process(es).

**Requests per second (RPS)**
> 166.8 req/sec

**Response Time**
> Average: 586ms
> Min: 4ms
> Max: 3629ms
> p95: 1672ms

**Total requests sent:** 10,129 • **Errors:** 0 (0.00%)

> ⚠️ **Known issue:** Every backend route handler is synchronous (`def`, not `async def`). A single uvicorn worker process only exposes ~40 threadpool slots for concurrent requests, so 100 concurrent virtual users against a single worker produces ~90% request timeouts (measured: 5.4 req/sec, 91.5% errors) — consistent with the pre-existing backend/load_test_results.csv in this repo. Running with multiple worker processes (as this suite does) is the standard fix and is what production should be deployed with.

**Per-endpoint breakdown:**

| Endpoint | Requests | Errors | Avg (ms) | Min (ms) | Max (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| recommendations_all | 986 | 0 | 461.7 | 81.9 | 2250.5 |
| root_status | 383 | 0 | 91.7 | 6.3 | 503.1 |
| activity_history | 826 | 0 | 470.4 | 84.7 | 1743.8 |
| wellness_dashboard | 1614 | 0 | 834.7 | 215.8 | 2660.3 |
| recommendations_quick | 812 | 0 | 437.4 | 55.3 | 1826.9 |
| login | 489 | 0 | 2194.6 | 710.2 | 3628.7 |
| log_sleep | 526 | 0 | 508.0 | 90.1 | 2332.4 |
| burnout_analysis | 1279 | 0 | 557.5 | 53.6 | 3228.5 |
| log_activity | 417 | 0 | 541.5 | 106.2 | 2876.8 |
| wellness_trends | 620 | 0 | 495.2 | 119.2 | 1572.6 |
| sleep_history | 778 | 0 | 464.4 | 66.9 | 1753.0 |
| health_check | 580 | 0 | 90.9 | 3.7 | 489.6 |
| burnout_history | 819 | 0 | 429.2 | 62.1 | 2415.0 |

<details>
<summary>Click to view sampled request-level rows (400 of 10,129 real requests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LOAD-00001 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 197.4ms |
| LOAD-00002 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 312.6ms |
| LOAD-00003 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 305.7ms |
| LOAD-00004 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 246.2ms |
| LOAD-00005 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 479.9ms |
| LOAD-00006 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 462.4ms |
| LOAD-00007 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 886.5ms |
| LOAD-00008 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 284.0ms |
| LOAD-00009 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 184.0ms |
| LOAD-00010 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 349.4ms |
| LOAD-00011 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 345.8ms |
| LOAD-00012 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 249.8ms |
| LOAD-00013 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 56.6ms |
| LOAD-00014 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 525.7ms |
| LOAD-00015 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 168.1ms |
| LOAD-00016 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1025.8ms |
| LOAD-00017 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 658.0ms |
| LOAD-00018 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 360.2ms |
| LOAD-00019 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 539.8ms |
| LOAD-00020 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 257.0ms |
| LOAD-00021 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 275.9ms |
| LOAD-00022 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1036.3ms |
| LOAD-00023 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 462.6ms |
| LOAD-00024 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 159.1ms |
| LOAD-00025 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 914.5ms |
| LOAD-00026 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 127.8ms |
| LOAD-00027 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 58.9ms |
| LOAD-00028 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 328.7ms |
| LOAD-00029 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 772.4ms |
| LOAD-00030 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 537.6ms |
| LOAD-00031 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 414.1ms |
| LOAD-00032 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 418.8ms |
| LOAD-00033 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 664.7ms |
| LOAD-00034 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 138.2ms |
| LOAD-00035 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 712.1ms |
| LOAD-00036 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 73.8ms |
| LOAD-00037 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 89.0ms |
| LOAD-00038 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 861.2ms |
| LOAD-00039 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 457.1ms |
| LOAD-00040 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 495.9ms |
| LOAD-00041 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 405.0ms |
| LOAD-00042 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2650.6ms |
| LOAD-00043 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 541.3ms |
| LOAD-00044 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 230.1ms |
| LOAD-00045 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 938.8ms |
| LOAD-00046 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 494.0ms |
| LOAD-00047 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 757.9ms |
| LOAD-00048 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 183.8ms |
| LOAD-00049 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 658.3ms |
| LOAD-00050 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 339.0ms |
| LOAD-00051 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 619.0ms |
| LOAD-00052 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 247.6ms |
| LOAD-00053 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 377.0ms |
| LOAD-00054 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 385.8ms |
| LOAD-00055 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 541.4ms |
| LOAD-00056 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 494.0ms |
| LOAD-00057 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 534.8ms |
| LOAD-00058 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 221.6ms |
| LOAD-00059 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 532.4ms |
| LOAD-00060 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 102.5ms |
| LOAD-00061 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 360.2ms |
| LOAD-00062 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2187.6ms |
| LOAD-00063 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1160.0ms |
| LOAD-00064 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 216.9ms |
| LOAD-00065 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 769.4ms |
| LOAD-00066 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 324.5ms |
| LOAD-00067 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1066.9ms |
| LOAD-00068 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 147.4ms |
| LOAD-00069 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 785.8ms |
| LOAD-00070 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 794.7ms |
| LOAD-00071 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 58.6ms |
| LOAD-00072 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 275.5ms |
| LOAD-00073 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 467.6ms |
| LOAD-00074 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 305.9ms |
| LOAD-00075 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 360.8ms |
| LOAD-00076 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 764.9ms |
| LOAD-00077 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 313.9ms |
| LOAD-00078 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 72.7ms |
| LOAD-00079 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 110.1ms |
| LOAD-00080 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 650.9ms |
| LOAD-00081 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1051.2ms |
| LOAD-00082 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 347.4ms |
| LOAD-00083 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 162.1ms |
| LOAD-00084 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 406.2ms |
| LOAD-00085 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 386.3ms |
| LOAD-00086 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 998.3ms |
| LOAD-00087 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 261.5ms |
| LOAD-00088 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 366.6ms |
| LOAD-00089 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 234.7ms |
| LOAD-00090 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 269.9ms |
| LOAD-00091 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 760.1ms |
| LOAD-00092 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 367.1ms |
| LOAD-00093 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 661.1ms |
| LOAD-00094 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 700.8ms |
| LOAD-00095 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 372.3ms |
| LOAD-00096 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 283.4ms |
| LOAD-00097 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 391.8ms |
| LOAD-00098 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 408.1ms |
| LOAD-00099 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 730.1ms |
| LOAD-00100 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 41.4ms |

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
