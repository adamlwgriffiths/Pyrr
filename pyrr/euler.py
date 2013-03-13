# -*- coding: utf-8 -*-
"""Provide functions for the creation and manipulation of Euler angles.
"""
import numpy


class index:
    pitch = 0
    roll = 1
    yaw = 2

def create( pitch, roll, yaw ):
    return numpy.array( [ pitch, roll, yaw ] )

def pitch( eulers ):
    return eulers[ 0 ]

def roll( eulers ):
    return eulers[ 1 ]

def yaw( eulers ):
    return eulers[ 2 ]
