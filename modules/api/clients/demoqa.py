import re

import requests

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class Demoqa:

    def __init__(self) -> None:
        self.username = None
        self.password = None
        self.user_id = None
        self.token = None
        self.token_status = None
        self.token_result = None
        self.headers = None
        self.book_list = None

    def create_new_user(self, username, password):
        new_user = requests.post(
            "https://demoqa.com/Account/v1/User",
            json={"userName": username, "password": password},
        )
        new_user.raise_for_status()

        response_body = new_user.json()
        self.username = username
        self.password = password
        self.user_id = response_body["userID"]
        logger.info("New user is created!")
        logger.info(f"New User: {response_body}")

        return response_body

    # check whether the userID matches the expected UUID pattern
    @staticmethod
    def check_user_id_format(user_id):
        uuid_pattern = r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
        logger.debug(f"userId format check: {uuid_pattern}")

        if re.match(uuid_pattern, user_id):
            logger.info("Valid userID format.")
            return (True, "Valid userID format.")
        else:
            logger.warning("Invalid userID format.")
            return (False, "Invalid userID format.")

    def check_authorization_of_new_user(self):
        r = requests.post(
            "https://demoqa.com/Account/v1/Authorized",
            json={"userName": self.username, "password": self.password},
        )
        r.raise_for_status()
        logger.info("User authorized successfully.")

        return True

    def get_user_token(self):
        r = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        r.raise_for_status()
        response_token = r.json()

        self.token = response_token["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.token_status = response_token["status"]
        self.token_result = response_token["result"]

        logger.info(f"Token {self.token} was successfully generated!")
        return self.token

    # check whether the token matches the expected JSON Web Token format
    @staticmethod
    def check_token_format(token):
        token_format = r"^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$"
        logger.debug(f"token format check: {token_format}")

        if re.match(token_format, token):
            logger.info("Valid JSON Web Token format.")
            return (True, "Valid JSON Web Token format.")
        else:
            logger.info("Invalid JSON Web Token format.")
            return (False, "Invalid JSON Web Token format.")

    def check_username_of_new_user(self):
        r = requests.get(
            f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers
        )
        r.raise_for_status()
        response = r.json()

        username_of_new_user = response["username"]
        if username_of_new_user == self.username:
            logger.info(
                f" Usernames are matched! {self.username} = {username_of_new_user}"
            )
            return (
                True,
                f" Usernames are matched! {self.username} = {username_of_new_user}",
            )
        else:
            logger.warning(
                f" Usernames are not matched. {self.username} != {username_of_new_user}"
            )
            return (
                False,
                f" Usernames are not matched. {self.username} != {username_of_new_user}",
            )

    def check_user_exists(self):
        r = requests.get(
            "https://demoqa.com/Account/v1/User",
            json={"userName": self.username, "password": self.password},
        )

        r.raise_for_status()
        logger.info(f"User {self.username} is exist.")

        return True

    def delete_user(self):
        r = requests.delete(
            f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers
        )

        r.raise_for_status()
        logger.info(f"User with userId {self.user_id} is deleted.")

        return True

    def check_user_doesnt_exist(self):
        try:
            r = requests.get(
                f"https://demoqa.com/Account/v1/User/{self.user_id}",
                headers=self.headers,
            )

            r.raise_for_status()
        except requests.exceptions.HTTPError:
            logger.info(f"User {self.user_id} does not exist.")
            return True

    def ensure_delete_user(self):
        self.check_user_exists()
        self.delete_user()
        self.check_user_doesnt_exist()

        logger.info(f"User {self.username} has been successfully deleted!")
        return True

    @staticmethod
    def test_internet_connection():
        try:
            r = requests.get("https://www.google.com", timeout=5)

            r.raise_for_status()
            logger.info("Connected successfully to internet.")
        except requests.ConnectionError:
            raise RuntimeError("Internet connection failed.")

    def get_book_list(self):
        r = requests.get("https://demoqa.com/BookStore/v1/Books", headers=self.headers)
        r.raise_for_status()

        book_list = r.json()
        self.book_list = book_list["books"] or []

        if self.book_list is None:
            logger.warning("Book list is None.")
        else:
            logger.info(f"Book list for {self.username} is received.")
            logger.debug(f"Book list check: {self.book_list}")

        return self.book_list

    @staticmethod
    def count_books(book_list):
        count_books = len(book_list)

        return count_books

    def get_title_book_with_ibsn(self, isbn):
        title = None

        for book in self.book_list:
            if isbn == book["isbn"]:
                title = book["title"]
                break

        logger.info(f"Title of the book with isbn {isbn} is: {title}")
        return title
