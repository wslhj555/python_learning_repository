from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

'''driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
input_0 = driver.find_element('xpath', '//*[@id="kw"]')
input_0.send_keys('selenium')
click_0 = driver.find_element('xpath', '//*[@id="su"]')
click_0.click()
time.sleep(5)
driver.quit()'''

chromedriver_path = 'chromedriver.exe'
if os.path.exists(chromedriver_path):
    print('ok')
else:
    print('chromedriver not found')

print(os.environ['PATH'])