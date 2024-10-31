from modules.ui.cosmosid.base_page import BasePage


class LoginPage(BasePage):
    url = "https://app.cosmosid.com/sign-in"
    
    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.goto(LoginPage.url)
        
    def try_login(self, username, password):
        self.page.fill("input#sign-in-form--email", username)
        self.page.fill("input#sign-in-form--password", password)
        self.page.locator("button#sign-in-form--submit").click()
        
    @staticmethod
    def check_incorrect_creds_message(error_locator, error_message):
        actual_error_message = error_locator.text_content()
        
        if error_locator.is_visible() and actual_error_message == error_message:
            return (True, "invalid creds.")
        else:
            return (False, "Creds is valid.")
    
    

