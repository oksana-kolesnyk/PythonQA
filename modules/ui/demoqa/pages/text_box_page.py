from modules.ui.demoqa.base_page import BasePage
from playwright.sync_api import expect
from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class TextboxPage(BasePage):
    
    # URL BLOCK
    URL = "https://demoqa.com/text-box"
    
    # ELEMENTS LOCATORS BLOCK
    FULL_NAME = "//input[@id='userName']"
    EMAIL = "//input[@id='userEmail']"
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    
    def __init__(self, browser) -> None:
        super().__init__(browser)
        
    # USER METHODS BLOCK  
    
    def go_to_text_box_page(self):
        self.goto(TextboxPage.URL)
        
    def fill_text_box(self, fullname, email, current_address, permanent_address):
        self.go_to_text_box_page()
        self.page.fill(self.FULL_NAME, fullname)
        self.page.fill(self.EMAIL, email)
        self.page.fill(self.CURRENT_ADDRESS, current_address)
        self.page.fill(self.PERMANENT_ADDRESS, permanent_address)
        self.page.locator(self.SUBMIT_BUTTON).click()
        return self
    
    @staticmethod
    def generate_random_fullname(name_len, surname_len):
        name =  BasePage.generate_random_string_name(name_len)
        surname = BasePage.generate_random_string_name(surname_len)
        fullname = f"{name} {surname}"
        return fullname
    
    @staticmethod
    def generate_random_email(length):
        local = BasePage.generate_random_string(length)
        domain = 'gmail.com'
        email = f"{local}@{domain}"
        return email
    
    def check_data_presence(self, under_form_locator, expected_data):
        locator = self.page.locator(under_form_locator)
        expect(locator).to_be_visible(timeout=10000)
        actual_text = locator.text_content() 
        logger.info(f"Actual text for locator {under_form_locator}: {actual_text}")
        expect(locator).to_contain_text(expected_data)

        