# search.py
import fire
from pybraries.search_helpers import search_api
from pybraries.set_pages import set_pages


class Search(object):
    """Class for wrapping the libraries.io API for 
    platform, project, repo, and user GET actions"""

    def __init__(self):
        pass

    def platforms(self, *args, **kwargs):
        """
        Return a list of supported package managers.

        Args:

        Returns:
            list: list of dicts response from libraries.io
        """

        return search_api("platforms", *args, **kwargs)

    def project(self, *args, **kwargs):
        """
        Return information about a package and its versions from a platform (e.g. PyPI).

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            dict: Information about the project from libraries.io
        """

        return search_api("pproject", *args, **kwargs)

    def project_dependencies(self, *args, **kwargs):
        """
        Get a list of dependencies for a version of a project.

        Returns latest version info.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            (dict): response from libraries.io
        """

        return search_api("pproject_dependencies", *args, **kwargs)

    def project_dependents(self, *args, **kwargs):
        """
        Get packages that have at least one version that depends on a given project.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            (list): list of dicts response from libraries.io
        """

        return search_api("pproject_dependendents", *args, **kwargs)

    def project_dependent_repositories(self, *args, **kwargs):
        """
        Get repositories that depend on a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            (list): list of dicts response from libraries.io
        """

        return search_api("pproject_dependendent_repositories", *args, **kwargs)

    def project_contributors(self, *args, **kwargs):
        """
        Get users that have contributed to a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            (list): list of dicts response from libraries.io
        """

        return search_api("pproject_contributors", *args, **kwargs)

    def project_sourcerank(self, *args, **kwargs):
        """
        Get breakdown of SourceRank score for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            dict: sourcerank info response from libraries.io
        """

        return search_api("pproject_sourcerank", *args, **kwargs)

    def project_usage(self, *args, **kwargs):
        """
        Get breakdown of version usage for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            (dict): verion usage info response from libraries.io
        """

        return search_api("pproject_usage", *args, **kwargs)

    def project_search(self, *args, **kwargs):
        """
        Search for projects.

        ** Accepts keyword arguments only right now. \
            API may change to accept a list of dicts in the future.**

        Args:
            filters (dict): optional dict of form
                dict(languages="python", keywords="data", \
                licenses="my_license", manager="pypi")

            sort (str): (optional) one of rank, stars, 
                dependents_count, dependent_repos_count, 
                latest_release_published_at, contributions_count, created_at
            
        Returns:
            (list): list of dicts of project info from libraries.io
        """

        return search_api("special_project_search", *args, **kwargs)

    def repository(self, *args, **kwargs):
        """
        Return information about a reposiotory and its versions.

        Args:
            host (str): host host name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return search_api("repository", *args, **kwargs)

    def repository_dependencies(self, *args, **kwargs):
        """
        Return information about a repository's dependencies.

        Args:
            host (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (dict): dict response from libraries.io
        """

        return search_api("repository_dependencies", *args, **kwargs)

    def repository_projects(self, *args, **kwargs):
        """
        Get a list of packages referencing the given repository.

        Args:
            host (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return search_api("repository_projects", *args, **kwargs)

    def user(self, *args, **kwargs):
        """
        Return information about a user.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            response (dict): response from libraries.io
        """
        return search_api("user", *args, **kwargs)

    def user_repositories(self, *args, **kwargs):
        """
        Return information about a user's repos.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            (list): list of dicts response from libraries.io
        """
        return search_api("user_repositories", *args, **kwargs)

    def user_packages(self, *args, **kwargs):
        """
        Return information about packages using a user's repos.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            (list): package with info in list of dicts 
            response from libraries.io
        """
        return search_api("user_packages", *args, **kwargs)

    def user_packages_contributions(self, *args, **kwargs):
        """
        Return information about packages a user has contributed to.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            (list): list of dicts response from libraries.io
        """
        return search_api("user_packages_contributions", *args, **kwargs)

    def user_repository_contributions(self, *args, **kwargs):
        """
        Return information about repositories a user has contributed to.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            (list): list of dicts response from libraries.io
        """
        return search_api("user_repositories_contributions", *args, **kwargs)

    def user_dependencies(self, *args, **kwargs):
        """
        Return Get a list of unique packages user's repositories' dependencies.

        Ordered by frequency of use in those repositories.

        Args:
            host (str): host (e.g. github)
            user (str): username
        Returns:
            (list): list of dicts response from libraries.io
        """
        return search_api("user_dependencies", *args, **kwargs)


# From the command line you can call any public function by name with arguments
if __name__ == "__main__":
    fire.Fire(Search)

    # manually testing actions
    api = Search()

    t = api.user("github", "discdiver")
    print(t)

    # x = set_pages(1, 3)
    # print(x)

    # d = api.project_search(
    #    sort="latest_release_published_at",
    #    filters=dict(keywords="visualization", manager="pypi"),
    # )
    # print(d)
