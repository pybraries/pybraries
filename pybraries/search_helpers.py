# search_helpers.py
from helpers import sess
from make_request import make_request


def search_api(action, *args, **kwargs):
    """
    build and call for search - refactor into two

    Args:
        action (str): function name
        *args (str): positional arguments
        **kwargs (str): keyword arguments
    Returns:
        response (dict, list, or str): response from libraries.io.
        Many are dicts or list of dicts.
    """

    url_end_list = ["https://libraries.io/api"]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url

    if action == "special_project_search":
        url_end_list.append("search?")

        # package seems to be ignored by the libraries.io API
        # - bug in docs or their api
        # if "package" in kwargs:
        #    url_end_list.append(kwargs["package"])

        if kwargs:
            sess.params = {**sess.params, **kwargs}  # append kwargs to params dict

        if args:
            more_args = [arg for arg in args]
            url_end_list = url_end_list + more_args

        url_combined = "/".join(url_end_list)

        response = make_request(url_combined)
        return response

    if action == "platforms":
        url_end_list.append("platforms")

    if "pproject" in action:
        if kwargs:
            if "manager" in kwargs:
                url_end_list.append(kwargs["manager"])
            if "package" in kwargs:
                url_end_list.append(kwargs["package"])
        if args:
            more_args = [arg for arg in args]
            url_end_list = url_end_list + more_args

        if action == "pproject_dependencies":
            url_end_list.append(
                "latest"
            )  # could make option to subscribe to other versions
            url_end_list.append("dependencies")

        if action == "pproject_dependents":
            url_end_list.append("dependendents")

        if action == "pproject_dependent_repositories":
            url_end_list.append("dependendent_repositories")

        if action == "pproject_contributors":
            url_end_list.append("contributors")

        if action == "pproject_sourcerank":
            url_end_list.append("sourcerank")

        if action == "pproject_usage":
            url_end_list.append("usage")

    if "repository" in action:
        if kwargs:
            if "host" in kwargs:
                url_end_list.append(kwargs["host"])
            if "owner" in kwargs:
                url_end_list.append(kwargs["owner"])
            if "repo" in kwargs:
                url_end_list.append(kwargs["repo"])
        if args:
            more_args = [arg for arg in args[1:]]
            url_end_list = url_end_list + more_args

        if action == "repository_dependencies":
            url_end_list.append("dependencies")

        if action == "repository_projects":
            url_end_list.append("projects")

    if "user" in action:
        if kwargs:
            if "host" in kwargs:
                url_end_list.append(kwargs["host"])
            if "user" in kwargs:
                url_end_list.append(kwargs["user"])
        if args:
            more_args = [arg for arg in args[1:]]
            url_end_list = url_end_list + more_args

        if action == "user_repositories":
            url_end_list.append("repositories")

        if action == "user_packages":
            url_end_list.append("projects")

        if action == "user_packages_contributions":
            url_end_list.append("project-contributions")

        if action == "user_repositories_contributions":
            url_end_list.append("repository-contributions")

        if action == "user_dependencies":
            url_end_list.append("dependencies")

        url_combined = "/".join(url_end_list)
        response = make_request(url_combined)

    return response
