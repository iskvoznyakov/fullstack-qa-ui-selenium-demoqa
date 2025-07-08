from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class DynamicPropertiesPage(BasePage):
    RANDOM_ID_TEXT = (By.XPATH, "(//h1[text()='Dynamic Properties']/following-sibling::p)[1]")
    WILL_ENABLE_BUTTON = (By.ID, "enableAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_BUTTON = (By.ID, "visibleAfter")

    def open(self):
        super().open(BASE_URL + "/dynamic-properties")

    @log_action
    def wait_until_button_enabled(self):
        return self.is_clickable(self.WILL_ENABLE_BUTTON)

    @log_action
    def wait_until_visible(self):
        return self.is_visible(self.VISIBLE_AFTER_BUTTON)

    @log_action
    def wait_until_color_changes(self):
        element = self.find(self.COLOR_CHANGE_BUTTON)
        color_before = element.value_of_css_property("color")
        try:
            self.wait.until(lambda d: element.value_of_css_property("color") != color_before)
            return True
        except TimeoutException:
            return False

    @log_action
    def find_random_id_text(self):
        return "This text has random Id" == self.get_text(self.RANDOM_ID_TEXT)
