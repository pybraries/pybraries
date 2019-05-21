from requests.exceptions import HTTPError
import fire
from pybraries.helpers import sess


class Libraries_API(object):
    """Class for wrapping the libraries.io API"""

    def __init__(self):
        pass

    def __call_api(self, thing, *args, **kwargs):
        """
        Calls the API.

        Args:
            thing (str): function name
            *args (str): positional arguments
            **kwargs (str): keyword arguments
        Returns:
            response (dict, list, or str): response from libraries.io.
            Many are dicts or list of dicts.
        """

        url_end_list = ["https://libraries.io/api"]  # start of list to build url
        more_args = []  # for unpacking args
        url_combined = ""  # final string url
        call_type = ""  # post, put or delete

        def _make_request(url):
            # call api server

            try:
                r = sess.get(url)
                r.raise_for_status()
                r_json = r.json()
            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"Other error occurred: {err}")

            return r_json

        if thing == "special_project_search":
            url_end_list.append("search?")

            # package seems to be ignored by the libraries.io API
            if "package" in kwargs:
                url_end_list.append(kwargs["package"])
            # params=dict(kwargs)  # append kwargs to params dict

            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            url_combined = "/".join(url_end_list)

            response = _make_request(url_combined)
            return response

        def __check_prerelease(*args, **kwargs):
            prerelease = kwargs.pop("include_prerelease", "")
            return prerelease

        if "subscribe" in thing:
            if thing == "subscribe":
                call_type = "post"
            if thing == "update_subscribe":
                call_type = "put"
            if thing == "delete_subscribe":
                call_type = "delete"

            if kwargs:
                if "manager" in kwargs:
                    manager = kwargs["manager"]
                if "package" in kwargs:
                    package = kwargs["package"]
                # if pre:
                #    if pre == "False" or pre == False:
                #       url_end_list.append('include_prerelease=0')
            if args:
                manager = args[0]
                package = args[1]

                more_args = [arg for arg in args]

            # first check if subscribed. Must be done before build url.
            check_pkg_subscribed = self.check_subscribed(manager, package)

            if call_type == "delete" and check_pkg_subscribed is None:
                msg = f"Unsubscribe unnecessary. You are not subscribed to {package}"
                return msg

            # reset url_end_list
            url_end_list = ["https://libraries.io/api", "subscriptions"]

            # pre = __check_prerelease(args, kwargs)

            url_end_list = url_end_list + more_args
            url_combined = "/".join(url_end_list)

            try:
                if call_type == "post":
                    r = sess.post(url_combined)
                    print(url_combined)
                if call_type == "put":
                    r = sess.put(url_combined)
                if call_type == "delete":
                    r = sess.delete(url_combined)

                if r:
                    if r.status_code == 204:
                        response = f"Successfully unsubscribed from {package}"
                    else:
                        response = r.json()
                    r.raise_for_status()
                return response
            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:

                print(f"Other error occurred: {err}")

        if thing == "platforms":
            url_end_list.append("platforms")

        if "pproject" in thing:
            if kwargs:
                if "manager" in kwargs:
                    url_end_list.append(kwargs["manager"])
                if "package" in kwargs:
                    url_end_list.append(kwargs["package"])
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            if thing == "pproject_dependencies":
                url_end_list.append(
                    "latest"
                )  # could make option to subscribe to other versions
                url_end_list.append("dependencies")

            if thing == "pproject_dependents":
                url_end_list.append("dependendents")

            if thing == "pproject_dependent_repositories":
                url_end_list.append("dependendent_repositories")

            if thing == "pproject_contributors":
                url_end_list.append("contributors")

            if thing == "pproject_sourcerank":
                url_end_list.append("sourcerank")

            if thing == "pproject_usage":
                url_end_list.append("usage")

        if "repository" in thing:
            if kwargs:
                if "provider" in kwargs:
                    url_end_list.append(kwargs["provider"])
                if "owner" in kwargs:
                    url_end_list.append(kwargs["owner"])
                if "repo" in kwargs:
                    url_end_list.append(kwargs["repo"])
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            if thing == "repository_dependencies":
                url_end_list.append("dependencies")

            if thing == "repository_projects":
                url_end_list.append("projects")

        if "user" in thing:
            if kwargs:
                if "provider" in kwargs:
                    url_end_list.append(kwargs["provider"])
                if "user" in kwargs:
                    url_end_list.append(kwargs["user"])
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            if thing == "user_repositories":
                url_end_list.append("repositories")

            if thing == "user_packages":
                url_end_list.append("projects")

            if thing == "user_packages_contributions":
                url_end_list.append("project-contributions")

            if thing == "user_repositories_contributions":
                url_end_list.append("repository-contributions")

            if thing == "user_dependencies":
                url_end_list.append("dependencies")

        if thing == "list_subscriptions":
            url_end_list.append("subscriptions")

        if thing == "check_subscription":
            url_end_list.append("subscriptions")
            if kwargs:
                if "manager" in kwargs:
                    url_end_list.append(kwargs["manager"])
                if "package" in kwargs:
                    url_end_list.append(kwargs["package"])
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

        url_combined = "/".join(url_end_list)
        response = _make_request(url_combined)

        if thing == "check_subscription":
            if response is not None:
                return True
            else:
                return False
        else:
            return response

    # public methods

    def platforms(self, *args, **kwargs):
        """
        Return a list of supported package managers.

        Args:

        Returns:
            list: list of dicts response from libraries.io
        """

        return self.__call_api("platforms", *args, **kwargs)

    def project(self, *args, **kwargs):
        """
        Return information about a package and its versions from a platform (e.g. PyPI).

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            dict: Information about the project from libraries.io
        """

        return self.__call_api("pproject", *args, **kwargs)

    def project_dependencies(self, *args, **kwargs):
        """
        Get a list of dependencies for a version of a project.

        Returns latest version info.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            response (dict): response from libraries.io
        """

        return self.__call_api("pproject_dependencies", *args, **kwargs)

    def project_dependents(self, *args, **kwargs):
        """
        Get packages that have at least one version that depends on a given project.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_dependendents", *args, **kwargs)

    def project_dependent_repositories(self, *args, **kwargs):
        """
        Get repositories that depend on a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_dependendent_repositories", *args, **kwargs)

    def project_contributors(self, *args, **kwargs):
        """
        Get users that have contributed to a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_contributors", *args, **kwargs)

    def project_sourcerank(self, *args, **kwargs):
        """
        Get breakdown of SourceRank score for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            dict: sourcerank info response from libraries.io
        """

        return self.__call_api("pproject_sourcerank", *args, **kwargs)

    def project_usage(self, *args, **kwargs):
        """
        Get breakdown of version usage for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (dict): verion usage info response from libraries.io
        """

        return self.__call_api("pproject_usage", *args, **kwargs)

    def project_search(self, *args, **kwargs):
        """
        Search for projects.

        Args:
            package (optional)(str): package name
            sort= (optional) (str): one of rank, stars, \
                dependents_count, dependent_repos_count, \
                latest_release_published_at, contributions_count, created_at
            filter= (optional) (list): list of strings. \
                Options: languages, licenses, keywords, platforms
        Returns:
            response (list): list of dicts of project info from libraries.io
        """

        return self.__call_api("special_project_search", *args, **kwargs)

    def repository(self, *args, **kwargs):
        """
        Return information about a reposiotory and its versions.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("repository", *args, **kwargs)

    def repository_dependencies(self, *args, **kwargs):
        """
        Return information about a repository's dependencies.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (dict): dict response from libraries.io
        """

        return self.__call_api("repository_dependencies", *args, **kwargs)

    def repository_projects(self, *args, **kwargs):
        """
        Get a list of packages referencing the given repository.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("repository_projects", *args, **kwargs)

    def user(self, *args, **kwargs):
        """
        Return information about a user.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (dict): response from libraries.io
        """
        return self.__call_api("user", *args, **kwargs)

    def user_repositories(self, *args, **kwargs):
        """
        Return information about a user's repos.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            respons (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_repositories", *args, **kwargs)

    def user_packages(self, *args, **kwargs):
        """
        Return information about packages using a user's repos.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_packages", *args, **kwargs)

    def user_packages_contributions(self, *args, **kwargs):
        """
        Return information about packages a user has contributed to.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_packages_contributions", *args, **kwargs)

    def user_repository_contributions(self, *args, **kwargs):
        """
        Return information about repositories a user has contributed to.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_repositories_contributions", *args, **kwargs)

    def user_dependencies(self, *args, **kwargs):
        """
        Return Get a list of unique packages user's repositories' dependencies.

        Ordered by frequency of use in those repositories.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_dependencies", *args, **kwargs)

    def list_subscriptions(self, *args, **kwargs):
        """
        Return a list of packages a user is subscribed to for release notifications.

        Args:

        Returns:
            response (dict): dict response from libraries.io
        """
        return self.__call_api("list_subscriptions", *args, **kwargs)

    def subscribe(self, *args, **kwargs):
        """
        Subscribe to receive notifications about new releases of a project.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
            include_prerelease (bool): default = True. Include prerelease notifications
        Returns:
            response (dict): dict of project info from libraries.io
        """
        return self.__call_api("subscribe", *args, **kwargs)

    def check_subscribed(self, *args, **kwargs):
        """
        Check if a user is subscribed to notifications for new project releases.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
        Returns:
            (bool): True if subscribed to given package, else False
        """
        return self.__call_api("check_subscription", *args, **kwargs)

    def update_subscription(self, *args, **kwargs):
        """
        Update the options for a subscription.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
            include_prerelease (bool): default = True. Include prerelease notifications.

        Returns:
            response (dict): dict of project info from libraries.io
            # make so a 404 for not found returns a nice message
            # maybe return a message if 304 is reponse (not updated)
        """
        return self.__call_api("update_subscribe", *args, **kwargs)

    def unsubscribe(self, *args, **kwargs):
        """
        Stop receiving release notifications from a project.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name

        Returns:
            response (str or int): response header status from libraries.io
        """

        return self.__call_api("delete_subscribe", *args, **kwargs)

    def set_pages(self, per_page=30, page=1):
        """
        Change pagination settings.

        Args:
            per_page (int): default=30 number of items per page.  max=100
            page (int): default=1 package name

        Returns:
            response (str): message with pagination information
        """

        if not all(isinstance(i, int) for i in [page, per_page]):
            raise TypeError("Must be an integer")
        if page < 1:
            raise ValueError("page must be an integer > 1")
        if per_page > 100 or per_page < 1:
            raise ValueError("perpage must be an integer between 1 and 100, inclusive")

        sess.params[
            "page"
        ] = page  # 1 returns page 1 of results, 2 returns page 2, etc.
        sess.params["per_page"] = per_page  # 30 is libraries api default, max is 100

        return f"per_page set to {per_page} and page set to {page}."


# From the command line you can call any public function by name with arguments
if __name__ == "__main__":
    fire.Fire(Libraries_API)

    # manually testing things
    api = Libraries_API()

    # x = api.subscribe(manager="pypi", package="pandas", y="h")
    # print(x)

    # a = api.unsubscribe(manager="pypi", package="pandas")
    # print(a)

    # y = api.check_subscribed('pypi', 'numpy')
    # print(y)

    # z = api.update_subscription(manager="pypi", package="plotly",
    # include_prerelease="False")
    # print(z)

    d = api.project_search(sort="stars", keywords="visualization", languages="python")
    print(d)
