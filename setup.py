# -*- coding: utf-8 -*-
import os.path
from setuptools import setup, find_packages

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name='dict-to-csv',
    version='0.1.3',
    packages=find_packages(exclude=('tests', 'tests.*')),
    install_requires=[
        'dotmap==1.2.17',
        'six==1.10.0',
        'typing==3.5.3.0; python_version < "3.5"',
    ],
    test_suite='tests',
    tests_require=[
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
