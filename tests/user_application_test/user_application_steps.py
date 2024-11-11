import time
from allure import step
import conftest
from library.pages.login_page import LoginPage
from library.pages.rmo_application_page import RMOApplicationPage
from library.support.user_management import User, update_json

driver = conftest.session()
login_page = LoginPage(driver)
rmo_page = RMOApplicationPage(driver)

users_data = 'library/data/users.json'
existing_user = User()


@step("Scenario: User Submits An RMO Application")
def step0(data):
    """Data parameters"""
    existing_user.set_json(data)

@step("Given the user is logged in & fully onboarded")
def step1():
    time.sleep(10)
    inputs = {
        "email": existing_user.email,
        "password": existing_user.password
    } 
    login_page.login(inputs)

@step("And the user starts an RMO application")
def step2():
    time.sleep(10)
    rmo_page.start_rmo()
    
@step("When the user selects the first 3 courses")
def step3():
    time.sleep(10)
    courses = [
        "Aboriginal Health And Wellbeing", 
        "Advanced Diploma Of Building Biology", 
        "Advanced Diploma Of Building Design (Architectural)"
    ] 
    rmo_page.select_categories(courses)

@step("And the user sets 'Kuala Lumpur' as their location")
def step4():
    time.sleep(10)
    location = {
        "search": "Kuala",
        "choice": "Kuala Lumpur"
    }
    rmo_page.select_location(location)

@step("And the user selects 'Full-time' as their study mode")
def step5():
    time.sleep(10)
    study_mode = {
        "choice": "Full-time", 
    }
    rmo_page.select_study_mode(study_mode)

    
@step("And the user selects 'Classroom' as their delivery type")
def step6():
    time.sleep(10)
    delivery_type = {
        "choice": "Classroom", 
    }
    rmo_page.select_delivery_type(delivery_type)
    
@step("And the user selects 'December 2024' as their intake date")
def step7():
    time.sleep(10)
    intake = {
        "choice": "December, 2024", 
    }
    rmo_page.select_intake(intake)

@step("And the user adds a reason for applying")
def step8():
    time.sleep(10)
    reason = {
        "text": "Random text to fill a minimum of 30 words. Yours truly, Kevin.", 
    }
    rmo_page.enter_reason(reason)
    
@step("And the user selects 'Weekday mornings' for their lesson times")
def step9():
    time.sleep(10)
    
    days = {
        "choice": "Weekdays"
    }
    time = {
        "choice": "Morning"
    }
    rmo_page.select_lesson_days(days)
    rmo_page.select_lesson_time(time)
    
@step("When the user submits their application")
def step10():
    time.sleep(10)
    rmo_page.click_finish_next_button()
    
@step("Then the user should receive an application url")
def step11():
    time.sleep(10)
    
    try:
        url = rmo_page.get_url_label_text
        print(f"URL retrieved: {url}")
        
        existing_user.tags["onboarded"] = True
        update_json(users_data, existing_user.to_json())
        
    except Exception as e:  # Catch any error that escapes the function
        print(f"Failed to retrieve URL on step 11: {e}")
        driver.quit()
        
    
    driver.quit()



