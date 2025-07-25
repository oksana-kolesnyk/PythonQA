from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.base_page import BasePage

logger = LOGGER.get_logger(__name__)


class TextboxPage:

    # URL BLOCK
    URL = "https://demoqa.com/text-box"

    # ELEMENTS LOCATORS BLOCK
    FULL_NAME = "//input[@id='userName']"
    EMAIL = "//input[@id='userEmail']"
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_text_box_page(self):
        self.demoqa_app.goto(TextboxPage.URL)

    def fill_text_box(self, fullname, email, current_address, permanent_address):
        self.demoqa_app.fill(self.FULL_NAME, fullname)
        self.demoqa_app.fill(self.EMAIL, email)
        self.demoqa_app.fill(self.CURRENT_ADDRESS, current_address)
        self.demoqa_app.fill(self.PERMANENT_ADDRESS, permanent_address)
        self.demoqa_app.click(self.SUBMIT_BUTTON)
        return self

    @staticmethod
    def generate_random_fullname(name_len, surname_len):
        name = BasePage.generate_random_string_name(name_len)
        surname = BasePage.generate_random_string_name(surname_len)
        fullname = f"{name} {surname}"
        return fullname

    @staticmethod
    def generate_random_email(length):
        local = BasePage.generate_random_string(length)
        domain = "gmail.com"
        email = f"{local}@{domain}"
        return email

    def expect_data_presence(self, under_form_locator, expected_data):
        locator = self.demoqa_app.page.locator(under_form_locator)
        actual_text = locator.text_content()
    
        logger.info(f"Actual text for locator {under_form_locator}: {actual_text}")
        BasePage.expect_text_appears(locator, expected_data)


