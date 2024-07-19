import pytest
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def setup_module(module):
    print("setup_module")

def teardown_module(module):
    print("teardown_module")

def setup_function(function):
    print("setup_function")

def teardown_function(function):
    print("teardown_function")

def test_0():
    print("test_0")

def test_1():
    print("test_1")


class TestClass:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")


    def setup_method(self, method):
        print("setup_method")

    def teardown_method(self, method):
        print("teardown_method")

    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")


if __name__ == "__main__":
    pytest.main(['-s','test_setup_teardown_demo.py'])