import requests
from requests.exceptions import HTTPError, RetryError
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import fire
import os
from pybraries.helpers import sess
import pybraries.wrapper  


class Mixin(object):

    def __call_api(self, thing, *args, **kwargs):
        """
        Calls the API.

        Args:
            thing (str): function name
            *args (str): positional arguments
            **kwargs (str): keyword arguments
        Returns:
            response (dict, list, or str): response from libraries.io. Many are dicts or list of dicts.
        """
            
        # response = {}                   # dictionary from api response to return
        url_end_list = ["https://libraries.io/api"]   # start of list to build url
        more_args = []             # for unpacking args
        url_combined = ""          # final string url
        
        if thing == "special_project_search":
            url_end_list.append('search?')

            # package seems to be ignored by the libraries.io API
            if "package" in kwargs:
                url_end_list.append(kwargs['package'])
            # params=dict(kwargs)  # append kwargs to params dict


            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            url_combined = '/'.join(url_end_list)

            try:
                r = sess.get(url_combined)
                r.raise_for_status()
                response = r.json()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  
            except Exception as err:
                print(f'Other error occurred: {err}')  

            return response

        def __check_prerelease(*args, **kwargs):
            prerelease = kwargs.pop('include_prerelease', '')
            return prerelease

        if "subscribe" in thing:
            url_end_list.append("subscriptions")

            pre = __check_prerelease(args, kwargs)

            if kwargs:
                if kwargs['manager']:
                    url_end_list.append(kwargs['manager'])
                    
                if kwargs['package']:
                    url_end_list.append(kwargs['package'])
                if pre:
                    if pre == "False" or pre == False:
                        url_end_list.append('include_prerelease=0')      
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            url_combined = '/'.join(url_end_list)

            call_type = ""                 # post, put or delete
            
            if thing == 'subscribe': call_type = 'post'
            if thing == "update_subscribe": call_type = 'put'
            if thing == "delete_subscribe": call_type = 'delete'

            try:
                if call_type == "post":
                    r = sess.post(url_combined)
                    print(url_combined)
                if call_type == 'put':
                    r = sess.put(url_combined)
                if call_type == 'delete':
                    r = sess.delete(url_combined)
                r.raise_for_status()
                response = r.json()
            except HTTPError as http_err:
                if http_err.code == 204 or http_err.code == 304:      
                    print(http_err.code)
                    response = f"Successfully unsubscribed from {kwargs['package']}"
                    pass
                else:
                    print(f'HTTP error occurred: {http_err}')  
            except RetryError as err:                             # for delete
                response = f"Not subscribed to {kwargs['package']} or unsubscribe unsuccessful"
                pass
            except Exception as err:
                print(f'Other error occurred: {err}')  
                response = err
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
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            if thing == 'pproject_dependencies':
                url_end_list.append("latest/")     # could make option to subscribe to other versions
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
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

            if thing == 'repository_dependencies':
                url_end_list.append("dependencies")

            if thing == 'repository_projects':
                url_end_list.append("projects")

        if "user" in thing:
            if kwargs:
                url_end_list.append(provider)
                url_end_list.append(user)
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args
            
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
        
        if thing == "check_subscription":
            url_end_list.append("subscriptions")
            if kwargs:
                if kwargs['manager']:
                    url_end_list.append(kwargs['manager'])
                if kwargs['package']:
                    url_end_list.append(kwargs['package'])
            if args:
                more_args = [arg for arg in args]
                url_end_list = url_end_list + more_args

        url_combined = '/'.join(url_end_list)

        try:
            r = sess.get(url_combined)
            r.raise_for_status()
            response = r.json()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  

        return response