import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class TestUpdateAssignmentLevel1:
    def setup_method(self):
        # Tạo một instance của ChromeOptions
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # "3" để tắt log lỗi

        # Khởi tạo ChromeDriver với các tuỳ chọn
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(800, 800)
        self.driver.get("https://school.moodledemo.net/login/index.php")

        # Đăng nhập vào Moodle
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("moodle2024")
        self.driver.find_element(By.ID, "loginbtn").click()

    def teardown_method(self):
        # Đăng xuất và đóng trình duyệt
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.quit()

    def test_update_assignment(self, testcase):
        try:
            # Truy cập URL chỉnh sửa bài tập
            self.driver.get(testcase["url"])
            time.sleep(2)

            # Xử lý trường "name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)

            if testcase["new_name"]:
                name_field.send_keys(testcase["new_name"])
            else:
                name_field.clear()  # Để trống nếu không có giá trị mới

            time.sleep(1)

            # Cuộn xuống và nhấn Submit
            self.driver.execute_script("window.scrollTo(0, 5100);")
            self.driver.find_element(By.ID, testcase["submit_button"]).click()
            time.sleep(2)

            # Kiểm tra kết quả
            if testcase["expected_result"] == "success":
                success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
                assert "Make a submission" in success_text
            elif testcase["expected_result"] == "error":
                error_message = self.driver.find_element(By.ID, "id_error_name").text
                assert "- You must supply a value here." in error_message

            print(f"Test passed: {testcase['name']}")

            return True
        except Exception as e:
            print(f"Test failed: {testcase['name']}, Error: {e}")
            return False

    def run(self, input_file):
        self.setup_method()

        with open(input_file, encoding="UTF-8") as f:
            testcases = json.load(f)

        results = [self.test_update_assignment(tc) for tc in testcases]

        fail_test_names = [testcases[i]["name"] for i, result in enumerate(results) if not result]
        fail_test_str = ("FAILED:\n\t" + "\n\t".join(fail_test_names) + "\n") if fail_test_names else ""

        print(f"\n-- Test Update Assignment (Level 1) --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")

        self.teardown_method()


# Chạy script
TestUpdateAssignmentLevel1().run('./input_UpdateAssignment.json')
