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
pkg2 = 'yellowbrick'                       # package name
provider = 'github'                        # host name
username = 'discdiver'                     # github username
username2 = 'jakevdp'                      # github username
owner = 'notebooktoall'                    # github repo owner
repo = 'notebooktoall'                     # repository name
owner2 = 'pandas-dev'                      # github repo owner
repo2 = 'pandas'                           # repository name
repo3 = 'scikit-learn'                     # repo name

# Integration tests

# Platforms functionality
def test_platforms():
    """returns a list of platforms whose name includes 'Go'"""
    all_platforms = api.platforms()
    assert all_platforms[0]['name'] == 'Go'

# Project functionality

def test_project_args():
    """returns a dict with correct package name"""
    pack = api.project(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_kwargs():
    """using kwargs - returns a dict with correct package name"""
    packs = api.project(manager="pypi", package="plotly")
    assert packs['name'] == 'plotly'

def test_project_dependencies():
    """returns a dict with correct package name"""
    pack = api.project_dependencies(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_dependents():
    """returns a dict with correct package name """
    packer = api.project_dependents(mgr, pkg)
    assert packer['name'] == 'plotly' 

def test_project_dependent_repositories():
    """returns a dict with correct package name"""
    pack = api.project_dependent_repositories(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_contributors():
    """returns a list item with a github_id >0 """
    pack = api.project_contributors(mgr, pkg2)
    assert float(pack[0]['github_id']) > 0

def test_project_sourcerank():
    """returns a dict with a package with basic_info_present key"""
    pack = api.project_sourcerank(mgr, pkg2)
    assert pack['basic_info_present'] >= 0

def test_project_usage():
    """returns a dict with a project usage score list item"""
    pack = api.project_usage(mgr, pkg2)
    assert pack['*'] >= 0

def test_project_search():
    """Project search returns a project list item with a name key"""
    projects = api.project_search()
    assert 'name' in projects[0].keys()

def test_project_search():
    """Project search with kwargs for vizualization keyword filter 
    and sort stars returns top visualization project list item with a name key"""
    projects = api.project_search(sort='stars', keywords='visualization')
    assert 'name' in projects[0].keys()

# Repository functionality

def test_repository():
    """returns a project with github_id from github"""
    repos = api.repository(provider, owner, repo)
    assert repos['github_id'] in repos.values() 

def test_repository_dependencies():
    """returns a project with full_name in keys"""
    repo_deps = api.repository_dependencies(provider, owner2, repo2)
    assert "full_name" in repo_deps.keys()

def test_repository_projects():
    """returns a project with name in keys"""
    repo_projs = api.repository_projects(provider, owner2, repo2)
    assert "name" in repo_projs[0].keys()

# User functionality

def test_user():
    """returns a repo with correct login name"""
    users = api.user(provider, username)
    assert users['login'] == "discdiver"

def test_user_repositories():
    """returns a repo in a list item with size > 0"""
    user_repos = api.user_repositories(provider, username)
    assert user_repos[0]['size'] > 0

def test_user_packages():
    """returns a package with rank >= 0"""
    user_pkgs = api.user_packages(provider, username2)
    assert user_pkgs[0]['rank'] >= 0

def test_user_packages_contributions():
    """returns a project in a list item with stars >=0"""
    user_package_contribs = api.user_packages_contributions(provider, username)
    assert user_package_contribs[0]['stars'] >= 0

def test_user_repository_contributions():
    """returns a project in a list item a size >= 0"""
    user_repo_contribs = api.user_repository_contributions(provider, username)
    assert user_repo_contribs[0]['size'] >= 0

def test_user_dependencies():
    """returns a project in a list item with a rank >= 0"""
    user_deps = api.user_dependencies(provider, username)
    assert user_deps[0]['rank'] >= 0


# first need to subscribe the user to package updates
# my api key is subscribed, so will work for travis tests
# won't pass locally if user's api_key isn't subscribed to any packages
def test_list_subscriptions():
    """for api key sent- returns a list item subscription with a project rank >= 0"""
    subs = api.list_subscriptions()
    assert subs[0]['project']['rank'] >= 0

def test_check_subscribed():
    """for api key sent - check if user is subscribed to a project with a rank >= 0"""
    check_sub = api.check_subscribed(mgr, repo3)
    assert check_sub['project']['rank'] >= 0

# feature implemented and checked manually
# need test
# unsubscribe after? mock?
@pytest.mark.skip()
def test_subscribe():
    """for api key sent- use args to check if subscribed"""
    sub = api.subscribe(mgr, repo2)
    assert sub['project']['rank'] >= 0

# feature implemented and checked manually
# need test
# unsubscribe after? mock?
@pytest.mark.skip()
def test_subscribe_kwargs():
    """for api key sent- use kwargs to check if subscribed"""
    sub = api.subscribe(manager=mgr, package=repo2)
    assert sub['project']['rank'] >= 0

# make sure include_prerelease is set to true before
@pytest.mark.skip()
def test_update_subscription():
    """for api key sent- change subscription for prerelease to false"""
    update = api.update_subscription(mgr, repo2, False)
    assert update['include_prerelease'] == False

@pytest.mark.skip()
def test_unsubscribe():
    """for api key sent- unsubscribe from package"""
    del_sub = api.unsubscribe(mgr, repo2)
    # check and make sure not subscribed
    pass

@pytest.mark.skip()
def test_unsubscribe():
    """for api key sent- if not subscribed, return not subscribed message """
    del_sub = api.unsubscribe(mgr, repo2)
    # check stdout contains "not subscribed"
    pass
