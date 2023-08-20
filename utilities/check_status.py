"""
Check Status class implementation
It provides functionality to assert the result
"""

from base.custom_driver import CustomDriver
import utilities.custom_logger as cl
import allure


class CheckStatus(CustomDriver):

    log = cl.custom_logger()

    def __init__(self, driver):
        super(CheckStatus, self).__init__(driver)

    def mark_result(self, result, result_message):
        if not result:
            self.log.info(f"### VERIFICATION FAILED :: {result_message}")
            filepath = self.take_screenshot()
            allure.attach.file(filepath, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        else:
            self.log.info(f"### VERIFICATION SUCCESSFUL :: {result_message}")
        assert result
