'''
Created on 09/04/2012

@author: adam

TODO: add transform( matrix )
TODO: add get_clamped_point( self, point )

TODO: bounding sphere

http://en.wikipedia.org/wiki/Bounding_volume
'''

import numpy


def empty():
    return numpy.zeros( (2,3), dtype = numpy.float )

def create_from_bounds( min, max ):
    return numpy.array(
        [ min, max ],
        dtype = numpy.float
        )

def create_from_points( points, out = None ):
    if out == None:
        out = empty()

    numpy.amin( points, axis = 0, out = out[ 0 ] ),
    numpy.amax( points, axis = 0, out = out[ 1 ] )
    return out

def add_points( aabb, points, out = None ):
    if out == None:
        out = empty()

    if points.ndim == 1:
        numpy.minimum( point, aabb[ 0 ] out = out[ 0 ] )
        numpy.maximum( point, aabb[ 1 ] out = out[ 1 ] )
    else:
        numpy.amin( points, axis = 0, out = out[ 0 ] ),
        numpy.amax( points, axis = 0, out = out[ 1 ] )
    return out

def add_aabb( aabb1, aabb2, out = None ):
    if out == None:
        out = empty()

    numpy.minimum( aabb1[ 0 ], aabb2[ 0 ] out = out[ 0 ] )
    numpy.maximum( aabb1[ 1 ], aabb2[ 1 ] out = out[ 1 ] )
    return out

def centre_point( aabb ):
    return (aabb[ 0 ] + aabb[ 1 ]) * 0.5

def minimum( aabb ):
    return aabb[ 0 ]

def maximum( aabb ):
    return aabb[ 1 ]

def clamp_points( aabb, points, out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )

    # clamp the point by getting the maximum of the
    # point and the AABB's minimum
    # then the minimum of the point and the AABB's
    # maximum
    if points.ndim == 1:
        aabb_min = aabb[ 0 ]
        aabb_max = aabb[ 1 ]
    else:
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

