import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from utils.logger import logger


class SliderPage(BasePage):
    SLIDER_OUTPUT = (By.ID, "sliderValue")
    SLIDER = (By.CSS_SELECTOR, ".range-slider")

    def open(self):
        super().open(BASE_URL + "/slider")

    @log_action
    def set_slider_value(self, value: int):
        slider = self.find(self.SLIDER)
        current_value = int(slider.get_attribute("value"))

        if current_value == value:
            return

        self.driver.execute_script("""
            const slider = arguments[0];
            const val = arguments[1];

            const nativeSetter = Object.getOwnPropertyDescriptor(
                HTMLInputElement.prototype, 'value').set;
            nativeSetter.call(slider, val);

            const inputEvent = new Event('input', { bubbles: true });
            const changeEvent = new Event('change', { bubbles: true });
            slider.dispatchEvent(inputEvent);
            slider.dispatchEvent(changeEvent);
        """, slider, value)

    @log_action
    def get_value(self):
        return self.find(self.SLIDER_OUTPUT).get_attribute("value")
