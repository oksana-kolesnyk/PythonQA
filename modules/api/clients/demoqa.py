import requests
import re


class Demoqa:

    def __init__(self, logger) -> None:
        self.username = None
        self.password = None
        self.user_id = None
        self.token = None
        self.token_status = None
        self.token_result = None
        self.headers = None
        
        self.logger = logger
    
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
        self.logger.info("New user is created!")
        self.logger.info(f"New User: {response_body}")

        return response_body
    
# check whether the userID matches the expected UUID pattern
    def check_user_id_format(self):
        uuid_pattern = r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
        if re.match(uuid_pattern, self.user_id):
            self.logger.info("Valid userID format.")
            return True
        else:
            self.logger.info("Invalid userID format.")
            return False

    def check_authorization_of_new_user(self):

        r = requests.post(
            "https://demoqa.com/Account/v1/Authorized",
            json={"userName": self.username, "password": self.password},
        )
        r.raise_for_status()
        self.logger.info("User authorized successfully.")

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
        
        self.logger.info("Token was successfully generated!")
        return self.token
    
# check whether the token matches the expected JSON Web Token format
    def check_token_format(self):
        token_format = r'^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$'
        if re.match(token_format, self.token):
            self.logger.info("Valid JSON Web Token format.")
            return True
        else:
            self.logger.info("Invalid JSON Web Token format.")
            return False

    def check_username_of_new_user(self):

        r = requests.get(f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
        r.raise_for_status()

        response = r.json()
        username_of_new_user = response["username"]

        if username_of_new_user == self.username:
            self.logger.info(
                f" Usernames are matched! {self.username} = {username_of_new_user}"
            )
            return True
        else:
            self.logger.warning(
                f" Usernames are not matched. {self.username} != {username_of_new_user}"
            )
            return False
    
    def check_user_exists(self):
        
        r = requests.get(
            "https://demoqa.com/Account/v1/User",
            json={"userName": self.username, "password": self.password})
        
        r.raise_for_status()
        self.logger.info("User is exist.")

        return True
    
    def delete_user(self):
        
        r = requests.delete(
            f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
        
        r.raise_for_status()
        self.logger.info("User is deleted.")

        return True
    
    def check_user_doesnt_exist(self):
        
        try:
            r = requests.get(
                f"https://demoqa.com/Account/v1/User/{self.user_id}", headers=self.headers)
            
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.info("User doesn't exist.")
            return True

    def ensure_delete_user(self):

        self.check_user_exists()
        self.delete_user()
        self.check_user_doesnt_exist()
        
        self.logger.info("The user has been successfully deleted!")
        return True

    def test_internet_connection(self):
        
        try:
            r = requests.get("https://www.google.com", timeout=5)
            
            r.raise_for_status()
            self.logger.info("Connected successfully to internet.")  
        except requests.ConnectionError:
            raise Exception("Internet connection failed.") 
    
