#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def read_req(req_file):
    with open(req_file) as req:
        return [line for line in req.readlines() if line and not line.isspace()]


requirements = read_req('requirements.txt')
requirements_validation = read_req('requirements_validation.txt')
requirements_dev = read_req('requirements_dev.txt')
requirements_test = read_req('requirements_test.txt')
0
setup(
    name='drf-swagger',
    version='1.0.0rc1',
    packages=find_packages(include=['drf_swagger']),
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements_test,
    extras_require={
        'validation': requirements_validation
    },
    license='BSD License',
    description='Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code.',
    long_description='',
    url='https://github.com/axnsan12/drf-swagger',
    author='Cristi V.',
    author_email='cristi@cvjd.me',
    keywords='drf-swagger drf django rest-framework schema swagger openapi ',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
