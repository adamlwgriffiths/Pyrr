# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of 3D Spheres.

A sphere is defined as tuple with two values.
The first value is the sphere's position as a numpy.array with shape 3.
The second value is the sphere's radius as a float.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr.utils import all_parameters_as_numpy_arrays


class index:
    #: The index of the position vector within the sphere
    position = 0

    #: The index of the radius within the sphere
    radius = 1


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
    return (
        numpy.array(
            [ 0.0, 0.0, 0.0 ],
            dtype = numpy.float
            ),
        radius
        )

