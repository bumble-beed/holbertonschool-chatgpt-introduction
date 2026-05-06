#!/usr/bin/python3
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TestChangeBackground(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        self.driver = webdriver.Chrome(options=options)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_button_changes_background_color(self):
        """Test that clicking the button changes the background color"""
        # Open the HTML file
        self.driver.get('file:///Users/shrtasz/Documents/repos/holbertonschool-chatgpt-introduction/debugging/change_background.html')
        
        # Get initial background color
        initial_color = self.driver.find_element(By.TAG_NAME, 'body').value_of_css_property('background-color')
        
        # Click the button
        button = self.driver.find_element(By.ID, 'colorButton')
        button.click()
        
        # Wait a bit for the change
        time.sleep(0.1)
        
        # Get new background color
        new_color = self.driver.find_element(By.TAG_NAME, 'body').value_of_css_property('background-color')
        
        # Assert that the color changed
        self.assertNotEqual(initial_color, new_color, "Background color should change after clicking the button")

if __name__ == "__main__":
    unittest.main()