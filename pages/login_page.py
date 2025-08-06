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
    INVALID_FIELD_ERROR = (By.ID, "name")

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

    @log_action
    def is_required_error_displayed(self, username, password):
        if username == "":
            elem = self.find(self.USERNAME_FIELD)
        elif password == "":
            elem = self.find(self.PASSWORD_FIELD)
        else:
            raise ValueError("Некорректное название поля")
        return "is-invalid" in elem.get_attribute("class")

    @log_action
    def is_invalid_error_displayed(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.INVALID_FIELD_ERROR))
        return "Invalid username or password!" in elem.text
