# -*- coding: utf-8 -*-
"""Common Vector manipulation functions.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy
from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


@all_parameters_as_numpy_arrays
def normalise( vec ):
    """Normalises an Nd list of vectors or a single vector
    to unit length.

    The vector is **not** changed in place.

    :param numpy.array vec: an Nd array with the final dimension
        being size 3 (a vector)
        ::

            numpy.array([ x, y, z ])

        Or an Nx3 array::

            numpy.array([
                [x1, y1, z1],
                [x2, y2, z2]
                ]).

    :rtype: A numpy.array the normalised value
    """
    # calculate the length
    # this is a duplicate of length(vec) because we
    # always want an array, even a 0-d array.
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )

    # repeat the value for each value of the vector
    lengths = lengths.repeat( vec.shape[-1] ).reshape( vec.shape )

    return vec / lengths

def squared_length( vec ):
    """Calculates the squared length of a vector.

    Useful when trying to avoid the performance
    penalty of a square root operation.

    :param numpy.array vec: An Nd numpy.array.
    :rtype: If one vector is supplied, the result with be a scalar.
        Otherwise the result will be an array of scalars with shape
        vec.ndim with the last dimension being size 1.
    """
    lengths = numpy.sum( vec ** 2, axis = -1 )

    return lengths

@all_parameters_as_numpy_arrays
def length( vec ):
    """Returns the length of an Nd list of vectors
    or a single vector.

    :param numpy.array vec: an Nd array with the final dimension
        being size 3 (a vector).

        Single vector::

            numpy.array([ x, y, z ])

        Nd array::
        
            numpy.array([
                [x1, y1, z1],
                [x2, y2, z2]
                ]).

    :rtype: If a 1d array was passed, it will be a scalar.
        Otherwise the result will be an array of scalars with shape
        vec.ndim with the last dimension being size 1.
    """
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )

    # a single vector will return a 0-d array
    # which doesn't act like a normal np array
    if lengths.ndim == 0:
        return lengths.item()
    return lengths

@parameters_as_numpy_arrays( 'vec' )
def set_length( vec, len ):
    """Resizes an Nd list of vectors or a single vector to 'length'.

    The vector is **not** changed in place.

    :param numpy.array vec: an Nd array with the final dimension
        being size 3 (a vector).

        Single vector::
            numpy.array([ x, y, z ])

        Nd array::
            numpy.array([
                [x1, y1, z1],
                [x2, y2, z2]
                ]).

    :rtype: A numpy.array of shape vec.shape.
    """
    # calculate the length
    # this is a duplicate of length(vec) because we
    # always want an array, even a 0-d array.
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )

    # repeat the value for each value of the vector
    lengths = lengths.repeat( vec.shape[-1] ).reshape( vec.shape )

    return vec / (lengths * (1.0 / len) )

def dot( v1, v2 ):
    """Calculates the dot product of two vectors.

    :param numpy.array v1: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v2: an Nd array with the final dimension
        being size 3 (a vector)
    :rtype: If a 1d array was passed, it will be a scalar.
        Otherwise the result will be an array of scalars with shape
        vec.ndim with the last dimension being size 1.
    """
    return numpy.sum( v1 * v2, axis = -1 )

def cross( v1, v2 ):
    """Calculates the cross-product of two vectors.

    :param numpy.array v1: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v2: an Nd array with the final dimension
        being size 3. (a vector)
    :rtype: A numpy.array with shape v1.shape.
    """
    return numpy.cross( v1, v2 )

def interpolate( v1, v2, delta ):
    """Interpolates between 2 arrays of vectors (shape = N,3)
    by the specified delta (0.0 <= delta <= 1.0).

    :param numpy.array v1: an Nd array with the final dimension
        being size 3. (a vector)
    :param numpy.array v2: an Nd array with the final dimension
        being size 3. (a vector)
    :param float delta: The interpolation percentage to apply,
        where 0.0 <= delta <= 1.0.
        When delta is 0.0, the result will be v1.
        When delta is 1.0, the result will be v2.
        Values inbetween will be an interpolation.
    :rtype: A numpy.array with shape v1.shape.
    """
    # scale the difference based on the time
    # we must do it this 'unreadable' way to avoid
    # loss of precision.
    # the 'readable' method (f_now = f_0 + (f1 - f0) * delta)
    # causes floating point errors due to the small values used
    # in md2 files and the values become corrupted.
    # this horrible code curtousey of this comment:
    # http://stackoverflow.com/questions/5448322/temporal-interpolation-in-numpy-matplotlib
    return v1 + ((v2 - v1) * delta)
    #return v1 * (1.0 - delta ) + v2 * delta
    t = delta
    t0 = 0.0
    t1 = 1.0
    delta_t = t1 - t0
    return (t1 - t) / delta_t * v1 + (t - t0) / delta_t * v2

def generate_normals( v1, v2, v3, normalise_result = True ):
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
    n = cross( b, a )
    if normalise_result:
        normalise( n )
    return n
