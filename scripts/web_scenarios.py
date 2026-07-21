"""
Real page/selector data for the HealthSense AI web app, gathered from the
actual source in web/src (routes, react-hook-form field ids, aria-labels,
visible text) — no data-testid attributes exist in the app, so every
locator here is a real id/name/type/aria-label/text selector that
genuinely resolves in the rendered DOM.
"""
from selenium.webdriver.common.by import By

BASE_PATH_TITLES = {
    "/login": "Sign In",
    "/register": "Create Account",
    "/dashboard": "Dashboard",
    "/sleep": "Sleep Tracker",
    "/phone": "Phone Usage",
    "/emotions": "Emotion Analysis",
    "/activity": "Activity Tracker",
    "/recommendations": "Recommendations",
    "/analytics": "Analytics",
    "/chat": "Wellness Chat",
    "/profile": "Profile",
}

SIDEBAR_LINKS = [
    ("Dashboard", "/dashboard"), ("Sleep Tracker", "/sleep"), ("Phone Usage", "/phone"),
    ("Emotion Analysis", "/emotions"), ("Activity Tracker", "/activity"),
    ("Recommendations", "/recommendations"), ("Analytics", "/analytics"),
    ("AI Coach Chat", "/chat"), ("Profile", "/profile"),
]

VIEWPORTS = [("mobile", 375, 812), ("tablet", 768, 1024), ("desktop", 1440, 900)]

# Per-page element-presence checks: (page_path, check_name, by, selector)
PAGE_ELEMENT_CHECKS = [
    ("/login", "username_input", By.ID, "username"),
    ("/login", "password_input", By.ID, "password"),
    ("/login", "submit_button", By.XPATH, "//button[@type='submit']"),
    ("/login", "register_link", By.LINK_TEXT, "Create one free"),
    ("/login", "password_toggle", By.CSS_SELECTOR, "[aria-label='Show password']"),

    ("/register", "full_name_input", By.ID, "full_name"),
    ("/register", "username_input", By.ID, "username"),
    ("/register", "email_input", By.ID, "email"),
    ("/register", "age_input", By.ID, "age"),
    ("/register", "gender_select", By.ID, "gender"),
    ("/register", "password_input", By.ID, "password"),
    ("/register", "confirm_password_input", By.ID, "confirmPassword"),
    ("/register", "submit_button", By.XPATH, "//button[@type='submit']"),
    ("/register", "login_link", By.LINK_TEXT, "Sign in"),

    ("/dashboard", "refresh_button", By.XPATH, "//button[contains(.,'Refresh')]"),
    ("/dashboard", "burnout_score_heading", By.XPATH, "//*[contains(text(),'Burnout Risk Score')]"),
    ("/dashboard", "wellness_score_heading", By.XPATH, "//*[contains(text(),'Wellness Score')]"),
    ("/dashboard", "health_dimensions_heading", By.XPATH, "//*[contains(text(),'Health Dimensions')]"),
    ("/dashboard", "emotional_stability_heading", By.XPATH, "//*[contains(text(),'Emotional Stability Trend')]"),
    ("/dashboard", "emotion_distribution_heading", By.XPATH, "//*[contains(text(),'Emotion Distribution')]"),
    ("/dashboard", "ai_recommendations_heading", By.XPATH, "//*[contains(text(),'AI Recommendations')]"),
    ("/dashboard", "progress_comparison_heading", By.XPATH, "//*[contains(text(),'Progress Comparison')]"),
    ("/dashboard", "quick_stats_heading", By.XPATH, "//*[contains(text(),'Quick Stats')]"),
    ("/dashboard", "view_all_link", By.LINK_TEXT, "View all"),

    ("/sleep", "overview_tab", By.XPATH, "//button[normalize-space()='overview']"),
    ("/sleep", "calendar_tab", By.XPATH, "//button[normalize-space()='calendar']"),
    ("/sleep", "log_tab", By.XPATH, "//button[normalize-space()='log']"),
    ("/sleep", "refresh_button", By.XPATH, "//button[contains(.,'Refresh')]"),
    ("/sleep", "log_sleep_button", By.XPATH, "//button[contains(.,'Log Sleep')]"),

    ("/recommendations", "filter_all", By.XPATH, "//button[normalize-space()='All']"),
    ("/recommendations", "filter_sleep", By.XPATH, "//button[normalize-space()='Sleep']"),
    ("/recommendations", "filter_phone", By.XPATH, "//button[normalize-space()='Phone']"),
    ("/recommendations", "filter_activity", By.XPATH, "//button[normalize-space()='Activity']"),
    ("/recommendations", "filter_mental_health", By.XPATH, "//button[normalize-space()='Mental Health']"),
    ("/recommendations", "filter_social", By.XPATH, "//button[normalize-space()='Social']"),
    ("/recommendations", "filter_nutrition", By.XPATH, "//button[normalize-space()='Nutrition']"),
    ("/recommendations", "sort_toggle", By.XPATH, "//button[contains(.,'Sort:')]"),

    ("/analytics", "range_7d", By.XPATH, "//button[normalize-space()='7D']"),
    ("/analytics", "range_30d", By.XPATH, "//button[normalize-space()='30D']"),
    ("/analytics", "export_button", By.XPATH, "//button[contains(.,'Export')]"),
    ("/analytics", "refresh_button", By.XPATH, "//button[contains(.,'Refresh')]"),

    ("/chat", "message_input", By.CSS_SELECTOR, "input[aria-label='Message']"),
    ("/chat", "send_button", By.CSS_SELECTOR, "button[aria-label='Send message']"),
    ("/chat", "new_chat_button", By.XPATH, "//button[contains(.,'New Chat')]"),

    ("/profile", "profile_tab", By.XPATH, "//button[normalize-space()='Profile']"),
    ("/profile", "notifications_tab", By.XPATH, "//button[normalize-space()='Notifications']"),
    ("/profile", "privacy_tab", By.XPATH, "//button[normalize-space()='Privacy']"),
    ("/profile", "edit_button", By.XPATH, "//button[contains(.,'Edit')]"),
    ("/profile", "sign_out_button", By.XPATH, "//button[contains(.,'Sign Out')]"),
]

# Pages that only get a basic load+heading check (less UI detail available)
BASIC_PAGES = ["/phone", "/emotions", "/activity"]
