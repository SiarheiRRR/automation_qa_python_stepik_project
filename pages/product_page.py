from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_FORM).click()
        self.solve_quiz_and_get_code()

    def compare_product_name(self):
        assert self.get_curr_product_name() in self.get_added_product_names(), 'Value "product name" not in basket'

    def compare_price(self):
        assert self.get_curr_product_price() == self.get_added_basket_price(), 'Price in basket != product price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_desapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should be desapear, but should not desapear"

    def get_curr_product_name(self):
        return self.browser.find_element(*ProductPageLocators.CURR_PRODUCT_NAME).text

    def get_added_product_names(self):
        return [product.text for product in self.browser.find_elements(*ProductPageLocators.ADDED_PRODUCT_NAME)]

    def get_curr_product_price(self):
        return self.browser.find_element(*ProductPageLocators.CURR_PRODUCT_PRICE).text

    def get_added_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_BASKET_PRICE).text



