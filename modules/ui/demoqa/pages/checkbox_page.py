import random

from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.base_page import BasePage

logger = LOGGER.get_logger(__name__)


class CheckboxPage(BasePage):

    # URL BLOCK
    URL = "https://demoqa.com/checkbox"

    # ELEMENTS LOCATORS BLOCK
    TOGGLE_BUTTON = "//button[text()='Toggle']]"
    EXPAND_ALL_BUTTON = "//button[text()='Expand all']"
    COLLAPSE_ALL_BUTTON = "//button[text()='Collapse all']"

    def __init__(self, browser) -> None:
        super().__init__(browser)

    # USER METHODS BLOCK

    def go_to_checkbox_page(self):
        self.goto(CheckboxPage.URL)

    def expand_collapse_box_tree_by_toggle(self):
        self.go_to_checkbox_page()
        self.page.locator(self.TOGGLE_BUTTON).click()

    def expand_all(self):
        self.go_to_checkbox_page()
        self.page.locator(self.EXPAND_ALL_BUTTON).click()

    def collapse_all(self):
        self.go_to_checkbox_page()
        self.page.locator(self.EXPAND_ALL_BUTTON).click()

    def get_random_items(
        self,
    ):
        items = [
            "Home",
            "Desktop",
            "Notes",
            "Commands",
            "Documents",
            "WorkSpace",
            "React",
            "Angular",
            "Veu",
            "Office",
            "Public",
            "Private",
            "Classified",
            "General",
            "Downloads",
            "Word File.doc",
            "Exel File.doc",
        ]
        num_elements

        random_elements = random.sample(items, num_elements)
