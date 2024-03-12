import pytest
from pages.main_page import Main


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        main_page = Main(browser)
        main_page.user_login()
