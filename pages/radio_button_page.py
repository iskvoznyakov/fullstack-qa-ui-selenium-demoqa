from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class RadioButtonPage(BasePage):
    RESULT_FIELD = (By.CLASS_NAME, "text-success")

    def open(self):
        super().open(BASE_URL + "/radio-button")

    @log_action
    def select_radio_button_by_name(self, name):
        locator = self._get_locator_by_name(name)
        if not self.is_radio_button_disabled(name):
            self.click(locator)

    def _get_locator_by_name(self, name):
        return By.XPATH, f"//label[@for='{name.lower()}Radio']"

    @log_action
    def get_selected_result(self):
        return self.get_text(self.RESULT_FIELD)

    @log_action
    def is_radio_button_disabled(self, name):
        locator = (By.ID, f"{name.lower()}Radio")
        element = self.find_in_dom(locator)
        return element.get_attribute("disabled") is not None
