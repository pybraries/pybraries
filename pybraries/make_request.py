from requests.exceptions import HTTPError

from pybraries.pagination import fix_pages
from pybraries.helpers import sess, clear_params


def make_request(url: str, kind: str) -> str:
    """ call api server 

        Args:
            url (str): base url to call
            kind (str): get, post, put, or delete
        Returns:
            json encoded response from libraries.io
    """

    try:
        params = {"include_prerelease": "False"} if kind == "post" else {}
        fix_pages()  # Must be called before any request for page validation
        r = getattr(sess, kind)(url, params=params)
        r.raise_for_status()
        return r.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    finally:
        clear_params()
