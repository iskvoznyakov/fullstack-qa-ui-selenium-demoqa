from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class MenuPage(BasePage):
    elements = {"MAIN_ITEM_1": (By.XPATH, "//a[text()='Main Item 1']"),
                "MAIN_ITEM_2": (By.XPATH, "//a[text()='Main Item 2']"),
                "MAIN_ITEM_3": (By.XPATH, "//a[text()='Main Item 3']"),
                "SUB_ITEM": (By.XPATH, "//a[text()='Sub Item']"),
                "SUB_SUB_LIST": (By.XPATH, "//a[text()='SUB SUB LIST »']"),
                "SUB_SUB_ITEM_1": (By.XPATH, "//a[text()='Sub Sub Item 1']"),
                "SUB_SUB_ITEM_2": (By.XPATH, "//a[text()='Sub Sub Item 2']")}

    def open(self):
        super().open(BASE_URL + "/menu")

    @log_action
    def hover_over_element(self, element_name):
        locator = self.elements[element_name]
        if self.is_visible(locator):
            element = self.find(locator)
            ActionChains(self.driver) \
                .move_to_element(to_element=element) \
                .perform()

    @log_action
    def is_menu_visible(self, element_name):
        return self.is_visible(self.elements[element_name])
