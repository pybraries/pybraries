""" test_misc.py miscellaneous tests '"""
from time import sleep

import pytest

from pybraries import Search
from pybraries import set_pages


# fixture to avoid hitting rate limit
@pytest.fixture(autouse=True, scope="function")
def wait_a_sec():
    yield
    sleep(1)


# variables for testing
# put in fixture
search = Search()  # instantiate search api object


def test_set_pages_page_return_type():
    """call to set_pages returns a string"""
    set_p = set_pages(page=1)
    assert type(set_p) is str


def test_set_pages_big_value():
    """set_pages returns a value error for large page argument"""
    with pytest.raises(ValueError):
        set_p = set_pages(per_page=101)
