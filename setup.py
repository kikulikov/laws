#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'laws',
    packages = ['laws'], # this must be the same as the name above
    version = '0.4',
    description = 'Filters AWS instances',
    author = 'Kirill Kulikov',
    author_email = 'kirill.kulikov@gmail.com',
    url='https://github.com/cyrillk/list-aws',
    download_url = 'https://github.com/cyrillk/list-aws/tarball/0.4',
    keywords = ['aws', 'ec2'],
    entry_points = {
        'console_scripts': ['laws=laws.__main__:main'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ],
    install_requires=['boto', 'tabulate'],
)
