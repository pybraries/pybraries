# subscription_helpers.py
from requests.exceptions import HTTPError
import fire
from helpers import sess
from make_request import make_request
from subscribe import Subscribe


def sub_api(action, *args, **kwargs):
    url_end_list = ["https://libraries.io/api"]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url
    call_type = ""  # post, put or delete

    # currently has no effect (perhaps due to libraries.io api glitch)
    def __check_prerelease(*args, **kwargs):
        prerelease = kwargs.pop("include_prerelease", "")
        return prerelease

    if action == "check_subscription":
        if response is not None:
            return True
        else:
            return False
    else:
        return response

    if "subscribe" in action:
        if action == "subscribe":
            call_type = "post"
        if action == "update_subscribe":
            call_type = "put"
        if action == "delete_subscribe":
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
            manager = args[1]
            package = args[2]

            more_args = [arg for arg in args]

        # first check if subscribed. Must be done before build url.
        check_pkg_subscribed = Subscribe.check_subscribed(manager, package)

        if call_type == "delete" and check_pkg_subscribed is None:
            msg = f"Unsubscribe unnecessary. You are not subscribed to {package}"
            return msg

        # reset url_end_list
        url_end_list = ["https://libraries.io/api", "subscriptions"]

        # pre = __check_prerelease(args, kwargs)

        if kwargs:
            if "manager" in kwargs:
                manager = kwargs["manager"]
            if "package" in kwargs:
                package = kwargs["package"]
            # if pre:
            #    if pre == "False" or pre == False:
            #       url_end_list.append('include_prerelease=0')
        if args:
            manager = args[1]
            package = args[2]

            more_args = [arg for arg in args]

        url_end_list.append(manager)
        url_end_list.append(package)
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

    if action == "list_subscriptions":
        url_end_list.append("subscriptions")

    if action == "check_subscription":
        url_end_list.append("subscriptions")
        if kwargs:
            if "manager" in kwargs:
                url_end_list.append(kwargs["manager"])
            if "package" in kwargs:
                url_end_list.append(kwargs["package"])
        if args:
            more_args = [arg for arg in args[1:]]
            url_end_list = url_end_list + more_args

    return make_request(url_end_list)
