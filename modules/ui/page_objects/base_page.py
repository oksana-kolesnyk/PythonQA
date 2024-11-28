from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service((ChromeDriverManager().install()))
        )

    #  self.driver.maximize_window()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def check_link(self, expected_link):
        return self.driver.current_url == expected_link

    def close(self):
        self.driver.close()
