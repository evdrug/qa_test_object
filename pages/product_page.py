from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def check_message_add_basket_for_product_name(self):
        name_product_object = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_object.text
        add_messages = self.wait_elements_located(*ProductPageLocators.MESSAGES_ADD_BASKET)
        assert add_messages[0].text == name_product, 'Incorrect name product when adding to basket'

    def check_message_add_basket_for_product_price(self):
        price_product_object = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product = price_product_object.text
        add_messages = self.wait_elements_located(*ProductPageLocators.MESSAGES_ADD_BASKET)
        assert add_messages[2].text == price_product, 'Incorrect price product when adding to basket'

    def check_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_ADD_BASKET), \
            'Element did not appear on the page'

    def check_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_ADD_BASKET), \
            'Element that appeared on the page'

    def check_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_ADD_BASKET), 'Element not disappeared on the page'
