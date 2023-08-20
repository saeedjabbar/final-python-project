import time
from base.base_page import BasePage
from utilities.check_status import CheckStatus
from utilities.util import Util


class CartPage(BasePage):
    # Locators
    _continue_shopping = "continue-shopping"
    _remove_from_cart = ".cart_button"
    _cart_items = ".cart_item"
    _checkout_button = ".checkout_button"
    _first_name_field = "first-name"
    _last_name_field = "last-name"
    _postal_code_field = "postal-code"
    _continue_button = "continue"
    _page_container_title = ".header_secondary_container .title"
    _finish_btn = "finish"
    _completion_message = ".complete-header"
    _back_to_products = "back-to-products"
    _shopping_cart_link = ".shopping_cart_link"
    _cart_header = "//span[text()='Your Cart']"
    _products_name = ".inventory_item_name"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()
        self.cs = CheckStatus(driver)

    def verify_page_title(self, expected_page_title):
        actual_text = self.get_text("css", self._page_container_title)
        return self.ut.verify_text_contains(actual_text, expected_page_title)

    def verify_product_name_added(self, expected_product_name: str):
        actual_product_name = self.get_text("css", self._products_name)
        return self.ut.verify_text_match(actual_product_name, expected_product_name)

    def remove_item_from_cart(self):
        self.click_element_when_ready("css", self._remove_from_cart)

    def visit_cart_page(self):
        self.click_element_when_ready("css", self._shopping_cart_link)

    def remove_all_items_from_cart(self):
        if self.is_element_present("css", self._shopping_cart_link):
            self.visit_cart_page()
            result = self.verify_cart_is_empty()
            while not result:
                self.remove_item_from_cart()
                result = self.verify_cart_is_empty()

    def back_to_shopping_page(self):
        self.click_element_when_ready("id", self._continue_shopping)

    def checkout_cart(self):
        self.click_element_when_ready("css", self._checkout_button)

    def verify_cart_items(self, expected_number_of_products_added: int):
        actual_number_of_products = len(self.get_elements("css", self._cart_items))
        return self.ut.verify_text_match(actual_number_of_products, expected_number_of_products_added)

    def fill_shipping_details(self, first_name, last_name, postal_code):
        self.send_keys_when_ready(first_name, "id", self._first_name_field)
        self.send_keys_when_ready(last_name, "id", self._last_name_field)
        self.send_keys_when_ready(postal_code, "id", self._postal_code_field)

    def finalize_cart(self):
        self.click_element_when_ready("id", self._continue_button)

    def place_order(self):
        self.click_element_when_ready("id", self._finish_btn)

    def verify_order_placed(self, expected_order_completing_text):
        actual_text = self.get_text("css", self._completion_message)
        return self.ut.verify_text_match(actual_text, expected_order_completing_text)

    def visit_back_to_home_page(self):
        self.click_element_when_ready("id", self._back_to_products)

    def collect_cart_products_name(self):
        result = []
        elements = self.get_elements("css", self._products_name, 5)
        for ele in elements:
            result.append(ele.text)
        return result

    def verify_cart_contains_product(self, product_name: str):
        items = self.collect_cart_products_name()
        return product_name in items

    def verify_cart_is_empty(self):
        items = self.collect_cart_products_name()
        return len(items) == 0
