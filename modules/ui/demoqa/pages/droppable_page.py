from playwright.sync_api import expect
from modules.ui.base_page import BasePage

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class DroppablePage:

    # URL BLOCK
    URL = "https://demoqa.com/droppable"

    # ELEMENTS LOCATORS BLOCK
    DRAGGED_ELEMENT_LOCATOR = "//*[@id='draggable']"
    DRROPPED_ELEMENT_LOCATOR = "//div[@id='simpleDropContainer']//div[@id='droppable']"
    TEXT_LOCATOR = "//*[text()='Dropped!']"

    EXPECTED_TEXT = "Dropped!"

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_droppable_page(self):
        self.demoqa_app.goto(DroppablePage.URL)

    def drag_and_drop_the_Drag_Me_item(self):
        self.demoqa_app.drag_and_drop_element(
            self.DRAGGED_ELEMENT_LOCATOR, self.DRROPPED_ELEMENT_LOCATOR
        )
        logger.info(f"Drag Me element was dropped.")
        
        text_locator = self.demoqa_app.page.locator(self.TEXT_LOCATOR)
        BasePage.expect_text_appears(text_locator, self.EXPECTED_TEXT)
        
