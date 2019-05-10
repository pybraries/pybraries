import requests
import json
import fire


# api_key = my_api_key

def __call_api(api_key, manager, package):
    r = requests.get(f'https://libraries.io/api/{manager}/{package}?api_key={api_key}')
    return r.json()

def package_info(manager, package):
    result = __call_api(api_key, manager, package)
    print(result)



package_info("Pypi", "pandas")