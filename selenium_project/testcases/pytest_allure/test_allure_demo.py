import pytest
import allure
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="module")
def setup():
    print("Setting up the test")

@allure.step("Step 1")
def test_step1():
    print("Step 1")
    assert 1 == 1

@allure.step("Step 2")
def test_step2():
    print("Step 2")
    assert 2 == 2

@allure.feature("编辑页面")
class TestEditPage:
    @allure.story("这是一个测试用例")
    def test_1(self, setup): 
        test_step1()
        test_step2()    
        print("Test 1")


    @allure.story("这是一个测试用例")
    def test_2(self, setup): 
        print("Test 2") 



if __name__ == '__main__':
    pytest.main(
        
        ["--alluredir", "./allure_reports", '-sv', "test_allure_demo.py"])
         #$env:PATH += ";C:\path\to\allure\bin"
     
