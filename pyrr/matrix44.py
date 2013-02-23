# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import math

import numpy

from pyrr import matrix33
from pyrr.utils import all_parameters_as_numpy_arrays


def identity():
    """
    Creates a new matrix44 and sets it to
    an identity matrix.
    """
    return numpy.identity( 4, dtype = 'float' )

def create_from_matrix33( mat ):
    mat4 = numpy.identity( 4, dtype = 'float' )
    mat4[ 0:3, 0:3 ] = mat
    return mat4

@all_parameters_as_numpy_arrays
def to_matrix33( mat ):
    """
    Converts a matrix44 to a matrix33.
    This is essentially a wrapper around the
    slice function mat[ 0:3, 0:3 ]

    @param mat: A matrix44
    @result: A matrix33 sliced from the specified
    matrix.
    """
    return mat[ 0:3, 0:3 ]

def create_from_eulers( eulers ):
    # set to identity matrix
    # this will populate our extra rows for us
    mat = identity()
    
    # we'll use Matrix33 for our conversion
    mat33 = mat[ 0:3, 0:3 ]
    mat[ 0:3, 0:3 ] = matrix33.create_from_eulers( eulers, mat33 )
    return mat

def create_from_quaternion( quat ):
    """
    Creates a matrix that applies a quaternions translations.

    This can be used to go from intertial space to object space.

    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.

    @param quat: The quaternion to create the matrix from.
    @result: The matrix that represents the quaternion.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    mat = identity()
    
    # we'll use Matrix33 for our conversion
    mat[ 0:3, 0:3 ] = matrix33.create_from_quaternion( quat )
    return mat

def create_from_inverse_of_quaternion( quat ):
    """
    Creates a matrix that applies the inverse of a quaternion's
    translations.

    This can be used to go from object space to intertial space.

    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.

    @param quat: The quaternion to make the matri from.
    @result: The matrix that respresents the inverse of the quaternion.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    mat = identity()
    
    # we'll use Matrix33 for our conversion
    mat[ 0:3, 0:3 ] = matrix33.create_from_inverse_of_quaternion( quat )
    return mat

def create_from_translation( vec ):
    """
    Creates an identity matrix with the translation set.

    @param vector: An array of shape (3).
    @param out: Optional parameter of where to store the
    output.
    @return: Returns an identity matrix with the translation
    set to the specified vector.
    """
    mat = identity()
    mat[ 3, 0:3 ] = vec[:3]
    return mat

def create_from_scale( scale ):
    """
    Creates an identity matrix with the scale set.

    @param vector: An array of shape (3).
    @param out: Optional parameter of where to store the
    output.
    @return: Returns an identity matrix with the scale 
    set to the specified vector.
    """
    # we need to expand 'scale' into it's components
    # because numpy isn't flattening them properly.
    return numpy.diagflat(
        [ scale[ 0 ], scale[ 1 ], scale[ 2 ], 1.0 ]
        )

def create_from_x_rotation( theta ):
    """Creates a matrix with the specified rotation about the X axis.
    
    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    mat = identity()
    mat[ 0:3, 0:3 ] = matrix33.create_from_x_rotation( theta )
    return mat

def create_from_y_rotation( theta ):
    """Creates a matrix with the specified rotation about the Y axis.
    
    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    mat = identity()
    mat[ 0:3, 0:3 ] = matrix33.create_from_y_rotation( theta )
    return mat

def create_from_z_rotation( theta ):
    """Creates a matrix with the specified rotation about the Z axis.
    
    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    mat = identity()
    mat[ 0:3, 0:3 ] = matrix33.create_from_z_rotation( theta )
    return mat

@all_parameters_as_numpy_arrays
def apply_to_vector( mat, vec ):
    if vec.size == 3:
        # convert to a vec4
        vec4 = numpy.array( [ vec[ 0 ], vec[ 1 ], vec[ 2 ], 1.0 ] )
        vec4 = numpy.dot( vec4, mat )

        # handle W value
        if vec4[-1] != 0.0:
            vec4 /= vec4[-1]
        return vec4[:-1]
    elif vec.size == 4:
        return numpy.dot( vec, mat )
    else:
        raise ValueError( "Vector size unsupported" )

def multiply( m1, m2, out = None ):
    """
    Multiplies two matricies, m1 . m2.
    This is essentially a wrapper around
    numpy.dot( m1, m2 )

    @param m1: The base matrix
    @param m2: The matrix to multiply with
    @result: The new matrix formed from multiplying
    m1 with m2.
    """
    # using an input as the out value will cause corruption
    if out == m1 or out == m2:
        raise ValueError( "Output must not be one of the inputs, use assignment instead" )

    return numpy.dot( m1, m2, out = out )

def create_projection_view_matrix(
    left,
    right,
    top,
    bottom,
    near,
    far
    ):
    """
    http://www.gamedev.net/topic/264248-building-a-projection-matrix-without-api/
    http://www.glprogramming.com/red/chapter03.html
    E  0  A  0
    0  F  B  0
    0  0  C  D
    0  0  -1 0

    A = (right+left)/(right-left)
    B = (top+bottom)/(top-bottom)
    C = -(far+near)/(far-near)
    D = -2*far*near/(far-near)
    E = 2*near/(right-left)
    F = 2*near/(top-bottom)
    """
    A = (right + left) / (right - left)
    B = (top + bottom) / (top - bottom)
    C = -(far + near) / (far - near)
    D = -2.0 * far * near / (far - near)
    E = 2.0 * near / (right - left)
    F = 2.0 * near / (top - bottom)

    return numpy.array(
        [
            [   E, 0.0, 0.0, 0.0 ],
            [ 0.0,   F, 0.0, 0.0 ],
            [   A,   B,   C,-1.0 ],
            [ 0.0, 0.0,   D, 0.0 ],
            ],
            dtype = 'float'
        )

def create_orthogonal_view_matrix(
    left,
    right,
    top,
    bottom,
    near,
    far
    ):
    """
    http://msdn.microsoft.com/en-us/library/dd373965(v=vs.85).aspx
    A 0 0 Tx
    0 B 0 Ty
    0 0 C Tz
    0 0 0 1

    A = 2 / (right - left)
    B = 2 / (top - bottom)
    C = -2 / (far - near)
    """
    A = 2 / (right - left)
    B = 2 / (top - bottom)
    C = -2 / (far - near)

    return numpy.array(
        [
            [   A, 0.0, 0.0, 0.0 ],
            [ 0.0,   B, 0.0, 0.0 ],
            [ 0.0, 0.0,   C, 0.0 ],
            [ 0.0, 0.0, 0.0, 1.0 ],
            ],
            dtype = 'float'
        )

def inverse( m ):
    return numpy.linalg.inv( m )
