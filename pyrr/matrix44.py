'''
Created on 23/06/2011

@author: adam
'''

import math

import numpy

import matrix33


def identity( out = None ):
    if out == None:
        out = numpy.empty( (4, 4), dtype = float )
    
    out[:] = [
        [ 1.0, 0.0, 0.0, 0.0 ],
        [ 0.0, 1.0, 0.0, 0.0 ],
        [ 0.0, 0.0, 1.0, 0.0 ],
        [ 0.0, 0.0, 0.0, 1.0 ]
        ]
    return out

def setup( eulers, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    mat33 = matrix33.setup( eulers, mat33 )
    
    return out

def from_inertial_to_object_quaternion( quat, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    matrix33.from_inertial_to_object_quaternion( quat, mat33 )
    
    return out

def from_object_to_inertial_quaternion( quat, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    matrix33.from_object_to_inertial_quaternion( quat, mat33 )
    
    return out

def inertial_to_object( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    # set to identity matrix
    # this will populate our extra rows for us
    out = identity( out )
    
    # we'll use Matrix33 for our conversion
    mat33 = out[ 0:3, 0:3 ]
    matrix33.inertial_to_object( vector, mat33 )
    
    return out

def multiply( m1, m2, out = None ):
    if out == None:
        out = numpy.empty( (4, 4), dtype = float )
    out[:] = numpy.dot( m1, m2 )
    return out

def set_translation( matrix, vector, out = None ):
    if out == None:
        out = numpy.empty( (4, 4), dtype = float )
    
    out[:] = matrix
    # apply the vector to the first 3 values of the last row
    out[ 3, 0:3 ] = vector
    
    return out

def scale( matrix, scale, out = None ):
    if out == None:
        out = identity() 
    
    # apply the scale to the values diagonally
    # down the matrix
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
        out = numpy.empty( (4, 4), dtype = float )

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
        out = numpy.empty( (4, 4), dtype = float )

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

