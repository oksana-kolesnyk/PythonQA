import requests

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
       
    def create_new_user(self, username, password):

        new_user = requests.post(
            "https://demoqa.com/Account/v1/User",
            json={"userName": username, "password": password},
        )
        response_body = new_user.json()
        self.username = username
        self.password = password
            
        self.user_id = response_body.get("userID")
        
        print(f"new UserID is {self.user_id}")
        return response_body

    def check_new_user_status_code(self):

        response = requests.get(
            "https://demoqa.com/Account/v1/User", auth=(self.username, self.password)
        )
        status_code = response.status_code

        if status_code == 200:
            print("New user is created!")
            return True
        else:
            print(f"New user wasn't created! Status code: {status_code}")
            return False
    
    def check_authorization_of_new_user(self):
        
        new_user_authorization = requests.post(
            "https://demoqa.com/Account/v1/Authorized", 
            json={"userName": self.username, "password": self.password},
        )
        status_code_of_autorization = new_user_authorization.status_code
        print(status_code_of_autorization)
        authorization_result = new_user_authorization.json()
        
        if status_code_of_autorization == 200:
            print(f"Authorization response is {authorization_result}")
            return True
        else:
            print("Authorization failed with status code: {status_code_of_autorization}")
            return False

    def get_user_token(self):
        
        response = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        generate_token = response.json()
        print(generate_token)

        token = generate_token.get("token")
        self.token = token

        print(f"Token is: {token}")
        return token

    def get_user_status_of_token(self):
        
        response = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        generate_token = response.json()
        status = generate_token.get('status')

        print(f"Status of token is: {status}")
        return status
    
    def get_result_of_token_generation(self):
        
        response = requests.post(
            "https://demoqa.com/Account/v1/GenerateToken",
            json={"userName": self.username, "password": self.password},
        )
        generate_token = response.json()
        result = generate_token.get('result')

        print(f"Result of token generation is: {result}")
        return result
    
    def check_username_of_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
                f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers
            )
        user_response = response.json()
        print(f"Response from API: {user_response} and Token: {token}")
        
        username_of_new_user = user_response.get("username")
        print(username_of_new_user)
        print(self.username)
        
        if username_of_new_user == self.username:
            return True
        return False
        
    def delete_new_user(self):
        uuid = self.user_id
        token = self.token

        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(
                f"https://demoqa.com/Account/v1/User/{uuid}", headers=headers
            )
        status_code = response.status_code

        if status_code == 200:
            print("New user is deleted!")
            return True
        else:
            print("New user isn't deleted!")
            return False
       
