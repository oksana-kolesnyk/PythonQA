import pytest
from modules.ui.cosmosid.pages.login_page import LoginPage


@pytest.mark.ui_cosmosid
@pytest.mark.parametrize(
    "username, password, check_func",
    [
        ('djghggukr', "123456DF", 'check_invalid_email_message'),
    ('djghgg@ukr.net', "", 'check_password_required_message'),
    ('', "123456DF", 'check_empty_email_mesage'),
    ('djghggukr@ukr.net', "123456DF", 'check_invalid_password_message'),
    ],
    ids =['test_login_invalid_username', 'test_login_without_password', 'test_login_without_email', 'test_login_invalid_pssword'],
)
def test_login_invalid_creds(login_page, username, password, check_func):
    login_page.try_login(username, password)
    
    assert getattr(login_page, check_func)()
    #Це вбудована функція Python для отримання динамічного атрибута об'єкта за його іменем (у вигляді рядка), якщо атрибут не знайдено, то викликається AttributeError.
    
@pytest.mark.ui_cosmosid
def test_login_invalid_username_with_expect(login_page):
    username = 'djghggukr'
    password = '123456DF'
    login_page.try_login(username, password)
    
    login_page.expect_invalid_email_message()

@pytest.mark.ui_cosmosid
def test_login_without_password_with_expect(login_page):
    username = 'djghgg@ukr.net'
    password = ''
    login_page.try_login(username, password)
    
    login_page.expect_pass_required_message()


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