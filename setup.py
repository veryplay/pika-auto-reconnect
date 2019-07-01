#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import setup, find_packages

NAME = "pika_auto_reconnect"
DESCRIPTION = "Pika Auto Reconnect"
URL = "git@github.com:veryplay/pika-auto-reconnect.git"
EMAIL = "linuxcoming@qq.com"
AUTHOR = "linuxcoming@qq.com"
REQUIRES_PYTHON = ">=2.7"
VERSION = None

# What packages are required for this module to be executed?
INSTALL_REQUIRED = [
    "pika==1.0.1"
]

DEPENDENCY_LINKS = [

]


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if "README.md" is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except IOError:
    try:
        with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
            long_description = "\n" + f.read()
    except IOError:
        try:
            with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
                long_description = "\n" + f.read()
        except IOError:
            long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name = NAME,
    version = about["__version__"],
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = EMAIL,
    platforms = "any",
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points = {
        "console_scripts": [
            "pika_auto_reconnect = pika_auto_reconnect.rabbitmq:main"
        ],
    },
    install_requires = INSTALL_REQUIRED,
    dependency_links = DEPENDENCY_LINKS,
    include_package_data = True,
    license = "GPL",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Natural Language :: Chinese",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    zip_safe = False
)
