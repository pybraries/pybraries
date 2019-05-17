import requests
from requests.exceptions import HTTPError
import fire
import os
import pdb

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
        # list to build url

        url_combined = ""
        # final string url


        if thing == 'platforms':
            url_end_list.append('platforms')

        if "pproject" in thing:
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

            if thing == 'pproject_dependencies':
                url_end_list.append("latest/")
                url_end_list.append("dependencies")

            if thing == 'ppproject_dependents':
                url_end_list.append("dependendents")
            
            if thing == 'ppproject_dependent_repositories':
                url_end_list.append("dependendent_repositories")


            # if "thing == project_search":
            # The search endpoint accepts a sort parameter, 
            # one of 
            # rank, stars, dependents_count, 
            # dependent_repos_count, latest_release_published_at, 
            # contributions_count, created_at

            # The search endpoint accepts number of other parameters to filter results:

            # languages
            # licenses
            # keywords
            # platforms

        if 'repository' in thing:
            if kwargs:
                url_end_list.append(provider)
                url_end_list.append(owner)
                url_end_list.append(repo)
            if args:
                args = list(args)
                args[0] = url_end_list.append(args[0])
                args[1] = url_end_list.append(args[1])
                args[2] = url_end_list.append(args[2])

            if thing == 'repository_dependencies':
                url_end_list.append("dependencies")

            if thing == 'repository_projects':
                url_end_list.append("projects")


        if "user" in thing:
            if kwargs:
                url_end_list.append(provider)
                url_end_list.append(user)
            if args:
                args = list(args)
                args[0] = url_end_list.append(args[0])
                args[1] = url_end_list.append(args[1])
            
            if thing == "user_repositories":
                url_end_list.append("repositories")

            if thing == "user_packages": 
                url_end_list.append("projects")

            if thing == "user_packages_contributions":
                url_end_list.append("project-contributions")

            if thing == "user_repositories_contributions":
                url_end_list.append("repository-contributions")
            
            if thing == "user_dependencies":
                url_end_list.append("dependencies")
            
            if thing == "user_subscriptions":
                url_end_list.append("subscriptions")


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


    def platforms(self, *args, **kwargs):
        """
        Return a list of supported package managers.

        Args:

        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("platforms", *args, **kwargs)


    def project(self, *args, **kwargs):
        """
        Return information about a package and its versions from a platform (e.g. PyPI).

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (dict): response from libraries.io
        """

        return self.__call_api("pproject", *args, **kwargs)


    def project_dependencies(self, *args, **kwargs):
        """
        Get a list of dependencies for a version of a project.
        
        Returns latest version info.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            response (dict): response from libraries.io
        """

        return self.__call_api("pproject_dependencies", *args, **kwargs)


    def project_dependents(self, *args, **kwargs):
        """
        Get packages that have at least one version that depends on a given project.

        Args:
            manager (str): package manager
            package (str): package name
            version (str): package version
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_dependendents", *args, **kwargs)


    def project_dependent_repositories(self, *args, **kwargs):
        """
        Get repositories that depend on a given project.

        Args:
            manager (str): package manager
            package (str): package name

        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_dependendent_repositories", *args, **kwargs)





    def repository(self, *args, **kwargs):
        """
        Return information about a reposiotory and its versions.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("repository", *args, **kwargs)

    def repository_dependencies(self, *args, **kwargs):
        """
        Return information about a repository's dependencies.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (dict): dict response from libraries.io
        """

        return self.__call_api("repository_dependencies", *args, **kwargs)

    def repository_projects(self, *args, **kwargs):
        """
        Get a list of packages referencing the given repository.

        Args:
            provider (str): host provider name (e.g. GitHub)
            owner (str): owner
            repo (str): repo
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("repository_projects", *args, **kwargs)
        


    def user(self, *args, **kwargs):
        """
        Return information about a user.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (dict): response from libraries.io
        """
        return self.__call_api("user", *args, **kwargs)

    def user_repositories(self, *args, **kwargs):
        """
        Return information about a user's repos.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            respons (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_repositories", *args, **kwargs)

    def user_packages(self, *args, **kwargs):
        """
        Return information about packages using a user's repos.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_packages", *args, **kwargs)

    def user_packages_contributions(self, *args, **kwargs):
        """
        Return information about packages a user has contributed to.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_packages_contributions", *args, **kwargs)
    
    def user_repository_contributions(self, *args, **kwargs):
        """
        Return information about repositories a user has contributed to.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_repositories_contributions", *args, **kwargs)

    def user_dependencies(self, *args, **kwargs):
        """
        Return Get a list of unique packages that the given user's repositories list as a dependency. 
        
        Ordered by frequency of use in those repositories.

        Args:
            provider (str): host (e.g. github)
            user (str): username
        Returns:
            response (list): list of dicts response from libraries.io
        """
        return self.__call_api("user_dependencies", *args, **kwargs)

    def user_subscriptions(self, *args, **kwargs):
        """
        Return a list of packages a user is subscribed to for release notifications.

        Args:
      
        Returns:
            response (dict): dict response from libraries.io
        """
        return self.__call_api("user_subscriptions", *args, **kwargs)


api = Api()
x = api.repository_projects("github", "pandas-dev", "pandas")

print(type(x))
print(x)



# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire(Api)
