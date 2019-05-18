import os
import requests
from requests.exceptions import HTTPError, RetryError
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

LIBRARIES_API_KEY = os.environ.get('LIBRARIES_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if LIBRARIES_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. "
        "See https://libraries.io to get your free key."
    )

# session settings
retries = Retry( 
    total=10, 
    backoff_factor=0.2, 
    status_forcelist=[500, 502, 503, 504]
)

sess = requests.Session()
sess.params = {}
sess.params['api_key'] = LIBRARIES_API_KEY
sess.mount('https://', HTTPAdapter(max_retries=retries))
