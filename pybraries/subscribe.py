# subscribe_api.py
import fire
from pybraries.subscription_helpers import sub_api


class Subscribe(object):
    """Class for libraries.io API for changing user's libraries.io subscriptions"""

    def __init__(self):
        pass

    def list_subscribed(self, *args, **kwargs):
        """
        Return a list of packages a user is subscribed to for release notifications.

        Args:

        Returns:
            response (dict): dict response from libraries.io
        """
        return sub_api("list_subscribed", *args, **kwargs)

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
        return sub_api("subscribe", *args, **kwargs)

    def check_subscribed(self, *args, **kwargs):
        """
        Check if a user is subscribed to notifications for new project releases.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
        Returns:
            (bool): True if subscribed to given package, else False
        """
        return sub_api("check_subscribed", *args, **kwargs)

    def update_subscribe(self, *args, **kwargs):
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
        return sub_api("update_subscribe", *args, **kwargs)

    def unsubscribe(self, *args, **kwargs):
        """
        Stop receiving release notifications from a project.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name

        Returns:
            response (str or int): response header status from libraries.io
        """

        return sub_api("delete_subscribe", *args, **kwargs)


# From the command line you can call any public function by name with arguments
if __name__ == "__main__":
    fire.Fire(Subscribe)

    # subs = Subscribe()

    # sub = subs.list_subscribed()
    # print(sub)

    # x = subs.subscribe(manager="pypi", package="pandas")
    # print(x)

    # a = subs.unsubscribe(manager="pypi", package="pandas")
    # print(a)

    # y = subs.check_subscribed("pypi", "numpy")
    # print(y)

    # z = subs.update_subscription(manager="pypi", package="plotly",
    # include_prerelease="False")
    # print(z)
