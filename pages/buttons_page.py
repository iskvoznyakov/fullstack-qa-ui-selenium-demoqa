from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    DYNAMIC_ID_BUTTON = (By.XPATH, "//button[text() ='Click Me']")
    DOUBLE_CLICK_OUTPUT_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_OUTPUT_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_ID_OUTPUT_MESSAGE = (By.ID, "dynamicClickMessage")

    def open(self):
        super().open(BASE_URL + "/buttons")

    @log_action
    def click_double_click_button(self):
        ActionChains(self.driver).double_click(self.find(self.DOUBLE_CLICK_BUTTON)).perform()

    @log_action
    def click_right_click_button(self):
        ActionChains(self.driver).context_click(self.find(self.RIGHT_CLICK_BUTTON)).perform()

    @log_action
    def click_button_with_dynamic_id(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    @log_action
    def click_result_is_visible(self, click_type: str):
        mapping = {
            "double": self.DOUBLE_CLICK_OUTPUT_MESSAGE,
            "right": self.RIGHT_CLICK_OUTPUT_MESSAGE,
            "dynamic": self.DYNAMIC_ID_OUTPUT_MESSAGE
        }
        return self.is_visible(mapping[click_type])
