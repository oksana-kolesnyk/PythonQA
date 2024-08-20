import requests
import json

'''
Call POST https://demoqa.com/Account/v1/User to create new user.
Save userId from Response.
Create Authorization Token by calling /Account/v1/GenerateToken with credentials of user created on step1. 
Call endpoint GET /Account/v1/User/{UUID} with user Token as Authorization Header (exact format: “Bearer Token”).
Verify that username in Response Body corresponds to data provided on step 1
'''


class Demoqa:
    def create_new_user(self, username, password):
       
        new_user = requests.post("https://demoqa.com/Account/v1/User", 
                                 json={"userName": username, "password": password})
        response_body = new_user.json()
        
        print(response_body)
        return (response_body)
         
    def get_new_user_status_code(self, username, password):
       
        response = requests.get("https://demoqa.com/Account/v1/User", 
                                 auth=(username, password))
        status_code = response.status_code
        
        return status_code
    
    def get_user_token(self, username, password):
        response = requests.post("https://demoqa.com/Account/v1/GenerateToken",
                               auth=(username, password))
        response = response.json()
        token = response.get("token")
        result = response.get("result")
        
        return token, result
    
    def get_user_id(self, username, password):
        response = requests.get("https://demoqa.com/Account/v1/User", 
                                 auth=(username, password))
        print(response.text)
        try:
            response_js = json.loads(response.text)
            id_of_user = response_js.get("userID")
        except json.JSONDecodeError:
            print("Json error parsel or empty answer")
            return None
    
        print( id_of_user)
        return id_of_user
    
    def delete_new_user(self, username, password):
        uuid = self.get_user_id(username, password)
        response = requests.delete(f"https://demoqa.com//Account/v1/User/{uuid}")
        status_code = response.status_code
        
        if status_code == 200:
            return True
        return False
    
    
   