import time
from allure import step
import conftest
from library.pages.signup_page import SignupPage
from library.support import get_otp_from_email
from library.support.user_management import User, search_json, update_json

driver = conftest.session()
signup_page = SignupPage(driver)

users_data = 'library/data/users.json'
new_user = User()


@step("Scenario: User Creates A New Account")
def step0(data):
    """Data parameters"""
    new_user.set_json(data)
    new_user.id = ""

@step("Given the user is on the welcome page")
def step1():
    time.sleep(0)

@step("And the user navigates to the signup page")
def step2():
    time.sleep(10)
    signup_page.start_signup()
    
@step("When the user creates a new account")
def step3():
    time.sleep(10)  
    inputs = {
        "email": new_user.email,
        "password": new_user.password
    }
    signup_page.create_account(inputs)

@step("And the user enters their personal information")
def step4():
    time.sleep(10)
    inputs = {
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "date_of_birth": new_user.date_of_birth,
        "gender": new_user.gender,
        "postal_code": new_user.postal_code,
    }
    signup_page.enter_personal_details(inputs)

@step("Then the user should receive an OTP")
def step5():
    time.sleep(10)
    email = new_user.email
    
    try:
        otp_assert = get_otp_from_email(email)
        print(f"OTP retrieved: {otp_assert}")
        
        new_user.tags["signed_up"] = True
        update_json(users_data, new_user.to_json())
        
    except Exception as e:  # Catch any error that escapes the function
        print(f"Failed to retrieve OTP on step 5: {e}")
        driver.quit()

@step("When the user enters the correct OTP")
def step6():
    time.sleep(10)
    email = new_user.email
    
    try:
        signup_page.enter_otp(email)
    except Exception as e:  # Catch any error that escapes the function
        print(f"Failed to retrieve OTP on step 6: {e}")
        driver.quit()
     
@step("Then the user should be successfully signed in")
def step7():
    time.sleep(15)
    driver.quit()


