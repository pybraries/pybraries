# make_request.pyß
from requests.exceptions import HTTPError
from pybraries.helpers import sess, clear_params
from typing import Dict, List, Optional, Any


def make_request(url: str, kind: str) -> Any:
    """ call api server 

        Args:
            url (str): base url to call
            kind (str): get, post, put, or delete
        Returns:
            response from libraries.io
    """

    try:
        if kind == "get":
            r = sess.get(url)
            r.raise_for_status()
            r_val = r.json()
        if kind == "post":
            r = sess.post(url, params={"include_prerelease": "False"})
            r.raise_for_status()
            r_val = "Successfully Subscribed"
            x = r.json()
        if kind == "put":
            r = sess.put(url)
            r.raise_for_status()
            r_val = "include_prerelease is always set to true"
        if kind == "delete":
            r = sess.delete(url)
            r.raise_for_status()
            r_val = "Successfully Unsubscribed"

        clear_params()
        return r_val

    except HTTPError as http_err:
        clear_params()
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        clear_params()
        print(f"Other error occurred: {err}")
