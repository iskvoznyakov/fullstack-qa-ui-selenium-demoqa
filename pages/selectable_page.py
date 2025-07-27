from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class SelectablePage(BasePage):
    LIST_TAB = (By.ID, "demo-tab-list")
    GRID_TAB = (By.ID, "demo-tab-grid")

    OPTIONS = {
        "List": (By.XPATH, "//ul[@id='verticalListContainer']//li[contains(@class, 'list-group-item')]"),
        "Grid": (By.XPATH, "//div[@id='demo-tabpane-grid']//li[contains(@class, 'list-group-item')]")
    }

    def open(self):
        super().open(BASE_URL + "/selectable")

    @log_action
    def switch_to_tab(self, tab_name):
        if tab_name == 'List':
            self.click(self.LIST_TAB)
        elif tab_name == 'Grid':
            self.click(self.GRID_TAB)

    @log_action
    def select_elements(self, tab_name, indexes):
        elements = self.driver.find_elements(*self.OPTIONS[tab_name])
        for index in indexes:
            elements[index - 1].click()

    @log_action
    def are_correct_elements_selected(self, tab_name, indexes):
        elements = self.driver.find_elements(*self.OPTIONS[tab_name])
        active_indexes = []
        for i, element in enumerate(elements, 1):
            if "active" in element.get_attribute("class"):
                active_indexes.append(i)
        return set(indexes) == set(active_indexes)
