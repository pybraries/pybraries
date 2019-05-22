# set_pages.py
from requests.exceptions import HTTPError
from pybraries.helpers import sess


def set_pages(per_page=30, page=1):
    """
    Change pagination settings.

    Args:
        per_page (int): default=30 number of items per page.  max=100
        page (int): default=1 package name

    Returns:
        response (str): message with pagination information
    """

    if not all(isinstance(i, int) for i in [page, per_page]):
        raise TypeError("Must be an integer")
    if page < 1:
        raise ValueError("page must be an integer > 1")
    if per_page > 100 or per_page < 1:
        raise ValueError("perpage must be an integer between 1 and 100, inclusive")

    sess.params["page"] = page  # 1 returns page 1 of results, 2 returns page 2, etc.
    sess.params["per_page"] = per_page  # 30 is libraries api default, max is 100

    return f"per_page set to {per_page} and page set to {page}."
