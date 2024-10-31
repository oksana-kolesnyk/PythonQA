import pytest
from modules.ui.cosmosid.pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.ui_cosmosid
def test_login_negative(cosmosid_ui_app):
    username = 'djghggukr'
    password = '123456DF'
    cosmosid_ui_app.try_login(username, password)
    
    error_message = 'Email address must be a valid email'
    error_locator = cosmosid_ui_app.page.locator("p#sign-in-form--email-helper-text")
    result, msg = LoginPage.check_incorrect_creds_message(error_locator, error_message)
    
    assert result, msg
    
@pytest.mark.ui_cosmosid
def test_login_negative_with_expect(cosmosid_ui_app):
    username = 'djghggukr'
    password = '123456DF'
    cosmosid_ui_app.try_login(username, password)
    
    error_message = 'Email address must be a valid email'
    error_locator = cosmosid_ui_app.page.locator("p#sign-in-form--email-helper-text")
    
    expect(error_locator).to_be_visible()
    expect(error_locator).to_have_text(error_message)



"""def test_login_positive():
    dashboard_page = login_page.try_login('user', 'password')
    assert dashboard_page.check_user_logged_in()


def test_login_complicated_api_ui(cosmosid_api_client, login_page, db): #cosmosid_api_client, login_page and db must be fixture
    dashboard_page = login_page.try_login('user', 'password')
    user = cosmosid_api_client.get_user_profile()
    user2 = db.get_user_from_table()
    
    assert user.token is not None
    assert dashboard_page.check_user_logged_in()
    """