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

Pybraries is a Python wrapper for the libraries.io API.

Use it to subscribe to and unsubscribe from upates
to packages on any package manager.

You can also use pybraries to find information about
many aspects related to repos and packages.

Quick Start
-----------

Install
_______

Install from PyPI.::

    pip install pybraries

Use
___

Get your API key from `libraries.io`_.

Set your API key as an environment variable from the command line with ::

    export LIBRARIES_API_KEY="your_libraries.io_api_key_goes_here"

Import the pybraries package and use it to subscribe to a package.

.. code:: python

    from pybraries import Libraries_API

    api = Libraries_API()

    api.subscribe("pypi", "pandas")

Now you're subscribed to updates to the pandas package.

Here's another example.

Import the pybraries package and use it to subscribe to a package.

.. code:: python

    from pybraries import Libraries_API

    api = Libraries_API()

    api.project_search("pypi", sort='stars', 'keywords'])

Now you're subscribed to updates to the pandas package.

Note that the Libraries.io API is rate limited to 60 requests per minute.

All libraries.io methods are implemented, 
except updating a subscription to not include prereleases. 
This option can be toggled on the `libaries.io`_ website.

Docs
____

* Check out the full pybraries `documentation`_.

Getting Help
____________

1. Check out the pybraries docs.
2. Check out the libraries.io docs.
3. Open an issue on `GitHub`_ or tag a question on `Stack Overflow`_ with "pybraries".

Contributing
____________

* Contributions are welcome and appreciated! See `contributing`_.

License
_______

* `BSD-3-clause: <https://github.com/pybraries/pybraries/blob/master/LICENSE>`_


.. _contributing: https://pybraries.readthedocs.io/contributing
.. _documentation: https://pybraries.readthedocs.io
.. _libraries.io: https://libraries.io
.. _GitHub: https://github.com/pybraries/pybraries/issues
.. _Stack Overflow: https://stackoverflow.com/questions/ask