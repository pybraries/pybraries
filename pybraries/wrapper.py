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

        url_end_list = ["https://libraries.io/api"]
        # list to append to base to build url

        if thing == "project":
            if kwargs:
                if kwargs['manager']:
                    url_end_list.append(kwargs['manager'])
                if kwargs['package']:
                    url_end_list.append(kwargs['package'])
            if args:
                args = list(args)
                # need to search list?
                if args[0]:
                    manager = args[0]
                if args[1]:
                    package = args[1]

        if thing == 'platforms':
            url_end_list.append('platforms')
            

        url_combined = '/'.join(url_end_list)
        print(url_combined)
        try:
            r = requests.get(
                url_combined,
                params=dict(api_key=self.api_key),
                timeout=5,
            )
            r.raise_for_status()
            response = r.json()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  

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

        output = self.__call_api("project", *args, **kwargs)
        return output

    def platforms(self, *args, **kwargs):
        """
        Return information about a package and its versions.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """

        output = self.__call_api("platforms", *args, **kwargs)
        return output

api = Api()
pkg = api.project(manager="pypi", package="plotly")

my_api = Api()
plats = my_api.platforms()

# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire(Api)
