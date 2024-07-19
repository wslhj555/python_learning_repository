from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# 指定 Hub 地址
hub_url = 'http://localhost:4444/wd/hub'

# 运行 Chrome 测试

chrome_options = Options()
chrome_options.add_argument('--start-maximized')  # 可以根据需要添加其他选项

desired_capabilities = DesiredCapabilities.CHROME.copy()

driver = webdriver.Remote(command_executor=hub_url,
                          options=chrome_options)

driver.get('http://www.baidu.com')
print(driver.title)
driver.quit()


# 运行 Firefox 测试
firefox_options = FirefoxOptions()
driver = webdriver.Remote(command_executor=hub_url,
                          options=firefox_options)
driver.get('https://www.selenium.dev/support/')
print(driver.title)
driver.quit()


