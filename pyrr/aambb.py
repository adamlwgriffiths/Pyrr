""" Provides functions to calculate and manipulate
Axis-Aligned Minimum Bounding Boxes (AAMBB).

AAMBB are a simple 3D rectangle with no orientation.
It is up to the user to provide translation.
AAMBB differ from AABB in that they allow for the
content to rotate freely and still be within the AAMBB.

An AAMBB is represented in the same way an AABB is;
a array of 2 x 3D vectors.
The first vector represents the minimum extent.
The second vector represents the maximum extent.

Note that because the AAMBB set's it's dimensions using
the vector length of any points set within it, the user
should be careful to avoid adding the AAMBB to itself
or the AAMBB will continue to grow.

TODO: add transform( matrix )
TODO: add point_within_aabb
TODO: use point_within_aabb for unit tests
"""

import numpy

import aabb
import vector


class index:
    minimum = 0
    maximum = 1

def zeros():
    return numpy.zeroes( (2,3) )

def create_from_bounds( min, max ):
    """ Creates an AAMBB using the specified minimum
    and maximum values.
    """
    # stack our bounds together and add them as points
    bounds = numpy.vstack( min, max )
    return create_from_points( bounds )

def create_from_points( points ):
    """ Creates an AAMBB from the list of specified points.

    Points must be a 2D list. Ie:
    [
        [ x, y, z ],
        [ x, y, z ],
    ]
    """
    # convert any negative values to positive
    abs_points = numpy.absolute( points )

    # extract the maximum extent as a vector
    vec = numpy.amax( abs_points, axis = 0 )

    # find the length of this vector
    length = vector.length( vec )

    # our AAMBB extends from +length to -length
    # in all directions
    return numpy.array(
        [
            [-length,-length,-length ],
            [ length, length, length ]
            ]
        )

def create_from_aabbs( aabbs ):
    """ Creates an AAMBB from a list of existing AABBs.

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
    """ Extends an AAMBB to encompass a list
    of points.

    It should be noted that this ensures that
    the encompassed points can rotate freely.
    Calling this using the min / max points from
    the AAMBB will create an even bigger AAMBB.
    """
    # add our AABB to the list of points
    values = numpy.vstack( points, aabb[ 0 ], aabb[ 1 ] )

    # convert any negative values to positive
    abs_points = numpy.absolute( values )

    # extract the maximum extent as a vector
    vec = numpy.amax( abs_points, axis = 0 )

    # find the length of this vector
    length = vector.length( vec )

    # our AAMBB extends from +length to -length
    # in all directions
    return numpy.array(
        [
            [-length,-length,-length ],
            [ length, length, length ]
            ]
        )

def add_aabbs( aabb, aabbs ):
    """ Extend an AAMBB to encompass a list
    of other AABBs or AAMBBs.

    It should be noted that this ensures that
    the encompassed AABBs can rotate freely.
    Using the AAMBB itself in this calculation
    will create an event bigger AAMBB.
    """
    # reshape the AABBs as a series of points
    points = aabbs.reshape( (-1, 3 ) )

    # use the add_points
    return add_points( aabb, points )

def centre_point( aabb ):
    """ Returns the centre point of the AABB.
    This should always be [0.0, 0.0, 0.0]
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

def clamp_points( aabb, points ):
    """ Takes a list of points and modifies them to
    fit within the AABB.
    """
    # use the same function as present in AABB
    aabb.clamp_points( aabb, points )

