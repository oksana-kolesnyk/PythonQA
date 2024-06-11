from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self) -> None: #  вказівка типу повертаємого значення функції (в даному випадку None)
        self.driver = webdriver.Chrome(service=Service((ChromeDriverManager().install())))

    def close(self):
        self.driver.close()