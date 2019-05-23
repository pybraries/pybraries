# make_request.pyß
from requests.exceptions import HTTPError
from pybraries.helpers import sess, clear_params


def make_request(url, kind):
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
            r = sess.post(url)
            r.raise_for_status()
            r_val = "successfully subscribed"
        if kind == "put":
            r = sess.put(url)
            r.raise_for_status()
            r_val = "successfully updated"
        if kind == "delete":
            r = sess.delete(url)
            r.raise_for_status()
            r_val = "successfully unsubscribed"
        return r_val

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
