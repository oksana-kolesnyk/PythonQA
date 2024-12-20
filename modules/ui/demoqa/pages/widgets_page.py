from playwright.sync_api import expect

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class WidgetsPage:

    # URL BLOCK
    URL = "https://demoqa.com/widgets"

    # ELEMENTS LOCATORS BLOCK
    SELECT_MENU_LOCATOR = "//*[@id='item-8'//*[@class='btn btn-light active']" # need to change xpath

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_widgets_page(self):
        self.demoqa_app.goto(WidgetsPage.URL)

    def click_on_select_menu(self):
        self.demoqa_app.click(self.SELECT_MENU_LOCATOR)
