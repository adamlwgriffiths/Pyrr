# -*- coding: utf-8 -*-
"""Provides functions for creating and manipulating 4D vectors.
"""
import numpy
from pyrr.utils import parameters_as_numpy_arrays


def create_identity(dtype=None):
    return numpy.array([0.0, 0.0, 0.0, 1.0], dtype=dtype)

def create_unit_length_x(dtype=None):
    return numpy.array([1.0, 0.0, 0.0, 1.0], dtype=dtype)

def create_unit_length_y(dtype=None):
    return numpy.array([0.0, 1.0, 0.0, 1.0], dtype=dtype)

def create_unit_length_z(dtype=None):
    return numpy.array([0.0, 0.0, 1.0, 1.0], dtype=dtype)

@parameters_as_numpy_arrays('vector')
def create_from_vector3(vector, dtype=None):
    dtype = dtype or vector.dtype
    return numpy.array([vec[0], vec[1], vec[2], 1.0], dtype=dtype)

def create_from_matrix44_translation(mat):
    return mat[3, 0:4].copy()


class index:
    #: The index of the X value within the vector
    x = 0

    #: The index of the Y value within the vector
    y = 1

    #: The index of the Z value within the vector
    z = 2

    #: The index of the W value within the vector
    w = 3


class unit:
    #: A vector of unit length in the X-axis. (1.0, 0.0, 0.0, 0.0)
    x = create_unit_length_x()

    #: A vector of unit length in the Y-axis. (0.0, 1.0, 0.0, 0.0)
    y = create_unit_length_y()

    #: A vector of unit length in the Z-axis. (0.0, 0.0, 1.0, 0.0)
    z = create_unit_length_z()
