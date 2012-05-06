'''
Created on 20/04/2012

@author: adam

A line is defined by two points but extends
infinitely.

A line segment only exists between two points.
It does not extend forever.
'''

import numpy

import vector


def create_from_points( v1, v2 ):
    """
    Creates a line from 2 independent vectors.
    This is just a convenience function that wraps
    two vectors into a single array.
    """
    return numpy.array( [ v1, v2 ], dtype = numpy.float )

def create_from_ray( ray, out = None ):
    """
    Converts a ray to a line.
    """
    if out == None:
        out = numpy.empty( (2,3), dtype = numpy.float )

    # convert ray relative direction to absolute
    # position
    out[ 0 ] = ray[ 0 ]
    out[ 1 ] = ray[ 0 ] + ray[ 1 ]

    return out

