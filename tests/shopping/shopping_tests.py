import time

from pages.registration.login_page import LoginPage
from pages.shopping.products_page import ProductPage
from pages.shopping.shopping_page import ShoppingPage
from pages.shopping.cart_page import CartPage
from utilities.check_status import CheckStatus
from utilities.util import Util
import pytest
import allure
from utilities.read_csv import read_data as rd


# Run specific suite test cases from different files
#  py.test -m smoke registration/*_tests.py --browser chrome


@pytest.mark.usefixtures("setup_teardown_class")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("Shopping Cart Feature")
class TestShopping:

    smoke_test_data = rd("shopping_smoke_test_data.csv")
    regression_test_data = rd("shopping_regression_test_data.csv")
    valid_username = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
    valid_password = "secret_sauce"

    @classmethod
    def setup_class(cls):
        cls.lp = LoginPage(cls.driver)
        cls.sp = ShoppingPage(cls.driver)
        cls.cp = CartPage(cls.driver)
        cls.ut = Util()
        cls.cs = CheckStatus(cls.driver)
        cls.pp = ProductPage(cls.driver)
        # cls.lp.login("standard_user", "secret_sauce")
        count = 0
        username = password = None
        while count < len(cls.smoke_test_data) and \
                username not in cls.valid_username \
                and password != cls.valid_password:
            username, password, _, _ = cls.smoke_test_data[count]
            count += 1
        count = 0
        while count < len(cls.smoke_test_data) and \
                username not in cls.valid_username \
                and password != cls.valid_password:
            username, password, _, _ = cls.smoke_test_data[count]
            count += 1
        if username in cls.valid_username \
                and password == cls.valid_password:
            cls.lp.login(username, password)
        else:
            assert False, "Please provide the valid login credentials."

    def teardown_method(self, method):
        for mark in method.pytestmark:
            if mark.name == 'regression':
                self.cp.remove_all_items_from_cart()
        self.sp.products_page()

    @pytest.mark.parametrize("a, b, test_case, product_name", smoke_test_data)
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_shopping_smoke(self, a, b, test_case, product_name):
        products = product_name.split(",")
        for item in products:
            self.sp.add_product_to_the_cart_from_inventory(item)
        self.sp.visit_cart_page()
        for item in products:
            verify_product_name = self.cp.verify_cart_contains_product(item)
            self.cs.mark_result(verify_product_name, "Product name verification in a cart")
            if test_case == "Verify remove a product from cart from inventory":
                self.cp.back_to_shopping_page()
                self.sp.remove_item_from_cart(item)
        if test_case == "Verify remove a product from cart from cart page":
            self.cp.remove_all_items_from_cart()
            empty_cart_result = self.cp.verify_cart_is_empty()
            self.cs.mark_result(empty_cart_result, "Empty cart verification")
        if test_case == "Verify adding a product from inventory page":
            # self.cp.back_to_shopping_page()
            empty_cart_result = self.sp.verify_product_has_added_successfully_to_the_cart()
            self.cs.mark_result(empty_cart_result, "Empty cart verification")

    @pytest.mark.parametrize("a, b, test_case, product_name", regression_test_data)
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    def test_shopping_regression(self, a, b, test_case, product_name):
        products = product_name.split(",")
        for item in products:
            if test_case == "Verify adding a product from products page":
                self.sp.go_to_product_page(item)
                self.pp.add_to_cart_btn()
                self.pp.go_back_to_inventory()
            else:
                self.sp.add_product_to_the_cart_from_inventory(item)
        self.sp.visit_cart_page()
        items = self.cp.collect_cart_products_name()
        self.cs.mark_result(len(items) == len(products), "Products successfully added in a cart verification")
        if test_case == "Verify return back to inventory page from cart":
            self.cp.back_to_shopping_page()
            header_result = self.sp.verify_page_title("Products")
            self.cs.mark_result(header_result, "Page header Verification!")
        elif test_case == "Verify place a successful order with multiple products":
            self.cp.checkout_cart()
            self.cp.fill_shipping_details("test-name", "last-name", "11111")
            self.cp.finalize_cart()
            pageHeader = self.cp.verify_page_title("Checkout")
            self.cs.mark_result(pageHeader, "Page header verification")
            self.cp.place_order()
            order_confirmation = self.cp.verify_order_placed("Thank you for your order!")
            self.cs.mark_result(order_confirmation, "Order completion message verification")
