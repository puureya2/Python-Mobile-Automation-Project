
import time
from appium.webdriver.common.appiumby import AppiumBy

from library.support import (
    click_element,
    fill_field,
    switch_to_webview,
    switch_to_native
)


class RMOApplicationPage:
    
    def __init__(self, driver):
        self.driver = driver


    # Element Locators: Education pop-up
    _education_button = (AppiumBy.XPATH, '//android.view.View[@text="1 / 2"]/android.view.View[2]')
    _undergraduate_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Undergraduate Lorem ipsum Lorem Ipsum Lorem Ipsum"]') 
    _this_user_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View')
    _education_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Next"]')

    # Element Locators: Category Select Pop-up
    _category_search_button = (AppiumBy.XPATH, '//android.widget.EditText')
    _course_A_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Aboriginal Health And Wellbeing"]') 
    _course_B_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Advanced Diploma Of Building Biology"]') 
    _course_C_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Advanced Diploma Of Building Design (Architectural)"]') 
    _course_choices_buttons = {
        """One or more selectable"""
            "Aboriginal Health And Wellbeing" : _course_A_button,
            "Advanced Diploma Of Building Biology" : _course_B_button,
            "Advanced Diploma Of Building Design (Architectural)" : _course_C_button
    }
    _category_done_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Done"]') 
    _category_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Let\'s add a Location"]')

        
    # Element Locators: Location Pop-up
    _location_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]')
    _location_search_input = (AppiumBy.XPATH, '//android.widget.EditText')
    _location_KL_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia"]')
    _location_choices_buttons = {
        """Provided you searched the appropriate text"""
            "Kuala Lumpur" : _location_KL_button
    }
    _location_done_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Done"]') 
    _location_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Let\'s add preferences"]')

    # Element Locators: Study Mode Pop-up
    _study_mode_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    _full_time_button = (AppiumBy.XPATH, '(//android.widget.CheckBox[@text="Full-time"])[1]/android.widget.Image') 
    _study_mode_choices_buttons = {
        """One selectable"""
            "Full-time" : _full_time_button,
    }
    _study_apply_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Apply"]') 
    
    # Element Locators: Delivery Type Pop-up
    _delivery_type_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    _delivery_classroom_button = (AppiumBy.XPATH, '//android.widget.ListView/android.view.View[2]/android.view.View/android.view.View/android.view.View') 
    _delivery_type_choices_buttons = {
        """One selectable"""
            "Classroom" : _delivery_classroom_button,
    }
    _delivery_apply_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Apply"]') 
    
    # Element Locators: Intake Pop-up
    _intake_button = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    _intake_december_2024_button = (AppiumBy.XPATH, '(//android.widget.CheckBox[@text="December, 2024"])[1]/android.widget.Image') 
    _intake_choices_buttons = {
        """One selectable"""
            "December, 2024" : _intake_december_2024_button,
    }
    _intake_apply_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Apply"]') 
    
    # Element Locators: Reason Input
    _reason_input = (AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    _reason_save_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Save"]') 

    # Element Locators: Day & Time Radio Buttons
    _weekdays_button = (AppiumBy.XPATH, '//android.widget.RadioButton[@text="Weekdays"]') 
    _days_choices_buttons = {
        """One selectable"""
            "Weekdays" : _weekdays_button,
    }
    
    # Element Locators: Day & Time Radio Buttons
    _morning_button = (AppiumBy.XPATH, '//android.widget.RadioButton[@text="Morning"]') 
    _time_choices_buttons = {
        """One selectable"""
            "Morning" : _morning_button,
    }
    
    # Element Locators: RMO Application Finish Button
    _finish_next_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Let\'s add Video"]')
    
    # Element Locators: Add Video Pop-up
    _video_skip_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Skip"]') 
    
    # Element Locators: Successful Application Pop-up
    _url_label = (AppiumBy.XPATH, '//*[@id="quick-apply-final-step"]/app-quick-apply-final-step/ion-content/div/ion-row[2]/ion-col/ion-item/ion-label') 
    _check_my_activities_button = (AppiumBy.XPATH, '//*[@id="quick-apply-final-step"]/app-quick-apply-final-step/ion-content/div/div[2]/ion-row/ion-col/ion-row/ion-col[1]/ion-button')
    _control_center_button = (AppiumBy.XPATH, '//*[@id="quick-apply-final-step"]/app-quick-apply-final-step/ion-content/div/div[2]/ion-row/ion-col/ion-row/ion-col[2]/ion-button')
    
    
    # Page Steps
    
    def rmo_application(self, data):
        """Full RMO application: Given you are on the home page""" 
        self.start_rmo()
        self.select_categories(data["courses"])
        self.select_location(data["location"])
        self.select_study_mode(data["study_mode"])
        self.select_delivery_type(data["delivery_type"])
        self.select_intake(data["intake"])
        self.enter_reason(data["reason"])
        self.select_lesson_times(data["days"], data["times"])
    
    def start_rmo(self):
        """Start an RMO application: Given you are on the home page"""
        self.click_education_button()
        self.click_undergraduate_button()
        self.click_this_user_button()
        self.click_education_next_button()
        
    def select_categories(self, courses):
        """RMO select courses: Given you started the RMO application"""
        self.click_category_search_button()
        
        for choice in courses:
            choice_button = self._course_choices_buttons[choice]
            self.click_category_choice_button(choice_button)

        self.click_category_done_button()
        self.click_category_next_button()
    
    def select_location(self, location):
        """RMO select location: Given you started the RMO application"""
        search_input = location["search"]
        choice_button = self._location_choices_buttons[location["choice"]]
        
        self.click_location_button()
        self.fill_location_search_input(search_input)
        time.sleep(5)
        self.click_location_choice_button(choice_button)
        self.click_location_done_button()
        self.click_location_next_button()
    
    def select_study_mode(self, study_mode):
        """RMO select study mode: Given you started the RMO application"""
        choice_button = self._study_mode_choices_buttons[study_mode["choice"]]

        self.click_study_mode_button()
        self.click_study_mode_choice_button(choice_button)
        self.click_study_apply_button()

    def select_delivery_type(self, delivery_type):
        """RMO select delivery type: Given you started the RMO application"""
        choice_button = self._delivery_type_choices_buttons[delivery_type["choice"]]
        
        self.click_delivery_type_button()
        self.click_delivery_type_choice_button(choice_button)
        self.click_delivery_apply_button()
        
    def select_intake(self, intake):
        """RMO select intake: Given you started the RMO application"""
        choice_button = self._intake_choices_buttons[intake["choice"]]

        self.click_intake_button()
        self.click_intake_choice_button(choice_button)
        self.click_intake_apply_button()
        
    def enter_reason(self, reason):
        """RMO enter reason: Given you started the RMO application"""
        text = reason["text"]
        self.fill_reason_input(text)
        self.click_reason_save_button()
        
    def select_lesson_days(self, days):
        """RMO days: Given you started the RMO application"""
        choice_button = self._days_choices_buttons[days["choice"]]
        self.click_days_choice_radio_button(choice_button)

    def select_lesson_time(self, time):
        """RMO time: Given you started the RMO application"""
        choice_button = self._time_choices_buttons[time["choice"]]
        self.click_time_choice_radio_button(choice_button)
    
    
    # Single Actions
    
    def click_education_button(self):
        click_element(self.driver, self._education_button)
        
    def click_undergraduate_button(self):
        click_element(self.driver, self._undergraduate_button) 
    
    def click_this_user_button(self):
        click_element(self.driver, self._this_user_button)
    
    def click_education_next_button(self):
        click_element(self.driver, self._education_next_button)
    
    
    def click_education_button(self):
        click_element(self.driver, self._education_button)
        
    def click_undergraduate_button(self):
        click_element(self.driver, self._undergraduate_button) 
    
    def click_this_user_button(self):
        click_element(self.driver, self._this_user_button)
    
    def click_education_next_button(self):
        click_element(self.driver, self._education_next_button)
    
    
    def click_category_search_button(self):
        click_element(self.driver, self._category_search_button)
        
    def click_category_choice_button(self, choice):
        click_element(self.driver, choice)
    
    def click_category_done_button(self):
        click_element(self.driver, self._category_done_button)
    
    def click_category_next_button(self):
        click_element(self.driver, self._category_next_button)
    
    
    def click_location_button(self):
        click_element(self.driver, self._location_button)
        
    def fill_location_search_input(self, location):
        fill_field(self.driver, self._location_search_input, location) 
    
    def click_location_choice_button(self, choice):
        click_element(self.driver, choice)
    
    def click_location_done_button(self):
        click_element(self.driver, self._location_done_button)

    def click_location_next_button(self):
        click_element(self.driver, self._location_next_button)

    
    def click_study_mode_button(self):
        click_element(self.driver, self._study_mode_button)
        
    def click_study_mode_choice_button(self, choice_button):
        click_element(self.driver, choice_button)

    def click_study_apply_button(self):
        click_element(self.driver, self._study_apply_button)

    
    def click_delivery_type_button(self):
        click_element(self.driver, self._delivery_type_button)

    def click_delivery_type_choice_button(self, choice):
        click_element(self.driver, choice)

    def click_delivery_apply_button(self):
        click_element(self.driver, self._delivery_apply_button)


    def click_intake_button(self):
        click_element(self.driver, self._intake_button)

    def click_intake_choice_button(self, choice_button):
        click_element(self.driver, choice_button)

    def click_intake_apply_button(self):
        click_element(self.driver, self._intake_apply_button)
    
    
    def fill_reason_input(self, text):
        fill_field(self.driver, self._reason_input, text)
        
    def click_reason_save_button(self):
        click_element(self.driver, self._reason_save_button)
        
    
    def click_days_choice_radio_button(self, days_choice):
        click_element(self.driver, days_choice)

    def click_time_choice_radio_button(self, time_choice):
        click_element(self.driver, time_choice)


    def click_finish_next_button(self):
        click_element(self.driver, self._finish_next_button)


    def get_url_label_text(self):
        """webview"""; switch_to_webview(self.driver)
        url = self._url_label.text
        return url
    
    def click_welcome_button(self):
        """webview"""
        pass
    
    def click_login_button(self):
        """webview"""
        pass    
    
    


