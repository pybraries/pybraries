import os
from typing import Union, List, Dict, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


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


def extract(*keys):
    class From:
        def of(self, container: Union[Dict, List, Tuple]):
            class Promise(list):  # workaround to allow monkeypatch to builtin list type
                def then(self, f) -> List: pass

            def then(f):
                try:
                    return [f(value) for value in values]
                except (ValueError, TypeError):
                    return [f(key, value) for key, value in zip(keys, values)]

            values = Promise()
            values.extend([container.pop(k) for k in keys if k in container])
            values.then = then
            return values

    return From()
