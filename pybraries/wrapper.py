import requests
import fire

def __call_api(api_key, manager, package):
    """
    Call the API for package manager info.
    Args:
        api_key (str): user api key
        manager (str): package manager
        package (str): package name
    Returns:
        r.json (json): response from libraries.io
    """
    if not isinstance(api_key, str):
        raise TypeError("Please provide your api key as a string.")

    r = requests.get(
        f'https://libraries.io/api/{manager}/{package}',
        params=dict(api_key=api_key),
        timeout=3,
    )
    response = r.json()

    return response


def package_info(api_key, manager, package):
    """
    Print result of API for package manager info.
    Args:
        manager (str): package manager
        package (str): package name
    Returns:
        r.json (json): response from libraries.io
    """
    result = __call_api(api_key, manager, package)
    print(result['name'])
    return 


if __name__ == "__main__":
    fire.Fire()
    