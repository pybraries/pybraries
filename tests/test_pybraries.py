"""Tests for `pybraries` package."""
import pytest
import os
from pybraries import API

api_key = os.environ['LIBRARIES_API_KEY']
# api_key for libraries.io

mgr = "pypi"
# package manager name

pkg = "plotly"
# package name

api = API()
# Integration tests


def test_project(capsys):
    """Correct package name prints"""
    pack = api.project(mgr, pkg)
    # captured = capsys.readouterr()
    # assert "plotly" in captured.out
    assert pack['name'] == 'plotly'

# Unit tests
# def test_api_arg_type():
    """Raise an exception if non-string argument passed"""
 #   with pytest.raises(TypeError):
   #     __call_api(0.99, mgr, pkg)
