# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

"""
A sphere is defined as a position (3d vector) and
a radius (float).
"""

import numpy

from pyrr.utils import all_parameters_as_numpy_arrays


class index:
    position = 0
    radius = 1

@all_parameters_as_numpy_arrays
def create_from_points( points ):
    """
    Creates a sphere centred around 0,0,0
    that encompasses the furthest point in
    the provided list.

    @return: Returns a sphere as a two value tuple.
    The first value is the sphere's position.
    The second value is the sphere's radius.
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

