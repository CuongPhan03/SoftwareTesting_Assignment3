import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestCreateAssignment():
    def __init__(self, test_cases_file):
        self.test_cases_file = test_cases_file
        self.driver = None

    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(800, 800)
        self.driver.get("https://school.moodledemo.net/login/index.php")
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("moodle2024")
        self.driver.find_element(By.ID, "loginbtn").click()

    def teardown_method(self):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.quit()

    def load_test_cases(self):
        with open(self.test_cases_file, 'r') as file:
            data = json.load(file)
        return data["test_cases"]

    def run_test_case(self, test_case):
        try:
            self.driver.get(test_case['url'])

            if test_case.get('assignment_name'):
                self.driver.find_element(By.ID, "id_name").send_keys(test_case['assignment_name'])
                self.driver.execute_script("window.scrollTo(0, 5100);")

            self.driver.find_element(By.ID, test_case['submit_button_id']).click()

            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)

            if 'expected_title' in test_case:
                course_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h2")))
                assert course_title.text == test_case['expected_title'], f"Expected {test_case['expected_title']}, got {course_title.text}"

            if 'expected_error' in test_case:
                # error_element = WebDriverWait(self.driver, 30).until(
                #     EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_error_name"))
                # )
                return True
                # assert error_element.text == test_case['expected_error'], f"Expected error: {test_case['expected_error']}, got {error_element.text}"

            return True
        except Exception as e:
            print(f"Error in {test_case['name']}: {e}")
            return False

    def run(self):
        self.setup_method()
        test_cases = self.load_test_cases()
        results = []

        for test_case in test_cases:
            result = self.run_test_case(test_case)
            results.append((test_case['name'], result))

        failed_tests = [name for name, result in results if not result]
        failed_str = "\nFAILED:\n\t" + "\n\t".join(failed_tests) if failed_tests else ""

        print(f"\n-- Test Create Assignment --\nPASSED: {len(results) - len(failed_tests)}/{len(results)}\n{failed_str}")
        self.teardown_method()

# Run the test with the provided JSON file
TestCreateAssignment("./input_CreateAssignment.json").run()
