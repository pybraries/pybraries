# make_request.pyß
from requests.exceptions import HTTPError
from helpers import sess


def make_request(url):
    # call api server

    try:
        r = sess.get(url)
        r.raise_for_status()
        r_json = r.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return r.json
