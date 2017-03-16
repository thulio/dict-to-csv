# -*- coding: utf-8 -*-
import os.path
from setuptools import setup, find_packages

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name='dict-to-csv',
    version='0.1.2',
    packages=find_packages(exclude=('tests', 'tests.*')),
    install_requires=[
        'dotmap==1.2.16',
        'six==1.10.0',
        'typing==3.5.3.0; python_version == "2.7"',
    ],
    test_suite='tests',
    tests_require=[
        'mock==2.0.0; python_version == "2.7"',
    ],
    url='https://github.com/thulio/dict-to-csv',
    license='MIT',
    author='Thúlio Costa',
    author_email='contact@thul.io',
    description="Transform nested Python dictionaries to CSV lines",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
