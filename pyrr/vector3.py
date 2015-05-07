# -*- coding: utf-8 -*-
"""Provides functions for creating and manipulating 3D vectors.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np

# import common vector operations
from .vector import *


def create(x=0., y=0., z=0., dtype=None):
    if isinstance(x, (list, np.ndarray)):
        raise ValueError('Function requires non-list arguments')
    return np.array([x,y,z], dtype=dtype)

def create_unit_length_x(dtype=None):
    return np.array([1.0, 0.0, 0.0], dtype=dtype)

def create_unit_length_y(dtype=None):
    return np.array([0.0, 1.0, 0.0], dtype=dtype)

def create_unit_length_z(dtype=None):
    return np.array([0.0, 0.0, 1.0], dtype=dtype)

@parameters_as_numpy_arrays('vector')
def create_from_vector4(vector, dtype=None):
    """Returns a vector3 and the W component as a tuple.
    """
    dtype = dtype or vector.dtype
    return (np.array([vector[0], vector[1], vector[2]], dtype=dtype), vector[3])

@parameters_as_numpy_arrays('mat')
def create_from_matrix44_translation(mat, dtype=None):
    return np.array(mat[3, :3], dtype=dtype)

def cross(v1, v2):
    """Calculates the cross-product of two vectors.

    :param numpy.array v1: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v2: an Nd array with the final dimension
        being size 3. (a vector)
    :rtype: A np.array with shape v1.shape.
    """
    return np.cross(v1, v2)

def generate_normals(v1, v2, v3, normalise_result=True):
    """Generates a normal vector for 3 vertices.

    The result is a normalised vector.
    
    It is assumed the ordering is counter-clockwise starting
    at v1, v2 then v3::

        v1      v3
          \    /
            v2

    The vertices are Nd arrays and may be 1d or Nd.
    As long as the final axis is of size 3.

    For 1d arrays::
        >>> v1 = numpy.array( [ 1.0, 0.0, 0.0 ] )
        >>> v2 = numpy.array( [ 0.0, 0.0, 0.0 ] )
        >>> v3 = numpy.array( [ 0.0, 1.0, 0.0 ] )
        >>> vector.generate_normals( v1, v2, v3 )
        array([ 0.,  0., -1.])

    For Nd arrays::
        >>> v1 = numpy.array( [ [ 1.0, 0.0, 0.0 ], [ 1.0, 0.0, 0.0 ] ] )
        >>> v2 = numpy.array( [ [ 0.0, 0.0, 0.0 ], [ 0.0, 0.0, 0.0 ] ] )
        >>> v3 = numpy.array( [ [ 0.0, 1.0, 0.0 ], [ 0.0, 1.0, 0.0 ] ] )
        >>> vector.generate_normals( v1, v2, v3 )
        array([[ 0.,  0., -1.],
               [ 0.,  0., -1.]])

    :param numpy.array v1: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v2: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v3: an Nd array with the final dimension
        being size 3. (a vector)
    :param boolean normalise_result: Specifies if the result should
        be normalised before being returned.
    """
    # make vectors relative to v2
    # we assume opengl counter-clockwise ordering
    a = v1 - v2
    b = v3 - v2
    n = cross(b, a)
    if normalise_result:
        normalise(n)
    return n


class index:
    #: The index of the X value within the vector
    x = 0

    #: The index of the Y value within the vector
    y = 1

    #: The index of the Z value within the vector
    z = 2


class unit:
    #: A vector of unit length in the X-axis. (1.0, 0.0, 0.0)
    x = create_unit_length_x()

    #: A vector of unit length in the Y-axis. (0.0, 1.0, 0.0)
    y = create_unit_length_y()

    #: A vector of unit length in the Z-axis. (0.0, 0.0, 1.0)
    z = create_unit_length_z()
