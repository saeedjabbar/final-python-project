import time
from base.base_page import BasePage
from utilities.check_status import CheckStatus
from utilities.util import Util
import random


class ShoppingPage(BasePage):
    # Locators
    _menu_button = "#react-burger-menu-btn"
    _products_page = "//a[text()='All Items']"
    _shopping_cart_with_item = ".shopping_cart_badge"
    _shopping_cart_link = ".shopping_cart_link"
    _inventory_items = ".inventory_item"
    _add_to_cart_button = ".btn_inventory"
    _continue_shopping = "continue-shopping"
    _remove_from_cart = ".cart_button"
    _page_container_title = ".header_secondary_container .title"
    _inventory_products_name = ".inventory_item_name"
    _products_hyperlink = "a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()
        self.cs = CheckStatus(driver)

    def products_page(self):
        self.click_element_when_ready("css", self._menu_button)
        self.click_element_when_ready("xpath", self._products_page)

    def add_to_cart_btn(self, element):
        add_cart_btn = self.get_element_from_an_element(element, "css", self._add_to_cart_button)
        add_cart_btn.click()

    def go_to_product_page(self, product_name: str):
        element = self.get_product(product_name.rstrip())
        self.get_element_from_an_element(element, "css", self._products_hyperlink).click()

    def go_to_product_page_randomly(self):
        elements = self.get_elements("css", self._inventory_items)
        idx = random.randint(0, len(elements))
        elements[idx].click()

    def get_product(self, product_name: str):
        elements = self.get_elements("css", self._inventory_items)
        for element in elements:
            product = self.get_element_from_an_element(element, "css", self._inventory_products_name)
            product_title = product.text
            if product_title == product_name:
                return element

    def add_product_to_the_cart_from_inventory(self, product_name: str):
        self.add_to_cart_btn(self.get_product(product_name.rstrip()))

    def add_product_to_the_cart_from_inventory_by_count(self, number_of_products: int):
        elements = self.get_elements("css", self._add_to_cart_button)
        for i in range(number_of_products):
            elements[i].click()

    def verify_product_has_added_successfully_to_the_cart(self):
        return self.is_element_present("css", self._shopping_cart_with_item)

    def verify_count_of_products_have_added_to_the_cart(self, expected_count_of_products: int):
        if self.is_element_present("css", self._shopping_cart_with_item):
            text = self.get_text("css", self._shopping_cart_with_item)
            return text == str(expected_count_of_products)

    def verify_page_title(self, expected_page_title: str):
        actual_text = self.get_text("css", self._page_container_title)
        return self.ut.verify_text_match(actual_text, expected_page_title)

    def visit_cart_page(self):
        self.click_element_when_ready("css", self._shopping_cart_link)

    def remove_item_from_cart(self, product_name: str):
        element = self.get_product(product_name.rstrip())
        self.get_element_from_an_element(element, "css", self._add_to_cart_button).click()
