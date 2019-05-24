# (generated with --quick)

import requests.adapters
import requests.sessions
from typing import Any, Optional, Type

HTTPAdapter: Type[requests.adapters.HTTPAdapter]
LIBRARIES_API_KEY: Optional[str]
Retry: Any
os: module
requests: module
retries: Any
sess: requests.sessions.Session

class APIKeyMissingError(Exception): ...

def clear_params() -> None: ...
