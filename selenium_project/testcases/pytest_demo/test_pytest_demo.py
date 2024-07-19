import pytest
import os
from selenium import webdriver
import time


class TestPytestDemo:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com/')
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.quit()

    @pytest.mark.do
    def test_01_add_two_numbers(self):
        assert 2 + 2 == 4
        print('this is test_01')

    @pytest.mark.undo
    def test_02(self):
        print("This is test_02")


if __name__ == '__main__':
    # os.chdir(
    # 'D:\\python_learning_program\\pythonProject\\selenium_project\\testcases\\pytest_project')
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    # pytest.main(['-s','-v','test_pytest_demo.py::TestPytestDemo::test_02'])
    # pytest.main(['-s','-k','test_02','test_pytest_demo.py'])
    pytest.main(['-s', '-m', 'undo', 'test_pytest_demo.py'])
