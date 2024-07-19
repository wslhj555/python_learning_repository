from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import string
import random
from selenium import webdriver
import pyautogui
import time
import os
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class TestUserRegister:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/register")
        self.driver.implicitly_wait(10)
    
    def test_user_name(self,username,email,password,confirm_password):
        ele_user_input= self.driver.find_element_by_xpath("//input[@name='username']")
        ele_user_input.send_keys(username)
        time.sleep(1)
        assert ele_user_input.get_attribute("value") == username
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == "Username is none"
        alert.accept()
        pass



