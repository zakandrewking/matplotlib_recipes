# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

setup(
    name='mpl_recipes',
    version='0.0.1',
    author='Zachary King',
    url='https://github.com/zakandrewking/mpl_recipes',
    packages=['mpl_recipes']
)
