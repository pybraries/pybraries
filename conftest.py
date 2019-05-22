import pytest
import os
from time import sleep
from pybraries.search import Search
from pybraries.subscribe import Subscribe
from pybraries.helpers import sess
from pybraries.subscription_helpers import sub_api
from pybraries.search_helpers import search_api
from pybraries.set_pages import set_pages
from pybraries.make_request import make_request

# fixture to avoid hitting rate limit
@pytest.fixture(autouse=True, scope="function")
def wait_a_sec():
    yield
    sleep(1)


# setup and teardown
@pytest.fixture(autouse=True, scope="function")
def setup():
    api_key = os.environ["LIBRARIES_API_KEY"]  # api_key for libraries.io

    yield


def teardown():
    api_key = ""
