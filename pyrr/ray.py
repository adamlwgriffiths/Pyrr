# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Rays.

A ray begins as a single point and extends
infinitely in a direction.

The first vector is the origin of the ray.
The second vector is the direction of the ray
relative to the origin.

The following functions will normalise the ray
direction to unit length.
Some functions may work correctly with directions
that are not unit length, but this may vary from
function to function.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr import vector
from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


class index:
    #: The index of the origin vector within the ray
    origin = 0

    #: The index of the direction vector within the ray
    direction = 1


def create_identity(dtype=None):
    return numpy.array(
        [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0,-1.0 ]
        ],
        dtype=dtype
    )

@parameters_as_numpy_arrays('start', 'direction')
def create_ray(start, direction, dtype=None):
    dtype = dtype or start.dtype
    return numpy.array(
        [
            start,
            vector.normalise(direction)
        ],
        dtype=dtype
    )

@parameters_as_numpy_arrays('line')
def create_from_line(line, dtype=None):
    """
    Converts a line or line segment to a ray.
    """
    dtype = dtype or line.dtype
    # direction = vend - vstart
    return numpy.array(
        [
            line[0],
            vector.normalise(line[1] - line[0])
        ],
        dtype=dtype
    )

def origin(ray):
    return ray[0].copy()

def direction(ray):
    return ray[1].copy()

