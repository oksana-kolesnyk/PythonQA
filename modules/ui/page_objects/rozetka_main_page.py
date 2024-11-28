from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from modules.ui.page_objects.base_page import BasePage


class RozetkaMainPage(BasePage):
    URL = "https://rozetka.com.ua/ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaMainPage.URL)

    def try_search(self, search_text):
        search_form = self.driver.find_element(By.NAME, "search")
        search_form.send_keys(search_text)
        search_form.send_keys(Keys.RETURN)
