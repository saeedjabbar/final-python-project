from base.custom_driver import CustomDriver
from utilities.util import Util


class BasePage(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()

    def verify_title(self, expected_title):
        actual_title = self.get_title()
        return self.ut.verify_text_contains(actual_title, expected_title)