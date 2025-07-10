import pytest
from pages.modal_dialogs_page import ModalDialogsPage


@pytest.mark.parametrize("modal_size", [
    "small",
    "large"
])
def test_modal_dialog_opens_on_click(driver, modal_size):
    modal_dialogs_page = ModalDialogsPage(driver)
    modal_dialogs_page.open()
    modal_dialogs_page.click_modal_button(modal_size)
    assert modal_dialogs_page.is_modal_opened(modal_size), f"Модальное окно с размером {modal_size} не отображается"


@pytest.mark.parametrize("modal_size", [
    "small",
    "large"
])
def test_modal_closes_on_button_click(driver, modal_size):
    modal_dialogs_page = ModalDialogsPage(driver)
    modal_dialogs_page.open()
    modal_dialogs_page.click_modal_button(modal_size)
    assert modal_dialogs_page.is_modal_opened(modal_size), "Модальное окно не отображается"
    assert modal_dialogs_page.close_modal("button", modal_size), "Модальное окно не закрылось по кнопке Close"


@pytest.mark.parametrize("modal_size", [
    "small",
    "large"
])
def test_modal_closes_on_x_click(driver, modal_size):
    modal_dialogs_page = ModalDialogsPage(driver)
    modal_dialogs_page.open()
    modal_dialogs_page.click_modal_button(modal_size)
    assert modal_dialogs_page.is_modal_opened(modal_size), "Модальное окно не отображается"
    assert modal_dialogs_page.close_modal("x", modal_size), "Модальное окно не закрылось по крестику"
