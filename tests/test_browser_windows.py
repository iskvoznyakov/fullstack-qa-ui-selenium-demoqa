from pages.browser_windows_page import BrowserWindowsPage


def test_open_new_tab(driver):
    browser_windows_page = BrowserWindowsPage(driver)
    browser_windows_page.open()
    browser_windows_page.click_new_tab_button()
    assert browser_windows_page.new_item_is_opened(), "Новая вкладка не открылась"


def test_open_new_window(driver):
    browser_windows_page = BrowserWindowsPage(driver)
    browser_windows_page.open()
    browser_windows_page.click_new_window_button()
    assert browser_windows_page.new_item_is_opened(), "Новое окно браузера не открылось"
