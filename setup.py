#!/usr/bin/env python

from setuptools import setup

setup(
    name='laws',
    packages=['laws'],
    version='0.6.1',
    description='-ls- for AWS EC2 instances',
    long_description='https://github.com/cyrillk/laws/README.md',
    author='Kirill Kulikov',
    author_email='kirill.kulikov@gmail.com',
    url='https://github.com/cyrillk/laws',
    download_url='https://github.com/cyrillk/laws/tarball/0.6.1',
    keywords=['aws', 'ec2'],
    entry_points={
        'console_scripts': ['laws=laws.__main__:main'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ],
    install_requires=['boto3', 'tabulate'],
)
