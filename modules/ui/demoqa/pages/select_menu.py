from playwright.sync_api import expect
from modules.ui.base_page import BasePage

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class SelectmenuPage:

    # URL BLOCK
    URL = "https://demoqa.com/select-menu"

    # ELEMENTS LOCATORS BLOCK
    SELECT_VALUE_LOCATOR = "//*[@class='mt-2 row']//*[@class = 'css-19bqh2r']" #need to change locator
    GROUP_2_OPTION_1_LOCATOR = "//div[text()='Group 2, option 1']"
    INPUT_OF_SELECT_VALUE_LOCATOR = "//div[contains(@class, 'css-1uccc91-singleValue')]"
    TEXT_GROUP_2_OPTION_1 = "Group 2, option 1"

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_select_menu_page(self):
        self.demoqa_app.goto(SelectmenuPage.URL)

    def check_select_menu_url(self):
        result_of_check, msg = self.demoqa_app.check_url(self.URL)
        return result_of_check, msg

    def select_in_select_value_option(self):
        self.demoqa_app.click(
            self.SELECT_VALUE_LOCATOR
        ) 
        self.demoqa_app.click(self.GROUP_2_OPTION_1_LOCATOR)
        logger.info("Option 'Group 2, option 1' selected successfully.")

    def check_selected_in_select_value_option_text_appears(self):
        BasePage.expect_text_appears(
            self.INPUT_OF_SELECT_VALUE_LOCATOR, self.TEXT_GROUP_2_OPTION_1
        )
