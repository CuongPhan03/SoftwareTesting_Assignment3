import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


from selenium.webdriver.chrome.options import Options

class TestCreateAssignment:
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
        
    def test_create_assignment_case1(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập
            self.driver.find_element(By.ID, "id_name").click()
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")
            self.driver.execute_script("window.scrollTo(0, 5100);")

            self.driver.find_element(By.ID, "id_submitbutton2").click()

            # Bước 4: Nhấn nút Submit
            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)
            course1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h2")))

            assert course1.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def test_create_assignment_case2(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập và click nút submit mới (id_submitbutton)
            self.driver.find_element(By.ID, "id_name").click()
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")
            self.driver.execute_script("window.scrollTo(0, 5100);")

            self.driver.find_element(By.ID, "id_submitbutton").click()  # Nhấn nút id_submitbutton

            # Bước 3: Xác nhận rằng bài tập đã được tạo thành công
            time.sleep(3)
            wait2 = WebDriverWait(self.driver, 20)
            course2 = wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h2")))

            assert course2.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    def test_create_assignment_case3(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhấn nút submit mà không nhập tên bài tập
            self.driver.execute_script("window.scrollTo(0, 5100);")

            self.driver.find_element(By.ID, "id_submitbutton").click()

            # Bước 3: Kiểm tra thông báo lỗi
            time.sleep(3)
            # wait = WebDriverWait(self.driver, 20)

            # # Xác nhận rằng phần tử lỗi tồn tại và chứa thông báo chính xác
            # error_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_error_name")))
            # assert error_element.text == "-You must supply a value here"
            error_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_error_name"))
            )
            assert error_element.text == "- You must supply a value here."

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False



    def test_create_assignment_case4(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")

            # Bước 3: Nhấn nút submit để tạo bài tập
            self.driver.find_element(By.ID, "id_submitbutton").click()

            # Bước 4: Kiểm tra xem tên bài tập đã xuất hiện trong phần tử có class "h2"
            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)
          
            h2_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".h2"))
            )

            # Kiểm tra nội dung của phần tử
            assert h2_element.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    def test_create_assignment_case5(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 3: Nhấn nút submit để tạo bài tập
            self.driver.find_element(By.ID, "id_submitbutton").click()

            # Bước 4: Kiểm tra xem tên bài tập đã xuất hiện trong phần tử có class "h2"
            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)
          
            h2_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".h2"))
            )

            # Kiểm tra nội dung của phần tử
            assert h2_element.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    def test_create_assignment_case6(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")
 # Thêm bước cuộn trang xuống 1100px
            self.driver.execute_script("window.scrollTo(0, 1100);")
            time.sleep(3)
            # Bước 4: Chọn ngày bắt đầu cho bài tập
            # Chọn ngày tháng năm cho "Sử dụng từ"
            # self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_enabled").click()
# Bước 5: Chọn ngày bắt đầu (Sử dụng click và select)
# Chọn ngày (1)
            self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_day").click()
            day_select = Select(self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_day"))
            day_select.select_by_visible_text("1")

            # Chọn tháng (January)
            self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_month").click()
            month_select = Select(self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_month"))
            month_select.select_by_visible_text("January")

            # Chọn năm (2020)
            self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_year").click()
            year_select = Select(self.driver.find_element(By.CSS_SELECTOR, "#id_allowsubmissionsfromdate_year"))
            year_select.select_by_visible_text("2020")
            time.sleep(3)

            # Bước 5: Chọn ngày hết hạn cho bài tập
            # self.driver.find_element(By.ID, "id_duedate_enable").click()
            self.driver.find_element(By.ID, "id_duedate_day").send_keys("1")
            self.driver.find_element(By.ID, "id_duedate_month").send_keys("February")
            self.driver.find_element(By.ID, "id_duedate_year").send_keys("2020")
            time.sleep(3)
            # Bước 6: Chọn ngày đánh giá cho bài tập
            self.driver.find_element(By.ID, "id_cutoffdate_enabled").click()
            self.driver.find_element(By.ID, "id_cutoffdate_day").send_keys("1")
            self.driver.find_element(By.ID, "id_cutoffdate_month").send_keys("March")
            self.driver.find_element(By.ID, "id_cutoffdate_year").send_keys("2020")
          
            self.driver.execute_script("window.scrollTo(0, 3000);")

            time.sleep(3)
            # Bước 7: Nhấn nút submit để lưu bài tập
            self.driver.find_element(By.ID, "id_submitbutton").click()

            # Bước 8: Kiểm tra xem tên bài tập đã hiển thị trong phần tử có class "h2"
            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)
            h2_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".h2"))
            )

            # Kiểm tra nội dung của phần tử
            assert h2_element.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    def test_create_assignment_case7(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(784, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 1100);")

            # Bước 3: Chọn "Allow submissions from"
            allow_submissions_checkbox = self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_enabled")
            # allow_submissions_checkbox.click()
            time.sleep(2)

            # Bước 4: Chọn ngày bắt đầu
            self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_day").click()
            allow_day_select = Select(self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_day"))
            allow_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng bắt đầu
            self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_month").click()
            allow_month_select = Select(self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_month"))
            allow_month_select.select_by_visible_text("January")
            time.sleep(2)

            # Chọn năm bắt đầu
            self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_year").click()
            allow_year_select = Select(self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_year"))
            allow_year_select.select_by_visible_text("2024")
            time.sleep(2)

            # Bước 5: Chọn ngày hết hạn
            self.driver.find_element(By.ID, "id_duedate_day").click()
            due_day_select = Select(self.driver.find_element(By.ID, "id_duedate_day"))
            due_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng hết hạn
            self.driver.find_element(By.ID, "id_duedate_month").click()
            due_month_select = Select(self.driver.find_element(By.ID, "id_duedate_month"))
            due_month_select.select_by_visible_text("January")
            time.sleep(2)

            # Chọn năm hết hạn
            self.driver.find_element(By.ID, "id_duedate_year").click()
            due_year_select = Select(self.driver.find_element(By.ID, "id_duedate_year"))
            due_year_select.select_by_visible_text("2024")
            time.sleep(2)

            # Bước 6: Chọn "Grading due date enabled"
            grading_due_checkbox = self.driver.find_element(By.ID, "id_gradingduedate_enabled")
            grading_due_checkbox.click()
            time.sleep(2)

            # Bước 7: Nhấn nút submit
            self.driver.execute_script("window.scrollTo(0, 3000);")

            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Bước 8: Xác minh lỗi được hiển thị
            error_element = self.driver.find_element(By.ID, "id_error_duedate")
            assert error_element.text == "Due date must be after the allow submissions from date."
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def test_create_assignment_case8(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 1100);")

            # Bước 3: Bật tùy chọn "Allow submissions from"
            allow_submissions_checkbox = self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_enabled")
            allow_submissions_checkbox.click()
            time.sleep(2)

            # Bước 4: Bật tùy chọn "Due date enabled"
            # due_date_checkbox = self.driver.find_element(By.ID, "id_duedate_enabled")
            # due_date_checkbox.click()
            time.sleep(2)

            # Bước 5: Chọn ngày hết hạn
            self.driver.find_element(By.ID, "id_duedate_day").click()
            due_day_select = Select(self.driver.find_element(By.ID, "id_duedate_day"))
            due_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng hết hạn
            self.driver.find_element(By.ID, "id_duedate_month").click()
            due_month_select = Select(self.driver.find_element(By.ID, "id_duedate_month"))
            due_month_select.select_by_visible_text("February")
            due_year_select = Select(self.driver.find_element(By.ID, "id_duedate_year"))
            due_year_select.select_by_visible_text("2024")


            time.sleep(2)

            # Bước 6: Bật tùy chọn "Cut-off date enabled"
            cutoff_date_checkbox = self.driver.find_element(By.ID, "id_cutoffdate_enabled")
            cutoff_date_checkbox.click()
            time.sleep(2)

            # Bước 7: Chọn ngày "Cut-off date"
            self.driver.find_element(By.ID, "id_cutoffdate_day").click()
            cutoff_day_select = Select(self.driver.find_element(By.ID, "id_cutoffdate_day"))
            cutoff_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng "Cut-off date"
            self.driver.find_element(By.ID, "id_cutoffdate_month").click()
            cutoff_month_select = Select(self.driver.find_element(By.ID, "id_cutoffdate_month"))
            cutoff_month_select.select_by_visible_text("January")
            cut_year_select = Select(self.driver.find_element(By.ID, "id_cutoffdate_year"))
            cut_year_select.select_by_visible_text("2024")
            time.sleep(2)

            # Bước 8: Bật tùy chọn "Grading due date enabled"
            # grading_due_checkbox = self.driver.find_element(By.ID, "id_gradingduedate_enabled")
            # grading_due_checkbox.click()
            time.sleep(2)

            # Bước 9: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")
            time.sleep(2)
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 1500);")
            # Bước 10: Xác minh lỗi "Cut-off date cannot be earlier than the due date"
            error_element = self.driver.find_element(By.ID, "id_error_cutoffdate")
            assert error_element.text == "Cut-off date cannot be earlier than the due date."
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def test_create_assignment_case9(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 1100);")

            # Bước 3: Bật tùy chọn "Allow submissions from"
            # allow_submissions_checkbox = self.driver.find_element(By.ID, "id_allowsubmissionsfromdate_enabled")
            # allow_submissions_checkbox.click()
            time.sleep(2)

            # Bước 4: Bật tùy chọn "Due date enabled"
            # due_date_checkbox = self.driver.find_element(By.ID, "id_duedate_enabled")
            # due_date_checkbox.click()
            time.sleep(2)

            # Bước 5: Chọn ngày "Due date"
            self.driver.find_element(By.ID, "id_duedate_day").click()
            due_day_select = Select(self.driver.find_element(By.ID, "id_duedate_day"))
            due_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng "Due date"
            self.driver.find_element(By.ID, "id_duedate_month").click()
            due_month_select = Select(self.driver.find_element(By.ID, "id_duedate_month"))
            due_month_select.select_by_visible_text("February")
            time.sleep(2)

            # Chọn năm "Due date"
            self.driver.find_element(By.ID, "id_duedate_year").click()
            due_year_select = Select(self.driver.find_element(By.ID, "id_duedate_year"))
            due_year_select.select_by_visible_text("2020")
            time.sleep(2)

            # Bước 6: Bật tùy chọn "Grading due date enabled"
            # grading_due_checkbox = self.driver.find_element(By.ID, "id_gradingduedate_enabled")
            # grading_due_checkbox.click()
            time.sleep(2)

            # Bước 7: Chọn ngày "Grading due date"
            self.driver.find_element(By.ID, "id_gradingduedate_day").click()
            grading_day_select = Select(self.driver.find_element(By.ID, "id_gradingduedate_day"))
            grading_day_select.select_by_visible_text("1")
            time.sleep(2)

            # Chọn tháng "Grading due date"
            self.driver.find_element(By.ID, "id_gradingduedate_month").click()
            grading_month_select = Select(self.driver.find_element(By.ID, "id_gradingduedate_month"))
            grading_month_select.select_by_visible_text("January")
            time.sleep(2)

            # Chọn năm "Grading due date"
            self.driver.find_element(By.ID, "id_gradingduedate_year").click()
            grading_year_select = Select(self.driver.find_element(By.ID, "id_gradingduedate_year"))
            grading_year_select.select_by_visible_text("2020")
            time.sleep(2)

            # Bước 8: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")  # Cuộn xuống cuối trang
            time.sleep(2)
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 1500);")

            # Bước 9: Xác minh lỗi "Remind me to grade by date cannot be earlier than the due date"
            error_element = self.driver.find_element(By.ID, "id_error_gradingduedate")
            assert error_element.text == "Remind me to grade by date cannot be earlier than the due date."
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False




    def test_create_assignment_case10(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 816)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)
            # Bước 3: Bật tùy chọn "File submissions"
            file_sub_checkbox = self.driver.find_element(By.ID, "collapseElement-2")
            file_sub_checkbox.click()
            file_submission_checkbox = self.driver.find_element(By.ID, "id_assignsubmission_file_enabled")
            file_submission_checkbox.click()
            time.sleep(2)

            # Bước 4: Mở phần tùy chọn "Activity completion"
            collapse_element = self.driver.find_element(By.ID, "collapseElement-10")
            collapse_element.click()
            time.sleep(2)

            # Bước 5: Chọn tùy chọn "Students can manually mark the activity as completed"
            completion_radio = self.driver.find_element(By.ID, "id_completion_2")
            completion_radio.click()
            time.sleep(2)

            # Bước 6: Bật tùy chọn "Require students to click the submit button"
            completionsubmit_checkbox = self.driver.find_element(By.ID, "id_completionsubmit")
            completionsubmit_checkbox.click()
            time.sleep(2)

            # Bước 7: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")  # Cuộn xuống cuối trang
            time.sleep(2)
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            submit_button.click()
            time.sleep(2)

            # Xác minh rằng không có lỗi (hoặc thêm xác minh cụ thể nếu cần)
            # Nếu yêu cầu kiểm tra lỗi thì thực hiện thêm các bước tìm và xác nhận lỗi

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def test_create_assignment_case11a(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)

            # Bước 3: Mở rộng phần "Grade"
            grade_section = self.driver.find_element(By.ID, "collapseElement-7")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", grade_section)
            time.sleep(2)
            grade_section.click()

            # Bước 4: Chọn "Point" trong "Grade type"
            grade_type_dropdown = self.driver.find_element(By.ID, "id_grade_modgrade_type")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", grade_type_dropdown)
            time.sleep(2)
            grade_type_dropdown.click()

            grade_point_option = self.driver.find_element(By.ID, "id_grade_modgrade_point")
            grade_point_option.click()
            time.sleep(2)

            # Bước 5: Chọn "Grade category"
        #    # Chọn "Grade category"
        #     grade_category = self.driver.find_element(By.ID, "id_gradecat")
        #     self.driver.execute_script("arguments[0].scrollIntoView(true);", grade_category)  # Cuộn tới phần tử
        #     time.sleep(2)

        #     # Thực hiện click bằng JavaScript thay vì Selenium
        #     self.driver.execute_script("arguments[0].click();", grade_category)
        #     time.sleep(2)

            grade_category_label = self.driver.find_element(By.ID, "id_gradecat_label")
            grade_category_label.click()
            time.sleep(2)

            # Bước 6: Nhập giá trị "Grade to pass"
            grade_pass = self.driver.find_element(By.ID, "id_gradepass")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", grade_pass)
            time.sleep(2)
            grade_pass.click()
            grade_pass.send_keys("5")
            time.sleep(2)

            # Bước 7: Mở rộng phần "Activity completion"
            activity_completion = self.driver.find_element(By.ID, "collapseElement-10")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", activity_completion)
            time.sleep(2)
            activity_completion.click()

            # Bước 8: Chọn "Students can manually mark the activity as completed"
            completion_option = self.driver.find_element(By.ID, "id_completion_2")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", completion_option)
            time.sleep(2)
            completion_option.click()

            # Bước 9: Bật tùy chọn "Require grade to complete activity"
            require_grade = self.driver.find_element(By.ID, "id_completionusegrade")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", require_grade)
            time.sleep(2)
            require_grade.click()

            # Bước 10: Chọn "Require students to click the submit button"
            require_submit = self.driver.find_element(By.ID, "id_completionsubmit")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", require_submit)
            time.sleep(2)
            require_submit.click()

            # Bước 11: Chọn "Passing grade required"
            passing_grade = self.driver.find_element(By.ID, "id_completionpassgrade_1")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", passing_grade)
            time.sleep(2)
            passing_grade.click()

            # Bước 12: Nhấn nút "Submit"
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(2)
            submit_button.click()

            # Bước 13: Xác minh tên bài tập được tạo
            assignment_title = self.driver.find_element(By.CSS_SELECTOR, ".h2")
            assert "New Assignment 1" in assignment_title.text
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    def test_create_assignment_case11a(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)

            # Bước 3: Mở phần "Grade"
            grade_section = self.driver.find_element(By.ID, "collapseElement-7")
            grade_section.click()
            time.sleep(2)

            # Bước 4: Chọn kiểu chấm điểm là "Point"
            grade_type_dropdown = self.driver.find_element(By.ID, "id_grade_modgrade_type")
            grade_type_dropdown.click()
            time.sleep(2)
            point_option = self.driver.find_element(By.ID, "id_grade_modgrade_point")
            point_option.click()
            time.sleep(2)

            # Bước 5: Chọn danh mục điểm
            grade_category = self.driver.find_element(By.ID, "id_gradecat")
            grade_category.click()
            time.sleep(2)
            grade_category_label = self.driver.find_element(By.ID, "id_gradecat_label")
            grade_category_label.click()
            time.sleep(2)

            # Bước 6: Đặt điểm để đạt là 5
            grade_pass = self.driver.find_element(By.ID, "id_gradepass")
            grade_pass.click()
            grade_pass.send_keys("5")
            time.sleep(2)

            # Bước 7: Mở phần "Activity completion"
            completion_section = self.driver.find_element(By.ID, "collapseElement-10")
            completion_section.click()
            time.sleep(2)

            # Bước 8: Chọn tùy chọn "Students can manually mark the activity as completed"
            completion_manual = self.driver.find_element(By.ID, "id_completion_2")
            completion_manual.click()
            time.sleep(2)

            # Bước 9: Bật tùy chọn "Require grade to complete"
            completion_usegrade = self.driver.find_element(By.ID, "id_completionusegrade")
            completion_usegrade.click()
            time.sleep(2)

            # Bước 10: Yêu cầu sinh viên nhấn nút nộp
            completionsubmit_checkbox = self.driver.find_element(By.ID, "id_completionsubmit")
            completionsubmit_checkbox.click()
            time.sleep(2)

            # Bước 11: Đặt điểm hoàn thành là đạt
            completion_passgrade = self.driver.find_element(By.ID, "id_completionpassgrade_1")
            completion_passgrade.click()
            time.sleep(2)

            # Bước 12: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")
            time.sleep(2)

            # Bước cuộn và nhấn nút Submit
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            
            # Cuộn đến nút và xử lý pop-up nếu có
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(2)
            try:
                popup = self.driver.find_element(By.CSS_SELECTOR, "div[style*='z-index: 99999999']")
                self.driver.execute_script("arguments[0].remove();", popup)
            except:
                pass

            # Nhấn nút Submit
            submit_button.click()

            # Xác minh kết quả
          
            # Xác minh lỗi "The grade to pass can not be greater than the maximum possible grade 2"
            error_element = self.driver.find_element(By.ID, "id_error_gradepass")
            assert error_element.text == "The grade to pass can not be greater than the maximum possible grade 1"
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    
    def test_create_assignment_case11(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 816)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)
            # Bước 3: Bật tùy chọn "File submissions"
            file_sub_checkbox = self.driver.find_element(By.ID, "collapseElement-2")
            file_sub_checkbox.click()
            file_submission_checkbox = self.driver.find_element(By.ID, "id_assignsubmission_file_enabled")
            file_submission_checkbox.click()
            time.sleep(2)

            # Bước 4: Mở phần tùy chọn "Activity completion"
            collapse_element = self.driver.find_element(By.ID, "collapseElement-10")
            collapse_element.click()
            time.sleep(2)

            # Bước 5: Chọn tùy chọn "Students can manually mark the activity as completed"
            completion_radio = self.driver.find_element(By.ID, "id_completion_2")
            completion_radio.click()
            time.sleep(2)

            # Bước 6: Bật tùy chọn "Require students to click the submit button"
            completionsubmit_checkbox = self.driver.find_element(By.ID, "id_completionsubmit")
            completionsubmit_checkbox.click()
            time.sleep(2)

            # Bước 7: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")  # Cuộn xuống cuối trang
            time.sleep(2)
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            submit_button.click()
            time.sleep(2)

            # Xác minh rằng không có lỗi (hoặc thêm xác minh cụ thể nếu cần)
            # Nếu yêu cầu kiểm tra lỗi thì thực hiện thêm các bước tìm và xác nhận lỗi

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    def test_create_assignment_case12a(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )
            self.driver.set_window_size(796, 817)
            time.sleep(2)

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            name_field = self.driver.find_element(By.ID, "id_name")
            name_field.click()
            name_field.send_keys("New Assignment 1")
            time.sleep(2)

            # Bước 3: Mở phần "Grade"
            grade_section = self.driver.find_element(By.ID, "collapseElement-7")
            grade_section.click()
            time.sleep(2)

            # Bước 4: Chọn kiểu chấm điểm là "Point"
            grade_type_dropdown = self.driver.find_element(By.ID, "id_grade_modgrade_type")
            grade_type_dropdown.click()
            time.sleep(2)
            point_option = self.driver.find_element(By.ID, "id_grade_modgrade_point")
            point_option.click()
            time.sleep(2)

            # Bước 5: Chọn danh mục điểm
            grade_category = self.driver.find_element(By.ID, "id_gradecat")
            grade_category.click()
            time.sleep(2)
            grade_category_label = self.driver.find_element(By.ID, "id_gradecat_label")
            grade_category_label.click()
            time.sleep(2)

            # Bước 6: Đặt điểm để đạt là 5
            grade_pass = self.driver.find_element(By.ID, "id_gradepass")
            grade_pass.click()
            grade_pass.send_keys("5")
            time.sleep(2)

            # Bước 7: Mở phần "Activity completion"
            completion_section = self.driver.find_element(By.ID, "collapseElement-10")
            completion_section.click()
            time.sleep(2)

            # Bước 8: Chọn tùy chọn "Students can manually mark the activity as completed"
            completion_manual = self.driver.find_element(By.ID, "id_completion_2")
            completion_manual.click()
            time.sleep(2)

            # Bước 9: Bật tùy chọn "Require grade to complete"
            completion_usegrade = self.driver.find_element(By.ID, "id_completionusegrade")
            completion_usegrade.click()
            time.sleep(2)

            # Bước 10: Yêu cầu sinh viên nhấn nút nộp
            completionsubmit_checkbox = self.driver.find_element(By.ID, "id_completionsubmit")
            completionsubmit_checkbox.click()
            time.sleep(2)

            # Bước 11: Đặt điểm hoàn thành là đạt
            completion_passgrade = self.driver.find_element(By.ID, "id_completionpassgrade_1")
            completion_passgrade.click()
            time.sleep(2)

            # Bước 12: Nhấn nút "Submit"
            self.driver.execute_script("window.scrollTo(0, 3000);")
            time.sleep(2)

            # Bước cuộn và nhấn nút Submit
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")
            
            # Cuộn đến nút và xử lý pop-up nếu có
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(2)
            try:
                popup = self.driver.find_element(By.CSS_SELECTOR, "div[style*='z-index: 99999999']")
                self.driver.execute_script("arguments[0].remove();", popup)
            except:
                pass

            # Nhấn nút Submit
            submit_button.click()

            # Xác minh kết quả
          
            # Xác minh lỗi "The grade to pass can not be greater than the maximum possible grade 2"
            error_element = self.driver.find_element(By.ID, "id_error_gradepass")
            assert error_element.text == "The grade to pass can not be greater than the maximum possible grade 1"
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False



    def test_create_assignment_case12(self):
        try:
            # Bước 1: Truy cập URL để thêm bài tập
            self.driver.get(
                "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=69&section=5&return=0&beforemod=0"
            )

            # Bước 2: Nhập tên bài tập vào trường "id_name"
            self.driver.find_element(By.ID, "id_name").send_keys("Test_assignment")
            self.driver.execute_script("window.scrollTo(0, 5100);")

            # Bước 3: Nhấn nút submit để tạo bài tập
            self.driver.find_element(By.ID, "id_submitbutton").click()

            # Bước 4: Kiểm tra xem tên bài tập đã xuất hiện trong phần tử có class "h2"
            time.sleep(3)
            wait = WebDriverWait(self.driver, 20)
          
            h2_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".h2"))
            )

            # Kiểm tra nội dung của phần tử
            assert h2_element.text == "Test_assignment"
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False




    def run(self):
        self.setup_method()

        test_list = [
     # Test case 3
    
            self.test_create_assignment_case1,  # Test case 1
            self.test_create_assignment_case2 ,# Test case 2
            self.test_create_assignment_case3 ,  # Test case 3                 
            self.test_create_assignment_case4  , # Test case 3
            self.test_create_assignment_case5 ,  # Test case 3
            self.test_create_assignment_case6,   # Test case 3
            self.test_create_assignment_case7   ,# Test case 3

            self.test_create_assignment_case8  , # Test case 3
            self.test_create_assignment_case9,  
            self.test_create_assignment_case10  , # Test case 3
           
            self.test_create_assignment_case11  ,# Test case 3

            self.test_create_assignment_case12

        
        
        ]

        results = [test() for test in test_list]

        fail_test_names = []
        for i in range(0, len(results)):
            if not results[i]:
                fail_test_names.append(test_list[i].__name__)

        fail_test_str = ("FAILED:\n\t" + "\n\t".join(name for name in fail_test_names) + "\n") if len(fail_test_names) > 0 else ""
        print(f"\n-- Test Create Assignment --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")
        
        self.teardown_method()

TestCreateAssignment().run()
