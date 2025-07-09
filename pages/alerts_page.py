from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage(BasePage):
    ALERT_BUTTON = (By.ID, "alertButton")
    TIME_ALERT_BUTTON = (By.ID, "timerAlertButton")
    CONFIRM_BOX_BUTTON = (By.ID, "confirmButton")
    CONFIRM_OUTPUT_FIELD = (By.ID, "confirmResult")
    PROMPT_BOX_BUTTON = (By.ID, "promtButton")
    PROMPT_OUTPUT_FIELD = (By.ID, "promptResult")

    def open(self):
        super().open(BASE_URL + "/alerts")

    @log_action
    def click_alert_button(self):
        self.click(self.ALERT_BUTTON)

    @log_action
    def click_time_alert_button(self):
        self.click(self.TIME_ALERT_BUTTON)

    @log_action
    def click_confirm_box_button(self):
        self.click(self.CONFIRM_BOX_BUTTON)

    @log_action
    def click_prompt_box_button(self):
        self.click(self.PROMPT_BOX_BUTTON)

    @log_action
    def alert_is_opened(self):
        text = self.alert_text()
        return text == "You clicked a button" if text else False

    @log_action
    def delayed_alert_is_opened(self):
        text = self.alert_text()
        return text == "This alert appeared after 5 seconds" if text else False

    @log_action
    def confirm_alert_is_opened(self, action):
        if action == "accept":
            self.alert_accept()
            return "Ok" in self.get_text(self.CONFIRM_OUTPUT_FIELD)
        elif action == "dismiss":
            self.alert_dismiss()
            return "Cancel" in self.get_text(self.CONFIRM_OUTPUT_FIELD)

    @log_action
    def prompt_alert_is_opened(self, text):
        self.alert_send_keys(text)
        return text in self.get_text(self.PROMPT_OUTPUT_FIELD)
