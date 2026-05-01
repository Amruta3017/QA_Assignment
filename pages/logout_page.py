from selenium.webdriver.common.by import By
from utils.waits import wait_for_element_clickable

class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    menu_btn = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    # Methods
    def logout(self):
        wait_for_element_clickable(self.driver, self.menu_btn).click()
        wait_for_element_clickable(self.driver, self.logout_link).click()