from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    CURR_PRODUCT_NAME = (By.CSS_SELECTOR, "div>h1")
    CURR_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    ADDED_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")



