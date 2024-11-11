import pytest
import user_application_steps as test
from library.support.user_management import search_json


users_data = 'library/data/users.json'
data_criteria = [{"tags.signed_up": True}]

@pytest.mark.user_application_test
@pytest.mark.happy_paths
@pytest.mark.valid_inputs
@pytest.mark.static_data
@pytest.mark.parametrize("new_user", search_json(users_data, data_criteria))

def test_user_application(new_user):
####################################################################################
    
    """Scenario: User Submits An RMO Application""";                  test.step0(new_user)
    "Rules: Happy paths, valid inputs, static data"
    
    "Given the user is logged in";                                    test.step1()
    "And the user starts an RMO application";                         test.step2()
    
    "When the user selects the first 3 courses";                      test.step3()
    "And the user sets 'Kuala Lumpur' as their location";             test.step4()
    "And the user selects 'Full-time' as their study mode";           test.step5()
    "And the user selects 'Classroom' as their delivery type";        test.step6()
    "And the user selects 'December 2024' as their intake date";      test.step7()
    "And the user adds a reason for applying";                        test.step8()
    "And the user selects 'Weekday mornings' for their lesson times"; test.step9()
    
    "When the user submits their application";                        test.step10()
    "Then the user should receive an application url";                test.step11()
    
####################################################################################
