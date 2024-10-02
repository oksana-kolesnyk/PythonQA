import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.base_page import BasePage
from modules.api.clients.demoqa import Demoqa
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
    logger.info('Test is started.')
    yield demo_api
    logger.info('Test is finished.')


@pytest.fixture(scope="session")
def demoqa_api_user(check_connection_session):
    demo_api_user = Demoqa()
    autotest = random.randint(0, 1000)
    username = f"{autotest}_Ksena"
    password = "Kse1111123@"

    logger.info('Tests session is started.')
    demo_api_user.create_new_user(username, password)
    demo_api_user.check_authorization_of_new_user()
    demo_api_user.get_user_token()
    yield demo_api_user
    demo_api_user.ensure_delete_user()
    logger.info('Tests session is finished.')


@pytest.fixture(scope="session")
def check_connection_session():
    Demoqa.test_internet_connection()

@pytest.fixture(scope="function")
def check_connection_function():
    Demoqa.test_internet_connection()