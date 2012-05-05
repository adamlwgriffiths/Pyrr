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

import vector


# the indices of each component in the
# ray array
origin = 0
direction = 1

def line_to_ray( line, out = None ):
    """
    Converts a line or line segment to a ray.
    TODO: make this work with a list of rays
    Ie. Nx2x3 dimension arrays
    """
    if out == None:
        out = numpy.empty( (2,3), dtype = numpy.float )

    out[ 0 ] = line[ 0 ]
    out[ 1 ] = line[ 1 ]

    # direction = vend - vstart
    out[ 1 ] -= out[ 0 ]
    vector.normalise( out[ 1 ] )

    return out


if __name__ == '__main__':
    ray = line_to_ray(
        numpy.array(
            [
                [ 0.0, 0.0, 0.0 ],
                [10.0, 0.0, 0.0 ]
                ],
            dtype = numpy.float
            )
        )

    assert ray[ 0 ][ 0 ] == 0.0
    assert ray[ 0 ][ 1 ] == 0.0
    assert ray[ 0 ][ 2 ] == 0.0
    assert ray[ 1 ][ 0 ] == 10.0
    assert ray[ 1 ][ 1 ] == 0.0
    assert ray[ 1 ][ 2 ] == 0.0

    ray = line_to_ray(
        numpy.array(
            [
                [ 0.0,10.0, 0.0 ],
                [10.0,10.0, 0.0 ]
                ],
            dtype = numpy.float
            )
        )

    assert ray[ 0 ][ 0 ] == 0.0
    assert ray[ 0 ][ 1 ] == 10.0
    assert ray[ 0 ][ 2 ] == 0.0
    assert ray[ 1 ][ 0 ] == 10.0
    assert ray[ 1 ][ 1 ] == 0.0
    assert ray[ 1 ][ 2 ] == 0.0

