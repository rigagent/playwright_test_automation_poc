import pytest
from pages.main_page import Main


@pytest.fixture(scope='class')
def user_login(browser):
    main_page = Main(browser)
    main_page.user_login()
