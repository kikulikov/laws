#!/bin/bash

pip install twine wheel

python setup.py egg_info
python setup.py sdist bdist_wheel

twine upload dist/*
