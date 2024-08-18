import os
import time
'''# 获取系统环境变量字典
env_vars = os.environ

# 打印所有环境变量及其值
for key, value in env_vars.items():
    print(key,value)'''


from selenium import webdriver

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开一个网页
driver.get('https://www.baidu.com')
time.sleep(3)

# 获取当前窗口的句柄
current_handle = driver.current_window_handle
print(f"当前窗口的句柄是: {current_handle}")

# 打开一个新窗口或新标签页
driver.execute_script("window.open('https://www.baidu.com', '_blank');")
time.sleep(3)
# 获取所有窗口的句柄
all_handles = driver.window_handles
print(f"所有窗口的句柄是: {all_handles}")

# 切换到新窗口
driver.switch_to.window(all_handles[-1])
time.sleep(3)

# 获取新窗口的句柄
new_handle = driver.current_window_handle
print(f"新窗口的句柄是: {new_handle}")

driver.switch_to.window(current_handle)
time.sleep(3)

# 关闭浏览器
driver.quit()


current_working_directory = os.getcwd()
print(f"当前工作目录是: {current_working_directory}")
