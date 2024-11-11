import pytest
from library.support.user_management import search_json
import signup_steps as test


users_data = 'library/data/users.json'
data_criteria = [{"tags.signed_up": False}]

@pytest.mark.signup_test
@pytest.mark.happy_paths
@pytest.mark.valid_inputs
@pytest.mark.parametrize("new_user", search_json(users_data, data_criteria))

def test_signup(new_user):
####################################################################################
    
    """Scenario: User Creates A New Account""";        test.step0(new_user)
    "Rules: Happy paths, valid inputs"
    
    "Given the user is logged in";                     test.step1()
    "And the user navigates to the signup page";       test.step2()
    
    "When the user creates a new account";             test.step3()
    "And the user enters their personal information";  test.step4()
    "Then the user should receive an OTP";             test.step5()
    "When the user enters the correct OTP";            test.step6()
    "Then the user should be successfully signed in";  test.step7()
    
####################################################################################
