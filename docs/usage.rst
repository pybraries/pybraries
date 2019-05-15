=====
Usage
=====

Use the pybraries API wrapper in a project to return a package name.

Set your the api_key environment variable to your libraries.io api_key. 

.. code:: python

    from pybraries import package_info

    package_info(api_key, manager, package)
