import pytest
from time import sleep
from pybraries.subscribe import Subscribe


# fixture to avoid hitting rate limit
@pytest.fixture(autouse=True, scope="function")
def wait_a_sec():
    yield
    sleep(1)


# unsubscribe from pandas
@pytest.fixture
def pre_sub():
    a = Subscribe()
    a.subscribe("pypi", "pandas")


# subscribe to pandas
@pytest.fixture
def pre_unsub():
    b = Subscribe()
    b.unsubscribe("pypi", "pandas")
