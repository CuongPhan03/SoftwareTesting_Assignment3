# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

def drop_files(element, files, offsetX=0, offsetY=0, wait=3):
  driver = element.parent
  isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
  paths = []
  
  # ensure files are present, and upload to the remote server if session is remote
  for file in (files if isinstance(files, list) else [files]) :
    if not os.path.isfile(file) :
      raise FileNotFoundError(file)
    paths.append(file if isLocal else element._upload(file))
  
  value = '\n'.join(paths)
  elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
  elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

WebElement.drop_files = drop_files

class TestPostToForum():
  def setup_method(self, tasks):
    self.driver = webdriver.Chrome()
    for task in tasks:
      self.runTask(task)
  
  def teardown_method(self, tasks):
    for task in tasks:
      self.runTask(task)
    self.driver.quit()


  def runTask(self, task):
    wait = WebDriverWait(self.driver, 20)
    action = task["action"]
    if action in ["set_window_size", "get_url", "switch_frame", "sleep"]: 
      value = task["value"]
      if action == "set_window_size":
        self.driver.set_window_size(value[0], value[1])  
      elif action == "get_url":
        self.driver.get(value)
      elif action == "switch_frame":
        if task["value"] != None:
          self.driver.switch_to.frame(task["value"])
        else: 
          self.driver.switch_to.default_content()
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
      elif action == "drop_files":
        paths = []
        for filename in task["value"]:
          path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
          paths.append(path)
        drop_target = wait.until(EC.element_to_be_clickable((element_type, element_locator)))
        drop_target.drop_files(paths)
      elif action == "assert_text":
        element = wait.until(EC.presence_of_element_located((element_type, element_locator)))
        assert task["value"] == element.text or task["value"] in element.text
      elif action == "assert_count":
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
    print(f"\n-- Test Find Course (Level 2) --\nPASSED: {results.count(True)}/{len(results)}\n{fail_test_str}")

    self.teardown_method(data["logout"])

TestPostToForum().run('./input_PostToForum.json')
