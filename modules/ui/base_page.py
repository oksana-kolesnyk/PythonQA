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
        self.page.goto(url)

    def get_url(self):
        return self.page.url

    def click(self, locator):
        self.page.locator(locator).hover()
        self.page.locator(locator).click()

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
