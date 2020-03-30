import pytest
from pyexpect import expect

from pybraries.search import Search

DEFAULT_PER_PAGE = 30
MAX_PER_PAGE = 100
PLATFORM = "Pypi"
NAME = "pybraries"


@pytest.fixture
def search():
    return Search()


def expect_correct_project(name, platform, project):
    expect(project).to_include("deprecation_reason", "description", "forks", "homepage", "language", "repository_url",
                               "licenses", "name", "rank", "stars", "dependents_count", "platform")
    expect(project["stars"]).is_greater_or_equal_than(1)
    expect(project["forks"]).is_greater_or_equal_than(1)
    expect(project["dependents_count"]).is_greater_or_equal_than(0)
    expect(project["platform"]).equals(platform)
    expect(project["name"]).equals(name)


def test_project(search):
    project = search.project(PLATFORM, NAME)

    expect_correct_project(NAME, PLATFORM, project)


def test_project_search(search, monkeypatch):
    from pybraries.helpers import sess

    old_get = sess.get

    def new_sess_get(*args, **kwargs):
        from urllib.parse import parse_qs, urlparse
        r = old_get(*args, **kwargs)
        params = parse_qs(urlparse(r.request.url).query)
        expect(params).includes("q", "api_key", "platforms")
        expect(params["q"][0]).equals("pybraries")
        expect(params["platforms"][0]).equals("pypi")
        return r

    monkeypatch.setattr(sess, "get", new_sess_get)

    projects = search.project_search(project="pybraries", platforms="pypi")

    monkeypatch.undo()

    project = projects[0]

    expect_correct_project(NAME, PLATFORM, project)


def dictfilt(x, y):
    return dict([(i, x[i]) for i in x if i in set(y)])


def test_projects(search):
    projects = search.project_search(sort="dependents_count", platforms="pypi", licenses="MIT")

    resorted_projects = sorted(projects, key=lambda project: project["dependents_count"], reverse=True)
    wanted_keys = ("name", "dependents_count")
    print(dictfilt(projects[0], wanted_keys))
    print(dictfilt(resorted_projects[0], wanted_keys))

    for actual, expected in zip(projects, resorted_projects):
        expect(actual["dependents_count"]).is_greater_or_equal_than(expected['dependents_count'])
        expect(actual["platform"]).equals("Pypi")
        expect(actual["licenses"]).has_substring("MIT")

    expect(len(projects)).to_be(DEFAULT_PER_PAGE)


def test_projects_100_per_page(search):
    projects = search.project_search(sort="dependents_count", platforms="pypi", licenses="MIT", per_page=MAX_PER_PAGE)
    expect(projects).of_size(MAX_PER_PAGE)
