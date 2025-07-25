from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class SortablePage(BasePage):
    LIST_TAB = (By.ID, "demo-tab-list")
    list_options = {"one": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'One')]"),
                    "two": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'Two')]"),
                    "three": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'Three')]"),
                    "four": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'Four')]"),
                    "five": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'Five')]"),
                    "six": (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'Six')]"), }
    LIST_OPTIONS = (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')]")

    GRID_TAB = (By.ID, "demo-tab-grid")
    grid_options = {"one": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'One')]"),
                    "two": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'Two')]"),
                    "three": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'Three')]"),
                    "four": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'Four')]"),
                    "five": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'Five')]"),
                    "six": (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(text(), 'Six')]"), }
    GRID_OPTIONS = (By.XPATH, "//div[@id='demo-tabpane-grid']//div[contains(@class, 'list-group-item')]")

    def open(self):
        super().open(BASE_URL + "/sortable")

    @log_action
    def drag_and_drop(self, from_index, to_index):
        (ActionChains(self.driver).
         drag_and_drop(self.driver.find_elements(*self.LIST_OPTIONS)[from_index],
                       self.driver.find_elements(*self.LIST_OPTIONS)[to_index]).
         perform())

    @log_action
    def get_list_items(self):
        return [elem.text for elem in self.driver.find_elements(*self.LIST_OPTIONS)]
