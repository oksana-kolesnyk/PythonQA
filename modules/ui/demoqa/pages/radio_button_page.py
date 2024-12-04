from playwright.sync_api import expect

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class RadiobuttonPage:

    # URL BLOCK
    URL = 'https://demoqa.com/radio-button'

    # ELEMENTS LOCATORS BLOCK
    RADIO_BUTTON_LOCATORS = {
        "Yes": "//input[@id='yesRadio']",
        "Impressive": "//input[@id='impressiveRadio']",
        "No": "//input[@id='noRadio']",
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

    def click_radiobutton(self, key):
        locator = self.RADIO_BUTTON_LOCATORS[key]
       
        if self.demoqa_app.is_disabled(locator):
            logger.info(f"Radio button: {key} is disabled.")
        else:
            self.demoqa_app.click(locator)
            logger.info(f"Radio button: {key} was clicked.")

    def check_message_text(self, key):

        expected_text = self.MESSAGE_TEXT[key]
        message_locator = self.demoqa_app.page.locator(self.MESSAGE_LOCATOR)

        expect(message_locator).to_be_visible(timeout=5000)
        expect(message_locator).to_contain_text(expected_text)
        logger.info(f"You have selected {expected_text}")
