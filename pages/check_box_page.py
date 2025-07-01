from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    RESULT_FIELD = (By.ID, "result")
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")

    def open(self):
        super().open(BASE_URL + "/checkbox")

    def expand_all_the_checkboxes(self):
        self.click(self.EXPAND_ALL_BUTTON)

    def click_checkbox_by_name(self, name):
        checkbox_locator = (By.XPATH, f"//span[contains(text(), '{name}')]")
        self.click(checkbox_locator)

    def _get_selected_items(self):
        if not self.is_visible(self.RESULT_FIELD):
            return []
        result_text = self.get_text(self.RESULT_FIELD)
        return [line.strip().lower() for line in result_text.split('\n') if
                "You have selected" not in line and line.strip()]

    def is_checkbox_selected(self, checkbox):
        return checkbox.lower() in self._get_selected_items()

    def are_checkboxes_selected(self, checkboxes: list):
        return set(checkbox.lower() for checkbox in checkboxes).issubset(set(self._get_selected_items()))
