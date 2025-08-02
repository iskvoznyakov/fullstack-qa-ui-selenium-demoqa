from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class DragabblePage(BasePage):
    TABS = {
        "simple_tab": (By.ID, "draggableExample-tab-simple"),
        "axis_restricted_tab": (By.ID, "draggableExample-tab-axisRestriction")
    }

    DRAGGABLE_ELEMENTS = {
        "drag_me_element": (By.ID, "dragBox"),
        "only_x_element": (By.ID, "restrictedX"),
        "only_y_element": (By.ID, "restrictedY"),
    }

    def open(self):
        super().open(BASE_URL + "/dragabble")

    @log_action
    def click_on_tab(self, tab_name):
        self.click(self.TABS[tab_name])

    @log_action
    def drag_element_by_offset(self, element_name, x_offset, y_offset):
        element = self.find(self.DRAGGABLE_ELEMENTS[element_name])
        (ActionChains(self.driver).
         drag_and_drop_by_offset(element, x_offset, y_offset).
         perform())

    @log_action
    def get_element_position(self, element_name):
        element = self.find(self.DRAGGABLE_ELEMENTS[element_name])
        location = element.location
        return location['x'], location['y']
