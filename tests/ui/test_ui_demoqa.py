import pytest

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
    
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("home")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("desktop")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("notes")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("commands")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("documents")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("workspace")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("react")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("angular")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("veu")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("office")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("public")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("private")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("classified")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("general")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("downloads")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("wordFile")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("excelFile")
    
   # demoqa_app.checkbox_page.uncheck_item("Home")
    
@pytest.mark.ui_demoqa
def test_Office_checkbox_checking(demoqa_app):
    demoqa_app.checkbox_page.go_to_checkbox_page()
    demoqa_app.checkbox_page.expand_all()
    demoqa_app.checkbox_page.check_item("Office")
    
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("office")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("public")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("private")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("classified")
    demoqa_app.checkbox_page.check_item_title_presence_under_the_tree("general")
    
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
def test_click_on_disabled_radio_button(demoqa_app):
    demoqa_app.radio_button_page.go_to_radiobutton_page()
    demoqa_app.radio_button_page.click_radiobutton("No")