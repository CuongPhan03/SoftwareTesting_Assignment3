import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


from selenium.webdriver.chrome.options import Options

class TestUpdateAssignment:
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
        
    def test_update_assignment1(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_1")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False
    def test_update_assignment2(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_2")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton2").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".h2").text
            # assert "Mindful course" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False

    def test_update_assignment3(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?return=1&update=980")
            time.sleep(2)

            # Bước 3: Click vào ô "Name" để kích hoạt
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            # Bước 6: Để trống ô "Name" và không nhập giá trị
            name_field.clear()
            time.sleep(1)

            # Bước 7: Nhấn chuột xuống nút "Submit"
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            webdriver.ActionChains(self.driver).move_to_element(submit_button).click_and_hold().perform()
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)

            # Bước 8: Xác minh thông báo lỗi hiển thị
            error_message = self.driver.find_element(By.ID, "id_error_name").text
            assert "- You must supply a value here." in error_message
            print("Test passed: Error message displayed correctly.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False

    def test_update_assignment4(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_2")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False
    
    def test_update_assignment5(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_5")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False

    
    def test_update_assignment6(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_6")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False



    
    def test_update_assignment7(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_7")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False




    
    def test_update_assignment8(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_8")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False
        
    
    def test_update_assignment9(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_9")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False



    
    def test_update_assignment10(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_10")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False


    
    def test_update_assignment11(self):
        try:
            # Bước 1: Truy cập URL để cập nhật bài tập
            self.driver.get("https://school.moodledemo.net/course/modedit.php?update=980&return=1")
            time.sleep(2)

            # Bước 2: Thay đổi tên bài tập
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.clear()
            time.sleep(1)
            
            name_field.send_keys("Test_11")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 6: Nhấn nút "Submit" để lưu thay đổi
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 7: Kiểm tra thông báo xác nhận đã thay đổi
            success_text = self.driver.find_element(By.CSS_SELECTOR, ".font-weight-normal").text
            assert "Make a submission" in success_text
            print("Test passed: Assignment updated successfully.")

            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False



    def run(self):
        self.setup_method()

        test_list = [
     # Test case 3
    
            self.test_update_assignment1 , # Test case 1
            self.test_update_assignment2 , # Test case 1
            self.test_update_assignment3, # Test case 1
            self.test_update_assignment4 , # Test case 1
            self.test_update_assignment5, # Test case 2
                
            self.test_update_assignment6, # Test case 2
       
          
            self.test_update_assignment7 , # Test case 1
            self.test_update_assignment8, # Test case 1
            self.test_update_assignment9 , # Test case 1
            self.test_update_assignment10, # Test case 2
                
            self.test_update_assignment11 # Test case 2
        
        ]

        results = [test() for test in test_list]

        fail_test_names = []
        for i in range(0, len(results)):
            if not results[i]:
                fail_test_names.append(test_list[i].__name__)

        fail_test_str = ("FAILED:\n\t" + "\n\t".join(name for name in fail_test_names) + "\n") if len(fail_test_names) > 0 else ""
        print(f"\n-- Test Create Assignment --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")
        
        self.teardown_method()

TestUpdateAssignment().run()
