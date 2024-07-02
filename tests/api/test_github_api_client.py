import pytest


@pytest.mark.api
def test_user_exists(github_api_client):
    user = github_api_client.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api_client):
    r = github_api_client.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api_client):
    r = github_api_client.search_repo("become-qa-auto")

    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api_client):
    r = github_api_client.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api_client):
    r = github_api_client.search_repo("s")

    assert r["total_count"] != 0


# new mark for HomeWork tests

@pytest.mark.api_hw  
def test_emojis_exists_by_url(github_api_client):
    emoji_name = "100"
    r = github_api_client.get_emoji_url(emoji_name)
    expected_url = (
        "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"
    )

    assert r == expected_url


@pytest.mark.api_hw
def test_emojis_exists_by_status_code(github_api_client):
    unique_code = "1f68f.png?v8"
    status_code = github_api_client.get_emoji_status_code_by_unique_code(unique_code)

    assert status_code == 200


@pytest.mark.api_hw
def test_emojis_exists_by_key(github_api_client):
    found_emoji_key = "blossom"
    emoji_key = github_api_client.get_emoji_key(found_emoji_key)

    assert emoji_key is not None


@pytest.mark.api_hw
def test_that_list_is_not_empty(github_api_client):
    OWNER = "oksana-kolesnyk"
    REPO = "PythonQA"
    amount = github_api_client.count_commits(OWNER, REPO)

    assert amount != 0


@pytest.mark.api_hw
def test_check_email_and_commit_by_user_and_by_repo(github_api_client):
    OWNER = "oksana-kolesnyk"
    REPO = "PythonQA"
    expected_email = 'oksanakolesnyk82@gmail.com'
    expected_message = 'search_repo and get_user for  github_api'
    commit_email, commit_message = github_api_client.check_email_and_commit_by_user_and_by_repo(
        OWNER,
        REPO,
        expected_email,
       expected_message,
    )

    assert commit_email == expected_email
    assert commit_message == expected_message
