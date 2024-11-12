import pytest
from modules.ui.cosmosid.pages.login_page import LoginPage

@pytest.mark.ui_cosmosid
def test_login_invalid_username(cosmosid_ui_app):
    username = 'djghggukr'
    password = '123456DF'
    cosmosid_ui_app.try_login(username, password)
    
    assert LoginPage.check_invalid_email_message()
    
@pytest.mark.ui_cosmosid
def test_login_invalid_username_with_expect(cosmosid_ui_app):
    username = 'djghggukr'
    password = '123456DF'
    cosmosid_ui_app.try_login(username, password)
    
    LoginPage.expect_invalid_email_message()

@pytest.mark.ui_cosmosid
def test_login_without_password(cosmosid_ui_app):
    username = 'djghgg@ukr.net'
    password = ''
    cosmosid_ui_app.try_login(username, password)
    
    assert LoginPage.check_pass_required_message()

@pytest.mark.ui_cosmosid
def test_login_without_password_with_expect(cosmosid_ui_app):
    username = 'djghgg@ukr.net'
    password = ''
    cosmosid_ui_app.try_login(username, password)
    
    LoginPage.expect_pass_required_message()


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