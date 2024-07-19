import pytest
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="function")
def setup():
    print("setup go ")
    yield
    print("teardown  over")


@pytest.mark.dependency()
def test_base_on():
    print("base_on")
    assert True


@pytest.mark.dependency(depends=["test_base_on"])
def test_case3(setup):
    print("test case3")
    assert True


if __name__ == "__main__":
    pytest.main(["-sv", "test_dependency_0.py"])
