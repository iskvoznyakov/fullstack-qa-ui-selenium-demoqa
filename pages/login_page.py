from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "userName")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    LOGOUT_BUTTON = (By.ID, "submit")

    def open(self):
        super().open(BASE_URL + "/login")

    @log_action
    def fill_the_login_form(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @log_action
    def is_login_successful(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        return "profile" in self.driver.current_url
