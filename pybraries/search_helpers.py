# search_helpers.py
from pybraries.helpers import sess, clear_params
from pybraries.make_request import make_request


def search_api(action, *args, **kwargs):
    """
    build and call for search 

    Args:
        action (str): function action name
        filters (list): list of strings 
        sort (str): to sort by. Options
        *args (str): positional arguments
        **kwargs (str): keyword arguments
    Returns:
        (list): list of dicts response from libraries.io.
            according to page and per page 
        Many are dicts or list of dicts.
    """

    url_end_list = ["https://libraries.io/api"]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url
    kind = "get"  # type of request

    if action == "special_project_search":
        url_end_list.append("search?")

        # package seems to be ignored by the libraries.io API
        # - bug in docs or their api
        # if "package" in kwargs:
        #    url_end_list.append(kwargs["package"])

        if kwargs:
            if "filters" in kwargs:
                filts = dict(kwargs["filters"])
                if "manager" in filts:
                    filts["platforms"] = filts.pop("manager")
                sess.params = {**sess.params, **filts}
            if "sort" in kwargs:
                sess.params["sort"] = kwargs["sort"]

        url_combined = "/".join(url_end_list)
        response = make_request(url_combined, kind)

        clear_params()
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
            url_end_list.append("dependents")

        if action == "pproject_dependent_repositories":
            url_end_list.append("dependent_repositories")

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
            more_args = [arg for arg in args]
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
            more_args = [arg for arg in args]
            url_end_list = url_end_list + more_args
            print(url_end_list)

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
    url_end_list = []
    response = make_request(url_combined, kind)
    return response
