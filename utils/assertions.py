from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def check_url(self, uri, msg):
        expect(self.page).to_have_url(f'{self.env.base_url}{uri}', timeout=10000), msg

    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000), msg

    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg

    def have_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg
