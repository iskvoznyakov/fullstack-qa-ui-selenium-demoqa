from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class AutocompletePage(BasePage):
    SINGLE_COLOR_INPUT = (By.ID, "autoCompleteSingleInput")
    SINGLE_COLOR_SELECTED = (By.CSS_SELECTOR, "div.auto-complete__single-value")
    MULTIPLE_COLOR_INPUT = (By.ID, "autoCompleteMultipleInput")
    MULTIPLE_COLORS_SELECTED = (By.CSS_SELECTOR, ".auto-complete__multi-value__label")
    SUGGESTIONS = (By.CSS_SELECTOR, ".auto-complete__option")

    def open(self):
        super().open(BASE_URL + "/auto-complete")

    @log_action
    def enter_single_color(self, color):
        self.find(self.SINGLE_COLOR_INPUT).send_keys(color)
        self.find(self.SINGLE_COLOR_INPUT).send_keys(Keys.ENTER)

    @log_action
    def get_selected_single_color(self):
        return self.get_text(self.SINGLE_COLOR_SELECTED)

    @log_action
    def enter_multiple_colors(self, colors):
        for color in colors:
            self.find(self.MULTIPLE_COLOR_INPUT).send_keys(color)
            self.find(self.MULTIPLE_COLOR_INPUT).send_keys(Keys.ENTER)

    @log_action
    def get_selected_multiple_colors(self):
        return {elem.text for elem in self.driver.find_elements(*self.MULTIPLE_COLORS_SELECTED)}

    @log_action
    def input_single_color_partial(self, text):
        self.find(self.SINGLE_COLOR_INPUT).send_keys(text)

    @log_action
    def get_dropdown_suggestions(self):
        return [el.text for el in self.driver.find_elements(By.CSS_SELECTOR, ".auto-complete__option")]

    @log_action
    def select_first_suggestion(self):
        self.find((By.CSS_SELECTOR, ".auto-complete__option")).click()
