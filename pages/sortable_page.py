from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class SortablePage(BasePage):
    LIST_TAB = (By.ID, "demo-tab-list")

    GRID_TAB = (By.ID, "demo-tab-grid")

    OPTIONS = {
        "List": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')]"),
        "Grid": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(@class, 'list-group-item')]")
    }

    def open(self):
        super().open(BASE_URL + "/sortable")

    @log_action
    def switch_to_tab(self, tab_name):
        if tab_name == 'List':
            self.click(self.LIST_TAB)
        elif tab_name == 'Grid':
            self.click(self.GRID_TAB)

    @log_action
    def drag_and_drop(self, tab_name, from_index, to_index):
        if tab_name not in self.OPTIONS:
            raise ValueError(f"Некорректное имя таба: {tab_name}")

        elements = self.driver.find_elements(*self.OPTIONS[tab_name])

        (ActionChains(self.driver).
         drag_and_drop(elements[from_index],
                       elements[to_index]).
         perform())

    @log_action
    def get_items(self, tab_name):
        if tab_name not in self.OPTIONS:
            raise ValueError(f"Некорректное имя таба: {tab_name}")

        elements = self.driver.find_elements(*self.OPTIONS[tab_name])
        return [elem.text for elem in elements]
