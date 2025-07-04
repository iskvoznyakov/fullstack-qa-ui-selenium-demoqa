import pytest
from pages.links_page import LinksPage


@pytest.mark.parametrize("link_name, expected_code", [
    ("created", 201),
    ("no content", 204),
    ("moved", 301),
    ("bad request", 400),
    ("unauthorized", 401),
    ("forbidden", 403),
    ("not found", 404)
])
def test_click_api_link(driver, link_name, expected_code):
    links_page = LinksPage(driver)
    links_page.open()
    links_page.click_link(link_name)
    assert links_page.link_response_code_is(expected_code), f"Ссылка {link_name} не была нажата"


@pytest.mark.parametrize("link_name", [
    "simple",
    "dynamic"
])
def test_click_new_tab_link(driver, link_name):
    links_page = LinksPage(driver)
    links_page.open()
    links_page.click_link(link_name)
    assert links_page.new_tab_is_opened(), f"Новая вкладка не открылась"
