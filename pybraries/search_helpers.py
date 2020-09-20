# search_helpers.py
from typing import List

from pybraries.helpers import sess, extract
from pybraries.make_request import make_request


def search_api(action, *args, keywords=None, filters=None, sort=None, **kwargs):
    """
    build and call for search

    Args:
        action (str): function action name
        keywords (str): keywords for project_search only
        filters (dict): filters passed to requests Session
        sort (str): to sort by. Options
        *args (str): positional arguments
        **kwargs (str): keyword arguments
    Returns:
        (list): list of dicts response from libraries.io.
            according to page and per page
        Many are dicts or list of dicts.
    """

    kind = "get"
    url_end_list = handle_path_params(action, *args, **kwargs)
    handle_query_params(action, keywords, filters, sort, **kwargs)
    url_combined = "/".join(url_end_list)
    return make_request(url_combined, kind)


def handle_query_params(action, keywords, filters, sort, **kwargs):

    if action == "special_project_search":
        sess.params["q"] = keywords

    elif "project" in kwargs:
        sess.params["q"] = kwargs["project"]
    if filters:
        extract(*list(filters.keys())).of(filters).then(sess.params.__setitem__)
    if sort:
        sess.params["sort"] = sort
    sess.params = {**sess.params, **kwargs}


def handle_path_params(action, *args, **kwargs):
    def from_kwargs(*keys):
        return extract(*keys).of(kwargs).then([].append)

    url_end_list: List[str] = ["https://libraries.io/api"]  # start of list to build url
    if action == "special_project_search":
        url_end_list.append("search?")
    elif action == "platforms":
        url_end_list.append("platforms")

    elif action.startswith("project"):
        action = action[7:]  # remove action prefix
        url_end_list += [*from_kwargs("platforms", "project"), *args]
        if action.startswith("_"):
            action = action[1:]  # remove remaining underscore from operation name
            if action == "dependencies":
                version = kwargs.pop("version") or "latest"  # defaults to latest
                url_end_list.append(version)
            url_end_list.append(action)
    elif action.startswith("repository"):
        action = action[len("repository") :]
        url_end_list += [*from_kwargs("host", "owner", "repo"), *args]
        if action.startswith("_"):
            url_end_list.append(action[1:])
    elif "user" in action:
        url_end_list += [*from_kwargs("host", "user"), *args]
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
    return url_end_list
