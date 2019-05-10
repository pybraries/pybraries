"""Tests for `pybraries` package."""
import pytest
import os

import pybraries

api_key = os.environ['LIBRARIES_API_KEY']

# required api_key

mgr = "pypi"
# package manager name

pkg = "plotly"
# package name


# Integration tests
def test_package_info(api_key, mgr, pkg):
    """Correct package name prints"""
    pybraries.package_info(pi_key, mgr, pkg)
    captured = capsys.readouterr()
    assert "plotly" in captured.out


# Unit tests
    """Raise an exception if non-string argument passed"""
    with pytest.raises(TypeError):
        pybraries.__call_api(99, mgr, pkg)
