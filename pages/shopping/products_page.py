from base.base_page import BasePage
from utilities.check_status import CheckStatus
from utilities.util import Util


class ProductPage(BasePage):

    # Locators
    _products_name = ".inventory_details_name"
    _add_to_cart_button = ".btn_inventory"
    _back_to_products = "back-to-products"
    _page_container_title = ".header_secondary_container .title"
    _inventory_items = ".inventory_item"
    _products_hyperlink = "a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()
        self.cs = CheckStatus(driver)

    def add_to_cart_btn(self):
        self.click_element_when_ready("css", self._add_to_cart_button)

    def verify_product_name_selected(self, expected_product_name: str):
        actual_product_name = self.get_text("css", self._products_name)
        return self.ut.verify_text_match(actual_product_name, expected_product_name)

    def verify_page_title(self, expected_page_title: str):
        actual_text = self.get_text("css", self._page_container_title)
        return self.ut.verify_text_match(actual_text, expected_page_title)

    def go_back_to_inventory(self):
        self.click_element_when_ready("id", self._back_to_products)
