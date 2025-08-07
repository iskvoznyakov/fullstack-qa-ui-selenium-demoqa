from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    LOGOUT_BUTTON = (By.ID, "submit")
    LOGIN_BUTTON = (By.ID, "login")

    @log_action
    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    @log_action
    def is_logout_successful(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        return "login" in self.driver.current_url
