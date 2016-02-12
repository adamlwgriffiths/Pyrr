# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Euler angles.

Eulers represent 3 rotations: Pitch, Roll and Yaw.

Eulers are represented using a numpy.array of shape (3,).
"""
from __future__ import absolute_import, division, print_function
import numpy as np


class index:
    """Defines the indices used to store the Euler values in the numpy array.

    If your axis (x, y, z) and rotations (roll, pitch, yaw) are not as defined
    by these values, please alter these values before using the Euler class.
    """
    #: The index of the roll value within the euler, defaults to X axis.
    roll = 0

    #: The index of the pitch value within the euler, defaults to Y axis.
    pitch = 1

    #: The index of the yaw value within the euler, defaults to Z axis.
    yaw = 2


def create(roll=0., pitch=0., yaw=0., dtype=None):
    """Creates an array storing the specified euler angles.

    Input values are in radians.

    :param float pitch: The pitch in radians.
    :param float roll: The roll in radians.
    :param float yaw: The yaw in radians.
    :rtype: numpy.array
    """
    e = np.empty((3,), dtype=dtype)
    e[[index.pitch, index.yaw, index.roll]] = [pitch, yaw, roll]
    print(e)
    return e


def create_from_x_rotation(theta, dtype=None):
    return np.array([theta, 0., 0.], dtype=dtype)


def create_from_y_rotation(theta, dtype=None):
    return np.array([0., theta, 0.], dtype=dtype)


def create_from_z_rotation(theta, dtype=None):
    return np.array([0., 0., theta], dtype=dtype)


def roll(eulers):
    """Extracts the roll value from the euler.

    :rtype: float.
    """
    return eulers[index.roll]


def yaw(eulers):
    """Extracts the yaw value from the euler.

    :rtype: float.
    """
    return eulers[index.yaw]


def pitch(eulers):
    """Extracts the pitch value from the euler.

    :rtype: float.
    """
    return eulers[index.pitch]
