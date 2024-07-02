from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RozetkaNavushnykyAksesuaryPage(BasePage):
    URL = "https://rozetka.com.ua/ua/naushniki-i-aksessuari/c4660594/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaNavushnykyAksesuaryPage.URL)

    def find_sorter(self, option_text):
        sort_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/rz-app-root/div/div/rz-category/div/main/rz-catalog/div/rz-catalog-settings/div/rz-sort/select",
                )
            )
        )
        sort_dropdown.click()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//option[contains(text(), '{option_text}')]")
            )
        )
        sort_option.click()
