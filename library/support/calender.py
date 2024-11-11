from appium.webdriver.common.appiumby import AppiumBy

import time
from datetime import date
todays_date = date.today()


def fake_swipe_month(driver, my_month):
    """Simulates swiping the calender scroll wheel to the given month."""

    month_button = '//android.widget.Button[@text="{month}"]'

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = months.index(my_month) + 1
    current_month = todays_date.month

    if month < current_month:
        number_of_clicks = current_month - month

        while number_of_clicks > 0:
            set_month = months[current_month]

            button = month_button.format(month=set_month)
            temp_month = driver.find_element(AppiumBy.XPATH, button)
            temp_month.click()

            current_month = current_month - 1
            number_of_clicks = number_of_clicks - 1

    elif month > current_month:
        number_of_clicks = month - current_month

        while number_of_clicks > 0:
            set_month = months[current_month]

            button = month_button.format(month=set_month)
            temp_month = driver.find_element(AppiumBy.XPATH, button)
            temp_month.click()

            current_month = current_month - 1
            number_of_clicks = number_of_clicks - 1

    else:
        set_month = months[current_month]

        button = month_button.format(month=set_month)
        temp_month = driver.find_element(AppiumBy.XPATH, button)
        temp_month.click()
        
    time.sleep(2)


def fake_swipe_day(driver, my_day):
    """Simulates swiping the calender scroll wheel to the given day."""

    day_button = '//android.widget.Button[@text="{day}"]'

    current_day = todays_date.day
    day = int(my_day)

    if day < current_day:
        number_of_clicks = current_day - day

        while number_of_clicks > 0:
            button = day_button.format(day=current_day)
            temp_day = driver.find_element(AppiumBy.XPATH, button)

            temp_day.click()

            current_day = current_day - 1
            number_of_clicks = number_of_clicks - 1

    elif day > current_day:
        number_of_clicks = day - current_day

        while number_of_clicks > 0:
            button = day_button.format(day=current_day)
            temp_day = driver.find_element(AppiumBy.XPATH, button)
            temp_day.click()

            current_day = current_day - 1
            number_of_clicks = number_of_clicks - 1

    else:
        button = day_button.format(day=current_day)
        temp_day = driver.find_element(AppiumBy.XPATH, button)
        temp_day.click()
        
    time.sleep(2)


def fake_swipe_year(driver, my_year):
    """Simulates swiping the calender scroll wheel to the given year.""" 
 
    year_button = '//android.widget.Button[@text="{year}"]'

    current_year = todays_date.year
    print(current_year)
    my_year = int(my_year)
    
    number_of_clicks = current_year - my_year

    while number_of_clicks > 0:
        current_year = current_year - 1
        number_of_clicks = number_of_clicks - 1
        
        time.sleep(1)

        button = year_button.format(year=str(current_year))
        print(button)
        temp_year = driver.find_element(AppiumBy.XPATH, button)
        temp_year.click()
        
    time.sleep(2)
    