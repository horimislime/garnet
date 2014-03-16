#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'horimislime'

from setuptools import setup

setup(
    name='garnet',
    version='0.5',
    description='Utility to print git branches with associated Redmine ticket information',
    author='horimislime',
    author_email='horimislime@gmail.com',
    url='https://github.com/horimislime/garnet',
    packages=['src', 'src/util'],
    install_requires=[
        'requests',
        'legit',
        'GitPython'
    ],
    entry_points={
        'console_scripts': [
            'garnet = src.__main__:main'
        ]
    }
)
