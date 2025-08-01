from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class DragabblePage(BasePage):
    TABS = {
        "simple_tab": (By.ID, "draggableExample-tab-simple"),
    }

    DRAG_ME_ELEMENT = (By.ID, "dragBox")

    def open(self):
        super().open(BASE_URL + "/dragabble")

    @log_action
    def click_on_tab(self, tab_name):
        self.click(self.TABS[tab_name])

    @log_action
    def drag_simple_element_by_offset(self, x_offset, y_offset):
        element = self.find(self.DRAG_ME_ELEMENT)
        (ActionChains(self.driver).
         drag_and_drop_by_offset(element, x_offset, y_offset).
         perform())

    @log_action
    def get_simple_element_position(self):
        element = self.find(self.DRAG_ME_ELEMENT)
        location = element.location
        return location['x'], location['y']
