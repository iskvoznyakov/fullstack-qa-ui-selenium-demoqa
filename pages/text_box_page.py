from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    FULL_NAME_FIELD = (By.ID, "userName")
    EMAIL_FIELD = (By.ID, "userEmail")
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_FIELD = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_FIELD = (By.ID, "output")

    def open(self):
        super().open(BASE_URL + "/text-box")

    def fill_the_form(self, full_name, email, current_address, permanent_address):
        self.enter_text(self.FULL_NAME_FIELD, full_name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.CURRENT_ADDRESS_FIELD, current_address)
        self.enter_text(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click(self.SUBMIT_BUTTON)

    def get_output(self):
        if not self.is_visible(self.OUTPUT_FIELD):
            raise AssertionError("Поле вывода не отображается — нельзя получить данные")
        output_text = self.get_text(self.OUTPUT_FIELD)
        return {pair.split(":")[0].strip(): pair.split(":")[1] for pair in output_text.split('\n')}

    def is_visible_output_field(self):
        return self.is_visible(self.OUTPUT_FIELD)
