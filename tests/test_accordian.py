import pytest
from pages.accordian_page import AccordianPage


@pytest.mark.parametrize("section_name, expected_text_excerpt", [
    ("section_1", "Lorem Ipsum is simply dummy text"),
    ("section_2", "It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old"),
    ("section_3", "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters")
])
def test_switch_to_frame(driver, section_name, expected_text_excerpt):
    accordian_page = AccordianPage(driver)
    accordian_page.open()
    accordian_page.click_section(section_name)
    accordian_page.wait_for_section_text(section_name)
    text = accordian_page.get_section_text(section_name)
    assert expected_text_excerpt in text, f"Неверный текст в {section_name}: {text}"
