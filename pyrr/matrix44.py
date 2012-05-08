'''
Created on 23/06/2011

@author: adam
'''

import math

import numpy

import matrix33


def empty():
    return numpy.empty( (4,4), dtype = numpy.float )

def identity( out = None ):
    """
    Creates a new matrix44 and sets it to
    an identity matrix.
    """
    if out == None:
        out = numpy.identity( 4, dtype = numpy.float )
    else:
        out[:] = [
            [ 1.0, 0.0, 0.0, 0.0 ],
            [ 0.0, 1.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 1.0, 0.0 ],
            [ 0.0, 0.0, 0.0, 1.0 ]
            ]
    return out

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

def create_from_eulers( eulers, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    out[ 0:3, 0:3 ] = matrix33.create_from_eulers( eulers, mat33 )
    
    return out

def create_from_quaternion( quat, out = None ):
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
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    matrix33.create_from_quaternion( quat, mat33 )
    
    return out

def create_from_inverse_of_quaternion( quat, out = None ):
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
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    matrix33.create_from_inverse_of_quaternion( quat, mat33 )
    
    return out

def apply_to_vector( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # we'll use Matrix33 for our conversion
    mat33 = matrix[ 0:3, 0:3 ]
    matrix33.apply_to_vector( vector, mat33, out )
    
    return out

def apply_transpose_to_vector( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # we'll use Matrix33 for our conversion
    mat33 = matrix[ 0:3, 0:3 ]
    matrix33.apply_transpose_to_vector( vector, mat33, out )
    
    return out


def multiply( m1, m2, out = None ):
    """
    Multiplies two matrixies, m1 . m2.
    This is essentially a wrapper around
    numpy.dot( m1, m2 )

    @param m1: The base matrix
    @param m2: The matrix to multiply with
    @result: The new matrix formed from multiplying
    m1 with m2.
    """
    if out == None:
        out = empty()

    out[:] = numpy.dot( m1, m2 )
    return out

def translate( matrix, vector, out = None ):
    if out == None:
        out = empty()
    
    out[:] = matrix
    # apply the vector to the first 3 values of the last row
    out[ 3, 0:3 ] += vector
    
    return out

def set_translation( matrix, vector, out = None ):
    if out == None:
        out = empty()
    
    out[:] = matrix
    # apply the vector to the first 3 values of the last row
    out[ 3, 0:3 ] = vector
    
    return out

def scale( matrix, scale, out = None ):
    # apply the scale to the values diagonally
    # down the matrix
    if out == None:
        out = empty()

    scale_matrix = numpy.diagflat(
        [
            scale[ 0 ],
            scale[ 1 ],
            scale[ 2 ],
            1.0
            ]
        )

    multiply( matrix, scale_matrix, out )

    return out

def create_projection_view_matrix(
    left,
    right,
    top,
    bottom,
    near,
    far,
    out = None
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
    if out == None:
        out = empty()

    A = (right + left) / (right - left)
    B = (top + bottom) / (top - bottom)
    C = -(far + near) / (far - near)
    D = -2.0 * far * near / (far - near)
    E = 2.0 * near / (right - left)
    F = 2.0 * near / (top - bottom)

    out[:] = [
        [   E, 0.0, 0.0, 0.0 ],
        [ 0.0,   F, 0.0, 0.0 ],
        [   A,   B,   C,-1.0 ],
        [ 0.0, 0.0,   D, 0.0 ],
        ]

    return out

def create_orthogonal_view_matrix(
    left,
    right,
    top,
    bottom,
    near,
    far,
    out = None
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
    if out == None:
        out = empty()

    A = 2 / (right - left)
    B = 2 / (top - bottom)
    C = -2 / (far - near)

    out[:] = [
        [   A, 0.0, 0.0, 0.0 ],
        [ 0.0,   B, 0.0, 0.0 ],
        [ 0.0, 0.0,   C, 0.0 ],
        [ 0.0, 0.0, 0.0, 1.0 ],
        ]

    return out

