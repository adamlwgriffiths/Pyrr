# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Planes.

Planes are represented using a numpy.array of shape (3,3).
The first value is the position vector.
The second value is the normal vector.
The third value is the up vector.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy
import numpy.linalg

from pyrr import vector


class index:
    #: The index of the position vector within the plane
    position = 0

    #: The index of the normal vector within the plane
    normal = 1

    #: The index of the up vector within the plane
    up = 2


def create_identity():
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
    """Create a plane from 3 co-planar vectors.

    The vectors must all lie on the same
    plane or an exception will be thrown.

    The vectors must not all be in a single line or
    the plane is undefined.

    The order the vertices are passed in will determine the
    normal of the plane.

    :param numpy.array vector1: a vector that lies on the desired plane.
    :param numpy.array vector2: a vector that lies on the desired plane.
    :param numpy.array vector3: a vector that lies on the desired plane.
    :raise ValueError: raised if the vectors are not co-planar.
    :raise ValueError: raised if the vectors are in a single line
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
    """Creates a plane at position with the normal being above the plane
    and up being the rotation of the plane.

    These 3 parameters are required as a plane must be defined by
    3 vectors otherwise rotation is undefined.

    :param numpy.array position: The position of the plane.
    :param numpy.array normal: The normal will be normalised during construction.
    :param numpy.array up: Must be co-planar. The up vector will be normalised
        during construction.
        The up vector must lie on the plane itself. Without it, the plane is
        undefined.
    :raise ValueError: Raised if the up vector is not co-planar.
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
    """Flips the normal of the plane.

    The plane is **not** changed in place.

    :rtype: A numpy.array with shape (3,3).
    """
    return numpy.array(
        [
            plane[ 0 ],
            plane[ 1 ] * -1.0,
            plane[ 2 ]
            ]
        )

def position( plane ):
    """Extracts the position vector from a plane.

    :param numpy.array plane: The plane.
    :rtype: A numpy.array with shape 3.
    """
    return plane[ 0 ]

def normal( plane ):
    """Extracts the normal vector from a plane.

    :param numpy.array plane: The plane.
    :rtype: A numpy.array with shape 3.
    """
    return plane[ 1 ]

def up( plane ):
    """Extracts the up vector from a plane.

    :param numpy.array plane: The plane.
    :rtype: A numpy.array with shape 3.
    """
    return plane[ 2 ]

