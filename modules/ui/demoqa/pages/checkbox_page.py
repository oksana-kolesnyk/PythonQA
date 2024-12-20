from playwright.sync_api import expect
from modules.ui.base_page import BasePage

from logger import LOGGER

logger = LOGGER.get_logger(__name__)


class CheckboxPage:

    # URL BLOCK
    URL = "https://demoqa.com/checkbox"

    # ELEMENTS LOCATORS BLOCK
    TOGGLE_BUTTON = "//button[@aria-label='Toggle']]"
    EXPAND_ALL_BUTTON = "//button[@aria-label='Expand all']"
    COLLAPSE_ALL_BUTTON = "//button[@aria-label='Collapse all']"

    CHECKBOX_ITEM_LOCATOR = {
        "Home": "//*[@id='tree-node-home']/parent::*//span[@class='rct-checkbox']",
        "Desktop": "//*[@id='tree-node-desktop']/parent::*//span[@class='rct-checkbox']",
        "Notes": "//*[@id='tree-node-notes']/parent::*//span[@class='rct-checkbox']",
        "Commands": "//*[@id='tree-node-commands']/parent::*//span[@class='rct-checkbox']",
        "Documents": "//*[@id='tree-node-documents']/parent::*//span[@class='rct-checkbox']",
        "WorkSpace": "//*[@id='tree-node-workspace']/parent::*//span[@class='rct-checkbox']",
        "React": "//*[@id='tree-node-react']/parent::*//span[@class='rct-checkbox']",
        "Angular": "//*[@id='tree-node-angular']/parent::*//span[@class='rct-checkbox']",
        "Veu": "//*[@id='tree-node-veu']/parent::*//span[@class='rct-checkbox']",
        "Office": "//*[@id='tree-node-office']/parent::*//span[@class='rct-checkbox']",
        "Public": "//*[@id='tree-node-public']/parent::*//span[@class='rct-checkbox']",
        "Private": "//*[@id='tree-node-private']/parent::*//span[@class='rct-checkbox']",
        "Classified": "//*[@id='tree-node-classified']/parent::*//span[@class='rct-checkbox']",
        "General": "//*[@id='tree-node-general']/parent::*//span[@class='rct-checkbox']",
        "Downloads": "//*[@id='tree-node-downloads']/parent::*//span[@class='rct-checkbox']",
        "Word File.doc": "//*[@id='tree-node-worldFile']/parent::*//span[@class='rct-checkbox']",
        "Exel File.doc": "//*[@id='tree-node-exelFile']/parent::*//span[@class='rct-checkbox']",
    }

    UNDER_TREE_ITEM_LOCATOR = {
        "home": "//div[@id='result']//span[@class='text-success' and text()='home']",
        "desktop": "//div[@id='result']//span[@class='text-success' and text()='desktop']",
        "notes": "//div[@id='result']//span[@class='text-success' and text()='notes']",
        "commands": "//div[@id='result']//span[@class='text-success' and text()='commands']",
        "documents": "//div[@id='result']//span[@class='text-success' and text()='documents']",
        "workspace": "//div[@id='result']//span[@class='text-success' and text()='workspace']",
        "react": "//div[@id='result']//span[@class='text-success' and text()='react']",
        "angular": "//div[@id='result']//span[@class='text-success' and text()='angular']",
        "veu": "//div[@id='result']//span[@class='text-success' and text()='veu']",
        "office": "//div[@id='result']//span[@class='text-success' and text()='office']",
        "public": "//div[@id='result']//span[@class='text-success' and text()='public']",
        "private": "//div[@id='result']//span[@class='text-success' and text()='private']",
        "classified": "//div[@id='result']//span[@class='text-success' and text()='classified']",
        "general": "//div[@id='result']//span[@class='text-success' and text()='general']",
        "downloads": "//div[@id='result']//span[@class='text-success' and text()='downloads']",
        "wordFile": "//div[@id='result']//span[@class='text-success' and text()='wordFile']",
        "excelFile": "//div[@id='result']//span[@class='text-success' and text()='excelFile']",
    }

    def __init__(self, demoqa_app) -> None:
        self.demoqa_app = demoqa_app

    # USER METHODS BLOCK

    def go_to_checkbox_page(self):
        self.demoqa_app.goto(CheckboxPage.URL)

    def expand_collapse_box_tree_by_toggle(self):
        self.demoqa_app.click(self.TOGGLE_BUTTON)

    def expand_all(self):
        self.demoqa_app.click(self.EXPAND_ALL_BUTTON)

    def collapse_all(self):
        self.demoqa_app.click(self.COLLAPSE_ALL_BUTTON)

    def check_checkbox(self, key):
        checkbox_locator = self.CHECKBOX_ITEM_LOCATOR[key]

        self.demoqa_app.check(checkbox_locator)
        self.demoqa_app.toBeChecked(checkbox_locator)
        logger.info(f"For item: {key} checkbox is checked")

        return self

    def uncheck_checkbox(self, key):
        checkbox_locator = self.CHECKBOX_ITEM_LOCATOR[key]
        self.demoqa_app.uncheck(checkbox_locator)
        logger.info(f"For item: {key} checkbox is unchecked")
        return self

    def expect_item_title_presence_under_the_tree(self, expected_title_of_checked_item):
        locator = self.demoqa_app.page.locator(
            self.UNDER_TREE_ITEM_LOCATOR[expected_title_of_checked_item]
        )
        actual_title = locator.text_content()
        logger.info(
            f"Actual title of checked item with locator {locator}: {actual_title}"
        )
        
        BasePage.expect_text_appears(locator, expected_title_of_checked_item)
        logger.info(
            f"{expected_title_of_checked_item} item is present under the item's tree."
        )
        
