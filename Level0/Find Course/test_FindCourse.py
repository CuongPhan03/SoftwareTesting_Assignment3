# Generated by Selenium IDE
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

class TestFindCourse():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.set_window_size(800, 800)
    self.driver.get('https://sandbox.moodledemo.net/login/index.php')    
    self.driver.find_element(By.ID, "username").send_keys('teacher')
    self.driver.find_element(By.ID, "password").send_keys('sandbox24')
    self.driver.find_element(By.ID, "loginbtn").click()

  def teardown_method(self, method):
    self.driver.find_element(By.ID, "user-menu-toggle").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
    self.driver.quit()

  
  def test_tC003001(self):
    try: 
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("cour")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      course2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[2]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      assert course2.text == "My second course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 2)
      return True
    except Exception as e:
      return False

  def test_tC003002(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("My first course")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 1)
      return True
    except Exception:
      return False

  def test_tC003003(self):
    try: 
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("My")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      course2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[2]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      assert course2.text == "My second course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 2)
      return True
    except Exception:
      return False

  def test_tC003004(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("blank")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      course2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[2]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      assert course2.text == "My second course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 2)
      return True
    except Exception:
      return False

  def test_tC003005(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("my First course")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 1)
      return True
    except Exception:
      return False

  def test_tC003006(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      course2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[2]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      assert course2.text == "My second course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 2)
      return True
    except Exception:
      return False

  def test_tC003007(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("     My first course")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='card-deck']/div[1]/div/div/div/div/a/span[3]/span[1]")))
      assert course1.text == "My first course"
      course_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".coursename"))
      assert(course_count == 1)
      return True
    except Exception:
      return False

  def test_tC003008(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("#@1")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='paged-content-page']/div/p")))
      assert message.text == "No courses"
      return True
    except Exception:
      return False

  def test_tC003009(self):
    try:
      self.driver.get("https://sandbox.moodledemo.net/my/courses.php")
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("My third course")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      time.sleep(3)
      wait = WebDriverWait(self.driver, 20)
      message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-region='paged-content-page']/div/p")))
      assert message.text == "No courses"
      return True
    except Exception:
      return False

  def run(self):
    self.setup_method(None)

    test_list = [
      self.test_tC003001,
      self.test_tC003002,
      self.test_tC003003,
      self.test_tC003004,
      self.test_tC003005,
      self.test_tC003006,
      self.test_tC003007,
      self.test_tC003008,
      self.test_tC003009
    ]

    results = [test() for test in test_list]

    fail_test_names = []
    for i in range(0, len(results)):
      if not results[i]:
        fail_test_names.append(test_list[i].__name__)

    fail_test_str = ("FAILED:\n\t" + "\n\t".join(name for name in fail_test_names) + "\n") if len(fail_test_names) > 0 else ""
    print(f"\n-- Test Find Course (Level 0) --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")
    
    self.teardown_method(None)

TestFindCourse().run()
