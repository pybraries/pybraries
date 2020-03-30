# search_helpers.py
from typing import List

from pybraries.helpers import sess
from pybraries.make_request import make_request


def search_api(action, *args, filters=None, sort=None, **kwargs):
    """
    build and call for search 

    Args:
        action (str): function action name
        filters (dict): filters passed to requests Session
        sort (str): to sort by. Options
        *args (str): positional arguments
        **kwargs (str): keyword arguments
    Returns:
        (list): list of dicts response from libraries.io.
            according to page and per page 
        Many are dicts or list of dicts.
    """

    url_end_list: List[str] = ["https://libraries.io/api"]  # start of list to build url
    url_combined: str  # final string url
    kind = "get"  # type of request, defaults to "get"

    # Handle path params
    if action == "special_project_search":
        url_end_list.append("search?")
    elif action == "platforms":
        url_end_list.append("platforms")

    elif action.startswith("project"):
        action = action[7:]  # remove action prefix
        if kwargs:
            if "platforms" in kwargs:
                url_end_list.append(kwargs.pop("platforms"))
            if "project" in kwargs:
                url_end_list.append(kwargs.pop("project"))
        if args:
            url_end_list += args
        if action.startswith("_"):
            action = action[1:]  # remove remaining underscore from operation name
            if action == "dependencies":
                version = kwargs.pop("version") or "latest"  # defaults to latest
                url_end_list.append(version)
            url_end_list.append(action)

    elif action.startswith("repository"):
        action = action[10:]
        if kwargs:
            if "host" in kwargs:
                url_end_list.append(kwargs.pop("host"))
            if "owner" in kwargs:
                url_end_list.append(kwargs.pop("owner"))
            if "repo" in kwargs:
                url_end_list.append(kwargs.pop("repo"))
        if args:
            url_end_list += args

        if action.startswith("_"):
            url_end_list.append(action[1:])

    elif "user" in action:
        if kwargs:
            if "host" in kwargs:
                url_end_list.append(kwargs.pop("host"))
            if "user" in kwargs:
                url_end_list.append(kwargs.pop("user"))
        if args:
            url_end_list += args
            print(url_end_list)

        if action == "user_repositories":
            url_end_list.append("repositories")

        if action == "user_projects":
            url_end_list.append("projects")

        if action == "user_projects_contributions":
            url_end_list.append("project-contributions")

        if action == "user_repositories_contributions":
            url_end_list.append("repository-contributions")

        if action == "user_dependencies":
            url_end_list.append("dependencies")
    # Handle query params
    if "project" in kwargs:
        sess.params['q'] = kwargs["project"]
    if filters is not None:
        sess.params = {**sess.params, **filters}
    if sort is not None:
        sess.params["sort"] = sort
    sess.params = {**sess.params, **kwargs}
    url_combined = "/".join(url_end_list)
    response = make_request(url_combined, kind)
    return response
