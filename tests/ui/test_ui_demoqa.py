import pytest
from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.demoqa.pages.main_page import MainPage
from modules.ui.demoqa.pages.text_box_page import TextboxPage

logger = LOGGER.get_logger(__name__)


@pytest.mark.ui_demoqa
def test_url_links_on_main_page(main_demoqa):

    EXPECTED_URL = {
        "Elements": "https://demoqa.com/elements",
        "Forms": "https://demoqa.com/forms",
        "Alerts": "https://demoqa.com/alertsWindows",
        "Widgets": "https://demoqa.com/widgets",
        "Interactions": "https://demoqa.com/interaction",
        "Bookstore": "https://demoqa.com/books",
    }
    ELEMENTS_LOCATORS = {
        "Elements": "//h5[text()='Elements']",
        "Forms": "//h5[text()='Forms']",
        "Alerts": "//h5[text()= 'Alerts, Frame & Windows']",
        "Widgets": "//h5[text()='Widgets']",
        "Interactions": "//h5[text()='Interactions']",
        "Bookstore": "//h5[text()='Book Store Application']",
    }

    for key in ELEMENTS_LOCATORS:
        main_demoqa.check_links_url(ELEMENTS_LOCATORS[key], EXPECTED_URL[key])
        logger.info(f"For {key} URL is as expected: {EXPECTED_URL[key]}")


"""
Заповнити поля "Full Name", "Email", "Current Address", "Permanent Address".
Натиснути кнопку "Submit".
Очікуваний результат: Після натискання кнопки "Submit" дані відображаються в полі результату під формою.
"""


@pytest.mark.ui_demoqa
def test_check_data_presence_under_form(textbox_demoqa):
    DATA = {
        "fullname": TextboxPage.generate_random_fullname(8, 10),
        "email": TextboxPage.generate_random_email(7),
        "current_address": "France, Paris, 75000",
        "permanent_address": "Ukraine, Kyiv, 03187",
    }

    textbox_demoqa.fill_text_box(
        DATA["fullname"],
        DATA["email"],
        DATA["current_address"],
        DATA["permanent_address"],
    )

    UNDERFORM_LOCATORS = {
        "fullname": "//div[@id='name']",
        "email": "//div[@id='email']",
        "current_address": "//div[@id='currentAddress']",
        "permanent_address": "//div[@id='permanentAddress']",
    }

    for key in UNDERFORM_LOCATORS:
        textbox_demoqa.check_data_presence(UNDERFORM_LOCATORS[key], DATA[key])
        logger.info(f"Such data as {key} is present under form.")


"""
Обрати "Check Box".
Розгорнути дерево елементів.
Поставити чекбокси для певних категорій.
Очікуваний результат: Вибрані елементи відображаються у списку під деревом.
"""


@pytest.mark.ui_demoqa
def test_checkbox_checking(checkbox_demoqa):
    checkbox_demoqa.expand_all()
