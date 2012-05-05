'''
Created on 21/06/2011

@author: adam
'''

import math

import numpy

import quaternion


def identity( out = None ):
    if out == None:
        out = numpy.empty( (3, 3), dtype = float )
    
    out[:] = [
        [ 1.0, 0.0, 0.0 ],
        [ 0.0, 1.0, 0.0 ],
        [ 0.0, 0.0, 1.0 ]
        ]
    return out

def create_from_eulers( eulers, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( (3, 3), dtype = float )
    
    pitchOver2 = eulers[ 0 ] * 0.5
    rollOver2 = eulers[ 1 ] * 0.5
    yawOver2 = eulers[ 2 ] * 0.5
    
    sinPitch = math.sin( pitchOver2 )
    cosPitch = math.cos( pitchOver2 )
    sinRoll = math.sin( rollOver2 )
    cosRoll = math.cos( rollOver2 )
    sinYaw = math.sin( yawOver2 )
    cosYaw = math.cos( yawOver2 )
    
    out[:] = [
        # m1
        [
            # m11 = cy * cr + sy * sp * sr
            (cosYaw * cosRoll) + (sinYaw * sinPitch * sinRoll),
            # m12 = -cy * sr + sy * sp * cr
            (-cosYaw * sinRoll) + (sinYaw * sinPitch * cosRoll),
            # m13 = sy * cp
            sinYaw * cosPitch
            ],
        # m2
        [
            # m21 = sr * cp
            sinRoll * cosPitch,
            # m22 = cr * cp
            cosRoll * cosPitch,
            # m23 = -sp
            -sinPitch
            ],
        # m3
        [
            # m31 = -sy * cr + cy * sp * sr
            (-sinYaw * cosRoll) + (cosYaw * sinPitch * sinRoll),
            # m32 = sr * sy + cy * sp * cr
            (sinRoll * sinYaw) + (cosYaw * sinPitch * cosRoll),
            # m33 = cy * cp
            cosYaw * cosPitch
            ]
        ]
    return out

def create_from_quaternion( quat, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( (3, 3), dtype = float )
    
    quatW = quat[ quaternion.w ]
    quatX = quat[ quaternion.x ]
    quatY = quat[ quaternion.y ]
    quatZ = quat[ quaternion.z ]
    
    out[:] = [
        # m1
        [
            # m11 = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
            1.0 - 2.0 * (quatY * quatY + quatZ * quatZ),
            # m12 = 2.0 * (q.x * q.y + q.w * q.z)
            2.0 * (quatX * quatY + quatW * quatZ),
            # m13 = 2.0 * (q.x * q.z - q.w * q.y)
            2.0 * (quatX * quatZ - quatW * quatY)
            ],
        # m2
        [
            # m21 = 2.0 * (q.x * q.y - q.w * q.z)
            2.0 * (quatX * quatY - quatW * quatZ),
            # m22 = 1.0 - 2.0 * (q.x * q.x + q.z * q.z)
            1.0 - 2.0 * (quatX * quatX + quatZ * quatZ),
            # m23 = 2.0 * (q.y * q.z + q.w * q.x)
            2.0 * (quatY * quatZ + quatW * quatX)
            ],
        # m3
        [
            # m31 = 2.0 * (q.x * q.z + q.w * q.y)
            2.0 * (quatX * quatZ + quatW * quatY),
            # m32 = 2.0 * (q.y * q.z - q.w * q.x)
            2.0 * (quatY * quatZ - quatW * quatX),
            # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
            1.0 - 2.0 * (quatX * quatX + quatY * quatY)
            ]
        ]
    return out

def create_from_inverse_of_quaternion( quat, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( (3, 3), dtype = float )
    
    quatW = quat[ quaternion.w ]
    quatX = quat[ quaternion.x ]
    quatY = quat[ quaternion.y ]
    quatZ = quat[ quaternion.z ]
    
    out[:] = [
        # m1
        [
            # m11 = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
            1.0 - 2.0 * (quatY * quatY + quatZ * quatZ),
            # m12 = 2.0 * (q.x * q.y - q.w * q.z)
            2.0 * (quatX * quatY - quatW * quatZ),
            # m13 = 2.0 * ( q.x * q.z + q.w * q.y)
            2.0 * (quatX * quatZ + quatW * quatY)
            ],
        # m2
        [
            # m21 = 2.0 * (q.x * q.y + q.w * q.z)
            2.0 * (quatX * quatY + quatW * quatZ),
            # m22 = 1.0 - 2.0 * (q.x * q.x + q.z * q.z)
            1.0 - 2.0 * (quatX * quatX + quatZ * quatZ),
            # m23 = 2.0 * (q.y * q.z - q.w * q.x)
            2.0 * (quatY * quatZ - quatW * quatX)
            ],
        # m3
        [
            # m31 = 2.0 * (q.x * q.z - q.w * q.y)
            2.0 * (quatX * quatZ - quatW * quatY),
            # m32 = 2.0 * (q.y * q.z + q.w * q.x)
            2.0 * ( quatY * quatZ - quatW * quatX),
            # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
            1.0 - 2.0 * (quatX * quatX + quatY * quatY)
            ]
        ]
    return out

def apply_to_vector( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( 3, dtype = float )
    
    vecX = vector[ 0 ]
    vecY = vector[ 1 ]
    vecZ = vector[ 2 ]
    
    out[:] = [
        # x = m11 * v.x + m21 * v.y + m31 * v.z
        (matrix[ (0, 0) ] * vecX) + (matrix[ (1, 0) ] * vecY) + (matrix[ (2, 0) ] * vecZ),
        # y = m12 * v.x + m22 * v.y + m32 * v.z
        (matrix[ (0, 1) ] * vecX) + (matrix[ (1, 1) ] * vecY) + (matrix[ (2, 1) ] * vecZ),
        # z = m13 * v.x + m23 * v.y + m33 * v.z
        (matrix[ (0, 2) ] * vecX) + (matrix[ (1, 2) ] * vecY) + (matrix[ (2, 2) ] * vecZ)
        ]
    return out

def object_to_inertial( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( 3, dtype = float )
    
    vecX = vector[ 0 ]
    vecY = vector[ 1 ]
    vecZ = vector[ 2 ]
    
    # Note: m11 and m12 are in the same column, not the same row
    out[:] = [
        # x = m11 * v.x + m12 * v.y + m13 * v.z
        (matrix[ (0, 0) ] * vecX) + (matrix[ (0, 1) ] * vecY) + (matrix[ (0, 2) ] * vecZ),
        # y = m21 * v.x + m22 * v.y + m23 * v.z
        (matrix[ (1, 0) ] * vecX) + (matrix[ (1, 1) ] * vecY) + (matrix[ (1, 2) ] * vecZ),
        # z = m31 * v.x + m32 * v.y + m33 * v.z
        (matrix[ (2, 0) ] * vecX) + (matrix[ (2, 1) ] * vecY) + (matrix[ (2, 2) ] * vecZ)
        ]
    return out

def multiply( m1, m2, out = None ):
    if out == None:
        out = numpy.empty( (3, 3), dtype = float )
    out[:] = numpy.dot( m1, m2 )
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
            ]
        )
    multiply( matrix, scale_matrix, out )
    
    return out

