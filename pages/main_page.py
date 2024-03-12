from pages.base import Base
from locators.auth import Auth
from utils.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open('')
        self.input(Auth.USERNAME_INPUT, self.env.auth_login)
        self.input(Auth.PASSWORD_INPUT, self.env.auth_password)
        self.click(Auth.LOGIN_BTN)
