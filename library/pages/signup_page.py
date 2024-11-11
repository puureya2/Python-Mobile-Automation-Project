
from appium.webdriver.common.appiumby import AppiumBy

from library.support import (
    click_element,
    fake_swipe_day,
    fake_swipe_month,
    fake_swipe_year,
    fill_field,
    get_otp_from_email,
    switch_to_webview,
    switch_to_native
)


class SignupPage:
    
    def __init__(self, driver):
        self.driver = driver


    # Element Locators: Welcome Page
    _welcome_button = (AppiumBy.XPATH, '//app-yuzee-welcome/ion-content/ion-footer/ion-button')
    _signup_button = (AppiumBy.XPATH, '//*[@id="main-content"]/app-identity/ion-content/app-guest-control-center/ion-footer/ion-row/ion-button[1]') 
   
    # Element Locators: Login Page
    _email_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _password_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText')
    _signup_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Next"]')
    
    # Element Locators: Login Details
    _first_name_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _last_name_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _date_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')
    _date_month_input = (AppiumBy.XPATH, '//android.widget.Button[@text="August"]')
    _date_day_input = (AppiumBy.XPATH, '//android.widget.Button[@text="1"]')
    _date_year_input = (AppiumBy.XPATH, '//android.widget.Button[@text="2006"]')
    _date_done_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')
    _gender_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')
    _gender_male_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Male"]')
    _gender_female_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Female"]')
    _postal_code_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _signup_finish_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Sign Up"]')
    
    # Element Locators: OTP Page
    _otp1_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText')
    _otp2_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
    _otp3_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.widget.EditText')
    _otp4_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText')
    _otp5_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText')
    _otp6_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.widget.EditText')
    _otp_confirm_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Confirm"]')

    
    # Page Steps
    
    def signup(self, data):
        """Full sign up: Given you are on the welcome screen"""
        self.start_signup()
        self.create_account(data["email and password"])
        self.enter_personal_details(data["personal details"])
        self.enter_otp(data["otp"])
        
    def start_signup(self):
        """Start sign up: Given you are on the welcome screen"""
        switch_to_webview(self.driver)
        self.click_welcome_button()
        self.click_signup_button()
        switch_to_native(self.driver)
        
    def create_account(self, data):
        """Add an email, password: Given you started the signup"""  
        self.fill_email(data["email"])
        self.fill_password(data["password"])
        self.click_signup_next_button()
        
    def enter_personal_details(self, data):
        """Add full personal details: Given you completed signup part 1"""
        self.fill_first_name(data["first_name"])
        self.fill_last_name(data["last_name"])
        self.enter_date(data["date_of_birth"])
        self.enter_gender(data["gender"])
        self.fill_postal_code(data["postal_code"])
        self.click_signup_finish_button()
        
    def enter_date(self, date_of_birth):
        """Add date of birth: Given you completed signup part 1"""
        self.click_date_button()
        fake_swipe_month(self.driver, date_of_birth["month"])
        fake_swipe_day(self.driver, date_of_birth["day"])
        fake_swipe_year(self.driver, date_of_birth["year"])
        self.click_date_done_button()
        
    def enter_gender(self, gender):
        """Add a gender: Given you completed signup part 1"""
        self.click_gender_button()
        self.click_choice_gender_button(gender["button"])
        
    def enter_otp(self, email):
        """Enter an otp: Given you completed signup part 2"""
        otp = get_otp_from_email(email)
        self.fill_otp_input(otp)
        self.click_otp_confirm_button()


    # Single Actions

    def click_welcome_button(self):
        """webview"""
        click_element(self.driver, self._welcome_button)    
    
    def click_signup_button(self):
        """webview"""
        click_element(self.driver, self._signup_button)   
    
    
    def fill_email(self, email):
        switch_to_native(self.driver)
        fill_field(self.driver, self._email_input, email)

    def fill_password(self, password):
        fill_field(self.driver, self._password_input, password)
        
    def click_signup_next_button(self):
        click_element(self.driver, self._signup_next_button)
    
    
    def fill_first_name(self, first_name):
        fill_field(self.driver, self._first_name_input, first_name)
        
    def fill_last_name(self, last_name):
        fill_field(self.driver, self._last_name_input, last_name)

        
    def click_date_button(self):
        click_element(self.driver, self._date_button)
    
    def swipe_to_month(self, month):
        fake_swipe_month(self.driver, month)
        
    def swipe_to_day(self, day):
        fake_swipe_day(self.driver, day)
        
    def swipe_to_year(self, year):
        fake_swipe_year(self.driver, year)
        
    def click_date_done_button(self):
        click_element(self.driver, self._date_done_button)
        
        
    def click_gender_button(self):
        click_element(self.driver, self._gender_button)
        
    def click_choice_gender_button(self, choice):
        click_element(self.driver, choice)
    
        
    def fill_postal_code(self, postal_code):
        fill_field(self.driver, self._postal_code_input, postal_code)
        
    def click_signup_finish_button(self):
        click_element(self.driver, self._signup_finish_button)


    def fill_otp_input(self, otp):
        fill_field(self.driver, self._otp1_input, otp[0])
        fill_field(self.driver, self._otp2_input, otp[1])
        fill_field(self.driver, self._otp3_input, otp[2])
        fill_field(self.driver, self._otp4_input, otp[3])
        fill_field(self.driver, self._otp5_input, otp[4])
        fill_field(self.driver, self._otp6_input, otp[5])
        
    def click_otp_confirm_button(self):
        click_element(self.driver, self._otp_confirm_button)
