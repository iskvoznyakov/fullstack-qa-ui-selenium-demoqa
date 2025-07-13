from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class AccordianPage(BasePage):
    HEADERS = {
        "section_1": (By.ID, "section1Heading"),
        "section_2": (By.ID, "section2Heading"),
        "section_3": (By.ID, "section3Heading"),
    }

    CONTENTS = {
        "section_1": (By.ID, "section1Content"),
        "section_2": (By.ID, "section2Content"),
        "section_3": (By.ID, "section3Content"),
    }

    def open(self):
        super().open(BASE_URL + "/accordian")

    @log_action
    def click_section(self, section_name):
        self.click(self.HEADERS[section_name])

    @log_action
    def wait_for_section_text(self, section_name):
        locator = self.CONTENTS[section_name]
        self.wait.until(
            lambda d: self.get_text(locator).strip() != ""
        )

    @log_action
    def get_section_text(self, section_name):
        return self.get_text(self.CONTENTS[section_name])
