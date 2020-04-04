""" test_pagination.py miscellaneous tests '"""
import pytest

from pybraries import fix_pages
from pybraries.helpers import sess, clear_params


@pytest.fixture
def clear_sess_params():
    clear_params()
    yield


def test_set_valid_per_pages(clear_sess_params):
    """call to fix_pages returns true for valid ranges"""

    assert fix_pages(per_page=15)
    assert sess.params["per_page"] == 15
    assert sess.params["page"] == 1


def test_set_per_pages_big_value(clear_sess_params):
    """fix_pages returns false for large per_page argument"""
    clear_params()

    assert not fix_pages(per_page=101)
    assert sess.params["per_page"] == 100
    assert sess.params["page"] == 1


def test_set_per_pages_small_value(clear_sess_params):
    """fix_pages returns false for small per_page argument"""
    clear_params()

    assert not fix_pages(per_page=0)
    assert sess.params["per_page"] == 1
    assert sess.params["page"] == 1


def test_set_valid_page(clear_sess_params):
    """call to fix_pages returns a string"""
    clear_params()

    assert fix_pages(page=1)
    assert sess.params["per_page"] == 30
    assert sess.params["page"] == 1


def test_set_pages_small_value(clear_sess_params):
    """fix_pages returns false for large page argument"""
    clear_params()

    assert not fix_pages(page=0)
    assert sess.params["per_page"] == 30
    assert sess.params["page"] == 1


def test_set_pages_big_value(clear_sess_params):
    """fix_pages returns false for large page argument"""
    clear_params()

    assert fix_pages(page=1000)
    assert sess.params["per_page"] == 30
    assert sess.params["page"] == 1000
