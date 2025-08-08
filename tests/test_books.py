import pytest

from pages.books_page import BooksPage


@pytest.mark.parametrize("string_for_searching, result", [
    ("Git", ["Git Pocket Guide"]),
    ("JavaScript", ["Learning JavaScript Design Patterns", "Speaking JavaScript", "Programming JavaScript Applications",
                    "Eloquent JavaScript, Second Edition"])
])
def test_find_books(driver, string_for_searching, result):
    books_page = BooksPage(driver)
    books_page.open()
    books_page.find_book_by_name(string_for_searching)
    books_found = books_page.find_result()
    assert set(books_found) == set(result), f"Найденные книги: {books_found}, не совпадают с ОР: {result}"
