import numpy
from utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


@all_parameters_as_numpy_arrays
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
    """
    Calculates the squared length of a vector.
    Useful when trying to avoid the performance
    penalty of a square root operation.
    """
    lengths = numpy.sum( vec ** 2, axis = -1 )

    return lengths

@all_parameters_as_numpy_arrays
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

    # a single vector will return a 0-d array
    # which doesn't act like a normal np array
    if lengths.ndim == 0:
        return lengths.item()
    return lengths

@parameters_as_numpy_arrays( 'vec' )
def set_length( vec, len ):
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
    """
    @param a: an Nd array with the final dimension
    being size 3. (a vector)
    @param b: an Nd array with the final dimension
    being size 3 (a vector)
    @return: the dot product of vectors a and b.
    """
    return numpy.sum( v1 * v2, axis = -1 )

def cross( v1, v2 ):
    """
    @param vector1: an Nd array with 3 elements (a vector)
    @param vector2: an Nd array with 3 elements (a vector)
    (eg. numpy.array( [ x, y, z ]) )
    (eg. numpy.array( [ [ x1, y1, z1 ], [x2, y2, z2] ]) )
    """
    return numpy.cross( v1, v2 )

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

def generate_normals( v1, v2, v3, normalise_result = True ):
    """Generates a normal vector for 3 vertices.
    The result is a normalised vector.
    
    It is assumed the ordering is counter-clockwise starting
    at v1, v2 then v3.

    v1      v3
      \    /
        v2

    The vertices are Nd arrays and may be 1d or Nd.
    As long as the final axis is of size 3.

    eg. For 1d arrays:
    vertices = numpy.array([
        x, y, z
        ])

    result = numpy.array([
        x, y, z
        ])

    eg. For Nd arrays:
    vertices = numpy.array([
        [x1, y1, z1],
        [x2, y2, z2],
        [x3, y3, z3]
        ])

    result = numpy.array([
        [ 1x, 1y, 1z ],
        [ 2x, 2y, 2x ]
        ])
    """
    # make vectors relative to v2
    # we assume opengl counter-clockwise ordering
    a = v1 - v2
    b = v3 - v2
    n = cross( b, a )
    if normalise_result:
        normalise( n )
    return n
