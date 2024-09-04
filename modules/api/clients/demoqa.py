import requests
import logging

"""
Call POST https://demoqa.com/Account/v1/User to create new user.
Save userId from Response.
Create Authorization Token by calling /Account/v1/GenerateToken with credentials of user created on step1. 
Call endpoint GET /Account/v1/User/{UUID} with user Token as Authorization Header (exact format: “Bearer Token”).
Verify that username in Response Body corresponds to data provided on step 1
"""
# Setting level of logging to Info
logging.basicConfig(level=logging.INFO)


class Demoqa:

    def __init__(self) -> None:
        self.username = None
        self.password = None
        self.user_id = None
        self.token = None
        self.token_status = None
        self.token_result = None

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
        logging.info(f"New User: {response_body}")

        return response_body

    def check_new_user_status_code(self):

        response = requests.get(
            "https://demoqa.com/Account/v1/User", auth=(self.username, self.password)
        )
        response.raise_for_status()
        status_code = response.status_code
        logging.info(f"New user is created! Status code: {status_code}")

        return True

    def check_authorization_of_new_user(self):

        r = requests.post(
            "https://demoqa.com/Account/v1/Authorized",
            json={"userName": self.username, "password": self.password},
        )
        r.raise_for_status()
        logging.info("User authorized successfully.")

        return True

    def get_user_token(self):

        r = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        r.raise_for_status()
        response_token = r.json()
        logging.info(f"Response on token request: {response_token}")

        token = response_token.get("token")
        self.token = token
        token_status = response_token.get("status")
        self.token_status = token_status
        token_result = response_token.get("result")
        self.token_result = token_result

        return token

    def check_username_of_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers)
        r.raise_for_status()

        response = r.json()
        username_of_new_user = response["username"]

        if username_of_new_user == self.username:
            logging.info(
                f" Usernames are matched! {self.username} = {username_of_new_user}"
            )
            return True
        else:
            logging.info(
                f" Usernames are not matched. {self.username} = {username_of_new_user}"
            )
            return False

    def delete_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        r = requests.delete(
            f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers
        )
        r.raise_for_status()

        try:
            response = requests.get(
                f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.info(f" New user was deleted! HTTPError: {e}")
            return True

        
