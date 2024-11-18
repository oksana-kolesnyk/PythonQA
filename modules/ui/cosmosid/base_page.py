from playwright.sync_api import expect
from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class BasePage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.page = browser.new_page()
    
    def goto(self, url):
        self.page.goto(url)
        
    def close_popup_if_present(self, pop_up_title, pop_up_close_button):
        expect(self.page.locator(pop_up_title)).to_be_visible(timeout=10000)
        logger.info(f"Pop-up {pop_up_title} is visible.")
        self.page.locator(pop_up_close_button).click()
        logger.info(f"Pop-up {pop_up_title} is closed")
        return self
