from setuptools import setup, find_packages


def readme():
    with open("docs/README.rst") as f:
        return f.read()


setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

requirements = ["requests>=2", "fire>0.1.1"]

setup(
    name="pybraries",
    version="0.2.0",
    author="Jeff Hale",
    author_email="jeffmshale@gmail.com",
    description="A Python wrapper for the libraries.io API",
    long_description=readme(),
    url="https://github.com/pybraries/pybraries/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
    ],
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
