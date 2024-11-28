from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.base_page import BasePage

logger = LOGGER.get_logger(__name__)


class MainPage(BasePage):

    # URL BLOCK
    URL = "https://demoqa.com/"

    def __init__(self, browser) -> None:
        super().__init__(browser)

    # USER METHODS BLOCK

    def go_to_main_page(self):
        self.goto(MainPage.URL)

    def check_links_url(self, elements_locator, expected_url):
        self.go_to_main_page()
        self.page.locator(elements_locator).click()
        expect(self.page).to_have_url(expected_url)
