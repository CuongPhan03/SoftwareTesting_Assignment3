import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

import os

class TestFramework:
    def __init__(self):
        self.driver = None

    def setup_method(self):
        """Thiết lập môi trường trước mỗi test case."""
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 800)
        self.driver.get('https://school.moodledemo.net/login/index.php')
        self.driver.find_element(By.ID, "username").send_keys('manager')
        self.driver.find_element(By.ID, "password").send_keys('moodle2024')
        self.driver.find_element(By.ID, "loginbtn").click()
        
    def logout(self):
        self.driver.get("https://school.moodledemo.net/my/courses.php")
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
    
    def login(self,name):
        self.driver.get('https://school.moodledemo.net/login/index.php')  
        time.sleep(2)
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "password").send_keys('moodle2024')
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)  
    def teardown_method(self):
        """Đóng driver sau mỗi test case."""
        if self.driver:
            self.driver.quit()

    def perform_action(self, action):
        """Thực hiện các hành động từ file cấu hình."""
        locator = (By.XPATH, action['locator']) if 'locator' in action else None
        if action['action'] == 'navigate':
            self.driver.get(action['value'])
        elif action['action'] == 'click':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        elif action['action'] == 'send_keys':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(action['value'])
        elif action['action'] == 'select':
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            Select(element).select_by_visible_text(action['value'])
        elif action['action'] == 'logout':
            self.logout()
        elif action['action'] == 'login':
            self.login(action['value'])

    def perform_assertion(self, assertion):
        """Thực hiện kiểm tra kết quả."""
        locator = (By.XPATH, assertion['locator'])
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        assert element.text == assertion['expected'], f"Expected: {assertion['expected']}, Got: {element.text}"

    def run_test(self, test_case):
        """Chạy một test case dựa trên cấu hình."""
        print(f"Running: {test_case['test_case']}")
        for action in test_case['actions']:
            self.perform_action(action)
        for assertion in test_case.get('assertions', []):
            self.perform_assertion(assertion)

    def run(self, filename):
        """Thực thi tất cả các test case từ file cấu hình."""
        try:
            with open(filename) as f:
                test_cases = json.load(f)

            results = []
            for test in test_cases:
                self.setup_method() 
                try:
                    self.run_test(test)
                    results.append((test['test_case'], True))
                except Exception as e:
                    print(f"Test {test['test_case']} failed: {e}")
                    results.append((test['test_case'], False))
                finally:
                    self.teardown_method()  # Đóng driver sau mỗi test

            # Tổng hợp kết quả
            passed = sum(1 for _, success in results if success)
            failed = len(results) - passed
            print(f"\n-- Test Edit Question (Level 2) --\nPASSED: {passed}/{len(results)}\nFAILED: {failed}")
            for test_name, success in results:
                if not success:
                    print(f"FAILED TEST: {test_name}")
        except Exception as e:
            print(f"Error loading test cases: {e}")
            

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
TestFramework().run(config_path) 