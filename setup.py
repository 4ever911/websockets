# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-08-24 20:12:17
# @Last Modified by:   Evan
# @Last Modified time: 2016-08-24 23:08:53
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='websockets',

    version='3.2.2',

    description='websockets module for python2.7',

    url='https://github.com/evanzd/websockets',

    author='evanzd',
    author_email='dongzhou@pku.edu.cn',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='websockets',

    packages=['websockets'],

    install_requires=['trollius'],

    platforms='all',

)