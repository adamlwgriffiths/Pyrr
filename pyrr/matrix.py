'''
Created on 22/06/2011

@author: adam
'''

import numpy


column_major = 1
row_major = 2


def apply_direction_scale( vectors, direction, scale ):
    """
    Applies a directional scaling to a set of vectors.
    An example usage for this is to flatten a mesh against a
    single plane.

    @param vectors: a 2d numpy array of vectors
    eg. numpy.array([ [x,y,z] ])
    @param direction: a 1d numpy array of the direction to scale
    eg. numpy.array([ x,y,z ])
    Direction MUST be normalised prior to this call.
    @param scale: a float value for the scaling. A scale of 0.0 will flatten
    the vertices. 
    """
    
    """
    scaling is defined as:
    
             [p'][1 + (k - 1)n.x^2, (k - 1)n.x n.y^2, (k - 1)n.x n.z   ]
    S(n,k) = [q'][(k - 1)n.x n.y,   1 + (k - 1)n.y,   (k - 1)n.y n.z   ]
             [r'][(k - 1)n.x n.z,   (k - 1)n.y n.z,   1 + (k - 1)n.z^2 ]
    
    where:
    v' is the resulting vector after scaling
    v is the vector to scale
    n is the direction of the scaling
    n.x is the x component of n
    n.y is the y component of n
    n.z is the z component of n
    k is the scaling factor
    """
    
    scaleMinus1 = scale - 1
    matrix = numpy.array([
        # m1
        [
            # m11 = 1 + (k - 1)n.x^2
            1 + scaleMinus1 * (direction[ 0 ]**2),
            # m12 = (k - 1)n.x n.y^2
            scaleMinus1 * direction[ 0 ] * direction[ 1 ]**2,
            # m13 = (k - 1)n.x n.z
            scaleMinus1 * direction[ 0 ] * direction[ 2 ]
            ],
        # m2
        [
            # m21 = (k - 1)n.x n.y
            scaleMinus1 * direction[ 0 ] * direction[ 1 ],
            # m22 = 1 + (k - 1)n.y
            1 + scaleMinus1 * direction[ 1 ],
            # m23 = (k - 1)n.y n.z
            scaleMinus1 * direction[ 1 ] * direction[ 2 ]
            ],
        # m3
        [
            # m31 = (k - 1)n.x n.z
            scaleMinus1 * direction[ 0 ] * direction[ 2 ],
            # m32 = (k - 1)n.y n.z
            scaleMinus1 * direction[ 1 ] * direction[ 2 ],
            # m33 = 1 + (k - 1)n.z^2
            1 + scaleMinus1 * direction[ 2 ]**2
            ]
        ])
    
    return numpy.dot( vectors, matrix )

def apply_scale( vectors, scalingVector ):
    """
    Applies a 3 dimensional scale to a set of vectors.

    @param vectors: a 2d numpy array of vectors
    eg. numpy.array([ [x,y,z] ])
    @param scalingVector: the scale vector, can be a 1x3 array, list or tuple
    """
    # create a scaling matrix
    matrix = numpy.array([
        [ scalingVector[ 0 ], 0.0, 0.0 ],
        [ 0.0, scalingVector[ 1 ], 0.0 ],
        [ 0.0, 0.0, scalingVector[ 2 ] ]
        ])
    return numpy.dot( vectors, matrix )


if __name__ == "__main__":
    # scale by vector
    print "Scale by vector"
    vectors = numpy.array([ [ 2.0, 2.0, 2.0 ] ])
    scale = ( 10.0, 2.0, 1.0 )
    result = apply_scale( vectors, scale )
    print result
    assert result[ 0 ][ 0 ] == 20.0
    assert result[ 0 ][ 1 ] == 4.0
    assert result[ 0 ][ 2 ] == 2.0
    
    # scale by direction and value
    print "Scale by direction and value"
    vectors = numpy.array([
        [ 0.0, 0.0, 0.0 ],
        [ 0.0, 0.0, 1.0 ],
        [ 1.0, 1.0, 1.0 ],
        [ 2.0, 1.0, 25.0 ]
        ])
    direction = numpy.array([ 0.0, 0.0, 1.0 ])
    newVectors = apply_direction_scale( vectors, direction, 0.0 )
    print newVectors
    for index in xrange( len( vectors ) ):
        assert newVectors[ index ][ 0 ] == vectors[ index ][ 0 ]
        assert newVectors[ index ][ 1 ] == vectors[ index ][ 1 ]
        assert newVectors[ index ][ 2 ] == 0.0

