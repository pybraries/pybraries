"""Tests for `pybraries` Search class."""
import pytest
import pybraries
from time import sleep

# variables for testing
# put in fixture
search = pybraries.Search()  # instantiate search api object
mgr = "pypi"  # package manager name
pkg = "plotly"  # package name
pkg2 = "yellowbrick"  # package name
host = "github"  # host name
username = "discdiver"  # github username
username2 = "jakevdp"  # github username
owner = "notebooktoall"  # github repo owner
repo = "notebooktoall"  # repository name
owner2 = "pandas-dev"  # github repo owner
repo2 = "pandas"  # repository name
repo3 = "scikit-learn"  # repo name


# Integration tests
# Platforms functionality
def test_platforms():
    """returns a list of platforms whose name includes 'Go'"""
    all_platforms = search.platforms()
    assert all_platforms[0]["name"] == "Go"


# Project functionality
def test_project_args():
    """returns a dict with correct package name"""
    pack = search.project(mgr, pkg)
    assert pack["name"] == "plotly"


def test_project_kwargs():
    """using kwargs - returns a dict with correct package name"""
    packs = search.project(manager="pypi", package="plotly")
    assert packs["name"] == "plotly"


def test_project_dependencies():
    """returns a dict with correct package name"""
    pack = search.project_dependencies(mgr, pkg)
    assert pack["name"] == "plotly"


def test_project_dependents():
    """returns a dict with correct package name """
    packer = search.project_dependents(mgr, pkg)
    assert packer["name"] == "plotly"


def test_project_dependent_repositories():
    """returns a dict with correct package name"""
    pack = search.project_dependent_repositories(mgr, pkg2)
    assert pack["name"] == "yellowbrick"


def test_project_contributors():
    """returns a list item with a github_id >0 """
    pack = search.project_contributors(mgr, pkg2)
    assert float(pack[0]["github_id"]) > 0


def test_project_sourcerank():
    """returns a dict with a package with a basic_info_present key"""
    pack = search.project_sourcerank(mgr, pkg2)
    assert pack["basic_info_present"] >= 0


def test_project_usage():
    """returns a dict with a project usage list item"""
    pack = search.project_usage(mgr, pkg2)
    assert pack["*"] >= 0


def test_project_search():
    """Project search returns a project list item with a name key"""
    projects = search.project_search()
    assert "name" in projects[0].keys()


def test_project_search_with_kwargs():
    """Project search with kwargs for vizualization 
    and sort stars returns project with visualization as keyword"""
    projects = search.project_search(
        sort="stars", filters=dict(keywords="visualization", manager="pypi")
    )
    assert "visualization" in projects[0]["keywords"]


# Repository functionality


def test_repository():
    """returns a project with github_id from github"""
    repos = search.repository(host, owner, repo)
    assert repos["github_id"] in repos.values()


def test_repository_dependencies():
    """returns a project with full_name in keys"""
    repo_deps = search.repository_dependencies(host, owner2, repo2)
    assert "full_name" in repo_deps.keys()


def test_repository_projects():
    """returns a project with name in keys"""
    repo_projs = search.repository_projects(host, owner2, repo2)
    assert "name" in repo_projs[0].keys()


# User functionality


def test_user():
    """returns a repo with correct login name"""
    users = search.user(host, username)
    assert users["login"] == "discdiver"


def test_user_repositories():
    """returns a repo in a list item with size > 0"""
    user_repos = search.user_repositories(host, username)
    assert user_repos[0]["size"] > 0


def test_user_packages():
    """returns a package with rank >= 0"""
    user_pkgs2 = search.user_packages(host, "wesm")
    assert user_pkgs2[0]["rank"] >= 0


def test_user_packages_contributions():
    """returns a project in a list item with stars >=0"""
    user_package_contribs = search.user_packages_contributions(host, username)
    assert user_package_contribs[0]["stars"] >= 0


def test_user_repository_contributions():
    """returns a project in a list item a size >= 0"""
    user_repo_contribs = search.user_repository_contributions(host, username)
    assert user_repo_contribs[0]["size"] >= 0


def test_user_dependencies():
    """returns a project in a list item with a rank >= 0"""
    user_deps = search.user_dependencies(host, username2)
    assert user_deps[0]["rank"] >= 0
