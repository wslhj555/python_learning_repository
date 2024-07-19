import logging
import pytest
import logging.handlers
import datetime
import os
import sys
import pytest
import unittest


os.chdir(os.path.abspath(os.path.dirname(__file__)))

# 获取或创建 logger_test_add
logger_test_add = logging.getLogger('test_add')
logger_test_add.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG
handler = logging.StreamHandler()  # 可以添加文件处理器等
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger_test_add.addHandler(handler)

list_0 = [(1, 2, True), (1, 3, True), (1, 4, True)]


class TestAdd:

    @pytest.mark.parametrize("x,y,expected", list_0)
    def test_add(self, x, y, expected):
        if x + y < 4:
            result = True
            logger_test_add.debug(
                f"x+y={x+y}, expected={expected}, result={result}")
        else:
            result = False
        assert result == expected


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_add.py'])
