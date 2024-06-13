import pytest


@pytest.mark.api                           
def test_user_exists(github_api_client):
    user = github_api_client.get_user('defunkt')

    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api_client):
    r = github_api_client.get_user('butenkosergii')

    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api_client):
    r = github_api_client.search_repo('become-qa-auto')

    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api_client):
    r = github_api_client.search_repo('sergiibutenko_repo_non_exist')

    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api_client):
    r = github_api_client.search_repo('s')

    assert r['total_count'] != 0


@pytest.mark. api_hw                         # new mark for HomeWork tests 
def test_emojis_exists_by_url(github_api_client):
    r = github_api_client.get_emoji_url("100")
    expected_url = "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"

    assert r == expected_url


@pytest.mark. api_hw                         
def test_emojis_exists_by_status_code(github_api_client):
    unique_code = '1f68f.png?v8'
    status_code = github_api_client.get_emoji_status_code_by_unique_code(unique_code)

    assert status_code == 200


@pytest.mark. api_hw                         
def test_emojis_exists_by_key(github_api_client):
    found_emoji_key = 'blossom'
    emoji_key = github_api_client.get_emoji_key(found_emoji_key)
    
    assert emoji_key is not None


@pytest.mark. api_hw
def test_that_list_is_not_empty(github_api_client):
    amount = github_api_client.count_commits("oksana-kolesnyk", "PythonQA")
    
    assert amount != 0


@pytest.mark. api_hw
def test_found_email_and_commit_by_user_and_repo(github_api_client):
    list = github_api_client.get_commits("oksana-kolesnyk", "PythonQA")
    quantity_of_all_commits = github_api_client.count_commits("oksana-kolesnyk", "PythonQA")
    expected_email = 'oksanakolesnyk82@gmail.com'
    expected_message = 'search_repo and get_user for  github_api'

    commit_email = None
    commit_message = None

    for index in range(0, quantity_of_all_commits):
        commit = list[index]
        if commit["commit"]["author"]['email'] == expected_email and commit["commit"]["message"] == expected_message:
            commit_email = commit["commit"]["author"]['email']
            commit_message = commit["commit"]["message"]
            break
    
    assert commit_email == expected_email
    assert commit_message == expected_message
