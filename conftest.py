import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


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
def github_api():
    api = GitHub()  #Створює об’єкт класа GitHub
    yield api  #Повертає створений об’єкт в тести

@pytest.fixture
def db_connection(): 
    db = Database()   #Створює об’єкт класа Database
    yield db          #Повертає створений об’єкт в тести
    db.close_connection()  # закриває з'єднання з базою даних, яке було встановлене в методі __init__ класу Database
