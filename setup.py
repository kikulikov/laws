#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'laws',
    packages = ['laws'], # this must be the same as the name above
    version = '0.3',
    description = 'Filters AWS instances',
    author = 'Kirill Kulikov',
    author_email = 'kirill.kulikov@gmail.com',
    url='https://github.com/cyrillk/list-aws',
    download_url = 'https://github.com/cyrillk/list-aws/tarball/0.1',
    keywords = ['aws', 'ec2'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ],
    install_requires=['boto', 'tabulate']
)
