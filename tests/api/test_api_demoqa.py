import pytest
import random

"""
Call POST https://demoqa.com/Account/v1/User to create new user.
Save userId from Response.
Create Authorization Token by calling /Account/v1/GenerateToken with credentials of user created on step1. 
Call endpoint GET /Account/v1/User/{UUID} with user Token as Authorization Header (exact format: “Bearer Token”).
Verify that username in Response Body corresponds to data provided on step 1
"""

@pytest.mark.api_demoqa
def test_new_user_by_user_id(demoqa_api):
    autotest = random.uniform(0.1, 100.09)
    username = f"{autotest}_Ksuvi"
    password = "Ksu111112@"

    new_user = demoqa_api.create_new_user(username, password)
    user_id = demoqa_api.user_id
    result, msg = demoqa_api.check_user_id_format(user_id)

    assert new_user["username"] == username
    assert result, msg
    assert len(new_user["books"]) == 0


@pytest.mark.api_demoqa
def test_new_user_token_format(demoqa_api_user):
    token = demoqa_api_user.token
    result, msg = demoqa_api_user.check_token_format(token)

    assert result, msg


@pytest.mark.api_demoqa
def test_new_user_by_token_status(demoqa_api_user):
    token_status = demoqa_api_user.token_status

    assert token_status == "Success"


@pytest.mark.api_demoqa
def test_get_result_of_token_generation(demoqa_api_user):
    token_result = demoqa_api_user.token_result

    assert token_result == "User authorized successfully."


@pytest.mark.api_demoqa
def test_check_username_of_new_user(demoqa_api_user):
    result, msg = demoqa_api_user.check_username_of_new_user()

    assert result, msg

"""
Get Books list as Test user
Create Authorization Token by calling GET /Account/v1/GenerateToken with Test user credentials.
Call GET https://demoqa.com/BookStore/v1/Books with Test user Token.
Verify that 8 Books were returned in result (it is suggested to use ArrayList to save value of “books” object from Response Body).
Verify that Book with isbn 9781449325862 has title Git Pocket Guide 
"""     

@pytest.mark.api_demoqa
def test_check_books_quantity(demoqa_api_user):
    book_list = demoqa_api_user.get_book_list()
    count = demoqa_api_user.count_books(book_list)
    expected_count = 8
    
    assert count == expected_count, f"{expected_count} books are expected in the list of the books"


@pytest.mark.api_demoqa
def test_check_book_title_by_ibsn(demoqa_api_user):
    isbn = "9781449325862"
    expected_title = "Git Pocket Guide"
    
    title = demoqa_api_user.get_title_book_with_ibsn(isbn)
     
    assert title == expected_title, f"Expected title: {expected_title}, but actual title: {title}"