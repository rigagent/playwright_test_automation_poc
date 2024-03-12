from playwright.sync_api import Page
from utils.environment import Environment


class Base:

    def __init__(self, page: Page):
        self.page = page
        self.env = Environment()

    def open(self, url):
        return self.page.goto(f'{self.env.base_url}{url}', wait_until='domcontentloaded')

    def input(self, locator, data: str):
        self.page.locator(locator).fill(data)

    def click(self, locator):
        self.page.click(locator)

    def get_text(self, element):
        return self.page.locator(element).text_content()

    def click_element_by_index(self, selector: str, index: int):
        self.page.locator(selector).nth(index).click()

    def input_value_by_index(self, selector: str, index: int, data: str):
        self.page.locator(selector).nth(index).fill(data)
