from pages.droppable_page import DroppablePage


def test_move_element_on_simple_tab(driver):
    droppable_page = DroppablePage(driver)
    droppable_page.open()
    droppable_page.click_on_tab("simple_tab")
    droppable_page.move_element_on_simple_tab()
    assert droppable_page.is_droppable_element_active("simple_tab"), "Элемент не активен"


def test_move_valid_element_on_accept_tab(driver):
    droppable_page = DroppablePage(driver)
    droppable_page.open()
    droppable_page.click_on_tab("accept_tab")
    droppable_page.move_element_on_accept_tab("acceptable")
    assert droppable_page.is_droppable_element_active("accept_tab"), "Элемент не активен"


def test_move_invalid_element_on_accept_tab(driver):
    droppable_page = DroppablePage(driver)
    droppable_page.open()
    droppable_page.click_on_tab("accept_tab")
    droppable_page.move_element_on_accept_tab("not_acceptable")
    assert not droppable_page.is_droppable_element_active("accept_tab"), "Элемент активен, хотя не должен"


def test_move_element_to_greedy_zone_on_prevent_propogation_tab(driver):
    droppable_page = DroppablePage(driver)
    droppable_page.open()
    droppable_page.click_on_tab("prevent_propogation_tab")
    droppable_page.move_element_to_inner_box_on_prevent_tab("greedy_zone")
    assert droppable_page.is_inner_element_active("greedy_zone"), "Внутренний элемент не активен"
    assert not droppable_page.is_outer_element_active("greedy_zone"), "Внешний элемент активен"


def test_move_element_to_not_greedy_zone_on_prevent_propogation_tab(driver):
    droppable_page = DroppablePage(driver)
    droppable_page.open()
    droppable_page.click_on_tab("prevent_propogation_tab")
    droppable_page.move_element_to_inner_box_on_prevent_tab("not_greedy_zone")
    assert droppable_page.is_inner_element_active("not_greedy_zone"), "Внутренний элемент не активен"
    assert droppable_page.is_outer_element_active("not_greedy_zone"), "Внешний элемент активен"
