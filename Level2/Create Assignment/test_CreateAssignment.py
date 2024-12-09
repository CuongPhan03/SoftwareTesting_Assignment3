import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestCreateAssignment:
    def setup_method(self, tasks):
        self.driver = webdriver.Chrome()
        self.data = [
            { "name": "New Assignment", "description": "This is a description for the new assignment." }
        ]
        for task in tasks:
            self.runTask(task)
  
    def teardown_method(self, tasks):
        for task in tasks:
            self.runTask(task)
        self.driver.quit()

    def runTask(self, task):
        wait = WebDriverWait(self.driver, 10)
        action = task["action"]
        if action in ["set_window_size", "get_url", "sleep"]: 
            value = task["value"]
            if action == "set_window_size":
                self.driver.set_window_size(value[0], value[1])  
            elif action == "get_url":
                self.driver.get(value)
            else: 
                time.sleep(value)
        else:
            element_type = getattr(By, task["element_type"])
            element_locator = task["element_locator"]
            if action == "click":
                wait.until(EC.element_to_be_clickable((element_type, element_locator))).click()
            elif action == "input":
                value = Keys.ENTER if task["value"] == "ENTER" else task["value"]
                wait.until(EC.element_to_be_clickable((element_type, element_locator))).send_keys(value)
            elif action == "wait":
                ec = getattr(EC, task["expected_condition"])
                wait.until(ec((element_type, element_locator)))
            elif action == 'assert_text':
                element = wait.until(EC.presence_of_element_located((element_type, element_locator)))
                assert element.text == task["value"]
            elif action == 'assert_count':
                elements = self.driver.find_elements(element_type, element_locator)
                assert len(elements) == task["value"]

    def test(self, tasks):
        try:
            for task in tasks:
                self.runTask(task)
            return True
        except Exception:
            return False

    def run(self, filename):
        with open(filename, encoding="UTF-8") as f:
            data = json.load(f)

        self.setup_method(data["login"])

        testcases = data["testcases"]
        results = [self.test(testcase["tasks"]) for testcase in testcases]

        fail_test_names = []
        for i in range(0, len(results)):
            if not results[i]:
                fail_test_names.append(testcases[i]["name"])
                
        fail_test_str = ("FAILED:\n\t"+ "\n\t".join(name for name in fail_test_names) + "\n") if len(fail_test_names) > 0 else ""
        print(f"\n-- Test Create Assignment --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")

        self.teardown_method(data["logout"])

TestCreateAssignment().run('./input_CreateAssignment.json')
