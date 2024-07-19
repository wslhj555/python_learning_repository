import pytest
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(scope="function")
def setup():
    print("setup go ")
    yield   
    print("teardown  over")

def test_case1(setup):
    print("test case1")
    assert True

@pytest.mark.dependency()
def base_on():
    print("base_on")
    assert True



@pytest.mark.dependency(depends=["base_on"])
def test_case3(setup):
    print("test case3")
    assert True



@pytest.fixture(scope="class")
def setup_class():
    print("setup class go ")
    yield   
    print("teardown class over")


class TestClass:

    @pytest.fixture(scope="function")
    def setup_function(self):
        print("setup function go ")
        yield   
        print("teardown function over")


    def test_case4(self, setup_class, setup_function):
        print("test case4")
        assert True




if __name__ == "__main__":
    pytest.main(["-sv", "test_dependency_demo.py"])