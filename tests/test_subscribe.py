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
    """for subscriber- returns a list item with a project rank >= 0"""
    sub = subs.list_subscribed()
    assert sub[0]["project"]["rank"] >= 0


def test_check_subscribed():
    """check if returns a boolean if check_subscribed to a package"""
    check_sub = subs.check_subscribed(mgr, repo3)
    assert type(check_sub) is bool


# feature implemented and checked manually
# need test
# unsubscribe after? mock?
@pytest.mark.skip()
def test_subscribe():
    """for subscribe key sent- use args to check if subscribed"""
    sub = subs.subscribe(mgr, repo2)
    assert sub["project"]["rank"] >= 0


# feature implemented and checked manually
# need test
# unsubscribe after? mock?
@pytest.mark.skip()
def test_subscribe_kwargs():
    """for api key sent- use kwargs to check if subscribed"""
    sub = subs.subscribe(manager=mgr, package=repo2)
    assert sub["project"]["rank"] >= 0


@pytest.mark.skip()
def test_update_subscribe():
    """for api key sent- doesn't error"""
    update = subs.update_subscribe(mgr, repo2)
    pass


# make sure include_prerelease is set to true prior
@pytest.mark.skip()
def test_update_subscribe_updates():
    """for api key sent- change subscription for prerelease to false"""
    update = subs.update_subscribe(mgr, repo2, False)
    assert update["include_prerelease"] is False


def test_unsubscribe_kwargs():
    """for api key sent- doesn't error for kwargs"""
    del_sub = subs.unsubscribe(manager=mgr, package=repo2)


@pytest.mark.skip()
def test_unsubscribe_args():
    """for api key sent- doesn't error for args"""
    del_sub = subs.unsubscribe(mgr, repo2)
    pass


@pytest.mark.skip()
def test_unsubscribe_unsubscribes():
    """for api key sent- unsubscribe from package"""
    del_sub = subs.unsubscribe(mgr, repo2)
    # check and make sure not subscribed
    pass
