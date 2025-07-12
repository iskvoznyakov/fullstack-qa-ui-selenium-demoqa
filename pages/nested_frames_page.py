from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class NestedFramesPage(BasePage):
    PARENT_FRAME = (By.ID, "frame1")
    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    BODY_TAG = (By.TAG_NAME, "body")

    def open(self):
        super().open(BASE_URL + "/nestedframes")

    @log_action
    def switch_to_parent_frame(self):
        self.switch_to_default()
        self.driver.switch_to.frame(self.find(self.PARENT_FRAME))

    @log_action
    def switch_to_child_frame(self):
        self.switch_to_parent_frame()
        self.driver.switch_to.frame(self.find(self.CHILD_FRAME))

    @log_action
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    @log_action
    def get_text_from_body(self):
        return self.get_text(self.BODY_TAG)
