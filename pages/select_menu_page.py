from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class SelectMenuPage(BasePage):
    SELECT_VALUE_DROPDOWN = (By.ID, "withOptGroup")
    SELECT_VALUE_OPTIONS = {
        "Group 1, option 1": (By.ID, "react-select-2-option-0-0"),
        "Group 1, option 2": (By.ID, "react-select-2-option-0-1"),
        "Group 2, option 1": (By.ID, "react-select-2-option-1-0"),
        "Group 2, option 2": (By.ID, "react-select-2-option-1-1"),
        "A root option": (By.ID, "react-select-2-option-2"),
        "Another root option": (By.ID, "react-select-2-option-3")
    }
    SELECT_VALUE_OUTPUT = (By.XPATH, "//div[contains(@class, 'singleValue')]")
    SELECT_ONE_DROPDOWN = (By.ID, "selectOne")
    SELECT_ONE_OPTIONS = {
        "Dr.": (By.ID, "react-select-3-option-0-0"),
        "Mr.": (By.ID, "react-select-3-option-0-1"),
        "Mrs.": (By.ID, "react-select-3-option-0-2"),
        "Ms.": (By.ID, "react-select-3-option-0-3"),
        "Prof.": (By.ID, "react-select-3-option-0-4"),
        "Other": (By.ID, "react-select-3-option-0-5")
    }
    OLD_STYLE_SELECT_MENU_DROPDOWN = (By.ID, "oldSelectMenu")
    MULTI_SELECT_DROPDOWN = (By.ID, "react-select-7-input")
    STANDARD_MULTI_SELECT = (By.ID, "cars")

    def open(self):
        super().open(BASE_URL + "/select-menu")

    @log_action
    def select_value_from_select_value_dropdown(self, value):
        self.click(self.SELECT_VALUE_DROPDOWN)
        if self.is_visible(self.SELECT_VALUE_OPTIONS[value]):
            self.click(self.SELECT_VALUE_OPTIONS[value])

    @log_action
    def get_selected_single_value(self):
        return self.get_text(self.SELECT_VALUE_OUTPUT)

    @log_action
    def select_value_from_select_one_dropdown(self, value):
        self.click(self.SELECT_ONE_DROPDOWN)
        if self.is_visible(self.SELECT_ONE_OPTIONS[value]):
            self.click(self.SELECT_ONE_OPTIONS[value])
