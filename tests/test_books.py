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


@pytest.mark.parametrize("number_of_books", [
    5
])
def test_page_books(driver, number_of_books):
    books_page = BooksPage(driver)
    books_page.open()
    books_page.choose_books_per_page(number_of_books)
    books_found = books_page.find_result()
    assert len(
        books_found) == number_of_books, f"На странице отображается не {number_of_books} книг, а {len(books_found)}"
