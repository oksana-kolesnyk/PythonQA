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
        self.headers = None

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
        logging.info("New user is created!")
        logging.info(f"New User: {response_body}")

        return response_body

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

        self.token = response_token.get("token")
        # verify key:value
        
        self.headers = {"Authorization": f"Bearer {self.token}"}

        self.token_status = response_token.get("status")
        # verify key:value

        self.token_result = response_token.get("result")
        # verify key:value
        
        logging.info("Token was successfully generated!")
        return self.token

    def check_username_of_new_user(self):

        r = requests.get(f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
        r.raise_for_status()

        response = r.json()
        username_of_new_user = response["username"]

        if username_of_new_user == self.username:
            logging.info(
                f" Usernames are matched! {self.username} = {username_of_new_user}"
            )
            return True
        else:
            logging.warning(
                f" Usernames are not matched. {self.username} != {username_of_new_user}"
            )
            return False
    
    def check_user_exists(self):
        
        r = requests.get(
            "https://demoqa.com/Account/v1/User",
            json={"userName": self.username, "password": self.password})
        
        r.raise_for_status()
        logging.info("User is exist.")

        return True
    
    def delete_user(self):
        
        r = requests.delete(
            f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
        
        r.raise_for_status()
        logging.info("User is deleted.")

        return True
    
    def check_user_doesnt_exist(self):
        
        try:
            r = requests.get(
                f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
            
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            logging.info("User doesn't exist.")
            return True

    def ensure_delete_user(self):

        self.check_user_exists()
        self.delete_user()
        self.check_user_doesnt_exist()
        
        logging.info("The user has been really deleted!")
        return True

    def test_internet_connection(self):
        
        try:
            r = requests.get("https://www.google.com", timeout=5)
            
            r.raise_for_status()
            logging.info("Connected successfully to internet.")  
        except requests.ConnectionError:
            raise Exception("Internet connection failed.") 
    
