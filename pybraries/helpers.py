import os
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class APIKeyMissingError(Exception):
    """Custom error for API Key missing"""

    pass


LIBRARIES_API_KEY = os.environ.get("LIBRARIES_API_KEY", None)

if LIBRARIES_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. "
        "See https://libraries.io to get your free key. "
        "Then set the key to the environment variable: LIBRARIES_API_KEY"
    )

# session retry settings
retries = Retry(total=3, backoff_factor=0.2, status_forcelist=[500, 502, 503, 504])

# session object common properties
sess = requests.Session()
# sess.params = {"include_prerelease": False}
sess.params["api_key"] = LIBRARIES_API_KEY
# sess.params["include_prerelease"] = 0
sess.mount("https://", HTTPAdapter(max_retries=retries))


def clear_params() -> None:
    sess.params.clear()
    sess.params["api_key"] = LIBRARIES_API_KEY
