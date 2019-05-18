import requests
from requests.exceptions import HTTPError
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
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
        # list to build url

        url_combined = ""
        # final string url
        
        # special case #1
        if thing == "special_project_search":
            url_end_list.append('search?')

            # package seems to be ignored by the libraries.io API
            if "package" in kwargs:
                url_end_list.append(kwargs['package'])

            url_combined = '/'.join(url_end_list)

            with requests.Session() as s:
                retries = Retry(
                    total=10,
                    backoff_factor=0.2,
                    status_forcelist=[500, 502, 503, 504])

                s.mount('https://', HTTPAdapter(max_retries=retries))

                try:
                    r = s.get(
                        url_combined,
                        params=dict(
                            kwargs,
                            api_key=self.api_key),
                            # add args support
                        timeout=5,
                    )
                    r.raise_for_status()
                    response = r.json()
                except HTTPError as http_err:
                    print(f'HTTP error occurred: {http_err}')  
                except Exception as err:
                    print(f'Other error occurred: {err}')  

            return response

        # special case #2
        if thing == "subscribe":
            url_end_list.append("subscriptions")

            if kwargs:
                if kwargs['manager']:
                    url_end_list.append(kwargs['manager'])
                if kwargs['package']:
                    url_end_list.append(kwargs['package'])
            if args:
                args = list(args)
                args[0] = url_end_list.append(args[0])
                if args[1]:
                    url_end_list.append(args[1])

            url_combined = '/'.join(url_end_list)

            with requests.Session() as s:
                retries = Retry(
                    total=10,
                    backoff_factor=0.3,
                    status_forcelist=[500, 502, 503, 504])

                s.mount('https://', HTTPAdapter(max_retries=retries))

                try:
                    r = s.post(
                        url_combined,
                        params=dict(
                            api_key=self.api_key),
                        timeout=10,
                    )
                    print(r)
                    r.raise_for_status()
                    response = r.json()
                except HTTPError as http_err:
                    print(f'HTTP error occurred: {http_err}')  
                except Exception as err:
                    print(f'Other error occurred: {err}')  
            return response

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

            if thing == 'pproject_dependents':
                url_end_list.append("dependendents")
            
            if thing == 'pproject_dependent_repositories':
                url_end_list.append("dependendent_repositories")

            if thing == 'pproject_contributors':
                url_end_list.append("contributors")

            if thing == 'pproject_sourcerank':
                url_end_list.append("sourcerank")
            
            if thing == 'pproject_usage':
                url_end_list.append("usage")

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
            

        if thing == "list_subscriptions":
            url_end_list.append("subscriptions")
        
        if thing == "subscribed":
            url_end_list.append("subscriptions")
            if kwargs:
                if kwargs['manager']:
                    url_end_list.append(kwargs['manager'])
                if kwargs['package']:
                    url_end_list.append(kwargs['package'])
            if args:
                args = list(args)
                args[0] = url_end_list.append(args[0])
                if args[1]:
                    url_end_list.append(args[1])


        url_combined = '/'.join(url_end_list)
        print(url_combined)

        with requests.Session() as s:
            retries = Retry(
                total=10,
                backoff_factor=0.2,
                status_forcelist=[500, 502, 503, 504])

            s.mount('https://', HTTPAdapter(max_retries=retries))

            try:
                r = s.get(
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

    # public methods 
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

        if thing == 'subscribe':
            url_end_list.append('subscriptions')


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

    def project_contributors(self, *args, **kwargs):
        """
        Get users that have contributed to a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (list): list of dicts response from libraries.io
        """

        return self.__call_api("pproject_contributors", *args, **kwargs)


    def project_sourcerank(self, *args, **kwargs):
        """
        Get breakdown of SourceRank score for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (dict): sourcerank info response from libraries.io
        """

        return self.__call_api("pproject_sourcerank", *args, **kwargs)


    def project_usage(self, *args, **kwargs):
        """
        Get breakdown of version usage for a given project.

        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            response (dict): verion usage info response from libraries.io
        """

        return self.__call_api("pproject_usage", *args, **kwargs)

    def project_search(self, *args, **kwargs):
        """
        Search for projects.

        Args:
            package (optional)(str): package name
            sort= (optional) (str): one of rank, stars, dependents_count, dependent_repos_count, latest_release_published_at, contributions_count, created_at
            filter= (optional) (list): list of strings. Options: languages, licenses, keywords, platforms
        Returns:
            response (list): list of dicts containing project info response from libraries.io
        """

        return self.__call_api("special_project_search", *args, **kwargs)





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

    def list_subscriptions(self, *args, **kwargs):
        """
        Return a list of packages a user is subscribed to for release notifications.

        Args:
      
        Returns:
            response (dict): dict response from libraries.io
        """
        return self.__call_api("list_subscriptions", *args, **kwargs)

    def subscribe(self, *args, **kwargs):
        """
        Subscribe to receive notifications about new releases of a project.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
            include_prelease (bool): default = True. Include prerelease notifications
        Returns:
            response (dict): dict of project info from libraries.io
        """
        return self.__call_api("subscribe", *args, **kwargs)

    def check_subscribed(self, *args, **kwargs):
        """
        Check if a users is subscribed to receive notifications about new releases of a project.

        Args:
            manager (str): package manager name (e.g. PyPI)
            package (str): package name
        Returns:
            response (dict): dict of project info from libraries.io
            # make so a 404 for not found returns a nice message 
            # maybe return true if dict not empty, false if 404
            # return error earlier if can't connect, server issue, etc.
        """
        return self.__call_api("subscribed", *args, **kwargs)



# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire(Api)

    api = Api()
    
    y = api.subscribe(manager="pypi", package="yellowbrick")
    print(y)
    # y = api.check_subscribed('pypi', 'yellowbrick')
    # print(y)