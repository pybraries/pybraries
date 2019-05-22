# make_request.pyß
from requests.exceptions import HTTPError
from pybraries.helpers import sess


def make_request(url, kind):
    """ call api server 
    
    
    """

    r_json = {}  # json object to return

    try:
        if kind == "get":
            r = sess.get(url)
            r.raise_for_status()
            r_json = r.json()
        if kind == "post":
            r = sess.post(url)
            r.raise_for_status()
            r_json = r.json()
        if kind == "put":
            pass
        if kind == "delete":
            pass

        return r_json
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
