import pytest
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from modules.ui.page_objects.rozetka_navushnyky_aksesuary_page import (RozetkaNavushnykyAksesuaryPage)


@pytest.mark.ui
def test_check_incorrect_username_page_object(page_creation):
    sign_in_page = SignInPage()
    sign_in_page.driver = page_creation.driver  # receive driver from fixture
    # open https://github.com/login
    sign_in_page.go_to()
    invalid_username = "page_object@gmail.com"
    invalid_password = "wrong password"
    sign_in_page.try_login(invalid_username, invalid_password)

    # verify that title of page is expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui_hw  # new mark for HomeWork tests
def test_search_text_in_searchfield_page_object(page_creation):
    search_on_page = RozetkaMainPage()
    search_on_page.driver = page_creation.driver
    # open 'https://rozetka.com.ua/ua/'
    search_on_page.go_to()
    text = "ноутбук"
    search_on_page.try_search(text)
    expected_link = "https://rozetka.com.ua/ua/notebooks/c80004/#search_text=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA"

    # verify that current URL equals expected URL
    assert search_on_page.check_link(expected_link)


@pytest.mark.ui_hw
def test_sorting_items_from_expensive_to_cheepeast_page_object(page_creation):
    sort_on_page = RozetkaNavushnykyAksesuaryPage()
    sort_on_page.driver = page_creation.driver
    # open 'https://rozetka.com.ua/ua/naushniki-i-aksessuari/c4660594/'
    sort_on_page.go_to()
    option_text = "Від дорогих до дешевих"
    sort_on_page.find_sorter(option_text)
    expected_link = (
        "https://rozetka.com.ua/ua/naushniki-i-aksessuari/c4660594/sort=expensive/"
    )

    # verify that current URL equals expected URL
    assert sort_on_page.check_link(expected_link)
