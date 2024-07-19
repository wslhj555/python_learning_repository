import os
import pytest
import unittest

os.os.chdir(os.path.abspath(os.path.dirname(__file__)))


class TestLogin(unittest.TestCase):

    def setUp(self):
        # 设置测试环境
        print("Setting up the test environment")

    def tearDown(self):
        # 清理测试环境
        print("Cleaning up the test environment")

    @pytest.mark.parametrize("username, password, expected", [
        ("user1", "pass1", True),
        ("user2", "pass2", False),
        ("user3", "pass3", True),
    ])
    def test_login(self, username, password, expected):
        # 模拟登录逻辑
        print(f"Testing login with username: {username}, password: {password}")
        result = self.authenticate(username, password)
        self.assertEqual(result, expected)

    def authenticate(self, username, password):
        # 模拟认证逻辑
        if username == "user1" and password == "pass1":
            return True
        elif username == "user3" and password == "pass3":
            return True
        else:
            return False


if __name__ == '__main__':
    pytest.main()
