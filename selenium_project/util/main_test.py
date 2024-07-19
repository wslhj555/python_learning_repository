from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if project_root not in sys.path:
    sys.path.append(project_root)
from testcases import case_0
from logs.logging_demo import logging_demo

from selenium import webdriver
import time


'''driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
expected="百度一下，你就知道"
WebDriverWait(driver,10).until(EC.title_is(expected))
driver.quit()'''

#cookie=driver.get_cookies()
#print(cookie)
#driver.quit()

#cookie_name=str(time.time())+'cookie.txt'
#cookie_path = os.path.join(project_root, 'config','cookie_testcase_0', cookie_name)
#case_0.save_cookie(driver, cookie_path)


logger=logging_demo.create_logger()
logger.info('test')
