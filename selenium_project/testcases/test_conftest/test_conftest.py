import pytest


def test_conftest(start_up):
    print('test_conftest')


if __name__ == '__main__':
    pytest.main(['-sv', r'.\testcases\test_conftest\test_conftest.py'])

