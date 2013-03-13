# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Lines.

A line is defined by two points but extends
infinitely.

A line segment only exists between two points.
It does not extend forever.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr import vector

class index:
    start = 0
    end = 1

def create_zeros():
    return numpy.zeros( (2,3) )

def create_from_points( v1, v2):
    """
    Creates a line from 2 independent vectors.
    This is just a convenience function that wraps
    two vectors into a single array.
    """
    return numpy.array( [ v1, v2 ] )

def create_from_ray( ray ):
    """
    Converts a ray to a line.
    """
    # convert ray relative direction to absolute
    # position
    return numpy.array( [ ray[ 0 ], ray[ 0 ] + ray[ 1 ] ] )

def start( line ):
    return line[ 0 ]

def end( line ):
    return line[ 1 ]

