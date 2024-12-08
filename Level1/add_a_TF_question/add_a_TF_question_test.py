# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INPUT_PATH = os.path.join(os.path.dirname(__file__), "add_a_TF_question_data.json")
def get_authen_info():
  with open(INPUT_PATH, 'r') as f:
    combined_data = json.load(f)
  # Lấy dữ liệu authen
  authen_data = combined_data.get('authen', [])  # Dùng get để tránh lỗi nếu key không tồn tại
  return authen_data
def get_test_data():
  with open(INPUT_PATH, 'r') as f:
    combined_data = json.load(f)
  test_data = combined_data.get('data', [])
  # Lấy dữ liệu test
  return [(d["name"], d["text"], d["default_mark"], d["expected"]) for d in test_data]
class TestTC002001():
  
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--inprivate")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def precondition(self):
    authen_data = get_authen_info()
    self.driver.delete_all_cookies()
    # Mở trang đăng nhập
    self.driver.get("https://sandbox.moodledemo.net/question/edit.php?courseid=1")
    time.sleep(1)
    # Nhập thông tin đăng nhập
    username = authen_data[0].get('username')  # Thay bằng tài khoản thật
    password = authen_data[0].get('password')  # Thay bằng mật khẩu thật
    
    # Tìm trường nhập username/password và nút đăng nhập
    self.driver.find_element(By.ID, "username").send_keys(username)  # ID của trường username
    self.driver.find_element(By.ID, "password").send_keys(password)  # ID của trường password
    
    self.driver.find_element(By.ID, "loginbtn").click()  # ID của nút đăng nhập
    
    #self.driver.get("https://sandbox.moodledemo.net/question/edit.php?courseid=1")
    time.sleep(3)
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[3]/div/section/div/div[2]/div[2]/div/div/div[1]/form/button").click()
    self.driver.find_element(By.ID, "item_qtype_truefalse").click()
    element = WebDriverWait(self.driver, 15).until(
      EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/form/div[3]/input[1]"))
    )
    element.click()
    #self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/form/div[3]/input[1]").click()
  def log_out(self):
    self.driver.find_element(By.ID, "user-menu-toggle").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(5)
  
  @pytest.mark.parametrize("name, text, default_mark, expected", get_test_data())
  def test_tC002001(self, name, text, default_mark, expected):
    self.precondition()
    # Test name: TC-002-001
    # Step # | name | target | value
    # 1 | open | https://sandbox.moodledemo.net/question/bank/editquestion/question.php?courseid=1&sesskey=4P82XMX64a&qtype=truefalse&returnurl=%2Fquestion%2Fedit.php%3Fcourseid%3D1%26deleteall%3D1&courseid=1&category=2 | 
    #self.driver.get("https://sandbox.moodledemo.net/question/bank/editquestion/question.php?courseid=1&sesskey=4P82XMX64a&qtype=truefalse&returnurl=%2Fquestion%2Fedit.php%3Fcourseid%3D1%26deleteall%3D1&courseid=1&category=2")
    # 2 | click | id=id_name | 
    self.driver.find_element(By.ID, "id_name").click()
    # 3 | type | id=id_name | a
    self.driver.find_element(By.ID, "id_name").send_keys(name)
    # 4 | selectFrame | index=0 | 
    frames = None
    #i = 0
    while (frames == None or len(frames) == 0):
      #print(i)
      #i = i + 1
      frames = self.driver.find_elements(By.TAG_NAME, "iframe")
      if (len(frames) != 0): 
        if (frames[0]): self.driver.switch_to.frame(frames[0])  # Chuyển đến frame đầu tiên
      time.sleep(1)

    # 5 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 6 | editContent | id=tinymce | <p>a</p>
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("""
    if(arguments[0].contentEditable === 'true') {
        arguments[0].innerText = arguments[1];
    }""", element, text)
    # 7 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 8 | click | id=id_defaultmark | 
    self.driver.find_element(By.ID, "id_defaultmark").click()
    # 9 | type | id=id_defaultmark | 10
    # Tìm phần tử có ID là "id_defaultmark"
    element = self.driver.find_element(By.ID, "id_defaultmark")
    # Xóa nội dung trong ô
    element.clear()
    self.driver.find_element(By.ID, "id_defaultmark").send_keys(default_mark)
    # 10 | click | id=id_submitbutton | 
    self.driver.find_element(By.ID, "id_submitbutton").click()
    time.sleep(5)
    # 11 | verifyText | //*[@id="questionscontainer"]/div/span/a | Reset columns
    if (expected == "Reset columns"):
          assert self.driver.find_element(By.XPATH, "//*[@id=\"questionscontainer\"]/div/span/a").text == expected
    elif (expected == "- You must supply a value here."):
      if (name == ""): assert self.driver.find_element(By.XPATH, "//*[@id=\"id_error_name\"]").text == expected
      if (text == ""): assert self.driver.find_element(By.XPATH, "//*[@id=\"id_error_questiontext\"]").text == expected
      if (default_mark == ""): assert self.driver.find_element(By.XPATH, "//*[@id=\"id_error_defaultmark\"]").text == expected
    elif (expected == "The default mark must be positive."):
      assert self.driver.find_element(By.XPATH, "//*[@id=\"id_error_defaultmark\"]").text == expected
    elif (expected == "You must enter a number here."): assert self.driver.find_element(By.XPATH, "//*[@id=\"id_error_defaultmark\"]").text == expected
    self.log_out()