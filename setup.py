from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

requirements = ["requests>=2"]

setup(
    name="pybraries",
    version="0.0.1",
    author="Jeff Hale",
    author_email="jeffmshale@gmail.com",
    description="A python wrapper for the libraries.io API",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    url="https://github.com/pybraries/pybraries/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD 3-Clause License",
    ],
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
