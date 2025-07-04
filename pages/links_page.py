from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class LinksPage(BasePage):
    SIMPLE_LINK = (By.ID, "simpleLink")
    DYNAMIC_LINK = (By.ID, "dynamicLink")
    CREATED_LINK = (By.ID, "created")
    NO_CONTENT_LINK = (By.ID, "no-content")
    MOVED_LINK = (By.ID, "moved")
    BAD_REQUEST_LINK = (By.ID, "bad-request")
    UNAUTHORIZED_LINK = (By.ID, "unauthorized")
    FORBIDDEN_LINK = (By.ID, "forbidden")
    NOT_FOUND_LINK = (By.ID, "invalid-url")
    LINK_RESPONSE_FIELD = (By.ID, "linkResponse")

    def open(self):
        super().open(BASE_URL + "/links")

    @log_action
    def click_link(self, link_name: str):
        mapping = {
            "simple": self.SIMPLE_LINK,
            "dynamic": self.DYNAMIC_LINK,
            "created": self.CREATED_LINK,
            "no content": self.NO_CONTENT_LINK,
            "moved": self.MOVED_LINK,
            "bad request": self.BAD_REQUEST_LINK,
            "unauthorized": self.UNAUTHORIZED_LINK,
            "forbidden": self.FORBIDDEN_LINK,
            "not found": self.NOT_FOUND_LINK,
        }
        self.click(mapping[link_name])

    @log_action
    def link_response_code_is(self, expected_code: int) -> bool:
        response_text = self.get_text(self.LINK_RESPONSE_FIELD)
        return str(expected_code) in response_text

    @log_action
    def new_tab_is_opened(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        return self.driver.current_url.startswith("https://demoqa.com/")
