""" Provides functions to calculate and manipulate
Axis-Aligned Bounding Boxes.

An AABB is represented by an array of 2 x 3D vectors.
The first vector represents the minimum extent.
The second vector represents the maximum extent.

TODO: add transform( matrix )
"""

import numpy


def _empty():
    return numpy.empty( (2,3), dtype = numpy.float )

def create_from_bounds( min, max ):
    """ Creates an AABB using the specified minimum
    and maximum values.
    """
    return numpy.array(
        [ min, max ],
        dtype = numpy.float
        )

def create_from_points( points, out = None ):
    """ Creates an AABB from the list of specified points.

    Points must be a 2D list. Ie:
    [
        [ x, y, z ],
        [ x, y, z ],
    ]
    """
    if out == None:
        out = _empty()

    numpy.amin( points, axis = 0, out = out[ 0 ] ),
    numpy.amax( points, axis = 0, out = out[ 1 ] )
    return out

def create_from_aabbs( aabbs, out = None ):
    """ Creates an AABB from a list of existing AABBs.

    AABBs must be a 2D list. Ie:
    [
        AABB,
        AABB,
    ]
    """
    if out == None:
        out = _empty()

    # extract the minimum and maximums from the list
    numpy.amin( aabbs[:, 0], axis = 0, out = out[ 0 ] )
    numpy.amax( aabbs[:, 1], axis = 0, out = out[ 1 ] )
    return out

def add_points( aabb, points, out = None ):
    """ Extends an AABB to encompass a list
    of points.
    """
    if out == None:
        out = _empty()

    # find the minimum and maximum point values
    minimum = numpy.amin( points, axis = 0 )
    maximum = numpy.amax( points, axis = 0 )

    # compare to existing AABB
    numpy.minimum( aabb[ 0 ], minimum, out = out[ 0 ] )
    numpy.maximum( aabb[ 1 ], maximum, out = out[ 1 ] )

    return out

def add_aabbs( aabb, aabbs, out = None ):
    """ Extend an AABB to encompass a list
    of other AABBs.
    """
    if out == None:
        out = _empty()

    # extract the AABB's minimum and maximum
    minimum = numpy.amin( aabbs[:, 0], axis = 0 )
    maximum = numpy.amax( aabbs[:, 1], axis = 0 )

    # compare to our existing AABB
    numpy.minimum( aabb[ 0 ], minimum, out = out[ 0 ] )
    numpy.maximum( aabb[ 1 ], maximum, out = out[ 1 ] )
    return out

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

def clamp_points( aabb, points, out = None ):
    """ Takes a list of points and modifies them to
    fit within the AABB.
    """
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )

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

    numpy.maximum( points, aabb_min, out = out[ 0 ] )
    numpy.minimum( points, aabb_max, out = out[ 1 ] )

    return out

