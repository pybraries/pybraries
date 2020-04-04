from typing import Union

from pybraries.helpers import extract
from pybraries.make_request import make_request


def sub_api(action, manager="", package="", *args, **kwargs) -> Union[bool, str]:
    url_end_list = [
        "https://libraries.io/api/subscriptions"
    ]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url
    kind = "get"  # get, post, put or delete

    if action == "list_subscribed":
        url_combined = "/".join(url_end_list)
        resp = make_request(url_combined, kind)
        return resp

    assert manager and package, "this operation requires manager and package definition"

    url_end_list += [manager, package]
    url_combined = "/".join(url_end_list)

    if action == "check_subscribed":
        resp = make_request(url_combined, kind)
        return resp is not None
    if action == "subscribe":
        extract("include_prerelease").of(kwargs).then(url_end_list.append)
        kind = "post"
        make_request(url_combined, kind)
        return "Successfully Subscribed"

    if action == "update_subscribe":
        kind = "put"
        # not implemented - seems libraries.io api has bug
        # if implemented in future, adjust modules in readme
        make_request(url_combined, kind)
        return "include_prerelease is always set to true"

    if action == "delete_subscribe":
        kind = "delete"

        # first check if subscribed. Must be done before build url.
        is_subscribed = sub_api(
            "check_subscribed", manager=manager, package=package
        )

        if is_subscribed:
            make_request(url_combined, kind)
            msg = "Successfully Unsubscribed"
        else:
            msg = f"Unsubscribe unnecessary. You are not subscribed to {package}."
        return msg


# prerelease option currently not changeable for subscribe or update
# (perhaps due to libraries.io api glitch)
def __check_prerelease(*args, **kwargs):
    prerelease = kwargs.pop("include_prerelease", "")
    return prerelease
