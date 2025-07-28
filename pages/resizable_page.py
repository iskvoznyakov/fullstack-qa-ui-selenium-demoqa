from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class ResizablePage(BasePage):
    boxes = {
        "box_with_restriction": (By.ID, "resizableBoxWithRestriction"),
        "box_without_restriction": (By.ID, "resizable")}
    corners = {
        "box_with_restriction": (
            By.XPATH, "//div[@id='resizableBoxWithRestriction']//span[contains(@class, 'react-resizable-handle')]"),
        "box_without_restriction": (
            By.XPATH, "//div[@id='resizable']//span[contains(@class, 'react-resizable-handle')]"),
    }


    def open(self):
        super().open(BASE_URL + "/resizable")

    @log_action
    def resize_box_by_offset(self, type_of_box, x_offset, y_offset):
        corner = self.find(self.corners[type_of_box])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", corner)
        (ActionChains(self.driver).
         click_and_hold(corner).
         move_by_offset(x_offset, y_offset).
         release().
         perform())

    @log_action
    def get_box_size(self, type_of_box):
        size = self.find(self.boxes[type_of_box]).size
        height, width = size["height"], size["width"]
        return height, width
