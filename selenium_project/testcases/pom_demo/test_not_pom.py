from selenium import webdriver
import unittest
import time

class TestBaidu(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    
    
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
