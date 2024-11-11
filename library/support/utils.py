import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Automation functions

def wait_for_element(driver, element, wait_time=10):
    """Waits for an element to be visible and returns it."""
    return WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located(element),
        f"Element with ID '{element[1]}' is not present!"
    )

def click_element(driver, element, wait_time=10):
    """Finds an element by XPath, waits for it to be present, and clicks it."""
    button = wait_for_element(driver, element, wait_time)
    button.click()
    
def fill_field(driver, element, text, wait_time=3):
    """Finds an element by XPath, waits for it to be present, and fills it with text."""
    input = wait_for_element(driver, element, wait_time)
    input.send_keys(text)
    
def click_temp(driver, element, wait_time=3):
    """Finds a webview element by XPath, waits for some time, and clicks it."""
    button = driver.find_element(*element)
    time.sleep(wait_time)
    button.click()

def fill_temp(driver, element, text, wait_time=3):
    """Finds an element by XPath, waits for some time, and fills it with text."""
    input = driver.find_element(*element)
    time.sleep(wait_time)
    input.send_keys(text)
    

# Gesture functions

def click_on_screen(driver, x, y):
    """Clicks on the given coordinates of the screen."""
    actions = ActionChains(driver)
    actions.move_by_offset(x, y).click().perform()
