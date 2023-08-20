from pages.registration.login_page import LoginPage
from utilities.check_status import CheckStatus
from utilities.util import Util
import pytest
import allure
from utilities.read_csv import read_data as rd


@pytest.mark.usefixtures("setup_teardown_class")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("Login Feature")
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.lp = LoginPage(cls.driver)
        cls.ut = Util()
        # cls.lp.navigate_to_login()
        cls.cs = CheckStatus(cls.driver)

    # @pytest.mark.parametrize("username, password", [
    #     ("testing1@email.com", "password1"),
    #     ("testing2email.com", "password1"),
    #     ("@testing3emailcom", "password1")
    # ])
    @pytest.mark.parametrize("username, password", rd("login_test_data.csv"))
    @pytest.mark.smoke
    def test_login(self, username, password):
        if username == '':
            self.lp.refresh()
            self.lp.login(username, password)
            result = self.lp.verify_empty_username_error_message()
            self.cs.mark_result(
                result, "Empty username error message verification")
        elif username in ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"] \
                and password == "secret_sauce":
            self.lp.login(username, password)
            result = self.lp.verify_home_page_header_post_successful_login("Swag Labs")
            self.cs.mark_result(
                result, "Valid credentials verification")
        else:
            self.lp.login(username, password)
            result = self.lp.verify_invalid_username_error_message()
            self.cs.mark_result(
                result, "Invalid username error message verification")
