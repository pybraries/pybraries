# pagination.py
from pybraries.helpers import sess

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 30


def fix_pages(page=None, per_page=None):
    """
    Change pagination settings.
    :arg
        per_page (int): (optional) use this value instead of current session params
        page (int): (optional) use this value instead of current session params

    Returns:
        valid_values_range (bool): page and per_page values within valid range
    """
    try:
        page = sess.params["page"] if page is None else page
    except KeyError:
        page = DEFAULT_PAGE
    try:
        per_page = sess.params["per_page"] if per_page is None else per_page
    except KeyError:
        per_page = DEFAULT_PER_PAGE

    sess.params["page"] = max(page, 1)  # Min value is 1
    sess.params["per_page"] = min(max(per_page, 1), 100)  # Values between 1 and 100

    valid_values_range = sess.params["page"] == page and sess.params["per_page"] == per_page
    return valid_values_range
