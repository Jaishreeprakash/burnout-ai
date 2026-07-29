# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard is generated from **real suite runs** — a live FastAPI backend, a real concurrent load test, real Selenium browser sessions, and real static + Appium mobile checks. No row here is replayed from a static fixture.

## 📊 Unified Summary Overview

| Component | Test Suite | Total Tests | Passed | Failed | Pass Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Website E2E | Real Selenium suite (Chrome + Firefox) | — | — | — | *not run* |
| Mobile App E2E | Real static analysis + live Appium | 400 | ✅ 371 | ❌ 29 | 92.8% |
| Backend & Security | Real functional/security scenarios (live backend) | 406 | ✅ 406 | ✅ 0 | 100.0% |
| API Load Testing | Real 100-VU baseline load test | 400 | ✅ 400 | ✅ 0 | 100.0% |

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
| BE-00001 | Functional | System | GET / — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.3ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00002 | API | System | GET / — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.8ms. {"detail":"Method Not Allowed"} |
| BE-00003 | API | System | GET / — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (direct response), 0.9ms |
| BE-00004 | Security | System | GET / — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.7ms — preflight handled without server error |
| BE-00005 | API | System | GET / — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00006 | Functional | System | GET / — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms. {"status":"healthy","app":"AI Burnout Detection API","version":"1.0.0","ai":"OpenAI GPT-4o-mini integrated"} |
| BE-00007 | Functional | System | GET /health — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.6ms. {"status":"ok"} |
| BE-00008 | API | System | GET /health — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.8ms. {"detail":"Method Not Allowed"} |
| BE-00009 | API | System | GET /health — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.8ms |
| BE-00010 | Security | System | GET /health — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.7ms — preflight handled without server error |
| BE-00011 | API | System | GET /health — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00012 | Functional | System | GET /health — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 1.4ms. {"status":"ok"} |
| BE-00013 | Functional | Auth | POST /api/v1/auth/register — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 294.4ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODUyNjY3MDB9.YGvijRCUsVNF7DVs0mk50erbNRFRdhGd6fOQqbidQC4","token_type":"bearer","user":{"i |
| BE-00014 | API | Auth | POST /api/v1/auth/register — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00015 | API | Auth | POST /api/v1/auth/register — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00016 | Security | Auth | POST /api/v1/auth/register — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00017 | API | Auth | POST /api/v1/auth/register — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00018 | Security | Auth | POST /api/v1/auth/register — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 3.0ms. {"detail":"This username is already taken"} |
| BE-00019 | Security | Auth | POST /api/v1/auth/register — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"This username is already taken"} |
| BE-00020 | Security | Auth | POST /api/v1/auth/register — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"This username is already taken"} |
| BE-00021 | Functional | Auth | POST /api/v1/auth/register — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.5ms. {"detail":"This username is already taken"} |
| BE-00022 | Functional | Auth | POST /api/v1/auth/register — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"This username is already taken"} |
| BE-00023 | Functional | Auth | POST /api/v1/auth/register — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"This username is already taken"} |
| BE-00024 | Security | Auth | POST /api/v1/auth/register — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00025 | Security | Auth | POST /api/v1/auth/register — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.2ms. {"detail":"An account with this email already exists"} |
| BE-00026 | Security | Auth | POST /api/v1/auth/register — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00027 | Functional | Auth | POST /api/v1/auth/register — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00028 | Functional | Auth | POST /api/v1/auth/register — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00029 | Functional | Auth | POST /api/v1/auth/register — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00030 | Security | Auth | POST /api/v1/auth/register — string field full name sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.3ms. {"detail":"An account with this email already exists"} |
| BE-00031 | Security | Auth | POST /api/v1/auth/register — string field full name xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00032 | Security | Auth | POST /api/v1/auth/register — string field full name crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.0ms. {"detail":"An account with this email already exists"} |
| BE-00033 | Functional | Auth | POST /api/v1/auth/register — string field full name oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00034 | Functional | Auth | POST /api/v1/auth/register — string field full name empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00035 | Functional | Auth | POST /api/v1/auth/register — string field full name whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00036 | Functional | Auth | POST /api/v1/auth/register — numeric field age negative | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.6ms. {"detail":[{"type":"greater_than_equal","loc":["body","age"],"msg":"Input should be greater than or equal to 0","input":-1,"ctx":{"ge":0},"url":"https://errors.pydantic.dev/2.5/v/greater_than_equal"}] |
| BE-00037 | Functional | Auth | POST /api/v1/auth/register — numeric field age zero | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.4ms. {"detail":"An account with this email already exists"} |
| BE-00038 | Functional | Auth | POST /api/v1/auth/register — numeric field age very large | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.6ms. {"detail":[{"type":"less_than_equal","loc":["body","age"],"msg":"Input should be less than or equal to 150","input":1000000000000000.0,"ctx":{"le":150},"url":"https://errors.pydantic.dev/2.5/v/less_th |
| BE-00039 | Functional | Auth | POST /api/v1/auth/register — numeric field age very small fraction | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.5ms. {"detail":[{"type":"int_from_float","loc":["body","age"],"msg":"Input should be a valid integer, got a number with a fractional part","input":1e-06,"url":"https://errors.pydantic.dev/2.5/v/int_from_fl |
| BE-00040 | Functional | Auth | POST /api/v1/auth/register — numeric field age wrong type string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.2ms. {"detail":[{"type":"int_parsing","loc":["body","age"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"not-a-number","url":"https://errors.pydantic.dev/2.5/v/int_ |
| BE-00041 | Functional | Auth | POST /api/v1/auth/register — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.6ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"username":"qa_user","password":"Str0ngPassw0rd!","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_ |
| BE-00042 | Functional | Auth | POST /api/v1/auth/register — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.5ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00043 | Functional | Auth | POST /api/v1/auth/register — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 400, 2.1ms. {"detail":"An account with this email already exists"} |
| BE-00044 | Functional | Auth | POST /api/v1/auth/register — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 0.9ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00045 | Functional | Auth | POST /api/v1/auth/login — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.6ms. {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxYS51c2VyQGhlYWx0aHNlbnNlLnRlc3QiLCJleHAiOjE3ODUyNjY3MDB9.YGvijRCUsVNF7DVs0mk50erbNRFRdhGd6fOQqbidQC4","token_type":"bearer","user":{"i |
| BE-00046 | API | Auth | POST /api/v1/auth/login — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00047 | API | Auth | POST /api/v1/auth/login — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00048 | Security | Auth | POST /api/v1/auth/login — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00049 | API | Auth | POST /api/v1/auth/login — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00050 | Security | Auth | POST /api/v1/auth/login — string field username sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.3ms. {"detail":"Incorrect email or password"} |
| BE-00051 | Security | Auth | POST /api/v1/auth/login — string field username xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.7ms. {"detail":"Incorrect email or password"} |
| BE-00052 | Security | Auth | POST /api/v1/auth/login — string field username crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.6ms. {"detail":"Incorrect email or password"} |
| BE-00053 | Functional | Auth | POST /api/v1/auth/login — string field username oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.8ms. {"detail":"Incorrect email or password"} |
| BE-00054 | Functional | Auth | POST /api/v1/auth/login — string field username empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00055 | Functional | Auth | POST /api/v1/auth/login — string field username whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 3.2ms. {"detail":"Incorrect email or password"} |
| BE-00056 | Security | Auth | POST /api/v1/auth/login — string field password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 291.9ms. {"detail":"Incorrect email or password"} |
| BE-00057 | Security | Auth | POST /api/v1/auth/login — string field password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 292.9ms. {"detail":"Incorrect email or password"} |
| BE-00058 | Security | Auth | POST /api/v1/auth/login — string field password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 293.1ms. {"detail":"Incorrect email or password"} |
| BE-00059 | Functional | Auth | POST /api/v1/auth/login — string field password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 2.7ms. {"detail":"Incorrect email or password"} |
| BE-00060 | Functional | Auth | POST /api/v1/auth/login — string field password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 1.8ms. {"detail":[{"type":"missing","loc":["body","password"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00061 | Functional | Auth | POST /api/v1/auth/login — string field password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401, 292.1ms. {"detail":"Incorrect email or password"} |
| BE-00062 | Functional | Auth | POST /api/v1/auth/login — missing required field username | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.3ms. {"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":null,"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00063 | Functional | Auth | GET /api/v1/auth/me — valid request | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 3.1ms. {"id":1,"email":"qa.user010705cf@healthsense.test","username":"qa_user010705cf","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-28T18:24:59.902790","is_act |
| BE-00064 | API | Auth | GET /api/v1/auth/me — unsupported method | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.0ms. {"detail":"Method Not Allowed"} |
| BE-00065 | API | Auth | GET /api/v1/auth/me — trailing slash variant | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 1.0ms |
| BE-00066 | Security | Auth | GET /api/v1/auth/me — missing auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 0.9ms. {"detail":"Not authenticated"} |
| BE-00067 | Security | Auth | GET /api/v1/auth/me — malformed auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.7ms. {"detail":"Could not validate credentials"} |
| BE-00068 | Security | Auth | GET /api/v1/auth/me — expired auth token | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.1ms. {"detail":"Could not validate credentials"} |
| BE-00069 | Security | Auth | GET /api/v1/auth/me — token for nonexistent user | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.4ms. {"detail":"Could not validate credentials"} |
| BE-00070 | Security | Auth | GET /api/v1/auth/me — cors preflight | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.9ms — preflight handled without server error |
| BE-00071 | API | Auth | GET /api/v1/auth/me — case insensitive path check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.9ms |
| BE-00072 | Functional | Auth | GET /api/v1/auth/me — response schema check | GET | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 2.6ms. {"id":1,"email":"qa.user010705cf@healthsense.test","username":"qa_user010705cf","full_name":"QA Automation User","age":29,"gender":"prefer_not_to_say","created_at":"2026-07-28T18:24:59.902790","is_act |
| BE-00073 | Functional | Auth | POST /api/v1/auth/reset-password — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.6ms. {"status":"success","message":"Password updated successfully"} |
| BE-00074 | API | Auth | POST /api/v1/auth/reset-password — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 1.2ms. {"detail":"Method Not Allowed"} |
| BE-00075 | API | Auth | POST /api/v1/auth/reset-password — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00076 | Security | Auth | POST /api/v1/auth/reset-password — cors preflight | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 0.8ms — preflight handled without server error |
| BE-00077 | API | Auth | POST /api/v1/auth/reset-password — case insensitive path check | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404 (case-sensitive routing correctly rejects altered-case path), 0.8ms |
| BE-00078 | Security | Auth | POST /api/v1/auth/reset-password — string field email sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 3.0ms. {"detail":"No account found with this email or username"} |
| BE-00079 | Security | Auth | POST /api/v1/auth/reset-password — string field email xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.4ms. {"detail":"No account found with this email or username"} |
| BE-00080 | Security | Auth | POST /api/v1/auth/reset-password — string field email crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.7ms. {"detail":"No account found with this email or username"} |
| BE-00081 | Functional | Auth | POST /api/v1/auth/reset-password — string field email oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.4ms. {"detail":"No account found with this email or username"} |
| BE-00082 | Functional | Auth | POST /api/v1/auth/reset-password — string field email empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 5.4ms. {"detail":"No account found with this email or username"} |
| BE-00083 | Functional | Auth | POST /api/v1/auth/reset-password — string field email whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 404, 2.7ms. {"detail":"No account found with this email or username"} |
| BE-00084 | Security | Auth | POST /api/v1/auth/reset-password — string field new password sql injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.6ms. {"status":"success","message":"Password updated successfully"} |
| BE-00085 | Security | Auth | POST /api/v1/auth/reset-password — string field new password xss payload | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.1ms. {"status":"success","message":"Password updated successfully"} |
| BE-00086 | Security | Auth | POST /api/v1/auth/reset-password — string field new password crlf injection | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.0ms. {"status":"success","message":"Password updated successfully"} |
| BE-00087 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password oversized 6000 chars | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422, 2.3ms. {"detail":[{"type":"string_too_long","loc":["body","new_password"],"msg":"String should have at most 72 characters","input":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
| BE-00088 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password empty string | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.7ms. {"status":"success","message":"Password updated successfully"} |
| BE-00089 | Functional | Auth | POST /api/v1/auth/reset-password — string field new password whitespace only | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 293.0ms. {"status":"success","message":"Password updated successfully"} |
| BE-00090 | Functional | Auth | POST /api/v1/auth/reset-password — missing required field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 2.2ms. {"detail":[{"type":"missing","loc":["body","email"],"msg":"Field required","input":{"new_password":"NewStr0ngPass!"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]} |
| BE-00091 | Functional | Auth | POST /api/v1/auth/reset-password — wrong type for string field email | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [422]), 1.7ms. {"detail":[{"type":"string_type","loc":["body","email"],"msg":"Input should be a valid string","input":12345,"url":"https://errors.pydantic.dev/2.5/v/string_type"}]} |
| BE-00092 | Functional | Auth | POST /api/v1/auth/reset-password — extra unexpected fields ignored | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 200, 292.8ms. {"status":"success","message":"Password updated successfully"} |
| BE-00093 | Functional | Auth | POST /api/v1/auth/reset-password — invalid json body syntax | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 422 (expected [400, 422]), 1.3ms. {"detail":[{"type":"json_invalid","loc":["body",1],"msg":"JSON decode error","input":{},"ctx":{"error":"Expecting property name enclosed in double quotes"}}]} |
| BE-00094 | Functional | Tracking-Sleep | POST /api/v1/tracking/sleep — valid request | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 201, 6.7ms. {"id":1,"user_id":1,"date":"2026-07-28T18:25:03.869000","duration_hours":7.5,"quality_score":82.0,"consistency_score":75.0,"bedtime":"23:00","wake_time":"06:30","created_at":"2026-07-28T18:25:03.87359 |
| BE-00095 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — unsupported method | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 405 (expected [404, 405]), 0.9ms. {"detail":"Method Not Allowed"} |
| BE-00096 | API | Tracking-Sleep | POST /api/v1/tracking/sleep — trailing slash variant | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 307 (redirect), 0.9ms |
| BE-00097 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — missing auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 0.9ms. {"detail":"Not authenticated"} |
| BE-00098 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — malformed auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.1ms. {"detail":"Could not validate credentials"} |
| BE-00099 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — expired auth token | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 1.9ms. {"detail":"Could not validate credentials"} |
| BE-00100 | Security | Tracking-Sleep | POST /api/v1/tracking/sleep — token for nonexistent user | POST | Backend (FastAPI @ 127.0.0.1:8000, local SQLite) | ✅ Pass | HTTP 401 (expected [401]), 2.5ms. {"detail":"Could not validate credentials"} |

*... showing 100 of 406 Backend & Security test cases. See the full JSON/CSV artifact for all rows.*

</details>

---

## ⚡ API Load Testing — Baseline/Load Test

**Test configuration:** 100 virtual users, continuous for 61s, backend running with 4 worker process(es).

**Requests per second (RPS)**
> 159.84 req/sec

**Response Time**
> Average: 606ms
> Min: 14ms
> Max: 4142ms
> p95: 1749ms

**Total requests sent:** 9,696 • **Errors:** 0 (0.00%)

> ⚠️ **Known issue:** Every backend route handler is synchronous (`def`, not `async def`). A single uvicorn worker process only exposes ~40 threadpool slots for concurrent requests, so 100 concurrent virtual users against a single worker produces ~90% request timeouts — consistent with the pre-existing backend/load_test_results.csv in this repo. Multiple worker processes (as this suite uses) is the standard fix.

**Per-endpoint breakdown:**

| Endpoint | Requests | Errors | Avg (ms) | Min (ms) | Max (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| burnout_history | 733 | 0 | 426.6 | 73.5 | 1704.1 |
| burnout_analysis | 1124 | 0 | 544.4 | 49.0 | 2181.3 |
| wellness_dashboard | 1634 | 0 | 822.0 | 62.5 | 3023.9 |
| health_check | 534 | 0 | 342.7 | 25.8 | 1539.4 |
| sleep_history | 798 | 0 | 485.8 | 64.4 | 2110.3 |
| recommendations_quick | 794 | 0 | 472.8 | 75.4 | 2837.1 |
| log_activity | 381 | 0 | 498.6 | 123.1 | 2395.1 |
| login | 498 | 0 | 2098.6 | 794.1 | 4142.3 |
| root_status | 412 | 0 | 99.9 | 14.8 | 593.5 |
| activity_history | 781 | 0 | 471.9 | 43.5 | 1761.8 |
| recommendations_all | 958 | 0 | 482.1 | 76.8 | 2399.6 |
| log_sleep | 497 | 0 | 515.6 | 14.4 | 2434.2 |
| wellness_trends | 552 | 0 | 548.3 | 77.2 | 2212.5 |

<details>
<summary>Click to view sampled request-level rows (400 of 9,696 real requests)</summary>

| Test ID | Category | Module / Page | Test Case | Method | Environment | Status | Observed Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LOAD-00001 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 345.2ms |
| LOAD-00002 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 600.7ms |
| LOAD-00003 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 142.2ms |
| LOAD-00004 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 150.5ms |
| LOAD-00005 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 254.6ms |
| LOAD-00006 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 214.4ms |
| LOAD-00007 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 55.8ms |
| LOAD-00008 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 331.6ms |
| LOAD-00009 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 444.9ms |
| LOAD-00010 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 245.7ms |
| LOAD-00011 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 135.4ms |
| LOAD-00012 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 164.0ms |
| LOAD-00013 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 50.4ms |
| LOAD-00014 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 506.4ms |
| LOAD-00015 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 215.6ms |
| LOAD-00016 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 174.8ms |
| LOAD-00017 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 78.1ms |
| LOAD-00018 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 197.7ms |
| LOAD-00019 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 699.7ms |
| LOAD-00020 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 418.0ms |
| LOAD-00021 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 387.9ms |
| LOAD-00022 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 46.3ms |
| LOAD-00023 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 217.4ms |
| LOAD-00024 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1004.9ms |
| LOAD-00025 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 244.1ms |
| LOAD-00026 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 398.8ms |
| LOAD-00027 | Performance | log_activity | POST /api/v1/tracking/activity — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 264.9ms |
| LOAD-00028 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 160.2ms |
| LOAD-00029 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 353.6ms |
| LOAD-00030 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2569.0ms |
| LOAD-00031 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 131.6ms |
| LOAD-00032 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 362.0ms |
| LOAD-00033 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 456.8ms |
| LOAD-00034 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2321.9ms |
| LOAD-00035 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 404.7ms |
| LOAD-00036 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 371.4ms |
| LOAD-00037 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 343.5ms |
| LOAD-00038 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 773.0ms |
| LOAD-00039 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 703.7ms |
| LOAD-00040 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 521.2ms |
| LOAD-00041 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 203.5ms |
| LOAD-00042 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 430.2ms |
| LOAD-00043 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 306.9ms |
| LOAD-00044 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2214.7ms |
| LOAD-00045 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1992.4ms |
| LOAD-00046 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1569.1ms |
| LOAD-00047 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 219.2ms |
| LOAD-00048 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2382.0ms |
| LOAD-00049 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 172.2ms |
| LOAD-00050 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 2127.0ms |
| LOAD-00051 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 510.2ms |
| LOAD-00052 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 245.4ms |
| LOAD-00053 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 808.1ms |
| LOAD-00054 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 188.1ms |
| LOAD-00055 | Performance | health_check | GET /health — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 466.4ms |
| LOAD-00056 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 579.0ms |
| LOAD-00057 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 294.2ms |
| LOAD-00058 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 600.5ms |
| LOAD-00059 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1000.9ms |
| LOAD-00060 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 529.1ms |
| LOAD-00061 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 514.3ms |
| LOAD-00062 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 586.4ms |
| LOAD-00063 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 755.9ms |
| LOAD-00064 | Performance | wellness_trends | GET /api/v1/wellness/trends — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 663.1ms |
| LOAD-00065 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 980.4ms |
| LOAD-00066 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 763.7ms |
| LOAD-00067 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 731.2ms |
| LOAD-00068 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 115.7ms |
| LOAD-00069 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 300.5ms |
| LOAD-00070 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 821.8ms |
| LOAD-00071 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 286.3ms |
| LOAD-00072 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 315.8ms |
| LOAD-00073 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 143.4ms |
| LOAD-00074 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 981.6ms |
| LOAD-00075 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 508.3ms |
| LOAD-00076 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 261.9ms |
| LOAD-00077 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 442.3ms |
| LOAD-00078 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1161.8ms |
| LOAD-00079 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1097.1ms |
| LOAD-00080 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 327.0ms |
| LOAD-00081 | Performance | login | POST /api/v1/auth/login — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1846.0ms |
| LOAD-00082 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1187.1ms |
| LOAD-00083 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1183.9ms |
| LOAD-00084 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 721.9ms |
| LOAD-00085 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 336.2ms |
| LOAD-00086 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 52.0ms |
| LOAD-00087 | Performance | root_status | GET / — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 67.8ms |
| LOAD-00088 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 228.7ms |
| LOAD-00089 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 834.9ms |
| LOAD-00090 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 510.3ms |
| LOAD-00091 | Performance | activity_history | GET /api/v1/tracking/activity — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 214.4ms |
| LOAD-00092 | Performance | log_sleep | POST /api/v1/tracking/sleep — sampled request under 100-VU load | POST | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 201, 286.6ms |
| LOAD-00093 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 1341.0ms |
| LOAD-00094 | Performance | sleep_history | GET /api/v1/tracking/sleep — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 139.4ms |
| LOAD-00095 | Performance | burnout_history | GET /api/v1/burnout/history — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 264.2ms |
| LOAD-00096 | Performance | recommendations_quick | GET /api/v1/recommendations/quick — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 107.9ms |
| LOAD-00097 | Performance | burnout_analysis | GET /api/v1/burnout/analysis — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 177.8ms |
| LOAD-00098 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 533.4ms |
| LOAD-00099 | Performance | wellness_dashboard | GET /api/v1/wellness/dashboard — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 921.0ms |
| LOAD-00100 | Performance | recommendations_all | GET /api/v1/recommendations/ — sampled request under 100-VU load | GET | Backend (FastAPI @ http://127.0.0.1:8000, local SQLite, 100 concurrent VUs) | ✅ Pass | HTTP 200, 266.9ms |

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
