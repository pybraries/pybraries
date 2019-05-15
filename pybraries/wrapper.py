import requests
import fire
import os

# api_key = os.environ['LIBRARIES_API_KEY']
class API:
    def __init__(self):
        self.api_key = os.environ['LIBRARIES_API_KEY']


    def __call_api(self, manager, package, *args, **kwargs):
        """
        Call the API.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """
        if not isinstance(self.api_key, str):
            raise TypeError("Please provide your api key as a string.")

        r = requests.get(
            f'https://libraries.io/api/{manager}/{package}',
            params=dict(api_key=self.api_key),
            timeout=3,
        )
        response = r.json()

        return response


    def project(self, manager, package):
        """
        Return information about a package and its versions.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """
        manager = manager.lower()
        x = self.__call_api(manager, package)
        return x

api = API()
pkg = api.package_info("pypi", "plotly")
print(pkg['platform'])


# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire()
