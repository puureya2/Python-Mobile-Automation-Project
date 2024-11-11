from appium import webdriver
from appium.options.common import AppiumOptions


# Capabilities
CONFIG = {
    
    "appium_server_url": "http://localhost:4723",
    
    "capabilities": {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\User\\Desktop\\niaP\\Kevin\\5\\SEEKA Stuff\\apk\\Yuzee25July.apk",
        "appium:deviceName": "Pixel_4_KEV_API_35",
        "appium:avd": "Pixel_4_KEV_API_35",
        "appium:platformVersion": "15.0"
    },
    
    "MAILOSAUR_API_KEY": "5wQzG7Qib98XSpO8hK9ly1yunN49k6AH",
    "BACKUP_MAILOSAUR_API_KEY": "qHNFO8LbNL9ZUxAnfR3bm99HQff4rTIf",

}


def session():
    """Pytest fixture to create and return the Appium driver."""
    capabilities = CONFIG["capabilities"]
    appium_server_url = CONFIG["appium_server_url"]
    driver = webdriver.Remote(
        appium_server_url,
        options=AppiumOptions().load_capabilities(capabilities)
    )
    
    return driver







