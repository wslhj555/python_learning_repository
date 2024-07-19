from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.driver_finder import DriverFinder
import subprocess
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_demo_0():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    input_0 = driver.find_element(By.XPATH, '//*[@id="kw"]')
    input_0.send_keys('selenium')
    click_0 = driver.find_element('xpath', '//*[@id="su"]')
    click_0.click()
    time.sleep(5)
    driver.quit()


def run_driver():
    a = subprocess.Popen(['chromedriver.exe'])
    a.communicate()


class web_driver():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_demo_0(self):
        driver = self.driver
        driver.get('https://www.baidu.com/')
        input_0 = driver.find_element('xpath', '//*[@id="kw"]')
        input_0.send_keys('selenium')
        click_0 = driver.find_element('xpath', '//*[@id="su"]')
        click_0.click()
        time.sleep(5)
        driver.quit()

    def link_text(self):
        driver = self.driver
        driver.get('https://www.baidu.com/')
        input_0 = driver.find_element('xpath', '//*[@id="kw"]')
        input_0.send_keys('selenium')
        time.sleep(3)
        link_0 = driver.find_element('link text', '百度首页')
        link_0.click()
        time.sleep(3)
        driver.quit()


driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
'''print(driver.title)
print(driver.name)
print(driver.current_url)
print(driver.window_handles)'''
# driver.find_element('xpath','//*[@id="kw"]')
# driver.find_element('xpath','//*[@id="su"]')

'''time.sleep(3)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.close()
time.sleep(10) 
driver.quit()'''

'''driver.get('http://sahitest.com/demo/linkTest.htm')
element_input=driver.find_element('xpath', '//*[@id="t1"]')
element_input.send_keys('selenium')
#print(element_input.id)
#print(element_input.tag_name)
#print(element_input.text)
print(element_input.get_attribute('type'))
print(element_input.get_attribute('value'))
print(element_input.get_attribute('placeholder'))
time.sleep(2)
driver.quit()

driver.get('https://www.baidu.com/')
driver.find_element('link text','新闻').click()
time.sleep(2)
list_windows=driver.window_handles
print(list_windows)         
driver.switch_to.window(list_windows[0])
print(driver.title)
time.sleep(2)
driver.switch_to.window(list_windows[1])
print(driver.title)
time.sleep(2)
driver.quit()'''

'''path = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(path, 'test_form.html')
driver.get('file:///'+html_file)
time.sleep(2)
driver.find_element('xpath', '//*[@id="username"]').send_keys('admin')
driver.find_element('xpath', '//*[@id="password"]').send_keys('123456')
input_username_value = driver.find_element(
    'id', 'username').get_attribute('value')
input_password_value = driver.find_element(
    'id', 'password').get_attribute('value')
driver.find_element('xpath', '//*[@id="submit"]').click()
print(input_username_value, input_password_value)
time.sleep(2)
driver.switch_to.alert.accept()
driver.find_element('id', 'username').clear()
driver.find_element('id', 'password').clear()
time.sleep(2)
driver.quit()

path = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(path, 'test_form.html')
driver.get('file:///'+html_file)
input_0 = driver.find_element('xpath', '/html/body/form[1]/input[1]')
input_1 = driver.find_element('xpath', '/html/body/form[1]/input[2]')
input_2 = driver.find_element('xpath', '/html/body/form[2]/input[1]')
input_3 = driver.find_element('xpath', '/html/body/form[2]/input[2]')
input_4 = driver.find_element('xpath', '/html/body/form[1]/input[3]')
input_5 = driver.find_element('xpath', '/html/body/form[2]/input[3]')
if input_0.is_selected() or input_1.is_selected():
    pass
else:  
    input_0.click()
    input_1.click()

input_2.click()
input_3.click()
time.sleep(3)
input_4.click()
driver.switch_to.alert.accept()
input_5.click()
driver.switch_to.alert.accept()
time.sleep(3)
print([input_0.get_attribute('value'), input_1.get_attribute('value'), input_2.get_attribute('value'), input_3.get_attribute('value'), input_4.get_attribute('value'), input_5.get_attribute('value')])
driver.quit()'''


'''path = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(path, 'test_form_1.html')
driver.get('file:///'+html_file)
select_0=Select(driver.find_element('id', 'province'))'''


'''time.sleep(2)
select_0.select_by_index(2)
time.sleep(2)
select_0.select_by_value('tj')
time.sleep(2)
select_0.select_by_visible_text('shanghai')
time.sleep(2)
for i in range(len(select_0.options)):
    select_0.select_by_index(i)
    time.sleep(2)
select_0.deselect_all()
time.sleep(2)
options=select_0.options
for option in options:
    print(option.text)
    print(option.get_attribute('value'))
option_0=select_0.first_selected_option


driver.quit()   '''


'''path = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(path, 'test_form_1.html')
driver.get('file:///'+html_file)'''


