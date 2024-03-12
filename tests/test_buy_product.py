import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:

    def test_buy_product(self, browser):
        market_page = MarketPage(browser)
        market_page.add_to_cart()
        market_page.checkout()
