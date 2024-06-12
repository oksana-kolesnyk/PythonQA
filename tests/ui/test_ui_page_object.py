from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(page_creation):
    sign_in_page = SignInPage()
    sign_in_page.driver = page_creation.driver  # receive driver from fixture

    # open https://github.com/login 
    sign_in_page.go_to()

    invalid_username = 'page_object@gmail.com'
    invalid_password = "wrong password"
    sign_in_page.try_login(invalid_username, invalid_password)

    # verify that title of page is expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
