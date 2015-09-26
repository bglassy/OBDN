#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
import re
import os
import sys

PY26 = sys.version_info[:2] == (2, 6)


long_description = (
    "OpenBazaar Documentation."
)


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """Return root package and all sub-packages."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name="obdocs",
    version=get_version("obdocs"),
    url='http://docs.openbazaar.org',
    license='BSD',
    description='OpenBazaar Documentation',
    long_description=long_description,
    author='bglassy',
    author_email='braden@openbazaar.org',  # SEE NOTE BELOW (*)
    packages=get_packages("obdocs  "),
    package_data=get_package_data("obdocs"),
    install_requires=[
        'click>=4.0',
        'ghp-import>=0.4.1',
        'Jinja2>=2.7.1',
        'livereload>=2.3.2',
        'Markdown>=2.3.1,<2.5' if PY26 else 'Markdown>=2.3.1',
        'PyYAML>=3.10',
        'six>=1.9.0',
        'tornado>=4.1',
    ],
    entry_points={
        'console_scripts': [
            'obdocs = obdocs.cli:cli',
        ],
    },
    zip_safe=False
)
