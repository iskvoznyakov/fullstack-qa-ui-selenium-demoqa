from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class TabsPage(BasePage):
    tab_names = {"what_tab": (By.ID, "demo-tab-what"),
                 "origin_tab": (By.ID, "demo-tab-origin"),
                 "use_tab": (By.ID, "demo-tab-use")}
    tab_contents = {"what_tab": (By.ID, "demo-tabpane-what"),
                    "origin_tab": (By.ID, "demo-tabpane-origin"),
                    "use_tab": (By.ID, "demo-tabpane-use")}

    def open(self):
        super().open(BASE_URL + "/tabs")

    @log_action
    def click_tab(self, tab_name):
        self.click(self.tab_names[tab_name])

    @log_action
    def get_tab_content(self, tab_name):
        return self.get_text(self.tab_contents[tab_name])

    @log_action
    def is_tab_active(self, tab_name):
        tab = self.find(self.tab_names[tab_name])
        return "active" in tab.get_attribute("class")

    @log_action
    def is_tab_content_visible(self, tab_name):
        content = self.find(self.tab_contents[tab_name])
        aria_hidden = content.get_attribute("aria-hidden")
        return aria_hidden == "false" or aria_hidden is None
