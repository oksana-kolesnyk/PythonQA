from playwright.sync_api import expect
from modules.ui.base_page import BasePage

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class RadiobuttonPage:

    # URL BLOCK
    URL = 'https://demoqa.com/radio-button'

    # ELEMENTS LOCATORS BLOCK
    RADIO_BUTTON_LOCATORS = {
        "Yes": "//input[@type='radio' and @id='yesRadio']",
        "Impressive": "//input[@type='radio' and @id='impressiveRadio']",
        "No": "//input[@type='radio' and @id='noRadio']",
    }
    MESSAGE_LOCATOR = "//*[@class = 'text-success']"

    MESSAGE_TEXT = {
        "Yes": "Yes",
        "Impressive": "Impressive",
        "No": "No",
    }

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_radiobutton_page(self):
        self.demoqa_app.goto(RadiobuttonPage.URL)

    def check_radiobutton(self, key):
        locator = self.RADIO_BUTTON_LOCATORS[key]
        expect(self.demoqa_app.page.locator(locator)).to_be_visible(timeout=5000)

        if self.demoqa_app.is_disabled(locator):
            logger.info(f"Radio button: {key} is disabled.")
        else:
            self.demoqa_app.check(locator) 
            self.demoqa_app.toBeChecked(locator)  
            logger.info(f"Radio button: {key} was selected.")

    def expect_message_text(self, key):

        expected_text = self.MESSAGE_TEXT[key]
        message_locator = self.demoqa_app.page.locator(self.MESSAGE_LOCATOR)

        BasePage.expect_text_appears(message_locator, expected_text)
        logger.info(f"You have selected {expected_text}")

