import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.base_page import BasePage
from modules.api.clients.demoqa import Demoqa
from modules.ui.cosmosid.pages.login_page import LoginPage
import random
from logger import LOGGER


logger = LOGGER.get_logger(__name__)

      
@pytest.fixture
def github_api_client():
    api = GitHub()
    yield api


@pytest.fixture
def db_connection():
    db = Database()
    
    yield db
    
    db.close_connection()  # close connection with database


@pytest.fixture
def page_creation():
    page = BasePage()
    
    yield page
    
    page.driver.close()  # close the page

              
@pytest.fixture(scope="function")
def demoqa_api(check_connection_function):
    demo_api = Demoqa()
    logger.info('Test demoqa_api is started.')
    
    yield demo_api
    
    logger.info('Test demoqa_api is finished.')


@pytest.fixture(scope="session")
def demoqa_api_user(check_connection_session):
    demo_api_user = Demoqa()
    autotest = random.randint(0, 1000)
    username = f"{autotest}_Ksena"
    password = "Kse1111123@"

    logger.info('Tests session demoqa_api is started.')
    demo_api_user.create_new_user(username, password)
    demo_api_user.check_authorization_of_new_user()
    demo_api_user.get_user_token()
    
    yield demo_api_user
    
    demo_api_user.ensure_delete_user()
    logger.info('Tests session demoqa_api is finished.')


@pytest.fixture(scope="session")
def check_connection_session():
    Demoqa.test_internet_connection()


@pytest.fixture(scope="function")
def check_connection_function():
    Demoqa.test_internet_connection()
    
#cosmosid_api_client, login_page and db - fixtures


@pytest.fixture(scope="session")
def login_page(browser, check_connection_session):
    login_page = LoginPage(browser)
    logger.info('Tests session ui_cosmosid is started.')
    login_page.close_login_page_pop_up_if_present()
    
    yield login_page
    
    browser.close()
    logger.info('Tests session ui_cosmosid is finished.')