# -*- coding: utf-8 -*-
"""3x3 Matrix which supports rotation, translation, scale and skew.

Matrices are laid out in row-major format and can be loaded directly
into OpenGL.
To convert to column-major format, transpose the array using the
numpy.array.T method.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import math

import numpy

from pyrr import quaternion
from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


def create_identity(dtype=None):
    """Creates a new matrix33 and sets it to
    an identity matrix.

    :rtype: numpy.array
    :return: A matrix representing an identity matrix with shape (3,3).
    """
    return numpy.identity(3, dtype = dtype)

@all_parameters_as_numpy_arrays
def create_from_matrix44(mat, dtype=None):
    """Creates a Matrix33 from a Matrix44.

    :rtype: numpy.array
    :return: A matrix with shape (3,3) with the input matrix rotation.
    """
    return numpy.array(mat[ 0:3, 0:3 ], dtype=dtype)

@parameters_as_numpy_arrays('eulers')
def create_from_eulers(eulers, dtype=None):
    """Creates a matrix from the specified Euler rotations.

    :param numpy.array eulers: A set of euler rotations in the format
        specified by the euler modules.
    :rtype: numpy.array
    :return: A matrix with shape (3,3) with the euler's rotation.
    """
    dtype = dtype or eulers.dtype

    pitchOver2 = eulers[0] * 0.5
    rollOver2 = eulers[1] * 0.5
    yawOver2 = eulers[2] * 0.5
    
    sinPitch = math.sin(pitchOver2)
    cosPitch = math.cos(pitchOver2)
    sinRoll = math.sin(rollOver2)
    cosRoll = math.cos(rollOver2)
    sinYaw = math.sin(yawOver2)
    cosYaw = math.cos(yawOver2)
    
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
        ],
        dtype=dtype
    )

@parameters_as_numpy_arrays('quat')
def create_from_quaternion(quat, dtype=None):
    """Creates a matrix with the same rotation as a quaternion.

    :param quat: The quaternion to create the matrix from.
    :rtype: numpy.array
    :return: A matrix with shape (3,3) with the quaternion's rotation.
    """
    dtype = dtype or quat.dtype

    x, y, z, w = quat

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
        ],
        dtype=dtype
    )

@parameters_as_numpy_arrays('quat')
def create_from_inverse_of_quaternion(quat, dtype=None):
    """Creates a matrix with the inverse rotation of a quaternion.

    :param numpy.array quat: The quaternion to make the matrix from (shape 4).
    :rtype: numpy.array
    :return: A matrix with shape (3,3) that respresents the inverse of
        the quaternion.
    """
    dtype = dtype or quat.dtype

    x, y, z, w = quat

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
        ],
        dtype=dtype
    )

def create_from_scale(scale, dtype=None):
    """Creates an identity matrix with the scale set.

    :param numpy.array scale: The scale to apply as a vector (shape 3).
    :rtype: numpy.array
    :return: A matrix with shape (3,3) with the scale 
        set to the specified vector.
    """
    # apply the scale to the values diagonally
    # down the matrix
    m = numpy.diagflat(scale)
    if dtype:
        m = m.astype(dtype)
    return m

def create_from_x_rotation(theta, dtype=None):
    """Creates a matrix with the specified rotation about the X axis.

    :param float theta: The rotation, in radians, about the X-axis.
    :rtype: numpy.array
    :return: A matrix with the shape (3,3) with the specified rotation about
        the X-axis.
    
    .. seealso:: http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    cosT = math.cos(theta)
    sinT = math.sin(theta)

    return numpy.array(
        [
            [ 1.0, 0.0, 0.0 ],
            [ 0.0, cosT,-sinT ],
            [ 0.0, sinT, cosT ]
        ],
        dtype=dtype
    )

def create_from_y_rotation(theta, dtype=None):
    """Creates a matrix with the specified rotation about the Y axis.

    :param float theta: The rotation, in radians, about the Y-axis.
    :rtype: numpy.array
    :return: A matrix with the shape (3,3) with the specified rotation about
        the Y-axis.
    
    .. seealso:: http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    cosT = math.cos(theta)
    sinT = math.sin(theta)
    
    return numpy.array(
        [
            [ cosT, 0.0, sinT ],
            [ 0.0, 1.0, 0.0 ],
            [-sinT, 0.0, cosT ]
        ],
        dtype=dtype
    )

def create_from_z_rotation(theta, dtype=None):
    """Creates a matrix with the specified rotation about the Z axis.

    :param float theta: The rotation, in radians, about the Z-axis.
    :rtype: numpy.array
    :return: A matrix with the shape (3,3) with the specified rotation about
        the Z-axis.
    
    .. seealso:: http://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
    """
    cosT = math.cos(theta)
    sinT = math.sin(theta)
    
    return numpy.array(
        [
            [ cosT,-sinT, 0.0 ],
            [ sinT, cosT, 0.0 ],
            [ 0.0, 0.0, 1.0 ]
        ],
        dtype=dtype
    )

@parameters_as_numpy_arrays('vec')
def apply_to_vector(mat, vec):
    """Apply a matrix to a vector.

    The matrix's rotation are applied to the vector.
    Supports multiple matrices and vectors.

    :param numpy.array mat: The rotation / translation matrix.
        Can be a list of matrices.
    :param numpy.array vec: The vector to modify.
        Can be a list of vectors.
    :rtype: numpy.array
    :return: The vectors rotated by the specified matrix.
    """
    if vec.size == 3:
        return numpy.dot(vec, mat)
    elif vec.size == 4:
        # convert to vec3 and undo w component
        vec3 = vec[:-1] / vec[-1]
        vec3 = numpy.dot( vec3, mat )
        # convert back to vec4
        return numpy.array([vec3[0], vec3[1], vec3[2], 1.0], dtype=vec.dtype)
    else:
        raise ValueError("Vector size unsupported")

def multiply(m1, m2, out=None):
    """Multiply two matricies, m1 . m2.

    This is essentially a wrapper around
    numpy.dot( m1, m2 )

    :param numpy.array m1: The first matrix.
        Can be a list of matrices.
    :param numpy.array m2: The second matrix.
        Can be a list of matrices.
    :rtype: numpy.array
    :return: A matrix that results from multiplying m1 by m2.
    """
    # using an input as the out value will cause corruption
    if out == m1 or out == m2:
        raise ValueError( "Output must not be one of the inputs, use assignment instead" )

    return numpy.dot(m1, m2, out=out)

def inverse(mat):
    """Returns the inverse of the matrix.

    This is essentially a wrapper around numpy.linalg.inv.

    :param numpy.array m: A matrix.
    :rtype: numpy.array
    :return: The inverse of the specified matrix.

    .. seealso:: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html
    """
    return numpy.linalg.inv(mat)
