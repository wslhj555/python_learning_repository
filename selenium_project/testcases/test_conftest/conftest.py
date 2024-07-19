import pytest



@pytest.fixture(scope="session")
def start_up():
    print("Start up")
    yield
    print("Shut down")

