from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class ToolTipsPage(BasePage):
    elements = {
        "button": (By.ID, "toolTipButton"),
        "text_field": (By.ID, "toolTipTextField"),
        "contrary_word": (By.XPATH, "//div[@id='texToolTopContainer']/a[text()='Contrary']"),
        "section_word": (By.XPATH, "//div[@id='texToolTopContainer']/a[text()='1.10.32']")
    }
    tooltips = {
        "button": (By.ID, "buttonToolTip"),
        "text_field": (By.ID, "textFieldToolTip"),
        "contrary_word": (By.ID, "contraryTexToolTip"),
        "section_word": (By.ID, "sectionToolTip")
    }

    def open(self):
        super().open(BASE_URL + "/tool-tips")

    @log_action
    def hover_over_element(self, element_name):
        element = self.find(self.elements[element_name])
        ActionChains(self.driver) \
            .move_to_element(to_element=element) \
            .perform()
        self.wait.until(
            lambda driver: self.get_text(self.tooltips[element_name]).strip() != ""
        )

    @log_action
    def get_hover_text(self, element_name):
        return self.get_text(self.tooltips[element_name])
