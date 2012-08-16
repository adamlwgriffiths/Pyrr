#!/usr/bin/env python

from distutils.core import setup

from pyrr import __version__

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
