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
def test_project_args():
    """Correct package returned with positional args"""
    pack = api.project(mgr, pkg)
    assert pack['name'] == 'plotly'

def test_project_kwargs():
    """Correct package returned with kwargs"""
    packs = api.project(manager="pypi", package="plotly")
    assert packs['name'] == 'plotly'

def test_platforms():
    """Go in returned platforms"""
    all_platforms = api.platforms()
    assert all_platforms[0]['name'] == 'Go'



# Unit tests
