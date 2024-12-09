import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUpdateAssignment:
    def setup_method(self, tasks):
        # Tạo một instance của ChromeOptions
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # "3" để tắt log lỗi

        # Khởi tạo ChromeDriver với các tuỳ chọn
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(800, 800)
        
        # Đăng nhập vào Moodle
        for task in tasks["login"]:
            self.run_task(task)

    def teardown_method(self, tasks):
        # Đăng xuất và đóng trình duyệt
        for task in tasks["logout"]:
            self.run_task(task)
        self.driver.quit()
    
    def run_task(self, task):
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
                value = task["value"]
                wait.until(EC.element_to_be_clickable((element_type, element_locator))).send_keys(value)
            elif action == "assert_text":
                element = wait.until(EC.presence_of_element_located((element_type, element_locator)))
                assert element.text == task["value"]
            elif action == "assert_count":
                elements = self.driver.find_elements(element_type, element_locator)
                assert len(elements) == task["value"]

    def update_assignment(self, assignment_data):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            url = f"https://school.moodledemo.net/course/modedit.php?update={assignment_data['id']}&return=1"
            self.driver.get(url)
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys(assignment_data['name'])
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert assignment_data['expected_text'] in success_text
            print(f"Test passed: Assignment {assignment_data['name']} updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False

    def test(self, tasks):
        try:
            for task in tasks["assignments"]:
                result = self.update_assignment(task)
                return result
        except Exception:
            return False

    def run(self, filename):
        with open(filename, encoding="UTF-8") as f:
            data = json.load(f)

        self.setup_method(data)

        results = [self.test(data) for _ in data["assignments"]]

        fail_test_names = []
        for i, result in enumerate(results):
            if not result:
                fail_test_names.append(data["assignments"][i]["name"])

        fail_test_str = ("FAILED:\n\t" + "\n\t".join(fail_test_names) + "\n") if len(fail_test_names) > 0 else ""
        print(f"\n-- Test Update Assignment --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")

        self.teardown_method(data)


# Run the tests
TestUpdateAssignment().run('./input_UpdateAssignment.json')
