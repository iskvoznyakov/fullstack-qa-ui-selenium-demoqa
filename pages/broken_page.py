from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class BrokenPage(BasePage):
    VALID_IMAGE = (By.XPATH, "(//p[text()='Valid image']/following-sibling::img)[1]")
    BROKEN_IMAGE = (By.XPATH, "(//p[text()='Broken image']/following-sibling::img)[1]")
    VALID_LINK = (By.XPATH, "//a[contains(text(), 'Valid Link')]")
    BROKEN_LINK = (By.XPATH, "//a[contains(text(), 'Broken Link')]")

    def open(self):
        super().open(BASE_URL + "/broken")

    @log_action
    def click_link(self, link_name: str):
        mapping = {
            "valid link": self.VALID_LINK,
            "broken link": self.BROKEN_LINK
        }
        self.click(mapping[link_name])

    @log_action
    def is_link_was_clicked(self, link_name: str):
        if link_name == "valid link":
            return self.driver.current_url.startswith("https://demoqa.com/")
        elif link_name == "broken link":
            return self.driver.current_url.startswith("https://the-internet.herokuapp.com/status_codes/500")

    @log_action
    def valid_image_is_displayed(self):
        return self.find(self.VALID_IMAGE).is_displayed()

    @log_action
    def broken_image_is_not_displayed(self):
        img = self.find(self.BROKEN_IMAGE)
        return self.driver.execute_script("return arguments[0].naturalWidth === 0", img)
