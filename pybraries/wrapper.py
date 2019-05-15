import requests
from requests.exceptions import HTTPError
import fire
import os

class Api:
    """The class for wrapping the libraries.io API
    """

    def __init__(self):
        self.api_key = os.environ['LIBRARIES_API_KEY']

        # check for valid API key

    def __call_api(self, thing, *args, **kwargs):
        """
        Call the API.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (dict): json response from libraries.io
        """
        response = {}
        # dictionary from api response to return

        if thing == "project":
            if kwargs:
                if kwargs['manager']:
                    manager = kwargs['manager'] 
                if kwargs['package']:
                    package = kwargs['package']
            if args:
                args = list(args)
                # need to search list?
                if args[0]:
                    manager = args[0]
                if args[1]:
                    package = args[1]

            try:
                r = requests.get(
                    f'https://libraries.io/api/{manager}/{package}',
                    params=dict(api_key=self.api_key),
                    timeout=5,
                )
                r.raise_for_status()
                response = r.json()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
            except Exception as err:
                print(f'Other error occurred: {err}')  # Python 3.6

        return response


    def project(self, *args, **kwargs):
        """
        Return information about a package and its versions.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """

        return self.__call_api("project", *args, **kwargs)




api = Api()
pkg = api.project(manager="pypi", package="plotly")

# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire(Api)
