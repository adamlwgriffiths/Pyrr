# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

'''
Created on 20/04/2012

@author: adam

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
'''

import numpy

from pyrr import vector


# the indices of each component in the
# ray array
class index:
    origin = 0
    direction = 1

def identity():
    return numpy.array(
        [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0,-1.0 ]
            ]
        )

def create_ray( start, direction ):
    return numpy.array(
        [
            start,
            vector.normalise( direction )
            ]
        )

def create_from_line( line ):
    """
    Converts a line or line segment to a ray.
    """
    # direction = vend - vstart
    return numpy.array(
        [
            line[ 0 ],
            vector.normalise( line[ 1 ] - line[ 0 ] )
            ]
        )

def origin( ray ):
    return ray[ 0 ]

def direction( ray ):
    return ray[ 1 ]

