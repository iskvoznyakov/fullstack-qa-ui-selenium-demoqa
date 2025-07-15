from pages.date_picker_page import DatePickerPage


def test_enter_valid_date(driver):
    page = DatePickerPage(driver)
    page.open()
    page.enter_date("06/30/2025")
    assert page.get_date_value() == "06/30/2025"


def test_enter_valid_datetime(driver):
    page = DatePickerPage(driver)
    page.open()
    page.enter_datetime("June 30, 2025 10:30 PM")
    assert page.get_datetime_value() == "June 30, 2025 10:30 PM"


def test_choose_date(driver):
    page = DatePickerPage(driver)
    page.open()
    page.choose_custom_date("1996", "February", "4")
    assert page.get_date_value() == "02/04/1996"


def test_choose_date_time(driver):
    page = DatePickerPage(driver)
    page.open()
    page.choose_date_time(year="2020", month="February", day="4", time="17:00")
    assert page.get_datetime_value() == "February 4, 2020 5:00 PM"
