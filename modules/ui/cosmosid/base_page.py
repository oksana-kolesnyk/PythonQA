from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class BasePage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.page = browser.new_page()
    
    def goto(self, url):
        self.page.goto(url)
        
    #using JavaScript to close pop-up
    def close_popup_if_present(self):
        self.page.evaluate("document.querySelector('div#new-features-dialog').style.display = 'none';")


   
