from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from config.config import *
from utils.screenshot import take_screenshot


# Logout functionality - verify user can logout successfully and is redirected to login page
def test_logout(setup):
    driver = setup

    login = LoginPage(driver)
    logout = LogoutPage(driver)

    login.open_url(BASE_URL)
    login.login(USERNAME, PASSWORD)

    logout.logout()

    try:
        assert "saucedemo" in driver.current_url  # Verify user is redirected to login page
    except:
        take_screenshot(driver, "logout_failed")
        raise