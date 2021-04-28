from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_message_basket_empty(self):
        content = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY)
        assert content.text == 'Your basket is empty. Continue shopping', 'Not message basket empty'

    def check_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Present product in basket'
