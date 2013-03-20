# -*- coding: utf-8 -*-
"""General Matrix functions.

Matrices are laid out in row-major format and can be loaded directly
into OpenGL.
To convert to column-major format, transpose the array using the
numpy.array.T method.
"""
import numpy


def apply_direction_scale( vectors, direction, scale ):
    """Applies a directional scaling to a set of vectors.

    An example usage for this is to flatten a mesh against a
    single plane.

    Direction MUST be normalised prior to this call.

    :param numpy.array vectors: a 2d numpy array of vectors:
        ::

            numpy.array([
                [x,y,z],
                [x,y,z]
                ])

    :param numpy.array direction: a 1d numpy array of the direction to scale:
        ::
        
            numpy.array([ x,y,z ])

    :param numpy.array scale: a float value for the scaling. A scale of 0.0
        will flatten the vertices. 
    :rtype: numpy.array
    :return: The vectors flattend in the specified direction.
        The array will be in the shape of the input parameter vectors.
    """
    """
    scaling is defined as:
    
    [p'][1 + (k - 1)n.x^2, (k - 1)n.x n.y^2, (k - 1)n.x n.z   ]
    S(n,k) = [q'][(k - 1)n.x n.y,   1 + (k - 1)n.y,   (k - 1)n.y n.z   ]
    [r'][(k - 1)n.x n.z,   (k - 1)n.y n.z,   1 + (k - 1)n.z^2 ]
    
    where:
    v' is the resulting vector after scaling
    v is the vector to scale
    n is the direction of the scaling
    n.x is the x component of n
    n.y is the y component of n
    n.z is the z component of n
    k is the scaling factor
    """
    scaleMinus1 = scale - 1
    matrix = numpy.array(
        [
            # m1
            [
                # m11 = 1 + (k - 1)n.x^2
                1 + scaleMinus1 * (direction[ 0 ]**2),
                # m12 = (k - 1)n.x n.y^2
                scaleMinus1 * direction[ 0 ] * direction[ 1 ]**2,
                # m13 = (k - 1)n.x n.z
                scaleMinus1 * direction[ 0 ] * direction[ 2 ]
                ],
            # m2
            [
                # m21 = (k - 1)n.x n.y
                scaleMinus1 * direction[ 0 ] * direction[ 1 ],
                # m22 = 1 + (k - 1)n.y
                1 + scaleMinus1 * direction[ 1 ],
                # m23 = (k - 1)n.y n.z
                scaleMinus1 * direction[ 1 ] * direction[ 2 ]
                ],
            # m3
            [
                # m31 = (k - 1)n.x n.z
                scaleMinus1 * direction[ 0 ] * direction[ 2 ],
                # m32 = (k - 1)n.y n.z
                scaleMinus1 * direction[ 1 ] * direction[ 2 ],
                # m33 = 1 + (k - 1)n.z^2
                1 + scaleMinus1 * direction[ 2 ]**2
                ]
            ],
        dtype = numpy.float
        )
    
    return numpy.dot( vectors, matrix )

def apply_scale( vectors, scale ):
    """Applies a 3 dimensional scale to a set of vectors.

    :param numpy.array vectors: A 2D numpy array of vectors:
        ::

            numpy.array([
                [x,y,z],
                [x,y,z]
                ])

    :param numpy.array scale: The scale vector to apply.
        Can be a 1x3 array, list or tuple
    :rtype: numpy.array
    :return: The vectors scaled by the scaling vector.
    """
    # create a scaling matrix
    matrix = numpy.array([
        [ scale[ 0 ], 0.0, 0.0 ],
        [ 0.0, scale[ 1 ], 0.0 ],
        [ 0.0, 0.0, scale[ 2 ] ]
        ])
    return numpy.dot( vectors, matrix )

