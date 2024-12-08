import json
from selenium.webdriver.common.by import By
import time

class TestAutomationHelper:
    def __init__(self, driver):
        self.driver = driver

    def load_actions(self, file_path):
        """
        Load actions from the JSON file.
        """
        with open(file_path, 'r') as file:
            actions = json.load(file)
        return actions

    def execute_action(self, action_name, file_path, data=None):
        """
        Execute steps for a given action_name.
        :param action_name: The name of the action to execute.
        :param file_path: Path to the JSON configuration file.
        :param data: Dictionary of dynamic data to be used in steps (optional).
        """
        actions = self.load_actions(file_path)
        action = next((a for a in actions if a['action_name'] == action_name), None)
        
        if not action:
            raise ValueError(f"Action '{action_name}' not found in {file_path}")

        for step in action['steps']:
            method = step.get('method')
            value = step.get('value')
            action_type = step.get('action')
            step_data = step.get('data')

            # Map the method to Selenium's By class
            locator = getattr(By, method, None) if method else None

            # Perform the action based on the action type
            if action_type == "get":
                self.driver.get(step_data)
                time.sleep(2)  # Wait for the page to load

            elif action_type == "click" and locator and value:
                self.driver.find_element(locator, value).click()
                time.sleep(1)  # Optional: Wait for UI to respond

            elif action_type == "send_keys" and locator and value:
                # Replace placeholder data if provided
                send_data = data.get(step_data) if data and step_data in data else step_data
                self.driver.find_element(locator, value).send_keys(send_data)
            
            else:
                raise ValueError(f"Unsupported action type '{action_type}' or missing parameters.")