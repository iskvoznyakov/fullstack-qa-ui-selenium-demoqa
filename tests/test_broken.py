from pages.broken_page import BrokenPage


def test_click_valid_link(driver):
    broken_links_page = BrokenPage(driver)
    broken_links_page.open()
    broken_links_page.click_link("valid link")
    assert broken_links_page.is_link_was_clicked(
        "valid link"), "Ожидался переход по валидной ссылке, но URL не изменился"


def test_click_broken_link(driver):
    broken_links_page = BrokenPage(driver)
    broken_links_page.open()
    broken_links_page.click_link("broken link")
    assert broken_links_page.is_link_was_clicked("broken link"), "Ожидалась ошибка 500 при переходе по битой ссылке"


def test_valid_image_is_displayed(driver):
    broken_links_page = BrokenPage(driver)
    broken_links_page.open()
    assert broken_links_page.valid_image_is_displayed(), "Валидная картинка не отображается"


def test_broken_image_is_not_displayed(driver):
    broken_links_page = BrokenPage(driver)
    broken_links_page.open()
    assert broken_links_page.broken_image_is_not_displayed(), "Битая картинка отображается, хотя не должна"
