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

def test_project_dependencies():
    pack = api.project_dependencies(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_dependents():
    packer = api.project_dependents(mgr, pkg)
    assert packer['name'] == 'plotly' 

def test_project_dependent_repositories():
    pack = api.project_dependent_repositories(mgr, pkg)
    assert pack['name'] == 'plotly' 

def test_project_contributors():
    pack = api.project_contributors(mgr, pkg2)
    assert float(pack[0]['github_id']) > 0

def test_project_sourcerank():
    pack = api.project_sourcerank(mgr, pkg2)
    assert pack['basic_info_present'] >= 0

def test_project_usage():
    pack = api.project_usage(mgr, pkg2)
    assert pack['*'] >= 0

def test_project_search():
    projects = api.project_search()
    assert 'name' in projects[0].keys()

def test_project_search():
    projects = api.project_search(sort='stars', keywords='visualization')
    assert 'name' in projects[0].keys()

# Repository functionality

def test_repository():
    repos = api.repository(provider, owner, repo)
    assert repos['github_id'] in repos.values() 

def test_repository_dependencies():
    repo_deps = api.repository_dependencies(provider, owner2, repo2)
    assert "full_name" in repo_deps.keys()

def test_repository_projects():
    repo_projs = api.repository_projects(provider, owner2, repo2)
    assert "name" in repo_projs[0].keys()

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
def test_list_subscriptions():
    user_subs = api.list_subscriptions()
    assert user_subs[0]['project']['rank'] >= 0

def test_check_subscribed():
    check_sub = api.check_subscribed(mgr, repo3)
    assert check_sub['project']['rank'] >= 0

# unsubscribe after? mock?
@pytest.mark.skip()
def test_subscribe():
    sub = api.subscribe(mgr, repo2)
    assert sub['project']['rank'] >= 0

@pytest.mark.skip()
def test_update_subscription():
    pass

@pytest.mark.skip()
def test_unsubscribe():
    pass
# Unit tests
