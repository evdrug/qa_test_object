import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    LINK = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.LINK)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, self.LINK)
        page.open()
        page.go_to_basket()
        basket = BasketPage(browser, browser.current_url)
        basket.check_basket_empty()
        basket.check_message_basket_empty()
