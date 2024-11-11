import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def switch_to_webview(driver):
    """Switches the driver context to the specified webview."""
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: len(driver.contexts) > 1)
    driver.switch_to.context(driver.contexts[1])
    time.sleep(2)

def switch_to_native(driver):
    """Switches the driver context back to native mode."""
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: len(driver.contexts) > 1)
    driver.switch_to.context(driver.contexts[0])
    time.sleep(2)

