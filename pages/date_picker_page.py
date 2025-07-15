from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action


class DatePickerPage(BasePage):
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    YEAR_SELECT = (By.XPATH, "//select/option[contains(text(), '1996')]")
    MONTH_SELECT = (By.XPATH, "//select/option[contains(text(), 'January')]")
    DAY_SELECT = (By.XPATH, "//div[contains(@class, 'react-datepicker__day')][contains(@class, '4')]")

    DATE_AND_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    MONTH_ARROW = (By.XPATH, "//span[@class='react-datepicker__month-read-view--down-arrow']")

    def open(self):
        super().open(BASE_URL + "/date-picker")

    @log_action
    def enter_date(self, date_str):
        el = self.find(self.DATE_INPUT)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.BACKSPACE)
        el.send_keys(date_str)

    @log_action
    def get_date_value(self):
        return self.find(self.DATE_INPUT).get_attribute("value")

    @log_action
    def enter_datetime(self, datetime_str):
        el = self.find(self.DATE_AND_TIME_INPUT)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.BACKSPACE)
        el.send_keys(datetime_str)

    @log_action
    def get_datetime_value(self):
        return self.find(self.DATE_AND_TIME_INPUT).get_attribute("value")

    @log_action
    def choose_custom_date(self, year, month, day):
        self.click(self.DATE_INPUT)

        year_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        Select(year_select).select_by_visible_text(year)

        month_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        Select(month_select).select_by_visible_text(month)

        formatted_day = f"{int(day):03d}"

        day_locator = (
            By.CSS_SELECTOR,
            f".react-datepicker__day--{formatted_day}:not(.react-datepicker__day--outside-month)"
        )
        self.click(day_locator)

    @log_action
    def choose_date_time(self, year: str, month: str, day: str, time: str):
        self.click(self.DATE_AND_TIME_INPUT)

        self.click((By.CLASS_NAME, "react-datepicker__month-read-view"))
        self.click((By.XPATH, f"//div[@class='react-datepicker__month-dropdown']//div[text()='{month}']"))

        self.click((By.CLASS_NAME, "react-datepicker__year-read-view"))
        self.click((By.XPATH, f"//div[@class='react-datepicker__year-dropdown']//div[text()='{year}']"))

        formatted_day = f"{int(day):03d}"
        self.click((
            By.CSS_SELECTOR,
            f".react-datepicker__day--{formatted_day}:not(.react-datepicker__day--outside-month)"
        ))

        self.click((By.XPATH, f"//li[contains(@class, 'react-datepicker__time-list-item') and text()='{time}']"))

    # TODO Добавить возможность выбирать любой год
    #  (на данный момент есть возможность работать только с годами, которые видны в выпадающем списке)
    # def select_year(self, target_year: str, max_attempts=25):
    #    self.click((By.CLASS_NAME, "react-datepicker__year-read-view"))
    #    attempts = 0
    #    while attempts < max_attempts:
    #        try:
    #            self.click((By.XPATH, f"//div[@class='react-datepicker__year-option' and text()='{target_year}']"))
    #            break
    #        except:
    #            self.click((By.CLASS_NAME, "react-datepicker__navigation--years-previous"))
    #            time.sleep(0.5)
    #            attempts += 1
    #    else:
    #        raise Exception(f"Year {target_year} not found after {max_attempts} attempts")
