from playwright.sync_api import expect
from modules.ui.base_page import BasePage

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class ButtonsPage:

    # URL BLOCK
    URL = "https://demoqa.com/buttons"

    # ELEMENTS LOCATORS BLOCK
    DOUBLE_CLICK_ME_BUTTON_LOCATOR = "//button[@id='doubleClickBtn']"
    RIGHT_CLICK_ME_BUTTON_LOCATOR = "//button[@id='rightClickBtn']"
    CLICK_ME_BUTTON_LOCATOR = "//button[@id='ZTreY']"
    
    TEXT_MESSAGES = {
        "Double_click_me": "You have done a double click",
        "Right_click_me": "You have done a right click",
        "Click_me": "You have done a dynamic click",
    }
    
    TEXT_LOCATORS = {
        "Double_click_me": "//*[@id='doubleClickMessage']",
        "Right_click_me": "//*[@id='rightClickMessage']",
        "Click_me": "//*[@id='dynamicClickMessage']",
    }

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_buttons_page(self):
        self.demoqa_app.goto(ButtonsPage.URL)
        
    def expect_text_after_double_click_on_button(self):
        self.demoqa_app.double_click(self.DOUBLE_CLICK_ME_BUTTON_LOCATOR)
        text_locator = self.demoqa_app.page.locator(self.TEXT_LOCATORS["Double_click_me"])
        return BasePage.expect_text_appears(self.demoqa_app.page, text_locator, self.TEXT_MESSAGES["Double_click_me"])
        
    def expect_text_after_click_on_button(self):
        self.demoqa_app.click(self.CLICK_ME_BUTTON_LOCATOR)
        text_locator = self.demoqa_app.page.locator(self.TEXT_LOCATORS["Click_me"])
        return BasePage.expect_text_appears(self.demoqa_app.page, text_locator, self.TEXT_MESSAGES["Click_me"])    
        
    def expect_text_after_right_click_on_button(self):
        self.demoqa_app.right_click(self.RIGHT_CLICK_ME_BUTTON_LOCATOR)
        text_locator = self.demoqa_app.page.locator(self.TEXT_LOCATORS["Right_click_me"])
        return BasePage.expect_text_appears(self.demoqa_app.page, text_locator, self.TEXT_MESSAGES["Right_click_me"])  
        
        
    
