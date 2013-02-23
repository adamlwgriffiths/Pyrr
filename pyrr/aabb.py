# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

""" Provides functions to calculate and manipulate
Axis-Aligned Bounding Boxes (AABB).

AABB are a simple 3D rectangle with no orientation.
It is up to the user to provide translation.

An AABB is represented by an array of 2 x 3D vectors.
The first vector represents the minimum extent.
The second vector represents the maximum extent.

It should be noted that rotating the object within
an AABB will invalidate the AABB.
It is up to the user to either:
    * recalculate the AABB.
    * use an AAMBB instead.

TODO: add transform( matrix )
"""

import numpy

from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


class index:
    minimum = 0
    maximum = 1

def zeros():
    return numpy.zeroes( (2,3) )

def create_from_bounds( min, max):
    """ Creates an AABB using the specified minimum
    and maximum values.
    """
    return numpy.array( [ min, max ] )

def create_from_points( points ):
    """ Creates an AABB from the list of specified points.

    Points must be a 2D list. Ie:
    [
        [ x, y, z ],
        [ x, y, z ],
    ]
    """
    return numpy.array(
        [
            numpy.amin( points, axis = 0 ),
            numpy.amax( points, axis = 0 )
            ]
        )

@all_parameters_as_numpy_arrays
def create_from_aabbs( aabbs ):
    """ Creates an AABB from a list of existing AABBs.

    AABBs must be a 2D list. Ie:
    [
        AABB,
        AABB,
    ]
    """
    # reshape the AABBs as a series of points
    points = aabbs.reshape( (-1, 3 ) )

    return create_from_points( points )

def add_points( aabb, points ):
    """ Extends an AABB to encompass a list
    of points.
    """
    # find the minimum and maximum point values
    minimum = numpy.amin( points, axis = 0 )
    maximum = numpy.amax( points, axis = 0 )

    # compare to existing AABB
    return numpy.array(
        [
            numpy.minimum( aabb[ 0 ], minimum ),
            numpy.maximum( aabb[ 1 ], maximum )
            ]
        )

@parameters_as_numpy_arrays( 'aabbs' )
def add_aabbs( aabb, aabbs ):
    """ Extend an AABB to encompass a list
    of other AABBs.
    """
    # convert to points and use our existing add_points
    # function
    points = aabbs.reshape( (-1, 3) )

    return add_points( aabb, points )

@all_parameters_as_numpy_arrays
def centre_point( aabb ):
    """ Returns the centre point of the AABB.
    """
    return (aabb[ 0 ] + aabb[ 1 ]) * 0.5

def minimum( aabb ):
    """ Returns the minimum point of the AABB.
    """
    return aabb[ 0 ]

def maximum( aabb ):
    """ Returns the maximum point of the AABB.
    """
    return aabb[ 1 ]

@all_parameters_as_numpy_arrays
def clamp_points( aabb, points ):
    """ Takes a list of points and modifies them to
    fit within the AABB.
    """
    # we need to compare the points against our AABB.
    # minimum( point, AABB maximum )
    # maximum( point, AABB minimum )

    # clamp the point by getting the maximum of the
    # point and the AABB's minimum
    # then the minimum of the point and the AABB's
    # maximum
    if points.ndim == 1:
        # only a single point
        # just take the existing AABB for comparisson
        aabb_min = aabb[ 0 ]
        aabb_max = aabb[ 1 ]
    else:
        # there are multiple points
        # so we'll repeat our AABB values for easy
        # comparison

        # use a stride trick to repeat the AABB arrays
        # without actually allocating any data
        # http://stackoverflow.com/questions/5564098/repeat-numpy-array-without-replicating-data
        aabb_min = np.lib.stride_tricks.as_strided(
            aabb[ 0 ],
            (points.shape[ 0 ], aabb[ 0 ].size),
            (0, aabb[ 0 ].itemsize)
            )
        aabb_max = np.lib.stride_tricks.as_strided(
            aabb[ 1 ],
            (points.shape[ 0 ], aabb[ 1 ].size),
            (0, aabb[ 1 ].itemsize)
            )

    return numpy.array(
        [
            numpy.maximum( points, aabb_min ),
            numpy.minimum( points, aabb_max )
            ]
        )

