import unittest
from selenium import webdriver
import time
import os
from  selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class  MyTestDemo(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.get("https://www.baidu.com")
        cls.driver.implicitly_wait(10)  # 设置隐式等待时间
        cls.driver.maximize_window()
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        print("tearDownClass")


    def setUp(self) -> None:
        #return super().setUp()
        print("setUp")

    def tearDown(self) -> None:
        # return super().tearDown()
        print("tearDown")

    def test_case0(self):
        print("test_case0")
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys("python")
        self.driver.find_element('xpath', '//*[@id="su"]').click()
        WebDriverWait(self.driver,10).until(EC.title_contains("python"))
        self.assertEqual(self.driver.title,"python - 百度搜索")

    def test_case1(self):
        print("test_case1")
        self.assertGreater(2,1)


  






if __name__ == '__main__':
    #unittest.main()
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    path=os.path.dirname(os.path.abspath(__file__))
    #suite.addTest(loader.loadTestsFromTestCase(MyTestDemo))
    #suite.addTest(loader.loadTestsFromModule(MyTestDemo))
    #suite.addTest(loader.discover(path,pattern='test*.py'))
    suite.addTest(loader.discover(path))

    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
