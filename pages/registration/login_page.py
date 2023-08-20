import time
from base.base_page import BasePage
from utilities.util import Util


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()

    # Locators
    _sign_in_link = "//a[normalize-space()='Sign In']"
    _username_field = "user-name"
    _password_field = "password"
    _login_button = "login-button"
    _invalid_username_error_message = ".error-message-container.error"
    _home_page_header = "header_label"
    # _invalid_username_error_message = "//span[@class='dynamic-text help-block']"
    # _empty_username_error_message = "//span[@class='error']"

    def navigate_to_login(self):
        self.get_element("xpath", self._sign_in_link).click()
        # self.log("Clicked on sign in button")

    def enter_username(self, username):
        # self.get_element("id", self._username_field).send_keys(email)
        self.send_keys_when_ready(username, "id", self._username_field)

    def enter_password(self, password):
        # self.get_element("id", self._password_field).send_keys(password)
        self.send_keys_when_ready(password, "id", self._password_field)

    def click_login_button(self):
        time.sleep(1)
        self.click_element_when_ready("id", self._login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_invalid_username_error_message(self):
        actual_error_message = self.get_text("css", self._invalid_username_error_message)
        expected_error_message = "Username and password do not match any user in this service"
        return self.ut.verify_text_contains(actual_error_message, expected_error_message)

    def verify_empty_username_error_message(self):
        actual_error_message = self.get_text(
            "css", self._invalid_username_error_message)
        expected_error_message = "Username is required"
        return self.ut.verify_text_contains(actual_error_message, expected_error_message)

    def verify_home_page_header_post_successful_login(self, expected_header_text):
        actual_header_text = self.get_text("class", self._home_page_header)
        return self.ut.verify_text_contains(actual_header_text, expected_header_text)
