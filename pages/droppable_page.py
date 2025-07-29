from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
from selenium.webdriver import ActionChains


class DroppablePage(BasePage):
    TABS = {
        "simple_tab": (By.ID, "droppableExample-tab-simple"),
        "accept_tab": (By.ID, "droppableExample-tab-accept"),
        "prevent_propogation_tab": (By.ID, "droppableExample-tab-preventPropogation"),
        "revert_draggable_tab": (By.ID, "droppableExample-tab-revertable")
    }

    DRAGGABLE_ELEMENT = (By.ID, "draggable")

    ACCEPTABLE_ELEMENT = (By.ID, "acceptable")
    NOT_ACCEPTABLE_ELEMENT = (By.ID, "notAcceptable")

    DROPPABLE_ELEMENTS_IN_TABS = {
        "simple_tab": (By.XPATH, "//div[@id='simpleDropContainer']//div[@id='droppable']"),
        "accept_tab": (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")
    }

    def open(self):
        super().open(BASE_URL + "/droppable")

    @log_action
    def click_on_tab(self, tab_name):
        self.click(self.TABS[tab_name])

    @log_action
    def move_element_on_simple_tab(self):
        draggable_element = self.find(self.DRAGGABLE_ELEMENT)
        droppable_element = self.find(self.DROPPABLE_ELEMENTS_IN_TABS["simple_tab"])
        (ActionChains(self.driver).
         click_and_hold(draggable_element).
         move_to_element(droppable_element).
         release().
         perform())

    @log_action
    def move_element_on_accept_tab(self, element_name):
        if element_name == 'acceptable':
            draggable_element = self.find(self.ACCEPTABLE_ELEMENT)
        elif element_name == 'not_acceptable':
            draggable_element = self.find(self.NOT_ACCEPTABLE_ELEMENT)
        else:
            raise ValueError("Некорректное имя перетаскиваемого элемента")
        droppable_element = self.find(self.DROPPABLE_ELEMENTS_IN_TABS["accept_tab"])
        (ActionChains(self.driver).
         click_and_hold(draggable_element).
         move_to_element(droppable_element).
         release().
         perform())

    @log_action
    def is_droppable_element_active(self, tab_name):
        droppable_element = self.find(self.DROPPABLE_ELEMENTS_IN_TABS[tab_name])
        return "highlight" in droppable_element.get_attribute("class")
