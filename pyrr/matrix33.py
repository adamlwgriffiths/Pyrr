# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import math

import numpy

from pyrr import quaternion
from pyrr.utils import all_parameters_as_numpy_arrays

def create_identity():
    return numpy.identity( 3, dtype = 'float' )

@all_parameters_as_numpy_arrays
def create_from_matrix44( mat ):
    return numpy.array( mat[ 0:3, 0:3 ] )

def create_from_eulers( eulers ):
    pitchOver2 = eulers[ 0 ] * 0.5
    rollOver2 = eulers[ 1 ] * 0.5
    yawOver2 = eulers[ 2 ] * 0.5
    
    sinPitch = math.sin( pitchOver2 )
    cosPitch = math.cos( pitchOver2 )
    sinRoll = math.sin( rollOver2 )
    cosRoll = math.cos( rollOver2 )
    sinYaw = math.sin( yawOver2 )
    cosYaw = math.cos( yawOver2 )
    
    return numpy.array(
        [
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
        )

def create_from_quaternion( quat ):
    x = quat[ 0 ]
    y = quat[ 1 ]
    z = quat[ 2 ]
    w = quat[ 3 ]

    y2 = y**2
    x2 = x**2
    z2 = z**2
    xy = x * y
    xz = x * z
    yz = y * z
    wx = w * x
    wy = w * y
    wz = w * z
    
    return numpy.array(
        [
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
        )

def create_from_inverse_of_quaternion( quat ):
    x = quat[ 0 ]
    y = quat[ 1 ]
    z = quat[ 2 ]
    w = quat[ 3 ]

    x2 = x**2
    y2 = y**2
    z2 = z**2
    wx = w * x
    wy = w * y
    xy = x * y
    wz = w * z
    xz = x * z
    yz = y * z
    
    return numpy.array(
        [
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
                2.0 * (yz - wx),
                # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
                1.0 - 2.0 * (x2 + y2)
                ]
            ]
        )

def create_from_scale( scale ):
    # apply the scale to the values diagonally
    # down the matrix
    return numpy.diagflat( scale )

def create_from_x_rotation( theta ):
    """Creates a matrix with the specified rotation about the X axis.

    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions

    :param float theta: angle in radiands
    :rtype: 3x3 float array
    """
    cosT = math.cos( theta )
    sinT = math.sin( theta )

    return numpy.array(
        [
            [ 1.0, 0.0, 0.0 ],
            [ 0.0, cosT,-sinT ],
            [ 0.0, sinT, cosT ]
            ]
        )

def create_from_y_rotation( theta ):
    """Creates a matrix with the specified rotation about the Y axis.
    
    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions

    :param float theta: angle in radiands
    :rtype: 3x3 float array
    """
    cosT = math.cos( theta )
    sinT = math.sin( theta )
    
    return numpy.array(
        [
            [ cosT, 0.0, sinT ],
            [ 0.0, 1.0, 0.0 ],
            [-sinT, 0.0, cosT ]
            ]
        )

def create_from_z_rotation( theta ):
    """Creates a matrix with the specified rotation about the Z axis.
    
    http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions

    :param float theta: angle in radiands
    :rtype: 3x3 float array
    """
    cosT = math.cos( theta )
    sinT = math.sin( theta )
    
    return numpy.array(
        [
            [ cosT,-sinT, 0.0 ],
            [ sinT, cosT, 0.0 ],
            [ 0.0, 0.0, 1.0 ]
            ]
        )

def apply_to_vector( mat, vec ):
    if vec.size == 3:
        return numpy.dot( vec, mat )
    elif vec.size == 4:
        # convert to vec3 and undo w component
        vec3 = vec[:-1] / vec[-1]
        vec3 = numpy.dot( vec3, mat )
        # convert back to vec4
        return numpy.array( [ vec3[0], vec3[1], vec3[2], 1.0 ] )
    else:
        raise ValueError( "Vector size unsupported" )

def multiply( m1, m2, out = None ):
    # using an input as the out value will cause corruption
    if out == m1 or out == m2:
        raise ValueError( "Output must not be one of the inputs, use assignment instead" )

    return numpy.dot( m1, m2, out = out )

def inverse( mat ):
    return numpy.linalg.inv( mat )

