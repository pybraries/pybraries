# subscription_helpers.py
from requests.exceptions import HTTPError
import fire
from pybraries.helpers import sess, clear_params
from pybraries.make_request import make_request


def sub_api(action, *args, **kwargs):
    url_end_list = [
        "https://libraries.io/api/subscriptions"
    ]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url
    call_type = ""  # post, put or delete
    manager = ""
    package = ""
    kind = "get"

    if kwargs:
        if "manager" in kwargs:
            manager = kwargs["manager"]
        if "package" in kwargs:
            package = kwargs["package"]

    if args:
        if args[0]:
            manager = args[0]
        if args[1]:
            package = args[1]

    if action == "list_subscribed":
        url_combined = "/".join(url_end_list)
        resp = make_request(url_combined, kind)
        return resp

    if action == "check_subscribed":
        # do we need to check for args?
        url_end_list.append(manager)
        url_end_list.append(package)
        url_combined = "/".join(url_end_list)

        check = make_request(url_combined, kind)

        if check is not None:
            r_bool = True
        else:
            r_bool = False

        return r_bool

    if action == "subscribe":
        kind = "post"
        url_end_list.append(manager)
        url_end_list.append(package)

        url_combined = "/".join(url_end_list)
        return make_request(url_combined, kind)

    if action == "update_subscribe":
        kind = "put"
        # not implemented - seems libraries.io api has bug
        # if implemented in future, adjust modules in readme
        url_end_list.append(manager)
        url_end_list.append(package)

        url_combined = "/".join(url_end_list)
        return make_request(url_combined, kind)

    if action == "delete_subscribe":
        kind = "delete"
        url_end_list.append(manager)
        url_end_list.append(package)
        url_combined = "/".join(url_end_list)

        # first check if subscribed. Must be done before build url.
        check_pkg_subscribed = sub_api(
            "check_subscribed", manager=manager, package=package
        )

        if check_pkg_subscribed is False:
            msg = f"Unsubscribe unnecessary. You are not subscribed to {package}."
            return msg
        else:
            return make_request(url_combined, kind)

        # prerelease option ccurrently not changeable for subscribe or update
        # (perhaps due to libraries.io api glitch)
        def __check_prerelease(*args, **kwargs):
            prerelease = kwargs.pop("include_prerelease", "")
            return prerelease
