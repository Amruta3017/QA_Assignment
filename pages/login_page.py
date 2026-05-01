from selenium.webdriver.common.by import By
from utils.waits import wait_for_element_visible, wait_for_element_clickable

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_msg = (By.XPATH, "//h3[@data-test='error']")

    # Methods
    def open_url(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        wait_for_element_visible(self.driver, self.username).send_keys(user)
        wait_for_element_visible(self.driver, self.password).send_keys(pwd)
        wait_for_element_clickable(self.driver, self.login_btn).click()

    # def click_login_only(self):
    #     wait_for_element_clickable(self.driver, self.login_btn).click()

    def get_error(self):
        return wait_for_element_visible(self.driver, self.error_msg).text

