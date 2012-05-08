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

def create_from_line( line, out = None ):
    """
    Converts a line or line segment to a ray.
    """
    if out == None:
        out = numpy.empty( (2,3), dtype = numpy.float )

    # direction = vend - vstart
    out[ 0 ] = line[ 0 ]
    out[ 1 ] = line[ 1 ] - line[ 0 ]

    # normalise the ray length
    vector.normalise( out[ 1 ] )

    return out

