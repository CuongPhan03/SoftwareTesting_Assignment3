import pytest
import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEnrollUsers():
    self.driver.find_element(By.XPATH, "//a[contains(@class, 'moreless-toggler')]").click()
    
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 768)
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("sandbox24")
        self.driver.find_element(By.ID, "loginbtn").click()

    def teardown_method(self, method):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.quit()

    def EnrollUsers(self, test_data):
        try:
            self.driver.get("https://sandbox.moodledemo.net/user/index.php?id=2")
        

            # Thêm người dùng
            self.driver.find_element(By.CSS_SELECTOR, "#enrolusersbutton-1 .btn").click()
            dropdown_arrow = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "form_autocomplete_downarrow-1732247948016"))
            )
            actions = ActionChains(self.driver)
            actions.double_click(dropdown_arrow).perform()

            for user in test_data["users"]:
                dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "id_userlist"))
                )
                dropdown.find_element(By.XPATH, f"//option[. = '{user}']").click()

            # Gán vai trò
            role_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "id_roletoassign"))
            )
            role_dropdown.find_element(By.XPATH, f"//option[. = '{test_data['role']}']").click()
            
            if test_data["show_more"] == "true":
                self.driver.find_element(By.XPATH, "//a[contains(@class, 'moreless-toggler')]").click()
            
            if test_data["recover"] == "true":
                self.driver.find_element(By.ID, "id_recovergrades").click()
            
            self.driver.find_element(By.ID, "id_startdate").click()
            dropdown = self.driver.find_element(By.ID, "id_startdate")
            dropdown.find_element(By.XPATH, f"//option[contains(text(), '{test_data["start_date"]}')]").click()
            
            if test_data["enable"] == "true":
                    self.driver.find_element(By.ID, "id_timeend_enabled").click()
                    if test_data["end_day"] != "":
                        self.driver.find_element(By.ID, "id_timeend_day").click()
                        dropdown = self.driver.find_element(By.ID, "id_timeend_day")
                        dropdown.find_element(By.XPATH, f"//option[. = '{test_data["end_day"]}']").click()
                    if test_data["end_month"] != "": 
                        self.driver.find_element(By.ID, "id_timeend_month").click()
                        dropdown = self.driver.find_element(By.ID, "id_timeend_month")
                        dropdown.find_element(By.XPATH, f"//option[. = '{test_data["end_month"]}']").click()
                    if test_data["end_year"] != "":
                        self.driver.find_element(By.ID, "id_timeend_year").click()
                        dropdown = self.driver.find_element(By.ID, "id_timeend_year")
                        dropdown.find_element(By.XPATH, f"//option[. = '{test_data["end_year"]}']").click()
                    if test_data["end_minutes"] != "":
                        self.driver.find_element(By.ID, "id_timeend_minute").click()
                        dropdown = self.driver.find_element(By.ID, "id_timeend_minute")
                        dropdown.find_element(By.XPATH, f"//option[. = '{test_data["end_minutes"]}']").click()
                    if test_data["end_hour"] != "":
                        self.driver.find_element(By.ID, "id_timeend_hour").click()
                        dropdown = self.driver.find_element(By.ID, "id_timeend_hour")
                        dropdown.find_element(By.XPATH, f"//option[. = '{test_data["end_hour"]}']").click()
            
            if test_data["duration"]!= "":
                self.driver.find_element(By.ID, "id_duration").click()
                dropdown = self.driver.find_element(By.ID, "id_duration")
                dropdown.find_element(By.XPATH, f"//option[. = '{test_data["duration"]}']").click()
                
            
            month_str_to_num = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12 }
            month_num = month_str_to_num[test_data["end_time"]["month"]]
            
            input_time = datetime( test_data["end_year"], month_num, test_data["end_day"], test_data["end_hour"], test_data["end_minutes"] )
            
            current_time = datetime.now()
            
            
            
            # Xác nhận ghi danh
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Enrol users')]").click()

            # Kiểm tra kết quả
            if test_data["cancel"] == "true":
                success_message =  self.driver.find_element(By.XPATH, "//*[@id=\"user-index-participants-3_r0_c1\"]/a/span").text == "TT"
                return success_message
            elif input_time < current_time:
                success_message =  self.driver.find_element(By.XPATH, "//*[@id=\"user-index-participants-3_r0_c1\"]/a/span").text == "TT"
                return success_message
            else:
                success_message = True
                for key, xpath in test_data["expected_results"]:
                    if self.driver.find_element(By.XPATH, xpath).text != key:
                        success_message = False
                        break
                    
                for key, xpath in test_data["expected_results"]:
                    if self.driver.find_element(By.XPATH, xpath).text != key:
                        self.driver.find_element(By.XPATH, "//i[@title='Unenrol']").click()
                        self.driver.find_element(By.XPATH, "//button[contains(text(),'Unenrol')]").click()
                
                return success_message

            
        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False

    def run(self, filename):
        """
        Run all test cases for adding categories from the input file.
        :param filename: Path to the JSON file containing test cases.
        """
        self.setup_method(None)
        
        with open(filename, encoding="UTF-8") as f:
            testcases = json.load(f)

        results = [self.test_add_category(testcase) for testcase in testcases]

        fail_test_names = [
            testcases[i]["name"] for i in range(len(results)) if not results[i]
        ]

        fail_test_str = (
            "FAILED:\n\t" + "\n\t".join(name for name in fail_test_names) + "\n"
            if len(fail_test_names) > 0
            else ""
        )

        print(
            f"\n-- Test Add Category --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}"
        )

        self.teardown_method(None)

TestEnrollUsers().run('./input_data.json')