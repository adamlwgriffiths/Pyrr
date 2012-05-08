'''
Created on 29/05/2011

@author: adam
'''

import numpy
import numpy.linalg

import vector


# the indices of each component in the
# plane array
position = 0
normal = 1
up = 2


def _empty():
    return numpy.empty( (3,3), dtype = numpy.float )

def create_from_points( vector1, vector2, vector3, out = None):
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
        up = relV1,
        out = out
        )

def create_from_position( position, normal, up, out = None ):
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
    if out == None:
        out = _empty()

    out[ 0 ] = numpy.array( position, dtype = float )
    out[ 1 ] = numpy.array( normal, dtype = float )
    out[ 2 ] = numpy.array( up, dtype = float )
    
    vector.normalise( out[ 1 ] )
    vector.normalise( out[ 2 ] )
    
    if numpy.dot( out[ 1 ], out[ 2 ] ) != 0.0:
        raise ValueError( "Vectors are not co-planar" )

    return out

def flip_normal( plane ):
    """
    Flips the normal of the plane in place.

    @return Returns the plane for convenience.
    """
    plane[ 1 ] *= -1.0
    return plane

