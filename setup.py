#!/usr/bin/env python

from setuptools import setup, find_packages



setup(
    name='tablette',
    version='0.0.1',
    description='Convert tabular data to json',
    author='Alberto Granzotto',
    author_email='agranzot@gmail.com',

    packages = find_packages(exclude=['tests']),

    zip_safe = True,

    test_suite = 'tests'
)

