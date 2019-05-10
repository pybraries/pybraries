from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="pybraries",
    version="0.0.1",
    author="Jeff Hale",
    author_email="jeffmshale@gmail.com",
    description="A python wrapper for the libraries.io API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD 3-Clause License",
    ],
)
