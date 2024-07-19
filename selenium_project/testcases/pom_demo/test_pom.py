from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class BaiduPage:
    def __init__(self): 
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.element_input=(By.ID,'kw')
        self.element_button=(By.ID,'su')
    def open_baidu(self,url):
        self.driver.get(url)
    def search_input(self):
        self.open_baidu('https://www.baidu.com/')
        self.driver.find_element(*self.element_input).send_keys('selenium')
        self.driver.find_element(*self.element_button).click()
        time.sleep(3)

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.baidu=BaiduPage()
    def test_search_input(self):
        self.baidu.search_input()
        print('testing')
        print(self.baidu.element_input)
        print(self.baidu.element_button)
        print(self.baidu.driver)
    def tearDown(self):
        self.baidu.driver.quit()

if __name__=='__main__':
    unittest.main()