import pytest
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture()
def my_fixture():
    # 初始化代码
    print("Initializing fixture")
    yield "some_value"  # 提供一个值给测试函数
    # 清理代码
    print("Cleaning up fixture")


def test_1(my_fixture):
    print('test_1')


def test_2(my_fixture):
    print('test_2')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_fixture.py'])
