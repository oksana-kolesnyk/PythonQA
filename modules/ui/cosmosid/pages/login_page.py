from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.base_page import BasePage

logger = LOGGER.get_logger(__name__)


class LoginPage(BasePage):

    # URL BLOCK
    URL = "https://app.cosmosid.com/sign-in"

    # ELEMENTS LOCATORS BLOCK
    SIGN_IN_EMAIL = "input#sign-in-form--email"
    SIGN_IN_PASS = "input#sign-in-form--password"
    SIGN_IN_BUTT = "button#sign-in-form--submit"
    POP_UP_TITLE = "h2#new-features-dialog--title"
    POP_UP_BUTTON_CLOSE = "button#new-features-dialog--close"  # xpath '//*[@id="new-features-dialog--close"]'
    ERROR_MESSAGES = {
        "email": "Email address must be a valid email",
        "empty_password": "Password is a required field",
        "empty_email": "Email address is a required field",
        "wrong_password": "Wrong email or password",
    }
    ERROR_LOCATORS = {
        "email": "p#sign-in-form--email-helper-text",
        "password": "p#sign-in-form--password-helper-text",
        "wrong_password": '//*[text()="Wrong email or password"]',
    }

    def __init__(self, browser) -> None:
        super().__init__(browser)

    # USER METHODS BLOCK

    def navigate_to(self):
        self.goto(LoginPage.URL)

    # close pop-up
    def close_login_page_pop_up_if_present(self):
        self.close_popup_if_present(self.POP_UP_TITLE, self.POP_UP_BUTTON_CLOSE)
        return self

    def try_login(self, username, password):
        self.page.fill(self.SIGN_IN_EMAIL, username)
        self.page.fill(self.SIGN_IN_PASS, password)
        self.page.locator(self.SIGN_IN_BUTT).click()
        return self

    # CHECK ON THE PAGE

    def check_password_required_message(self):
        return self._check_invalid_creds_message(
            self.page,
            self.ERROR_LOCATORS["password"],
            self.ERROR_MESSAGES["empty_password"],
        )

    def check_invalid_email_message(self):
        return self._check_invalid_creds_message(
            self.page, self.ERROR_LOCATORS["email"], self.ERROR_MESSAGES["email"]
        )

    def check_empty_email_message(self):
        return self._check_invalid_creds_message(
            self.page, self.ERROR_LOCATORS["email"], self.ERROR_MESSAGES["empty_email"]
        )

    def check_invalid_password_message(self):
        return self._check_invalid_creds_message(
            self.page,
            self.ERROR_LOCATORS["wrong_password"],
            self.ERROR_MESSAGES["wrong_password"],
        )

    @staticmethod
    def _check_invalid_creds_message(page, error_locator, error_message):
        error_locator = page.locator(error_locator)
        actual_error_message = error_locator.text_content()

        if error_locator.is_visible() and actual_error_message == error_message:
            logger.info(f"Error text equal to expected: {error_message}")
            return True, f"Error text equal to expected: {error_message}"
        else:
            logger.warning("Error text is not equal to expected.")
            return False, "Error text is not equal to expected."

    # the same methods but with expect using

    def expect_pass_required_message(self):
        self._expect_creds_message(
            self.page.locator(self.ERROR_LOCATORS["password"]),
            self.ERROR_MESSAGES["empty_password"],
        )

    def expect_invalid_email_message(self):
        self._expect_creds_message(
            self.page.locator(self.ERROR_LOCATORS["email"]),
            self.ERROR_MESSAGES["email"],
        )

    @staticmethod
    def _expect_creds_message(error_locator, error_message) -> None:
        expect(
            error_locator, f"Locator {error_locator} is not visible."
        ).to_be_visible()
        logger.info(f"Locator {error_locator} is visible.")

        expect(
            error_locator,
            f"Error {error_locator} text differs from expected {error_message}.",
        ).to_have_text(error_message)
        logger.info(
            f"Error {error_locator} text is the same as expected {error_message}."
        )
