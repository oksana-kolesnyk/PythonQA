import random
import string

from playwright.sync_api import expect

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class BasePage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.page = browser.new_page()

    def goto(self, url):
        page = self.page.goto(url)
        logger.info(f"{page} page loaded successfully.")

    def get_url(self):
        return self.page.url

    def check_url(self, expected_url):
        actual_url = self.get_url()
        if actual_url == expected_url:
            logger.info(f"URL: {actual_url} is equal to expected.")
            return True, "URL: {actual_url} is equal to expected."
        else:
            logger.warning(f"Expected URL: {expected_url}, but got {actual_url}.")
            return False, "Expected URL: {expected_url}, but got {actual_url}."

    def click(self, locator):
        # self.page.locator(locator).hover()
        self.page.locator(locator).click()

    def click_with_index(self, locator, index=None):
        # self.page.locator(locator).hover()
        self.page.locator(locator).nth(index).click()

    def fill(self, locator, text):
        element = self.page.locator(locator)
        element.fill(text)

    def check(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=10000)
        self.page.locator(locator).check()

    # expect(self.page.locator(locator)).to_have_class("rct-icon rct-icon-check")

    def uncheck(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=5000)
        self.page.locator(locator).uncheck()

    # expect(self.page.locator(locator)).to_have_class("rct-icon rct-icon-uncheck")

    def check_text_appears(self, text_locator, expected_text):

        text_locator = self.page.locator(text_locator)

        expect(text_locator).to_be_visible(timeout=5000)
        expect(
            text_locator,
            f"Locator '{text_locator}' expected to contain text '{expected_text}'",
        ).to_have_text(expected_text)

        logger.info(f"The text '{expected_text}' appears.")
        
    def is_disabled(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=10000)
        self.page.locator(locator).is_disabled()

    def select_option(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=5000)
        self.page.locator(locator).select_option()

    @staticmethod
    def generate_random_string_name(length):  # Generate random alphabet
        alphabet = string.ascii_lowercase
        random_string = "".join(random.choice(alphabet) for i in range(length - 1))
        return random_string.capitalize()

    @staticmethod
    def generate_random_string(length):  # Generate random digits and number
        alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
        random_string = "".join(random.choice(alphabet) for i in range(length))
        return random_string

    def close_popup_if_present(self, pop_up_title, pop_up_close_button):
        expect(self.page.locator(pop_up_title)).to_be_visible(timeout=5000)
        logger.info(f"Pop-up {pop_up_title} is visible.")
        self.page.locator(pop_up_close_button).click()
        logger.info(f"Pop-up {pop_up_title} is closed")
        return self
