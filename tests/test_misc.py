""" test_misc.py miscellaneous tests '"""
import pytest
from pybraries import Search
from pybraries import set_pages

# variables for testing
# put in fixture
search = Search()  # instantiate search api object

# API key check
@pytest.mark.skip()
def test_api_key_missing_msg():
    """if api key doesn't exist, message to get is returned'"""
    # temporarily set api key env var to None
    # attempt to instatiate api object
    # assert libraries.io in stdout
    pass


def test_set_pages_page_return_type():
    """call to set_pages returns a string"""
    set_p = set_pages(page=1)
    assert type(set_p) is str


def test_set_pages_big_value():
    """set_pages returns a value error for large page argument"""
    with pytest.raises(ValueError):
        set_p = set_pages(per_page=101)
