from playwright.sync_api import expect

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class MainPage:

    # URL BLOCK
    URL = "https://demoqa.com/"

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_main_page(self):
        self.demoqa_app.goto(MainPage.URL)

    def check_links_url(self, elements_locator, expected_url):
        self.go_to_main_page()
        self.demoqa_app.click(elements_locator)
        expect(self.demoqa_app.page).to_have_url(expected_url)
