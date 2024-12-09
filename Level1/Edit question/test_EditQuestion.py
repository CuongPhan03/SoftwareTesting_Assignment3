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
        
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800, 800)
        self.driver.get('https://school.moodledemo.net/login/index.php')
        self.driver.find_element(By.ID, "username").send_keys('teacher')
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
        locator_type = action.get('type', 'xpath')  # Mặc định sử dụng 'xpath' nếu không có 'type'
        locator_value = action.get('locator', '')  # Lấy giá trị của 'locator'
        locator = None

        # Xác định kiểu định vị
        if locator_type == 'xpath':
            locator = (By.XPATH, locator_value)
        elif locator_type == 'css':
            locator = (By.CSS_SELECTOR, locator_value)
        elif locator_type == 'id':
            locator = (By.ID, locator_value)
        elif locator_type == 'name':
            locator = (By.NAME, locator_value)
        elif locator_type == 'tag_name':
            locator = (By.TAG_NAME, locator_value)
        elif locator_type == 'class_name':
            locator = (By.CLASS_NAME, locator_value)
        elif locator_type == 'link_text':
            locator = (By.LINK_TEXT, locator_value)
        elif locator_type == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, locator_value)

        # Xử lý các hành động
        if action['action'] == 'navigate':
            self.driver.get(action['value'])
        elif action['action'] == 'click':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
            time.sleep(2)
        elif action['action'] == 'send_keys':
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            element.clear()  # Clear trước khi gửi (nếu cần thiết)
            element.send_keys(action['value'])
            # Gửi thêm các phím đặc biệt nếu có
            if 'extra_keys' in action:
                special_key = getattr(Keys, action['extra_keys'].upper(), None)
                if special_key:
                    element.send_keys(special_key)
                else:
                    raise ValueError(f"Unsupported extra key: {action['extra_keys']}")
        elif action['action'] == 'clear':
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).clear()
        elif action['action'] == 'select':
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            Select(element).select_by_visible_text(action['value'])
        elif action['action'] == 'logout':
            self.logout()
        elif action['action'] == 'login':
            self.login(action['value'])
        elif action['action'] == 'switch_to_default_content':
            self.driver.switch_to.default_content()
        

    def perform_assertion(self, assertion):
    
        locator = None
        if 'locator' in assertion:
            locator_type = assertion.get('type', 'xpath').upper()
            if locator_type == "XPATH":
                locator = (By.XPATH, assertion['locator'])
            elif locator_type == "ID":
                locator = (By.ID, assertion['locator'])
            elif locator_type == "CSS":
                locator = (By.CSS_SELECTOR, assertion['locator'])
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator),
            message=f"Element not found with locator: {locator}"
        )

        assertion_type = assertion.get('assertion_type', 'text').lower()
        expected_value = assertion['expected']

        if assertion_type == 'text':
            actual_value = element.text
            assert actual_value == expected_value, f"Assertion failed: Expected text '{expected_value}', but got '{actual_value}'"

        elif assertion_type == 'value':
            actual_value = element.get_attribute('value')
            assert actual_value == expected_value, f"Assertion failed: Expected value '{expected_value}', but got '{actual_value}'"

        elif assertion_type == 'attribute':
            attribute_name = assertion.get('attribute_name')
            if not attribute_name:
                raise ValueError("Missing 'attribute_name' for attribute assertion.")
            actual_value = element.get_attribute(attribute_name)
            assert actual_value == expected_value, f"Assertion failed: Expected attribute '{attribute_name}' to be '{expected_value}', but got '{actual_value}'"

        else:
            raise ValueError(f"Unsupported assertion type: {assertion_type}")

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
            print(f"\n-- Test Edit Question (Level 1) --\nPASSED: {passed}/{len(results)}\nFAILED: {failed}")
            for test_name, success in results:
                if not success:
                    print(f"FAILED TEST: {test_name}")
        except Exception as e:
            print(f"Error loading test cases: {e}")
            

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
TestFramework().run(config_path) 