# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of 3D Spheres.

A sphere is defined as a 4D vector.
The first three values are the sphere's position.
The fourth value is the sphere's radius.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr.utils import all_parameters_as_numpy_arrays

@all_parameters_as_numpy_arrays
def create_from_points( points ):
    """Creates a sphere centred around 0,0,0 that encompasses
    the furthest point in the provided list.

    :param numpy.array points: An Nd array of vectors.
    :rtype: A sphere as a two value tuple.
    """
    # calculate the lengths of all the points
    # use squared length to save processing
    lengths = numpy.apply_along_axis(
        numpy.sum,
        points.ndim - 1,
        points**2
        )

    # find the maximum value
    maximum = lengths.max()

    # square root this, this is the radius
    radius = numpy.sqrt( maximum )
    return numpy.array( [ 0.0, 0.0, 0.0, radius ] )

def position( sphere ):
    return sphere[ :3 ]

def radius( sphere ):
    return sphere[ 3 ]
