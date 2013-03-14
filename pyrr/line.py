# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Lines.

A Line data structure is simply a numpy.array with 2 vectors::

    start = numpy.array( [ -1.0, 0.0, 0.0 ] )
    end = numpy.array( [ 1.0, 0.0, 0.0 ] )
    line = numpy.array( [ start, end ] )

Both Lines and Line Segments are defined using the same data structure.
The only difference is how the data is interpreted.

A line is defined by two points but extends infinitely.

A line segment only exists between two points.
It does not extend forever.

The choice to interprete a line as a line or line segment is up to the
function being called. Check the function signature of documentation
to determine how a line will be interpreted.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr import vector


class index:
    #: The index of the start vector within the line
    start = 0

    #: The index of the end vector within the line
    end = 1


def create_zeros():
    """Creates a line with the start and end at the origin.

    :rtype: A numpy.array with shape (2,3).
    """
    return numpy.zeros( (2,3) )

def create_from_points( v1, v2 ):
    """Creates a line from 2 vectors.

    The 2 vectors represent the start and end point of the line.

    :param numpy.array v1: Start point.
    :param numpy.array v2: End point.
    :rtype: A numpy.array with shape (2,3).
    """
    return numpy.array( [ v1, v2 ] )

def create_from_ray( ray ):
    """Converts a ray to a line.

    The line will extend from 'ray origin -> ray origin + ray direction'.

    :param numpy.array ray: The ray to convert.
    :rtype: A numpy.array with shape (2,3).
    """
    # convert ray relative direction to absolute
    # position
    return numpy.array( [ ray[ 0 ], ray[ 0 ] + ray[ 1 ] ] )

def start( line ):
    """Extracts the start point of the line.

    :param numpy.array line: The line to extract the start from.
    :rtype: A numpy.array with shape 3.
    """
    return line[ 0 ]

def end( line ):
    """Extracts the end point of the line.

    :param numpy.array line: The line to extract the end from.
    :rtype: A numpy.array with shape 3.
    """
    return line[ 1 ]

