'''
Created on 21/06/2011

@author: adam
'''

import math

import numpy

import quaternion


def _empty():
    return numpy.empty( (3,3), dtype = numpy.float )

def identity( out = None ):
    if out == None:
        out = numpy.identity( 3, dtype = numpy.float )
    else:    
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
        out = _empty()
    
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
        out = _empty()
    
    x = quat[ quaternion.x ]
    y = quat[ quaternion.y ]
    z = quat[ quaternion.z ]
    w = quat[ quaternion.w ]

    y2 = y**2
    x2 = x**2
    z2 = z**2
    xy = x * y
    xz = x * z
    yz = y * z
    wx = w * x
    wy = w * y
    wz = w * z
    
    out[:] = [
        # m1
        [
            # m11 = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
            1.0 - 2.0 * (y2 + z2),
            # m12 = 2.0 * (q.x * q.y + q.w * q.z)
            2.0 * (xy + wz),
            # m13 = 2.0 * (q.x * q.z - q.w * q.y)
            2.0 * (xz - wy)
            ],
        # m2
        [
            # m21 = 2.0 * (q.x * q.y - q.w * q.z)
            2.0 * (xy - wz),
            # m22 = 1.0 - 2.0 * (q.x * q.x + q.z * q.z)
            1.0 - 2.0 * (x2 + z2),
            # m23 = 2.0 * (q.y * q.z + q.w * q.x)
            2.0 * (yz + wx)
            ],
        # m3
        [
            # m31 = 2.0 * (q.x * q.z + q.w * q.y)
            2.0 * (xz + wy),
            # m32 = 2.0 * (q.y * q.z - q.w * q.x)
            2.0 * (yz - wx),
            # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
            1.0 - 2.0 * (x2 + y2)
            ]
        ]
    return out

def create_from_inverse_of_quaternion( quat, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = _empty()
    
    x = quat[ quaternion.x ]
    y = quat[ quaternion.y ]
    z = quat[ quaternion.z ]
    w = quat[ quaternion.w ]

    x2 = x**2
    y2 = y**2
    z2 = z**2
    xy = x * y
    xz = x * z
    yz = y * z
    wx = w * x
    wy = w * y
    wz = w * z
    
    out[:] = [
        # m1
        [
            # m11 = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
            1.0 - 2.0 * (y2 + z2),
            # m12 = 2.0 * (q.x * q.y - q.w * q.z)
            2.0 * (xy - wz),
            # m13 = 2.0 * ( q.x * q.z + q.w * q.y)
            2.0 * (xz + wy)
            ],
        # m2
        [
            # m21 = 2.0 * (q.x * q.y + q.w * q.z)
            2.0 * (xy + wz),
            # m22 = 1.0 - 2.0 * (q.x * q.x + q.z * q.z)
            1.0 - 2.0 * (x2 + z2),
            # m23 = 2.0 * (q.y * q.z - q.w * q.x)
            2.0 * (yz - wx)
            ],
        # m3
        [
            # m31 = 2.0 * (q.x * q.z - q.w * q.y)
            2.0 * (xz - wy),
            # m32 = 2.0 * (q.y * q.z + q.w * q.x)
            2.0 * ( yz - wx),
            # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
            1.0 - 2.0 * (x2 + y2)
            ]
        ]
    return out

def create_from_scale( scale, out = None ):
    if out == None:
        out = _empty()
    
    # apply the scale to the values diagonally
    # down the matrix
    out[:] = numpy.diagflat( scale )
    return out

def apply_to_vector( vector, matrix, out = None ):
    """
    Proper matrix layout and layout used for DirectX.
    For OpenGL, transpose the matrix after calling this.
    """
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )
    
    x = vector[ 0 ]
    y = vector[ 1 ]
    z = vector[ 2 ]
    
    out[:] = [
        # x = m11 * v.x + m21 * v.y + m31 * v.z
        (matrix[ (0, 0) ] * x) + (matrix[ (1, 0) ] * y) + (matrix[ (2, 0) ] * z),
        # y = m12 * v.x + m22 * v.y + m32 * v.z
        (matrix[ (0, 1) ] * x) + (matrix[ (1, 1) ] * y) + (matrix[ (2, 1) ] * z),
        # z = m13 * v.x + m23 * v.y + m33 * v.z
        (matrix[ (0, 2) ] * x) + (matrix[ (1, 2) ] * y) + (matrix[ (2, 2) ] * z)
        ]
    return out

def multiply( m1, m2, out = None ):
    if out == None:
        out = _empty()

    out[:] = numpy.dot( m1, m2 )
    return out

def inverse( m, out = None ):
    if out == None:
        out = _empty()

    out[:] = numpy.linalg.inv( m )

    return out

