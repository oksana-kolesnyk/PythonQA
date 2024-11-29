from modules.ui.base_page import BasePage
from modules.ui.demoqa.pages.checkbox_page import CheckboxPage
from modules.ui.demoqa.pages.main_page import MainPage
from modules.ui.demoqa.pages.text_box_page import TextboxPage
from modules.ui.demoqa.pages.radio_button_page import RadiobuttonPage

class DemoQaApp(BasePage):

    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.checkbox_page = CheckboxPage(self)
        self.main_page = MainPage(self)
        self.text_box_page = TextboxPage(self)
        self.radio_button_page = RadiobuttonPage(self)
