from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class ModalDialogsPage(BasePage):
    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    SMALL_MODAL_CLOSE_BUTTON = (By.ID, "closeSmallModal")
    LARGE_MODAL_BUTTON = (By.ID, "showLargeModal")
    LARGE_MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")
    MODAL_HEADER = (By.XPATH, "//div[@class='modal-title h4']")
    MODAL_BODY = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@class='close']")

    def open(self):
        super().open(BASE_URL + "/modal-dialogs")

    @log_action
    def click_modal_button(self, modal):
        self.click(self.SMALL_MODAL_BUTTON) if modal == "small" else self.click(self.LARGE_MODAL_BUTTON)

    @log_action
    def get_modal_header_text(self):
        return self.get_text(self.MODAL_HEADER)

    @log_action
    def is_modal_opened(self, modal):
        header_text = self.get_modal_header_text()
        body_text = self.get_text(self.MODAL_BODY)
        expected_text = "Small Modal" if modal == "small" else "Large Modal"
        return header_text == expected_text and body_text

    @log_action
    def close_modal(self, method, modal):
        if method == "button":
            locator = self.SMALL_MODAL_CLOSE_BUTTON if modal == "small" else self.LARGE_MODAL_CLOSE_BUTTON
        elif method == "x":
            locator = self.CLOSE_MODAL_BUTTON
        self.click(locator)
        return self.is_not_visible(self.MODAL_HEADER)
