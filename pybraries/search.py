# search.py
from typing import Any

from pybraries.search_helpers import search_api


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

    def project(self, platforms: str, name: str) -> Any:
        """
        Return information about a project and its versions from a platform (e.g. PyPI).

        Args:
            platforms: package manager (e.g. "pypi").
            name: project name.
        Returns:
            Dict of information about the project from libraries.io.
        """

        return search_api("project", platforms, name)

    def project_dependencies(
        self, platforms: str, project: str, version: str = None
    ) -> Any:
        """
        Get dependencies for a version of a project.

        Returns latest version info.

        Args:
            platforms: package manager (e.g. "pypi").
            project: project name.
            version: (optional) project version
        Returns:
            Dict of dependencies for a version of a project from libraries.io.
        """

        return search_api("project_dependencies", platforms, project, version=version)

    def project_dependents(
        self, platforms: str, project: str, version: str = None
    ) -> Any:
        """
        Get projects that have at least one version that depends on a given project.

        Args:
            platforms: package manager (e.g. "pypi").
            project: project name
            version: project version
        Returns:
            List of dicts project dependents from libraries.io.
        """

        return search_api("project_dependents", platforms, project, version=version)

    def project_dependent_repositories(self, platforms: str, project: str) -> Any:
        """
        Get repositories that depend on a given project.

        Args:
            platforms: package manager (e.g. "pypi")
            project: project name
        Returns:
            List of dicts of dependent repositories from libraries.io.
        """

        return search_api("project_dependent_repositories", platforms, project)

    def project_contributors(self, platforms: str, project: str) -> Any:
        """
        Get users that have contributed to a given project.

        Args:
            platforms: package manager
            project: project name
        Returns:
            List of dicts of project contributor info from libraries.io.
        """

        return search_api("project_contributors", platforms, project)

    def project_sourcerank(self, platforms: str, project: str) -> Any:
        """
        Get breakdown of SourceRank score for a given project.

        Args:
            platforms: package manager
            project: project name
        Returns:
            Dict of sourcerank info response from libraries.io.
        """

        return search_api("project_sourcerank", platforms, project)

    def project_usage(self, platforms: str, project: str) -> Any:
        """
        Get breakdown of usage for a given project.

        Args:
            platforms: package manager
            project: project name
        Returns:
            Dict with info about usage from libraries.io.
        """

        return search_api("project_usage", platforms, project)

    def project_search(self, **kwargs):
        """
        Search for projects.
        Args - keywords only:
            keywords (str):  required argument: keywords to search
            languages (str): optional programming languages to filter
            licenses (str): license type to filter
            platforms (str):, platforms to filter

            sort str: (optional) one of rank, stars,
                dependents_count, dependent_repos_count,
                latest_release_published_at, contributions_count, created_at

        Returns:
            List of dicts of project info from libraries.io.
        """
        return search_api("special_project_search", **kwargs)

    def repository(self, host: str, owner: str, repo: str) -> Any:
        """
        Return information about a repository and its versions.

        Args:
            host: host provider name (e.g. GitHub)
            owner: owner
            repo: repo
        Returns:
            List of dicts of info about a repository from libraries.io.
        """

        return search_api("repository", host, owner, repo)

    def repository_dependencies(self, host: str, owner: str, repo: str) -> Any:
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

    def repository_projects(self, host: str, owner: str, repo: str) -> Any:
        """
        Get a list of projects referencing the given repository.

        Args:
            host: host provider name (e.g. GitHub)
            owner: owner
            repo: repo
        Returns:
            List of dicts of projects referencing a repo from libraries.io.
        """

        return search_api("repository_projects", host, owner, repo)

    def user(self, host: str, user: str) -> Any:
        """
        Return information about a user.

        Args:
            host: host provider name (e.g. GitHub)
            user: username
        Returns:
        Dict of info about user from libraries.io.
        """
        return search_api("user", host, user)

    def user_repositories(self, host: str, user: str) -> Any:
        """
        Return information about a user's repos.

        Args:
            host: host provider name (e.g. GitHub)
            user: username
        Returns:
            List of dicts with info about user repos from libraries.io.
        """
        return search_api("user_repositories", host, user)

    def user_projects(self, host: str, user: str) -> Any:
        """
        Return information about projects using a user's repos.

        Args:
            host: host provider name (e.g. GitHub)
            user: username
        Returns:
            List of dicts of project info from libraries.io.
        """
        return search_api("user_projects", host, user)

    def user_projects_contributions(self, host: str, user: str) -> Any:
        """
        Return information about projects a user has contributed to.

        Args:
            host: host provider name (e.g. GitHub)
            user: username
        Returns:
            List of dicts with user project contribution info from libraries.io.
        """
        return search_api("user_projects_contributions", host, user)

    def user_repository_contributions(self, host: str, user: str) -> Any:
        """
        Return information about repositories a user has contributed to.

        Args:
            host: host provider name (e.g. GitHub)
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
            host: host provider name (e.g. GitHub)
            user: username
        Returns:
            List of dicts with user project dependency info.
        """
        return search_api("user_dependencies", host, user)
