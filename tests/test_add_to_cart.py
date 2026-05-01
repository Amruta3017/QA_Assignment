from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import *
from utils.screenshot import take_screenshot

#Add item to cart and verify the cart count
def test_add_to_cart(setup):
    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open_url(BASE_URL)
    login.login(USERNAME, PASSWORD)

    try:
        dashboard.add_first_product_to_cart()
        assert dashboard.get_cart_count() == "1"
    except:
        take_screenshot(driver, "add_to_cart_failed")
        raise