'''time.sleep(2)
test_ele_0=driver.find_element('id','alert')
test_ele_1=driver.find_element('id','confirm')
test_ele_2=driver.find_element('id','prompt')'''

'''test_ele_0.click()
time.sleep(2)
alert_0=driver.switch_to.alert
print(alert_0.text)
alert_0.accept()'''

'''time.sleep(2)
test_ele_1.click()
time.sleep(2)
confirm_0=driver.switch_to.alert
print(confirm_0.text)
confirm_0.dismiss()
time.sleep(2)'''

'''test_ele_2.click()
time.sleep(2)
prompt_0=driver.switch_to.alert
print(prompt_0.text)
prompt_0.send_keys('13345678')
time.sleep(5)
prompt_0.accept()
time.sleep(2)'''


'''driver.get('https://www.baidu.com/')
wait_10=WebDriverWait(driver,10)
wait_10.until(EC.title_is('百度一下，你就知道'))
driver.implicitly_wait(10)
driver.find_element('id','kw').send_keys('selenium')
driver.find_element('id','su').click()
driver.quit()'''

'''driver.get('http://sahitest.com/demo/clicks.htm')
action_0=ActionChains(driver)
driver.maximize_window()
input_0 = driver.find_element('xpath', '/html/body/form/textarea')
double_click_0 = driver.find_element('xpath', '/html/body/form/input[2]')
right_click_0 = driver.find_element('xpath', '/html/body/form/input[4]')
#action_0.double_click(double_click_0).perform()
#time.sleep(2)
#print(input_0.get_attribute('value'))
action_0.move_to_element(right_click_0).context_click().perform()
time.sleep(2)

time.sleep(2)
driver.quit()'''

'''driver.get('https://www.baidu.com/')
action_0 = ActionChains(driver)
driver.maximize_window()
time.sleep(2)
log_in_bu = driver.find_element('xpath', '//*[@id="s-top-loginbtn"]')
action_0.move_to_element(log_in_bu).click().perform()'''

'''input_0=driver.find_element('xpath','//*[@id="kw"]')
input_0.send_keys('selenium')
time.sleep(2)
#action_0.move_to_element(input_0).click().send_keys(Keys.ENTER).perform()
#input_0.send_keys(Keys.ENTER)
input_0.send_keys(Keys.CONTROL,'a')
time.sleep(2)
input_0.send_keys(Keys.CONTROL,'x')
time.sleep(2)
input_0.send_keys(Keys.CONTROL,'v')'''


'''driver.get('https://www.baidu.com/')
action_0 = ActionChains(driver)
driver.maximize_window()
time.sleep(2)
#driver.execute_script("alert('hello world')")
#js_0 = "return document.title"
js_1='var q=document.getElementById("kw");q.style.border="1px solid red"'
#title=driver.execute_script(js_1)
input_0=driver.find_element('xpath','//*[@id="kw"]')
input_0.send_keys('selenium',Keys.ENTER)
time.sleep(2)

js_2="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js_2)

#driver.execute_script(js_1)'''


'''driver.get('https://www.baidu.com/')
driver.find_element('xpath','//*[@id="kw"]').send_keys('selenium')
driver.find_element('xpath','//*[@id="su"]').click()
time.sleep(2)
date_0=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
file_name=date_0+'.png'
screenshot_path=os.path.abspath('my_pricture')
print(screenshot_path)
picture_path=os.path.join(screenshot_path,file_name)
print(picture_path)
driver.get_screenshot_as_file(picture_path)
time.sleep(3)
driver.quit()'''


'''driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element('xpath', '//*[@id="kw"]').send_keys('selenium')
driver.find_element('xpath', '//*[@id="su"]').click()
time.sleep(2)
# date_0 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
# file_name = '1.png'
# 使用相对路径
# screenshot_path = os.path.dirname(os.path.abspath(__file__))
# print(screenshot_path)
# picture_path = os.path.join(screenshot_path, file_name)
# print(picture_path)
picture_path = './'+'2.png'
driver.get_screenshot_as_file(picture_path)
time.sleep(3)
driver.quit()'''


#print(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
#print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


#w_w199606

driver.get('http://sahitest.com/demo/framesTest.htm')
time.sleep(2)
#element_0 = driver.find_element('xpath', '/html/body/table/tbody/tr/td[1]/a[1]')
#element_0.click()
#time.sleep(2)
first_frame = driver.find_element('name', 'top')
driver.switch_to.frame(first_frame)
element_1 = driver.find_element('xpath', '/html/body/table/tbody/tr/td[1]/a[1]')
element_1.click()
time.sleep(2)
driver.switch_to.default_content()
second_frame = driver.find_element('xpath', '/html/frameset/frame[2]')
driver.switch_to.frame(second_frame)
element_2 = driver.find_element('xpath', '/html/body/table/tbody/tr/td[1]/a[1]')
element_2.click()
time.sleep(3)
driver.quit()


