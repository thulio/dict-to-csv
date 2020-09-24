# -*- coding: utf-8 -*-
import os.path

from setuptools import find_packages, setup

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name="dict-to-csv",
    version="0.2.0",
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[
        "dotmap>=1.3.17",
    ],
    test_suite="tests",
    tests_require=[],
    url="https://github.com/thulio/dict-to-csv",
    license="MIT",
    author="Thúlio Costa",
    author_email="contact@thul.io",
    description="Transform nested Python dictionaries to CSV lines",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
