from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    def check_empty_basket_text(self):
        empty_flag = True
        try:
            self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        except NoSuchElementException:
            empty_flag = False
        assert empty_flag, 'No text "Your basket is empty"'

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "There are product(s) in basket, but should not be"