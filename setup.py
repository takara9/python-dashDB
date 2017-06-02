"""
python sample code that accessing dashDB on blumix or local 
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-dashDB',
    version='1.0.0',
    description='dashDB app for running Python apps on Bluemix',
    long_description=long_description,
    url='https://github.com/takara9/python-dashDB',
    license='MIT'
)


