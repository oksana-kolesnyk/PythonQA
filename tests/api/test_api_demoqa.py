import pytest


@pytest.mark.api_demoqa
def test_new_user_creation_by_user_id(demoqa_api):
    username = "Ksu3"
    password = "Ksu111111@"
    
    user_id = demoqa_api.get_user_id(username, password)
    
    print(user_id)
    assert user_id != " "
    
 
@pytest.mark.api_demoqa
def test_new_user_creation_by_status_code(demoqa_api):
    username = "Ksu3"
    password = "Ksu111111@"
    status_code = demoqa_api.get_new_user_status_code(username, password)

    if status_code == 201 or status_code == 200:
       print(f"Success: {status_code}")
    else:
       print(f"Error: {status_code}")
  
  
@pytest.mark.api_demoqa
def test_check_id_of_deleted_user(demoqa_api):
    username = "Ksu3"
    password = "Ksu111111@"
    
    demoqa_api.delete_new_user(username, password)
    user_id = demoqa_api.get_user_id(username, password)

    assert user_id is None
