from pages.buttons_page import ButtonsPage


def test_double_click_button(driver):
    buttons_page = ButtonsPage(driver)
    buttons_page.open()
    buttons_page.click_double_click_button()
    assert buttons_page.click_result_is_visible("double"), "Кнопка с двойным кликом не была нажата"


def test_right_click_button(driver):
    buttons_page = ButtonsPage(driver)
    buttons_page.open()
    buttons_page.click_right_click_button()
    assert buttons_page.click_result_is_visible("right"), "Кнопка с правым кликом не была нажата"


def test_click_button_with_dynamic_id(driver):
    buttons_page = ButtonsPage(driver)
    buttons_page.open()
    buttons_page.click_button_with_dynamic_id()
    assert buttons_page.click_result_is_visible("dynamic"), "Кнопка с динамическим ID не была нажата"
