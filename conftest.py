import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", help="libraries.io api key"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
