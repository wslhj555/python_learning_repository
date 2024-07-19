import logging.handlers
import datetime
import os
import sys
import pytest
import unittest




os.chdir(os.path.abspath(os.path.dirname(__file__)))
list_0 = [(1, 2, True), (1, 3, True), (1, 4, True),(0,1,True)]

'''class TestAdd(unittest.TestCase):

    def setUp(self):
        # 设置测试环境
        print("Setting up the test environment")

    def tearDown(self):
        # 清理测试环境
        print("Cleaning up the test environment")

    def test_add(self, x, y, expected):
        # 模拟登录逻辑
        if x + y < 4:
            result = True
        else:
            result = False
        self.assertEqual(result, expected)


@pytest.mark.parametrize("x, y, expected", list_0)
def test_add_wrapper(x, y, expected):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(TestAdd('test_add', x=x, y=y, expected=expected))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    assert result.wasSuccessful()

if __name__ == '__main__':
    pytest.main()'''


def logging_record():
    import logging


    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


    demo_handler = logging.handlers.TimedRotatingFileHandler(
        filename='./logs/logging_demo_0.log', when='D', interval=1, backupCount=7)
    demo_handler.setLevel(logging.DEBUG)
    demo_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'))

    error_handler = logging.FileHandler(filename='./logs/error_0.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(demo_handler)
    logger.addHandler(error_handler)
    return logger


logger_test_add = logging_record()

class TestAdd:

    @pytest.mark.parametrize("x,y,expected", list_0)
    def test_add(self,x,y,expected):
            if x+y<4:   
                result=True
               
            else:
                result=False
            logger_test_add.debug(
                    f"x+y={x+y}, expected={expected}, result={result},judge={result==expected}")
            assert result==expected

if __name__ == '__main__':
    pytest.main(['-s','-v','test_add.py'])