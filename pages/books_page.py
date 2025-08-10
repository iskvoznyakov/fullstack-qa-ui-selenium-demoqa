from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class BooksPage(BasePage):
    SEARCH_FIELD = (By.ID, "searchBox")
    FIND_BUTTON = (By.ID, "basic-addon2")
    BOOK_TITLES = (By.CLASS_NAME, "action-buttons")
    ROWS_DROPDOWN = (By.XPATH, "//select[@aria-label='rows per page']")

    def open(self):
        super().open(BASE_URL + "/books")

    @log_action
    def find_book_by_name(self, book_name):
        self.enter_text(self.SEARCH_FIELD, book_name)

    @log_action
    def find_result(self):
        books_found = self.driver.find_elements(*self.BOOK_TITLES)
        return [book.text for book in books_found]

    def choose_books_per_page(self, number_of_books):
        elem = self.find(self.ROWS_DROPDOWN)
        select = Select(elem)
        select.select_by_value(str(number_of_books))
