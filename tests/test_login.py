

import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import *
from utils.screenshot import take_screenshot


#Valid login with correct credentials
def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open_url(BASE_URL)
    login.login(USERNAME, PASSWORD)

    try:
        # URL validation
        assert "inventory" in driver.current_url

        # Page title (UI)
        #assert dashboard.get_page_title() == "Products"
        assert dashboard.get_dashboard_heading() == "Swag Labs"

        # UI elements (at least 3)
        assert dashboard.is_cart_visible()
        assert dashboard.is_menu_visible()
        assert dashboard.is_add_to_cart_visible()

        # Product section
        assert dashboard.is_product_list_visible()

    except:
        take_screenshot(driver, "dashboard_validation_failed")
        raise

# invalid login with wrong_user and wrong_pass
def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url(BASE_URL)
    login.login("wrong_user", "wrong_pass")

    try:
        assert "Username and password do not match" in login.get_error()
    except:
        take_screenshot(driver, "invalid_login_failed")
        raise


#Empty username and password
def test_empty_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url(BASE_URL)
    login.login("", "")

    try:
        assert "Username is required" in login.get_error()
    except:
        take_screenshot(driver, "empty_login_failed")
        raise





#Login with empty username
def test_empty_username(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url(BASE_URL)
    login.login("", PASSWORD)

    try:
        assert "Username is required" in login.get_error()

    except:
        take_screenshot(driver, "empty_username_login_failed")
        raise


#login with wrong password
def test_empty_password(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url(BASE_URL)
    login.login(USERNAME, "")

    try:
        assert "Password is required" in login.get_error()

    except:
        take_screenshot(driver, "empty_password_login_failed")
        raise


#Enter Special characters
def test_special_characters_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url(BASE_URL)
    login.login("@@@###", "$$$%%%")

    try:
        assert "Username and password do not match" in login.get_error()

    except:
        take_screenshot(driver, "Special_characters_login_failed")
        raise


#Long input values
def test_long_input_login(setup):
    driver = setup
    login = LoginPage(driver)

    long_text = "a" * 200

    login.open_url(BASE_URL)
    login.login(long_text, long_text)

    try:
        assert "Username and password do not match" in login.get_error()

    except:
        take_screenshot(driver, "long_input_login_failed")
        raise


