#!/usr/bin/env python

import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# get pygly's version but don't import it
# or we'll need our dependencies already installed
# https://github.com/todddeluca/happybase/commit/63573cdaefe3a2b98ece87e19d9ceb18f00bc0d9
exec(open('pyrr/version.py').read())

setup(
    name = 'pyrr',
    version = __version__,
    description = '3D mathematical functions using NumPy',
    license = 'BSD',
    author = 'Adam Griffiths',
    author_email = 'adam.lw.griffiths@gmail.com',
    url = 'https://github.com/adamlwgriffiths/Pyrr',
    requires = [
        'numpy',
        ],
    platforms = [ 'any' ],
    test_suite = "pyrr.test",
    packages = [
        'pyrr',
        ],
    classifiers = [
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
