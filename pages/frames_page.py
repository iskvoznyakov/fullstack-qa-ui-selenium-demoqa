from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class FramesPage(BasePage):
    FRAME_1 = (By.ID, "frame1")
    FRAME_2 = (By.ID, "frame2")
    FRAME_HEADER = (By.ID, "sampleHeading")

    def open(self):
        super().open(BASE_URL + "/frames")

    @log_action
    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)

    @log_action
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    @log_action
    def get_text_from_frame(self, frame_name):
        self.switch_to_default()
        locator = self.FRAME_1 if frame_name == 'frame_1' else self.FRAME_2
        elem = self.find(locator)
        self.switch_to_frame(elem)
        return self.get_text(self.FRAME_HEADER)
