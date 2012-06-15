'''
Created on 30/05/2011

@author: adam

TODO: make the 'cross' function accept Nd arrays
TODO: make the 'dot' function accept Nd arrays
'''

import numpy


def zeros():
    return numpy.zeros( 3, dtype = numpy.float )

def create_unit_length_x( out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )
    out[:] = [ 1.0, 0.0, 0.0 ]
    return out

def create_unit_length_y( out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )
    out[:] = [ 0.0, 1.0, 0.0 ]
    return out

def create_unit_length_z( out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = numpy.float )
    out[:] = [ 0.0, 0.0, 1.0 ]
    return out

def normalise( vec ):
    """
    Normalises an Nd list of vectors or a single vector
    to unit length.
    The value will be changed in place. The return value
    is for convenience.

    @param vec: an Nd array with the final dimension
    being size 3 (a vector).
    (eg. numpy.array([ x, y, z ]) or a Nx3 array
    (eg. numpy.array([ [x1, y1, z1], [x2, y2, z2] ]).
    This value will be updated in place.
    @return the normalised value
    """
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )
    shape = list( vec.shape )
    shape[ -1 ] = 1
    vec /= lengths.reshape( shape )
    return vec

def squared_length( vec ):
    """
    Calculates the squared length of a vector.
    Useful when trying to avoid the performance
    penalty of a square root operation.
    """
    lengths = numpy.sum( vec * vec, axis = -1 )

    return lengths

def length( vec ):
    """
    Returns the length of an Nd list of vectors
    or a single vector.

    @param vec: an Nd array with the final dimension
    being size 3 (a vector).
    (eg. numpy.array([ x, y, z ]) or a Nx3 array
    (eg. numpy.array([ [x1, y1, z1], [x2, y2, z2] ]).
    @return The length of the vectors.
    If a 1d array was passed, it will be an integer.
    Otherwise the result will be shape vec.ndim
    with the last dimension being size 1.
    """
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )
    shape = list( vec.shape )
    shape[ -1 ] = 1
    lengths.reshape( shape )

    return lengths

def set_length( vec, length ):
    """
    Changes the length of an Nd list of vectors or
    a single vector to 'length'.
    The value will be changed in place. The return value
    is for convenience.

    @param vec: an Nd array with the final dimension
    being size 3 (a vector).
    (eg. numpy.array([ x, y, z ]) or a Nx3 array
    (eg. numpy.array([ [x1, y1, z1], [x2, y2, z2] ]).
    This value will be updated in place.
    @return the updated vectors
    """
    lengths = numpy.apply_along_axis(
        numpy.linalg.norm,
        vec.ndim - 1,
        vec
        )
    shape = list( vec.shape )
    shape[ -1 ] = 1
    lengths.reshape( shape )

    scale = numpy.empty_like( lengths )
    scale.fill( length )
    scale /= lengths

    vec *= scale.reshape( shape )

    return vec

def dot( a, b ):
    """
    @param a: an Nd array with the final dimension
    being size 3. (a vector)
    @param b: an Nd array with the final dimension
    being size 3 (a vector)
    @return: the dot product of vectors a and b.
    """
    return numpy.sum( a * b, axis = -1 )

def cross( vector1, vector2 ):
    """
    @param vector1: a 1d array with 3 elements (a vector)
    @param vector2: a 1d array with 3 elements (a vector)
    """
    return numpy.cross( vector1, vector2 )

def interpolate( v1, v2, delta ):
    """
    Interpolates between 2 arrays of vectors (shape = N,3)
    by the specified delta (0.0 <= delta <= 1.0).
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

