"""Tests for `pybraries` package."""
import pytest
from pybraries import wrapper

# api_key = cmdopt

# os.environ['LIBRARIES_API_KEY']

# required api_key

mgr = "pypi"
# package manager name

pkg = "plotly"
# package name

# Integration tests
def test_package_info(cmdopt, capsys):
    """Correct package name prints"""

    wrapper.package_info(cmdopt, mgr, pkg)
    captured = capsys.readouterr()
    assert "plotly" in captured.out


# Unit tests
def test_api_arg_type(cmdopt):
    """Raise an exception if non-string argument passed"""
    wrapper.__call_api(0.99, mgr, pkg)
