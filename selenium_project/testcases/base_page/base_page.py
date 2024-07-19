from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def input_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)
    
    def click_element(self, *locator):
        self.get_element(*locator).click()

    def get_title(self):
        return self.driver.title

class BaiduPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        driver.get("https://www.baidu.com")

    def test_search(self):
        locator_kw=(By.ID, "kw")
        self.input_text("selenium",*locator_kw)
        locator_su = (By.ID, "su")
        self.click_element(*locator_su)

if __name__=='__main__':
    baiduPage=BaiduPage(webdriver.Chrome())
    baiduPage.test_search() 
