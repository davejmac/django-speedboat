#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'Django >= 1.7',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Django-TestApp',
    version='0.1.0',
    description="Django Test App",
    long_description=readme + '\n\n' + history,
    author="Dave",
    author_email='dave@mobelux.com',
    url='',
    packages=[
        'testapp',
    ],
    package_dir={'testapp':
                 'testapp'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='testapp',
    # classifiers=[
    #     'Development Status :: 2 - Pre-Alpha',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: BSD License',
    #     'Natural Language :: English',
    #     "Programming Language :: Python :: 2",
    #     'Programming Language :: Python :: 2.6',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.3',
    #     'Programming Language :: Python :: 3.4',
    # ],
    test_suite="testrunner.run_tests",
    # tests_require=test_requirements
)
