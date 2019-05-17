=============
Pybraries
=============

.. image:: https://travis-ci.org/pybraries/pybraries.svg?branch=master
    :target: https://travis-ci.org/pybraries/pybraries

.. image:: https://coveralls.io/repos/github/pybraries/pybraries/badge.svg?branch=master 
    :alt: coveralls  
    :target: https://coveralls.io/github/pybraries/pybraries?branch=master

.. image:: https://readthedocs.org/projects/pybraries/badge/?version=latest 
    :target: https://pybraries.readthedocs.io/en/latest/?badge=latest 
    :alt: Documentation Status
      
Pybraries is a wrapper for the libraries.io API.

We hope you enjoy it. If you see something that could be improved, please let us know.

Quick Start
-----------

Install
_______

Install from PyPI.::

    pip install pybraries

Use
___

Get your API key from `libraries.io`_.

Set it as an environment variable from the command line with ::

    export API_KEY="your_api_key_goes_here"

Import the package and use it with

.. code:: python

    import pybraries
    import os

    api_key = os.environ['API_KEY']

    package_info(api_key, manager, package)

The package name should be returned.

Note that you can only call the API at a rate of once per second.


License
_______

* BSD-3-clause: https://github.com/pybraries/pybraries/blob/master/LICENSE

Docs
____

* Documentation: https://pybraries.readthedocs.io.

Contributing
____________

Contributions are appreciated. See Contributing.

.. _libraries.io: https://libraries.io


