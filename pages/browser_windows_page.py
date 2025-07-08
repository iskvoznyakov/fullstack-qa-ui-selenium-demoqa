from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")

    def open(self):
        super().open(BASE_URL + "/browser-windows")

    @log_action
    def click_new_tab_button(self):
        self.click(self.NEW_TAB_BUTTON)

    @log_action
    def click_new_window_button(self):
        self.click(self.NEW_WINDOW_BUTTON)

    @log_action
    def new_item_is_opened(self):
        self.switch_to_new_window()
        return self.driver.current_url.startswith("https://demoqa.com/sample") and self.get_text(
            (By.ID, "sampleHeading")).strip() == "This is a sample page"
