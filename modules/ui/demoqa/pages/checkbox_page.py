from playwright.sync_api import expect

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
        "Home": "//*[@id='tree-node']/ol/li/span/label/span[1]",
        "Desktop": "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]",
        "Notes": "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]",
        "Commands": "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]",
        "Documents": "//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]/svg",
        "WorkSpace": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]",
        "React": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]",
        "Angular": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]",
        "Veu": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]",
        "Office": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]",
        "Public": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]",
        "Private": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]",
        "Classified": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]",
        "General": "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]",
        "Downloads": "//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]",
        "Word File.doc": "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]",
        "Exel File.doc": "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]",
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

    def check_item(self, key):
        checkbox_locator = self.CHECKBOX_ITEM_LOCATOR[key]
        self.demoqa_app.check(checkbox_locator)
        logger.info(f"For item: {key} checkbox is checked")
        return self

    def uncheck_item(self, key):
        checkbox_locator = self.CHECKBOX_ITEM_LOCATOR[key]
        self.demoqa_app.uncheck(checkbox_locator)
        logger.info(f"For item: {key} checkbox is unchecked")
        return self

    def check_item_title_presence_under_the_tree(self, expected_title_of_checked_item):
        locator = self.demoqa_app.page.locator(
            self.UNDER_TREE_ITEM_LOCATOR[expected_title_of_checked_item]
        )
        expect(locator).to_be_visible(timeout=10000)

        actual_title = locator.text_content()
        logger.info(
            f"Actual title of checked item with locator {locator}: {actual_title}"
        )
        expect(locator).to_contain_text(expected_title_of_checked_item)
        logger.info(
            f"{expected_title_of_checked_item} item is present under the item's tree."
        )
