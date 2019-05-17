"""Tests for `pybraries` package."""
import pytest
import os
from time import sleep
from pybraries import Api

# fixture to avoid rate limiting
@pytest.fixture(autouse=True, scope='function')
def wait_a_sec():
    yield
    sleep(1)

api_key = os.environ['LIBRARIES_API_KEY']  # api_key for libraries.io
api = Api()                                # instantiate object
mgr = 'pypi'                               # package manager name
pkg = 'plotly'                             # package name
provider = 'github'                        # host name
username = 'discdiver'                     # github username
username2 = 'jakevdp'                      # github username

# Integration tests

# Platforms functionality
def test_platforms():
    """Go in returned platforms"""
    all_platforms = api.platforms()
    assert all_platforms[0]['name'] == 'Go'

# Project functionality

def test_project_args():
    """Correct package returned with positional args"""
    pack = api.project(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_kwargs():
    """Correct package returned with kwargs"""
    packs = api.project(manager="pypi", package="plotly")
    assert packs['name'] == 'plotly'

# add more project functionality

@pytest.mark.skip()
def test_project_dependencies():
    pass

@pytest.mark.skip()
def test_project_dependents():
    pass

@pytest.mark.skip()
def test_project_repositories():
    pass

@pytest.mark.skip()
def test_project_contributors():
    pass

@pytest.mark.skip()
def test_project_sourcerank():
    pass

@pytest.mark.skip()
def test_project_usage():
    pass

@pytest.mark.skip()
def test_project_search():
    pass


# Repository functionality

@pytest.mark.skip()
def test_repository():
    pass

@pytest.mark.skip()
def test_repository_dependencies():
    pass

@pytest.mark.skip()
def test_repository_projects():
    pass



# User functionality
def test_user():
    users = api.user(provider, username)
    assert users['login'] == "discdiver"

def test_user_repositories():
    user_repos = api.user_repositories(provider, username)
    assert user_repos[0]['size'] > 0

def test_user_packages():
    user_pkgs = api.user_packages(provider, username2)
    assert user_pkgs[0]['rank'] >= 0

def test_user_packages_contributions():
    user_package_contribs = api.user_packages_contributions(provider, username)
    assert user_package_contribs[0]['stars'] >= 0

def test_user_repository_contributions():
    user_repo_contribs = api.user_repository_contributions(provider, username)
    assert user_repo_contribs[0]['size'] >= 0

def test_user_dependencies():
    user_deps = api.user_dependencies(provider, username)
    assert user_deps[0]['rank'] >= 0


# first need to subscribe the user to package updates
# my api key is subscribed, so will work for travis tests
# won't pass locally if user's api_key isn't subscribed to any packages
def test_user_subscriptions():
    user_subs = api.user_subscriptions()
    assert user_subs[0]['project']['rank'] >= 0

@pytest.mark.skip()
def test_subscribe():
    pass

@pytest.mark.skip()
def test_subscribed():
    pass

@pytest.mark.skip()
def test_update_subscription():
    pass

@pytest.mark.skip()
def test_unsubscribe():
    pass
# Unit tests
