import pytest
from playwright.sync_api import expect

from logger import LOGGER
from modules.ui.demoqa.pages.text_box_page import TextboxPage

logger = LOGGER.get_logger(__name__)


@pytest.mark.ui_demoqa
def test_url_links_on_main_page(demoqa_app):
    demoqa_app.main_page.go_to_main_page()

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
    demoqa_app.main_page.go_to_main_page()

    for key in ELEMENTS_LOCATORS:
        demoqa_app.main_page.check_links_url(ELEMENTS_LOCATORS[key], EXPECTED_URL[key])
        logger.info(f"For {key} URL is as expected: {EXPECTED_URL[key]}")


"""
Заповнити поля "Full Name", "Email", "Current Address", "Permanent Address".
Натиснути кнопку "Submit".
Очікуваний результат: Після натискання кнопки "Submit" дані відображаються в полі результату під формою.
"""


@pytest.mark.ui_demoqa
def test_check_data_presence_under_form(demoqa_app):
    demoqa_app.text_box_page.go_to_text_box_page()

    DATA = {
        "fullname": TextboxPage.generate_random_fullname(8, 10),
        "email": TextboxPage.generate_random_email(7),
        "current_address": "France, Paris, 75000",
        "permanent_address": "Ukraine, Kyiv, 03187",
    }

    demoqa_app.text_box_page.fill_text_box(
        DATA["fullname"],
        DATA["email"],
        DATA["current_address"],
        DATA["permanent_address"],
    )

    UNDERFORM_LOCATORS = {
        "fullname": "//*[@id='name']",
        "email": "//*[@id='email']",
        "current_address": "//*[@id='output']//*[@id='currentAddress']",
        "permanent_address": "//*[@id='output']//*[@id='permanentAddress']",
    }

    for key in UNDERFORM_LOCATORS:
        demoqa_app.text_box_page.check_data_presence(UNDERFORM_LOCATORS[key], DATA[key])
        logger.info(f"Such data as {key} is present under form.")


"""
Обрати "Check Box".
Розгорнути дерево елементів.
Поставити чекбокси для певних категорій.
Очікуваний результат: Вибрані елементи відображаються у списку під деревом.
"""


@pytest.mark.ui_demoqa
def test_Home_checkbox_checking(demoqa_app):
    demoqa_app.checkbox_page.go_to_checkbox_page()
    demoqa_app.checkbox_page.expand_all()
    demoqa_app.checkbox_page.check_item("Home")

    EXPECTED_TITLE = [
        "home",
        "desktop",
        "notes",
        "commands",
        "documents",
        "workspace",
        "react",
        "angular",
        "veu",
        "office",
        "public",
        "private",
        "classified",
        "general",
        "downloads",
        "wordFile",
        "excelFile",
    ]

    for key in EXPECTED_TITLE:
        demoqa_app.checkbox_page.check_item_title_presence_under_the_tree(key)
        logger.info(f"For {key} URL is as expected: {key}")


# demoqa_app.checkbox_page.uncheck_item("Home")


@pytest.mark.ui_demoqa
def test_Office_checkbox_checking(demoqa_app):

    demoqa_app.checkbox_page.go_to_checkbox_page()
    demoqa_app.checkbox_page.expand_all()
    demoqa_app.checkbox_page.check_item("Office")

    EXPECTED_TITLE = ["office", "public", "private", "classified", "general"]

    for key in EXPECTED_TITLE:
        demoqa_app.checkbox_page.check_item_title_presence_under_the_tree(key)
        logger.info(f"For {key} URL is as expected: {key}")


# demoqa_app.checkbox_page.uncheck_item("Office")

"""
Перейти на DemoQA.
Натиснути на "Elements".
Обрати "Radio Button".
Натиснути на радіо-кнопку "Yes".
Очікуваний результат: Під кнопками відображається повідомлення з текстом "You have selected Yes".
"""


@pytest.mark.ui_demoqa
def test_check_message_if_select_radio_button(demoqa_app):
    demoqa_app.radio_button_page.go_to_radiobutton_page()

    for key in ["Yes", "Impressive"]:
        demoqa_app.radio_button_page.click_radiobutton(key)
        demoqa_app.radio_button_page.check_message_text(key)


@pytest.mark.ui_demoqa
def test_check_click_on_disabled_radio_button(demoqa_app):
    button = "No"

    demoqa_app.radio_button_page.go_to_radiobutton_page()
    demoqa_app.radio_button_page.click_radiobutton(button)


# test to check status of checkbox


"""
Перейти на DemoQA.
Натиснути на "Widgets".
Обрати "Select Menu".
Вибрати певний елемент із списку.
Очікуваний результат: Вибраний елемент відображається у полі вибору.
"""


@pytest.mark.ui_demoqa
def test_check_text_appears_if_select_element_in_select_value_option_drop_down(demoqa_app):

    demoqa_app.widgets_page.go_to_widgets_page()
    demoqa_app.widgets_page.click_on_select_menu()
    demoqa_app.select_menu_page.check_select_menu_url()
    demoqa_app.select_menu_page.select_in_select_value_option()
    demoqa_app.select_menu_page.check_selected_in_select_value_option_text_appears()
    
"""
Перетягнути елемент "Drag me" на зону "Drop here".
Очікуваний результат: З'являється повідомлення "Dropped!".
"""
@pytest.mark.ui_demoqa
def test_check_message_after_drag_and_drop_element(demoqa_app):
    demoqa_app.droppable_page.go_to_droppable_page()
    demoqa_app.droppable_page.drag_and_drop_the_Drag_Me_item()