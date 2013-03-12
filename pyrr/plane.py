# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy
import numpy.linalg

from pyrr import vector


# the indices of each component in the
# plane array
class index:
    position = 0
    normal = 1
    up = 2

def identity():
    """Creates a plane at the origin, with a normal of 0,0,1 and up of 0,1,0.

    This is a plane that lies at the origin on the X,Y plane and faces +Z.
    """
    return numpy.array(
        [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 1.0 ],
            [ 0.0, 1.0, 0.0 ]
            ]
        )

def create_from_points( vector1, vector2, vector3 ):
    """
    Create a plane from 3 co-planar vectors.

    The vectors must all lie on the same
    plane or an exception will be thrown.

    The vectors must not all be in a single line or
    the plane is undefined.

    The order the vertices are passed in will determine the
    normal of the plane.

    @param vector1: a vector that lies on the desired plane.
    @param vector2: a vector that lies on the desired plane.
    @param vector3: a vector that lies on the desired plane.
    @raise ValueError: raised if the vectors are not co-planar.
    @raise ValueError: raised if the vectors are in a single line
    """
    # make the vectors relative to vector2
    relV1 = vector1 - vector2
    relV2 = vector3 - vector2
    
    # cross our relative vectors
    normal = numpy.cross( relV1, relV2 )
    
    # create our plane
    return create_from_position(
        position = vector2,
        normal = normal,
        up = relV1
        )

def create_from_position( position, normal, up ):
    """
    Creates a plane at position with the normal being above the plane
    and up being the rotation of the plane.
    This is required as a plane must be defined by
    3 vectors otherwise rotation is undefined.

    @param position: The position of the plane.
    @param normal: The normal will be normalised during construction.
    @param up: Must be co-planar. The up vector will be normalised
    during construction.
    The up vector must lie on the plane itself. Without it, the plane is
    undefined.
    @raise ValueError: Raised if the up vector is not co-planar.
    """
    result = numpy.array(
        [
            position,
            vector.normalise( normal ),
            vector.normalise( up )
            ]
        )
    
    if numpy.dot( result[ 1 ], result[ 2 ] ) != 0.0:
        raise ValueError( "Vectors are not co-planar" )

    return result

def flip_normal( plane ):
    """
    Flips the normal of the plane in place.

    @return Returns the plane for convenience.
    """
    return numpy.array(
        [
            plane[ 0 ],
            plane[ 1 ] * -1.0,
            plane[ 2 ]
            ]
        )

def position( plane ):
    return plane[ 0 ]

def normal( plane ):
    return plane[ 1 ]

def up( plane ):
    return plane[ 2 ]

