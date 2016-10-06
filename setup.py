#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'laws',
    packages = ['laws'], # this must be the same as the name above
    version = '0.5',
    description = 'Lists AWS instances',
    long_description=open('README.md', 'rt').read(),
    author = 'Kirill Kulikov',
    author_email = 'kirill.kulikov@gmail.com',
    url='https://github.com/cyrillk/laws',
    download_url = 'https://github.com/cyrillk/laws/tarball/0.5',
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
