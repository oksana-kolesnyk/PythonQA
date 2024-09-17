import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.base_page import BasePage
from modules.api.clients.demoqa import Demoqa
import random
import logging

logging.basicConfig(level=logging.INFO)


class Logger:
    def __init__(self) -> None:
        pass 


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Oksana"
        self.second_name = "Kolesnyk"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


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
    logging.info('Test is started.')
    yield demo_api
    logging.info('Test is finished.')


@pytest.fixture(scope="session")
def demoqa_api_user(check_connection_session):
    demo_api_user = Demoqa()
    autotest = random.randint(0, 1000)
    username = f"{autotest}_Ksena"
    password = "Kse1111123@"

    logging.info('Tests session is started.')
    demo_api_user.create_new_user(username, password)
    demo_api_user.check_authorization_of_new_user()
    demo_api_user.get_user_token()
    yield demo_api_user
    demo_api_user.ensure_delete_user()
    logging.info('Tests session is finished.')


@pytest.fixture(scope="session")
def check_connection_session():
    connection_api = Demoqa()
    connection_api.test_internet_connection()
    yield connection_api

@pytest.fixture(scope="function")
def check_connection_function():
    connection_api = Demoqa()
    connection_api.test_internet_connection()
    yield connection_api
    