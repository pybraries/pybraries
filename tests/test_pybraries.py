"""Tests for `pybraries` package."""
import pytest
import os
from pybraries import Api

api_key = os.environ['LIBRARIES_API_KEY']
# api_key for libraries.io

mgr = "pypi"
# package manager name

pkg = "plotly"
# package name

api = Api()

# Integration tests
def test_project():
    """Correct package returned"""
    pack = api.project(mgr, pkg)
    assert pack['name'] == 'plotly'


def test_platforms():
    """Go in returned platforms"""
    all_platforms = api.platforms()
    assert all_platforms[0]['name'] == 'Go'



# Unit tests
