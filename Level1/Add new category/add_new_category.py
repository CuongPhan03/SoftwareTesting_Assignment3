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

class TestAddCategory:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 768)
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("sandbox24")
        self.driver.find_element(By.ID, "loginbtn").click()

    def teardown_method(self, method):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.quit()

    def test_add_category(self, category_data):
        """
        Add a new category using the provided data.
        :param category_data: Dictionary containing 'name' and optional 'parent_category'.
        """
        try:
            self.driver.get("https://sandbox.moodledemo.net/course/management.php")
            
            # Click on 'Add a category'
            self.driver.find_element(By.LINK_TEXT, "Add a category").click()

            # Fill in the category name
            self.driver.find_element(By.ID, "id_name").click()
            self.driver.find_element(By.ID, "id_name").send_keys(category_data["name"] if category_data["name"] else "")
            
            self.driver.find_element(By.ID, "id_idnumber").click()
            self.driver.find_element(By.ID, "id_idnumber").send_keys(category_data["id_category"] if category_data["id_category"] else "")

            if category_data["parent_category"] == "none":
                self.driver.find_element(By.CSS_SELECTOR, "#form_autocomplete_selection-1733641173057-0 > span").click()
                dropdown = self.driver.find_element(By.ID, "id_parent")
                dropdown.find_element(By.XPATH, "//option[. = 'label']").click()
            else:         
            # Select parent category if provided
                parent_select = self.driver.find_element(By.ID, "id_parent")
                parent_select.click()
                parent_options = parent_select.find_elements(By.TAG_NAME, "option")
                for option in parent_options:
                    if option.text.strip() == category_data["parent_category"]:
                        option.click()
                        break
                    
            self.driver.switch_to.frame(0)
            description_element = self.driver.find_element(By.ID, "tinymce")
            self.driver.execute_script(
                "arguments[0].innerHTML = arguments[1]", 
                description_element, 
                category_data["description"]
            )
            self.driver.switch_to.default_content()
            
            if (category_data["cancel"] == "true"):
                self.driver.find_element(By.ID, "id_cancel").click()
            else:
                # Click 'Save changes'
                self.driver.find_element(By.ID, "id_submitbutton").click()
            if (category_data["cancel"] == "true"):
            # Verify if the category is added successfully
                success_message = self.driver.find_element(By.XPATH, "//*[@id=\"course-listing-title\"]").text != category_data["name"]
                return success_message
            elif category_data["parent_category"] == "none":
                success_message = self.driver.find_element(By.XPATH, "//*[@id=\"id_error_parent\"]").text == "- You must supply a value here."
                return success_message
            else:
                success_message = self.driver.find_element(By.XPATH, "//*[@id=\"course-listing-title\"]").text ==  category_data["name"]
                self.driver.find_element(By.CSS_SELECTOR, "#action-menu-toggle-2 > .icon").click()
                self.driver.find_element(By.LINK_TEXT, "Delete").click()
                self.driver.find_element(By.ID, "id_submitbutton").click()
                return success_message
                

        except Exception as e:
            print(f"Error adding category '{category_data['name']}': {e}")
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

# Run the tests
TestAddCategory().run('./input_AddCategory.json')
