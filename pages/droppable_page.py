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
        "accept_tab": (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']"),
        "prevent_propogation_tab": {
            "greedy_zone": {
                "GREEDY_OUT_DROP_BOX": (By.ID, "greedyDropBox"),
                "GREEDY_INNER_DROP_BOX": (By.ID, "greedyDropBoxInner")},
            "not_greedy_zone": {
                "NOT_GREEDY_OUT_DROP_BOX": (By.ID, "notGreedyDropBox"),
                "NOT_GREEDY_INNER_DROP_BOX": (By.ID, "notGreedyInnerDropBox")},
        },
        "revert_tab": (By.XPATH, "//div[@id='revertableDropContainer']//div[@id='droppable']")
    }

    DRAGGABLE_ELEMENT_ON_PREVENT_TAB = (
        By.XPATH, "//div[@id='droppableExample-tabpane-preventPropogation']//div[@id='dragBox']")

    DRAGGABLE_ELEMENTS_ON_REVERT_TAB = {
        "revertable": (By.ID, "revertable"),
        "not_revertable": (By.ID, "notRevertable")
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

    @log_action
    def move_element_to_inner_box_on_prevent_tab(self, zone_name):
        draggable_element = self.find(self.DRAGGABLE_ELEMENT_ON_PREVENT_TAB)
        if zone_name == 'greedy_zone':
            inner_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["GREEDY_INNER_DROP_BOX"])
        elif zone_name == 'not_greedy_zone':
            inner_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["NOT_GREEDY_INNER_DROP_BOX"])
        else:
            raise ValueError("Некорректное название зоны элемента")

        (ActionChains(self.driver).
         click_and_hold(draggable_element).
         move_to_element(inner_droppable).
         release().
         perform())

    @log_action
    def is_outer_element_active(self, zone_name):
        if zone_name == 'greedy_zone':
            outer_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["GREEDY_OUT_DROP_BOX"])
        elif zone_name == 'not_greedy_zone':
            outer_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["NOT_GREEDY_OUT_DROP_BOX"])
        else:
            raise ValueError("Некорректное название зоны элемента")
        return "highlight" in outer_droppable.get_attribute("class")

    @log_action
    def is_inner_element_active(self, zone_name):
        if zone_name == 'greedy_zone':
            inner_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["GREEDY_INNER_DROP_BOX"])
        elif zone_name == 'not_greedy_zone':
            inner_droppable = self.find(
                self.DROPPABLE_ELEMENTS_IN_TABS["prevent_propogation_tab"][zone_name]["NOT_GREEDY_INNER_DROP_BOX"])
        else:
            raise ValueError("Некорректное название зоны элемента")
        return "highlight" in inner_droppable.get_attribute("class")

    @log_action
    def _move_revertable_element(self, element_name):
        draggable_element = self.find(self.DRAGGABLE_ELEMENTS_ON_REVERT_TAB[element_name])
        droppable_element = self.find(self.DROPPABLE_ELEMENTS_IN_TABS["revert_tab"])
        (ActionChains(self.driver).
         click_and_hold(draggable_element).
         move_to_element(droppable_element).
         release().
         perform())

    @log_action
    def has_element_moved_back(self, element_name, timeout=2):
        element = self.find(self.DRAGGABLE_ELEMENTS_ON_REVERT_TAB[element_name])
        start_location = element.location

        self._move_revertable_element(element_name)

        try:
            self.wait.until(
                lambda d: self.find(self.DRAGGABLE_ELEMENTS_ON_REVERT_TAB[element_name]).location == start_location)
            return True
        except:
            return False
