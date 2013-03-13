# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Euler angles.
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
    return numpy.array( [ pitch, roll, yaw ] )

def pitch( eulers ):
    return eulers[ 0 ]

def roll( eulers ):
    return eulers[ 1 ]

def yaw( eulers ):
    return eulers[ 2 ]
