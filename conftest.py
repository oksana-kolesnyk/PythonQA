import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.base_page import BasePage
from modules.api.clients.demoqa import Demoqa


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
      
@pytest.fixture
def demoqa_api():
    demo_api = Demoqa() 
    username = "Ksu3"
    password = "Ksu111111@"
    
    demo_api.create_new_user(username, password)
    yield demo_api 
    demo_api.delete_new_user(username, password)
