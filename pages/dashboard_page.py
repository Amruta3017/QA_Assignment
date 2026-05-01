from selenium.webdriver.common.by import By
from utils.waits import wait_for_element_visible

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    page_title = (By.CLASS_NAME, "title")
    dashboard_heading = (By.CLASS_NAME, "app_logo")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    menu_btn = (By.ID, "react-burger-menu-btn")
    product_list = (By.CLASS_NAME, "inventory_list")
    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    # Methods
    def get_page_title(self):
        return wait_for_element_visible(self.driver, self.page_title).text

    def get_dashboard_heading(self):
        return wait_for_element_visible(self.driver, self.dashboard_heading).text

    def is_cart_visible(self):
        return wait_for_element_visible(self.driver, self.cart_icon).is_displayed()

    def is_menu_visible(self):
        return wait_for_element_visible(self.driver, self.menu_btn).is_displayed()

    def is_product_list_visible(self):
        return wait_for_element_visible(self.driver, self.product_list).is_displayed()

    def is_add_to_cart_visible(self):
        return wait_for_element_visible(self.driver, self.add_to_cart_btn).is_displayed()

    def add_first_product_to_cart(self):
        wait_for_element_visible(self.driver, self.add_to_cart_btn).click()

    def get_cart_count(self):
        return wait_for_element_visible(self.driver, self.cart_badge).text