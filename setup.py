#!/usr/bin/env python

from distutils.core import setup

import pyrr

setup(
    name = 'Pyrr',
    version = pyrr.__version__,
    description = '3D mathematical functions using NumPy',
    license = 'MIT',
    author = 'Adam Griffiths',
    author_email = 'adam.lw.griffiths@gmail.com',
    url = 'https://github.com/adamlwgriffiths/Pyrr',
    platforms = [ 'any' ],
    packages = [ 'pyrr', ],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
