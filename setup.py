from setuptools import setup, find_packages

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

requirements = ["requests>=2"]

setup(
    name="pybraries",
    version="0.0.1",
    author="Jeff Hale",
    author_email="jeffmshale@gmail.com",
    description="A Python wrapper for the libraries.io API",
    url="https://github.com/pybraries/pybraries/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD 3-Clause License",
    ],
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
