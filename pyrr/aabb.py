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
        [
            min,
            max
            ],
        dtype = numpy.float
        )

def add_point( aabb, point, out = None ):
    if out == None:
        out = empty()

    numpy.minimum(
        point,
        aabb[ 0 ]
        out = out[ 0 ]
        )
    numpy.maximum(
        point,
        aabb[ 1 ]
        out = out[ 1 ]
        )
    return out

def add_aabb( aabb1, aabb2, out = None ):
    if out == None:
        out = empty()

    numpy.minimum(
        aabb1[ 0 ],
        aabb2[ 0 ]
        out = out[ 0 ]
        )
    numpy.maximum(
        aabb1[ 1 ],
        aabb2[ 1 ]
        out = out[ 1 ]
        )
    return out


def centre( aabb ):
    return (aabb[ 0 ] + aabb[ 1 ]) * 0.5

