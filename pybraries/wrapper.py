import requests
from requests.exceptions import HTTPError
import fire
import os

class Api:
    """The class for wrapping the libraries.io API
    """

    def __init__(self):
        self.api_key = os.environ['LIBRARIES_API_KEY']
        # TODO
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
                # this is kind of hacky
                args[0] = url_end_list.append(args[0])
                if args[1]:
                    url_end_list.append(args[1])

        if thing == 'platforms':
            url_end_list.append('platforms')

        if thing == "user_packages":
            if kwargs:
                url_end_list.append(provider)
                url_end_list.append(user)
            if args:
                args = list(args)
                args[0] = url_end_list.append(args[0])
                args[1] = url_end_list.append(args[1])
            url_end_list.append("project-contributions")


        # if thing == "user_repositories":
            

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

        Returns:
            r.json (json): response from libraries.io
        """

        output = self.__call_api("platforms", *args, **kwargs)
        return output

    def user_packages(self, *args, **kwargs):
        """
        Return information about packages a user has contributed to.
        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            r.json (json): response from libraries.io
        """
        output = self.__call_api("user_packages", *args, **kwargs)
        return output

api = Api()
x = api.user_packages("github", "discdiver")
print(x)

# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire(Api)
