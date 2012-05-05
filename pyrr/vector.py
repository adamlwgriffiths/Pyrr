'''
Created on 30/05/2011

@author: adam

TODO: make the 'cross' function accept Nd arrays
TODO: make the 'dot' function accept Nd arrays
'''

import numpy


def zeros():
    return numpy.zeros( 3, dtype = float )

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
    return \
        vec[ 0 ] * vec[ 0 ] + \
        vec[ 1 ] * vec[ 1 ] + \
        vec[ 2 ] * vec[ 2 ]

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
    @param a: a 1d array with 3 elements (a vector)
    @param b: a 1d array with 3 elements (a vector)
    @return: the dot product of vectors a and b.
    """
    assert len( a ) == len( b ) == 3
    return numpy.dot( a, b )

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


if __name__ == "__main__":
    import math
    
    #
    # normalise / length
    # single vectors
    #
    print "Normalise vectors"
    vec = numpy.array( [ 1.0, 1.0, 1.0 ], dtype = float )
    normalise( vec )
    vecLength = math.sqrt( vec[ 0 ]**2 + vec[ 1 ]**2 + vec[ 2 ]**2 )
    assert vecLength == 1.0
    # individual length calc
    assert length( vec ) == 1.0

    vec = numpy.array([ 1.0, 1.0, 1.0 ])
    normalise( vec )
    value = length( vec )
    assert value == 1.0

    set_length( vec, 2.0 )
    value = length( vec )
    assert value == 2.0
    
    #
    # normalise / length
    # list of vectors
    #
    vecs = numpy.array([
        [ 1.0, 1.0, 1.0 ],
        [ 0.0, 2.0, 0.0 ]
        ])
    print "input %s" % str(vecs)
    normalise( vecs )
    print "output %s" % str(vecs)
    
    for vec in vecs:
        print "vec %s" % str(vec)
        vecLength = math.sqrt( vec[ 0 ]**2 + vec[ 1 ]**2 + vec[ 2 ]**2 )
        print vecLength
        assert vecLength == 1.0
        
        # individual length calc
        assert length( vec ) == 1.0
    
    #
    # group length calc
    #
    lengths = length( vecs )
    for value in lengths:
        assert value == 1.0

    set_length( vecs, 2.0 )
    lengths = length( vecs )
    for value in lengths:
        assert value == 2.0

    #
    # dot product
    #
    def dot_test( vec1, vec2 ):
        return \
            vec1[ 0 ] * vec2[ 0 ] + \
            vec1[ 1 ] * vec2[ 1 ] + \
            vec1[ 2 ] * vec2[ 2 ]

    vec1 = [ 1.0, 0.0, 0.0 ]
    vec2 = [ 0.5, 0.5, 0.0 ]
    assert dot( vec1, vec2 ) == dot_test( vec1, vec2 )

    vec1 = [ 20.0, 0.0, 0.0 ]
    vec2 = [ 0.5, 0.5, 0.0 ]
    assert dot( vec1, vec2 ) == dot_test( vec1, vec2 )

    #
    # cross product
    #
    vec1 = [ 1.0, 0.0, 0.0 ]
    vec2 = [ 0.0, 1.0, 0.0 ]
    result = cross( vec1, vec2 )
    assert result[ 0 ] == 0.0
    assert result[ 1 ] == 0.0
    assert result[ 2 ] == 1.0

    #
    # interpolate
    #
    vec1 = numpy.array(
        [ 0.0, 0.0, 0.0 ],
        dtype = numpy.float
        )
    vec2 = numpy.array(
        [ 1.0, 1.0, 1.0 ],
        dtype = numpy.float
        )
    result = interpolate( vec1, vec2, 0.5 )
    assert result[ 0 ] == 0.5
    assert result[ 1 ] == 0.5
    assert result[ 2 ] == 0.5

