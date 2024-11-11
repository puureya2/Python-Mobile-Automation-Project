
from appium.webdriver.common.appiumby import AppiumBy

from library.support import (
    click_element,
    fill_field,
    switch_to_webview,
    switch_to_native
)


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver


    # Element Locators: Welcome Page
    _welcome_button = (AppiumBy.XPATH, '//app-yuzee-welcome/ion-content/ion-footer/ion-button')
    _login_button = (AppiumBy.XPATH, '//*[@id="main-content"]/app-identity/ion-content/app-guest-control-center/ion-footer/ion-row/ion-button[2]') 
   
    # Element Locators: Login Page
    _email_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _password_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText')
    _login_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Sign in"]')
    
    
    # Page Steps
    
    def login(self, data):
        """Login to the app: Given you are on the welcome screen"""
        
        switch_to_webview(self.driver)
        self.click_welcome_button()
        self.click_login_button()
        
        switch_to_native(self.driver)
        self.fill_email(data["email"])
        self.fill_password(data["password"])
        self.click_login_next_button()


    # Single Actions

    def click_welcome_button(self):
        """webview"""
        click_element(self.driver, self._welcome_button)    

    def click_login_button(self):
        """webview"""
        click_element(self.driver, self._login_button)   
    
    
    def fill_email(self, email):
        switch_to_native(self.driver)
        fill_field(self.driver, self._email_input, email)

    def fill_password(self, password):
        fill_field(self.driver, self._password_input, password)

    def click_login_next_button(self):
        click_element(self.driver, self._login_next_button)
