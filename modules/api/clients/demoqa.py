import requests
import logging

"""
Call POST https://demoqa.com/Account/v1/User to create new user.
Save userId from Response.
Create Authorization Token by calling /Account/v1/GenerateToken with credentials of user created on step1. 
Call endpoint GET /Account/v1/User/{UUID} with user Token as Authorization Header (exact format: “Bearer Token”).
Verify that username in Response Body corresponds to data provided on step 1
"""


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
        response_body = new_user.json()
        self.username = username
        self.password = password

        self.user_id = response_body["userID"]

        logging.info(f"new UserID is {self.user_id}")
        return response_body

    def check_new_user_status_code(self):

        response = requests.get(
            "https://demoqa.com/Account/v1/User", auth=(self.username, self.password)
        )
        response.raise_for_status()

        status_code = response.status_code

        if status_code == 200:
            print("New user is created!")
            return True
        else:
            print(f"New user wasn't created! Status code: {status_code}")
            return False


    def check_authorization_of_new_user(self):

        r = requests.post(
            "https://demoqa.com/Account/v1/Authorized",
            json={"userName": self.username, "password": self.password},
        )
        status_code_of_autorization = r.status_code
        print(status_code_of_autorization)
        authorization_result = r.json()
        
        if status_code_of_autorization == 200:
            print(f"Authorization response is {authorization_result}")
            return True
        else:
            print("Authorization failed with status code: {status_code_of_autorization}")
            return False

    def get_user_token(self):

        r = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        response_token = r.json()
        print(response_token)

        token = response_token.get("token")
        self.token = token
        token_status = response_token.get("status")
        self.token_status = token_status
        token_result = response_token.get("result")
        self.token_result = token_result

        print(f"Token is: {token}")
        return token

    def check_username_of_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers)
        response = r.json()
        print(f"Response from API: {response} and Token: {token}")

        username_of_new_user = response["username"]
        print(username_of_new_user)
        print(self.username)

        if username_of_new_user == self.username:
            return True
        return False

    def delete_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        r = requests.delete(
            f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers
        )
        status_code = r.status_code

        if status_code == 200:
            print("New user is deleted!")
            return True
        else:
            print("New user isn't deleted!")
            return False
