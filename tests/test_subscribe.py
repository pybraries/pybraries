"""Tests for `pybraries Subscribe` package."""
import pytest
import pybraries

# variables for testing
subs = pybraries.Subscribe()  # instantiate subscribe api object
mgr = "pypi"  # package manager name
repo2 = "pandas"  # repository name
repo3 = "scikit-learn"  # repo name


# first need to subscribe the user to package updates
# my search key is subscribed, so will work for travis tests
# won't pass locally for development if user search_key isn't subscribed to any packages
def test_list_subscribed():
    """for subscriber- returns a list item subscription with a project rank >= 0"""
    sub = subs.list_subscribed()
    assert sub[0]["project"]["rank"] >= 0


def test_check_subscribed():
    """for subscriber - check if user is subscribed to a project with a rank >= 0"""
    check_sub = subs.check_subscribed(mgr, repo3)
    assert type(check_sub) is bool


def test_subscribe(pre_unsub):
    """for subscribe key sent- use args to check if subscribed"""
    sub = subs.subscribe(mgr, repo2)
    assert type(sub) is str


def test_subscribe_kwargs(pre_unsub):
    """for api key sent- use kwargs to check if subscribed"""
    sub = subs.subscribe(manager=mgr, package=repo2)
    assert type(sub) is str


@pytest.mark.skip()
def test_update_subscribe():
    """for api key sent- doesn't error"""
    update = subs.update_subscribe(mgr, repo2)
    pass


@pytest.mark.skip()
def test_update_subscribe_updates():
    """for api key sent- change subscription for prerelease to false"""
    update = subs.update_subscribe(mgr, repo2, False)
    assert update["include_prerelease"] is False


def test_unsubscribe_kwargs(pre_sub):
    """for api key sent- doesn't error for kwargs"""
    del_sub = subs.unsubscribe(manager=mgr, package=repo2)
    assert del_sub == "successfully unsubscribed"


def test_unsubscribe_intercept(pre_unsub):
    """returns no unsubscribe needed if not subscribed"""
    del_sub = subs.unsubscribe(manager=mgr, package=repo2)
    assert "Unsubscribe unnecessary" in del_sub


# slow
def test_unsubscribe_args(pre_sub):
    """for api key sent- doesn't error if not already subscribed"""
    del_sub = subs.unsubscribe(mgr, repo2)
    assert del_sub == "successfully unsubscribed"


def test_unsubscribe_works():
    """unsubscribes and verifies"""
    del_sub = subs.unsubscribe(mgr, repo2)
    bsub = subs.check_subscribed(mgr, repo2)
    assert bsub is False
