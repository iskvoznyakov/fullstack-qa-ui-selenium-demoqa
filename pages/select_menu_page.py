from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    SELECT_ONE_DROPDOWN = (By.ID, "selectOne")
    SELECT_ONE_OPTIONS = {
        "Dr.": (By.ID, "react-select-3-option-0-0"),
        "Mr.": (By.ID, "react-select-3-option-0-1"),
        "Mrs.": (By.ID, "react-select-3-option-0-2"),
        "Ms.": (By.ID, "react-select-3-option-0-3"),
        "Prof.": (By.ID, "react-select-3-option-0-4"),
        "Other": (By.ID, "react-select-3-option-0-5")
    }

    SELECT_VALUE_AND_SELECT_ONE_OUTPUT = (By.XPATH, "//div[contains(@class, 'singleValue')]")

    OLD_STYLE_SELECT_MENU_DROPDOWN = (By.ID, "oldSelectMenu")

    MULTI_SELECT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'placeholder')][text()='Select...']")
    MULTI_SELECT_OPTIONS = {
        "Green": (By.ID, "react-select-4-option-0"),
        "Blue": (By.ID, "react-select-4-option-1"),
        "Black": (By.ID, "react-select-4-option-2"),
        "Red": (By.ID, "react-select-4-option-3")
    }
    MULTI_SELECT_OUTPUT = (By.XPATH, "//div[contains(@class, 'multiValue')]")

    STANDARD_MULTI_SELECT = (By.ID, "cars")

    def open(self):
        super().open(BASE_URL + "/select-menu")

    @log_action
    def select_value_from_select_value_dropdown(self, value):
        self.click(self.SELECT_VALUE_DROPDOWN)
        if self.is_visible(self.SELECT_VALUE_OPTIONS[value]):
            self.click(self.SELECT_VALUE_OPTIONS[value])

    @log_action
    def select_value_from_select_one_dropdown(self, value):
        self.click(self.SELECT_ONE_DROPDOWN)
        if self.is_visible(self.SELECT_ONE_OPTIONS[value]):
            self.click(self.SELECT_ONE_OPTIONS[value])

    @log_action
    def get_selected_single_value(self):
        return self.get_text(self.SELECT_VALUE_AND_SELECT_ONE_OUTPUT)

    @log_action
    def select_value_from_old_style_select_menu(self, color):
        select = Select(self.find(self.OLD_STYLE_SELECT_MENU_DROPDOWN))
        select.select_by_visible_text(color)
        return select.first_selected_option.text

    @log_action
    def select_values_from_multi_select_dropdown(self, values):
        self.click(self.MULTI_SELECT_DROPDOWN)
        for value in values:
            if self.is_visible(self.MULTI_SELECT_OPTIONS[value]):
                self.click(self.MULTI_SELECT_OPTIONS[value])

    @log_action
    def get_selected_multi_values(self):
        elements = self.driver.find_elements(*self.MULTI_SELECT_OUTPUT)
        result = [element.text for element in elements]
        # return self.get_text(self.MULTI_SELECT_OUTPUT)
        return result

    @log_action
    def select_values_from_standard_multi_select(self, values):
        select = Select(self.find(self.STANDARD_MULTI_SELECT))
        for value in values:
            select.select_by_value(value)
        return [opt.text for opt in select.all_selected_options]
