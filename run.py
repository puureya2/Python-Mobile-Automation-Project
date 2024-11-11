import os
import subprocess
import time


def appium():
    # appium --allow-insecure chromedriver_autodownload
    subprocess.run(["appium", "--allow-insecure", "chromedriver_autodownload"])


def tests():
    tests = { 
             "Demo" : ["test_test", "tests/test_test.py"],
             "User Application" : ["user_application_test", "tests/user_application_test/user_application_test.py"]
             }
    
    return tests


def run_test(test=["test_test", "tests/test_test.py"]):
    # pytest tests/test_test.py -s -v --alluredir tests/output/allure-results/test_test --clean-alluredir
    
    test_name = test[0]
    test = test[1]
    allure_dir = "tests/output/allure-results/" + test_name
    
    subprocess.run(
        ["pytest", test, "-s", "-v", "--alluredir", allure_dir, "--clean-alluredir"])


def generate_report(test=["test_test", "tests/test_test.py"]):
    # allure serve tests/output/allure-results/test_test
    
    test_name = test[0]
    allure_dir = "tests/output/allure-results/" + test_name
    
    subprocess.run(["allure", "serve", allure_dir])


###########################################################################


if __name__ == "__main__":
    
    # 0. Choose a test: "Demo", "User Application"
    test = tests()["User Application"]
    
    # 1. Start Appium server (if not already running)
    # appium()
    
    # 2. Run test and generate allure report
    run_test(test)
    
    # 3. Run allure serve to open the report
    # generate_report(test)
