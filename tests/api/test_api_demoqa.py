import pytest
import random


@pytest.mark.api_demoqa
def test_new_user_by_user_id(demoqa_api):
    autotest = random.uniform(0.1, 100.09)
    username = f"{autotest}_Ksuvi"
    password = "Ksu111112@"

    new_user = demoqa_api.create_new_user(username, password)

    assert new_user["username"] == username
    assert new_user["userID"] != " " # need to change
    assert len(new_user["books"]) == 0


@pytest.mark.api_demoqa
def test_new_user_by_token(demoqa_api_user):

    assert demoqa_api_user.token is not None


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

    result_of_check_username = demoqa_api_user.check_username_of_new_user()

    assert result_of_check_username
