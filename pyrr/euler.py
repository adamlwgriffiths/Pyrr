# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Euler angles.

Eulers are represented as 3 rotations: Pitch, Roll and Yaw.

Euler functions use numpy.arrays with 3 floats representing these values.
"""
import numpy


class index:
    #: The index of the pitch value within the euler
    pitch = 0

    #: The index of the roll value within the euler
    roll = 1

    #: The index of the yaw value within the euler
    yaw = 2


def create( pitch, roll, yaw ):
    """Creates an array storing the specified euler angles.

    Input values are in radians.

    :param float pitch: The pitch in radians.
    :param float roll: The roll in radians.
    :param float yaw: The yaw in radians.
    :rtype: A numpy.array of shape 3.
    """
    return numpy.array( [ pitch, roll, yaw ] )

def pitch( eulers ):
    """Extracts the pitch value from the euler.

    :rtype: A float.
    """
    return eulers[ 0 ]

def roll( eulers ):
    """Extracts the roll value from the euler.

    :rtype: A float.
    """
    return eulers[ 1 ]

def yaw( eulers ):
    """Extracts the yaw value from the euler.

    :rtype: A float.
    """
    return eulers[ 2 ]
