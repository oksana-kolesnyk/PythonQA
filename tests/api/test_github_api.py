import pytest


@pytest.mark.api                            # має мітку api
def test_user_exists(github_api):           # Використовує фікстуру github_api
    user = github_api.get_user('defunkt')   # В тілі тесту використати метод get_user фікстури github_api
    assert user['login'] == 'defunkt'       # Перевірити, що тіло відповіді від сервера має атрибут login, значення якого має дорівнювати  defunkt


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found' # Перевірити, що тіло відповіді від сервера має атрибут message значення якого має дорівнювати  Not Found


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto') # В тілі тесту використати метод search_repo фікстури github_api. Використати ім’я репозиторія для пошуку become-qa-auto
    assert r['total_count'] == 58 # Перевірити, що тіло відповіді від сервера має атрибут total_count, значення якого має дорівнювати очікуваному на момент створення тесту значенню, наприклад 58.
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist') # Використати ім’я репозиторія для пошуку sergiibutenko_repo_non_exist або будь-яке інше ім’я, що не існує на момент створення тесту
    assert r['total_count'] == 0 # Перевірити, що тіло відповіді від сервера має атрибут total_count, значення якого має дорівнювати 0.
    

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s') # Використати ім’я репозиторія для пошуку s або будь-яке інше ім’я, що складається з одного символу
    assert r['total_count'] != 0 # Перевірити, що тіло відповіді від сервера має атрибут total_count, значення якого має не дорівнювати 0.