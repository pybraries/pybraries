=============
Pybraries
=============

.. image:: https://travis-ci.org/pybraries/pybraries.svg?branch=master&kill_cache=1
    :target: https://travis-ci.org/pybraries/pybraries
    :alt: Travis Status

.. image:: https://coveralls.io/repos/github/pybraries/pybraries/badge.svg?branch=master&kill_cache=1
    :target: https://coveralls.io/github/pybraries/pybraries?branch=master
    :alt: coveralls

.. image:: https://readthedocs.org/projects/pybraries/badge/?version=latest&kill_cache=1
    :target: https://pybraries.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badgen.net/github/license/pybraries/pybraries?kill_cache=1
    :target: https://pybraries.readthedocs.io/en/latest/README.html
    :alt: License

.. image:: https://badgen.net/github/release/pybraries/pybraries?kill_cache=1
    :target: https://pybraries.readthedocs.io/en/latest/README.html
    :alt: Latest Release

.. image:: https://img.shields.io/pypi/wheel/pybraries.svg?kill_cache=1
    :target: https://pybraries.readthedocs.io/en/latest/README.html
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/pybraries.svg?kill_cache=1   
    :target: https://pybraries.readthedocs.io/en/latest/README.html
    :alt: PyPI - Python Version

Pybraries is a Python wrapper for the libraries.io API.

You can use it to subscribe to email alerts for
new versions of open source packages.

You can also use it to find information about
many aspects of open source packages and repositories.

The full documentation is hosted at `Read the Docs`_.

Quick Start
-----------

Install
_______

Install from PyPI.::

    pip install pybraries

Use
___

Get your API key from `libraries.io`_.

Set your API key as to the ``LIBRARIES_API_KEY`` environment variable from the command line with ::

    export LIBRARIES_API_KEY="your_libraries.io_api_key_goes_here"

Import the pybraries package and use it to subscribe to a package.

.. code:: python

    from pybraries.subscribe import Subscribe

    s = Subscribe()

    s.subscribe("pypi", "pandas")

Now you'll get an email update every time a new version of *pandas* is released.

Here's another example. 
Search for projects with *visualization* as a keyword and *python* as a language.
Sort by the number of stars.

.. code:: python

    from pybraries.search import Search

    search = Search()

    info = search.project_search(sort='stars', keywords='visualization', languages='python')
    print(info)

A list of dictionaries with project names and other project information is returned.


Note that the Libraries.io API is rate limited to 60 requests per minute.

All libraries.io methods are implemented, 
except updating a subscription to not include prereleases. 
This option can be toggled at the `libraries.io`_ website.


Search() and Subscribe() are the two classes in this package. 
See all their available methods by clicking on the methods in the `documentation`_.


Key Terms
_________

    *host* 
        A repository host platform. e.g. GitHub

    *owner* 
        A repository owner. e.g. pandas-dev

    *repo* 
        A repository. e.g. pandas

    *user* 
        A repository user  e.g. a GitHub username. e.g. discdiver

    *manager* 
        A package manager. e.g. PyPI

    *package* 
        A package distributed by a package manager. e.g. pandas


Note that many repos and packages share the same name. 
Many owners and repos also share the same name.
Further, many owners are also users.


Pybraries methods that return one item generally return a dict with information.

Methods that return multiple items return a list of dicts.

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

* Contributions are welcome and appreciated! See `Contributing`_.

License
_______

* `BSD-3-clause`_


.. _BSD-3-clause: https://github.com/pybraries/pybraries/blob/master/LICENSE
.. _Contributing: https://pybraries.readthedocs.io/en/latest/CONTRIBUTING.html
.. _Read the Docs: https://pybraries.readthedocs.io/en/latest/README.html
.. _documentation: https://pybraries.readthedocs.io/en/latest/README.html
.. _libraries.io: https://libraries.io
.. _GitHub: https://github.com/pybraries/pybraries/issues
.. _Stack Overflow: https://stackoverflow.com/questions/ask
