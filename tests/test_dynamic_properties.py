from pages.dynamic_properties_page import DynamicPropertiesPage


def test_button_enabled_after_5_sec(driver):
    page = DynamicPropertiesPage(driver)
    page.open()
    assert page.wait_until_button_enabled(), "Кнопка не стала активной"


def test_color_change(driver):
    dynamic_properties_page = DynamicPropertiesPage(driver)
    dynamic_properties_page.open()
    assert dynamic_properties_page.wait_until_color_changes(), "Цвет кнопки не изменился"


def test_button_becomes_visible(driver):
    dynamic_properties_page = DynamicPropertiesPage(driver)
    dynamic_properties_page.open()
    assert dynamic_properties_page.wait_until_visible(), "Кнопка не появилась"


def test_find_random_id_text(driver):
    dynamic_properties_page = DynamicPropertiesPage(driver)
    dynamic_properties_page.open()
    assert dynamic_properties_page.find_random_id_text(), "Текст с рандомным ID не найден"
