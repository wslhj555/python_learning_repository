from selenium import webdriver
import pyautogui
import time
import os
from PIL import Image
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import random
import string
import pickle



def test_case_0():
    print('this is a test case 0')


def test_checkbox_jpress():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    driver.maximize_window()
    time.sleep(2)
    element_identify=driver.find_element('xpath','//*[@id="captcha"]')
    element_identify_pict = driver.find_element('xpath', '//*[@id="captchaimg"]')
    print(element_identify.rect,element_identify_pict.rect)
    #pyautogui.click(element_identify.rect['x']+20,element_identify.rect['y']+15)
    pyautogui.click(810, 565)
    time.sleep(2)
    input()
    driver.quit()


def get_identify_code_pricture():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    driver.maximize_window()
    screenshot_name=str(time.time())+'.png'
    screenshot_path = os.path.join(
        'D:\python_learning_program\pythonProject\selenium_project\screenshot\case_0\screen_shoot',screenshot_name)
    driver.save_screenshot(screenshot_path)
    element_identify_pict = driver.find_element('xpath', '//*[@id="captchaimg"]')
    x=element_identify_pict.rect['x']
    y=element_identify_pict.rect['y']
    w=element_identify_pict.rect['width']
    h=element_identify_pict.rect['height']
    right=x+w
    bottom=y+h
    im = Image.open(screenshot_path)
    im = im.crop((x, y, right, bottom))
    identify_picture_name=str(time.time())+'.png'
    identify_picture_path = os.path.join(
        'D:\python_learning_program\pythonProject\selenium_project\screenshot\case_0\identify_picture', identify_picture_name)
    im.save(identify_picture_path)
    
    time.sleep(2)
    driver.quit()


def read_identify_code():
    picture_path = r'D:\python_learning_program\pythonProject\selenium_project\screenshot\case_0\identify_picture\1719307064.3242185.png'
    image=Image.open(picture_path)
    code=pytesseract.image_to_string(image)
    print(code)
    
def demo_read_picture():
    picture_path = r'D:\python_learning_program\pythonProject\selenium_project\screenshot\case_0\identify_picture\1.png'
    image=Image.open(picture_path)
    code = pytesseract.image_to_string(image)
    print(code)

def create_random_str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))

def save_cookie(driver,path):
    with open(path, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookie(driver,path):
    with open(path, 'rb') as f:
        cookies = pickle.load(f)
    for cookie in cookies:  
        driver.add_cookie(cookie)


'''#0表示自主品牌，1表示外包品牌
list_techfin_0=[30,24,18,21.5,15.5,22.5,15.5,20,20]
list_techfin_1=[17.5,13.5,15.5,15.5,15,16.5,16,20,15,16,15.5,17.5]
sum_techfin_0=sum(list_techfin_0)
sum_techfin_1=sum(list_techfin_1)
average_techfin_0=sum_techfin_0/len(list_techfin_0)
average_techfin_1=sum_techfin_1/len(list_techfin_1)
print(average_techfin_0,average_techfin_1)'''



