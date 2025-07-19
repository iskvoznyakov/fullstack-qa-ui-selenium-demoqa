from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.common.exceptions import TimeoutException


class ProgressBarPage(BasePage):
    START_STOP_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.ID, "progressBar")
    RESET_BUTTON = (By.ID, "resetButton")

    def open(self):
        super().open(BASE_URL + "/progress-bar")

    @log_action
    def start_progress(self):
        self.click(self.START_STOP_BUTTON)

    @log_action
    def get_progress_value(self):
        progress_bar = self.find(self.PROGRESS_BAR)
        value = progress_bar.get_attribute("aria-valuenow")
        if value and value.isdigit():
            return int(value)

        text_value = progress_bar.text.strip().replace("%", "")
        if text_value.isdigit():
            return int(text_value)

        return 0

    @log_action
    def _check_progress(self, driver, value):
        current = self.get_progress_value()
        return current >= value

    @log_action
    def wait_for_progress_to_reach(self, value, stop_after=True):
        try:
            self.wait.until(lambda d: self._check_progress(d, value))
            if stop_after and value < 100:
                self.click(self.START_STOP_BUTTON)
        except TimeoutException:
            current = self.get_progress_value()
            raise TimeoutException(f"Не удалось дождаться {value}%. Текущее значение: {current}%")

    @log_action
    def reset_progress(self):
        self.driver.find_element(*self.RESET_BUTTON).click()
