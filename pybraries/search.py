# search.py
import fire
from pybraries.search_helpers import search_api
from pybraries.set_pages import set_pages
from typing import Dict, List, Optional, Any


class Search(object):
    """Class for wrapping the libraries.io API for 
    platform, project, repo, and user GET actions"""

    def __init__(self):
        pass

    def platforms(self) -> Any:
        """
        Return a list of supported package managers.

        Returns:
            List of dicts of platforms with platform info from libraries.io.
        """

        return search_api("platforms")

    def project(self, manager: str, package: str) -> Any:
        """
        Return information about a package and its versions from a platform (e.g. PyPI).

        Args:
            manager: package manager (e.g. "pypi").
            package: package name.
        Returns:
            Dict of information about the project from libraries.io.
        """

        return search_api("pproject", manager, package)

    def project_dependencies(self, manager: str, package: str) -> Any:
        """
        Get dependencies for a version of a project.

        Returns latest version info.

        Args:
            manager: package manager (e.g. "pypi").
            package: package name.
        Returns:
            Dict of dependencies for a version of a project from libraries.io.
        """

        return search_api("pproject_dependencies", manager, package)

    def project_dependents(self, manager: str, package: str) -> Any:
        """
        Get packages that have at least one version that depends on a given project.

        Args:
            manager: package manager (e.g. "pypi").
            package: package name
            version: package version
        Returns:
            List of dicts package dependents from libraries.io.
        """

        return search_api("pproject_dependents", manager, package)

    def project_dependent_repositories(self, manager: str, package: str) -> Any:
        """
        Get repositories that depend on a given project.

        Args:
            manager: package manager (e.g. "pypi")
            package: package name
        Returns:
            List of dicts of dependent repositories from libraries.io.
        """

        return search_api("pproject_dependent_repositories", manager, package)

    def project_contributors(self, manager: str, package: str) -> Any:
        """
        Get users that have contributed to a given project.

        Args:
            manager: package manager
            package: package name
        Returns:
            List of dicts of project contributor info from libraries.io.
        """

        return search_api("pproject_contributors", manager, package)

    def project_sourcerank(self, manager: str, package: str) -> Any:
        """
        Get breakdown of SourceRank score for a given project.

        Args:
            manager: package manager
            package: package name
        Returns:
            Dict of sourcerank info response from libraries.io.
        """

        return search_api("pproject_sourcerank", manager, package)

    def project_usage(selfself, manager: str, package: str) -> Any:
        """
        Get breakdown of usage for a given project.

        Args:
            manager: package manager
            package: package name
        Returns:
            Dict with info about usage from libraries.io.
        """

        return search_api("pproject_usage", manager, package)

    def project_search(self, **kwargs):
        """
        Search for projects. Accepts keyword arguments only.

        Args:
            filters (dict): optional dict of form
                dict(languages="python", keywords="data", 
                licenses="my_license", manager="pypi")

            sort (str): (optional) one of rank, stars, 
                dependents_count, dependent_repos_count, 
                latest_release_published_at, contributions_count, created_at
        
        Returns:
            List of dicts of project info from libraries.io.
        """

        return search_api("special_project_search", **kwargs)

    def repository(self, host: (str), owner: (str), repo: (str)) -> Any:
        """
        Return information about a repository and its versions.

        Args:
            host: host host name (e.g. GitHub)
            owner: owner
            repo: repo
        Returns:
            List of dicts of info about a repository from libraries.io.
        """

        return search_api("repository", host, owner, repo)

    def repository_dependencies(self, host: (str), owner: (str), repo: (str)) -> Any:
        """
        Return information about a repository's dependencies.

        Args:
            host: host provider name (e.g. GitHub)
            owner: owner
            repo: repo
        Returns:
            Dict of repo dependency info from libraries.io.
        """

        return search_api("repository_dependencies", host, owner, repo)

    def repository_projects(self, host: (str), owner: (str), repo: (str)) -> Any:
        """
        Get a list of packages referencing the given repository.

        Args:
            host: host provider name (e.g. GitHub)
            owner: owner
            repo: repo
        Returns:
            List of dicts of packages referencing a repo from libraries.io.
        """

        return search_api("repository_projects", host, owner, repo)

    def user(self, host: (str), user: (str)) -> Any:
        """
        Return information about a user.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
        Dict of info about user from libraries.io.
        """
        return search_api("user", host, user)

    def user_repositories(self, host: (str), user: (str)) -> Any:
        """
        Return information about a user's repos.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
            List of dicts with info about user repos from libraries.io.
        """
        return search_api("user_repositories", host, user)

    def user_packages(self, host: (str), user: (str)) -> Any:
        """
        Return information about packages using a user's repos.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
            List of dicts of package info from libraries.io.
        """
        return search_api("user_packages", host, user)

    def user_packages_contributions(self, host: (str), user: (str)) -> Any:
        """
        Return information about packages a user has contributed to.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
            List of dicts with user package contribution info from libraries.io.
        """
        return search_api("user_packages_contributions", host, user)

    def user_repository_contributions(self, host: (str), user: (str)) -> Any:
        """
        Return information about repositories a user has contributed to.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
            (list): list of dicts response from libraries.io
        """
        return search_api("user_repositories_contributions", host, user)

    def user_dependencies(self, host, user):
        """
        Return a list of unique user's repositories' dependencies.

        Ordered by frequency of use in those repositories.

        Args:
            host: host (e.g. github)
            user: username
        Returns:
            Liist of dicts with user package dependency info.
        """
        return search_api("user_dependencies", host, user)


# From the command line you can call any public function by name with arguments
if __name__ == "__main__":
    fire.Fire(Search)

    # manually testing actions
    api = Search()

    # t = api.user("github", "discdiver")

    x = api.project_dependents("pypi", "plotly")
    print(x[0]["name"])

    y = api.project_dependent_repositories("pypi", "yellowbrick")
    print(y[0])
    print(type(y))

    # x = set_pages(1, 3)
    # print(x)

    # d = api.project_search(
    #    sort="latest_release_published_at",
    #    filters=dict(keywords="visualization", manager="pypi"),
    # )
    # print(d)
