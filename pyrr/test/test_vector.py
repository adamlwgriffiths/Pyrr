import unittest
import math

import numpy

from pyrr import vector

def vec_length( vec ):
    x, y, z = vec
    return math.sqrt( x**2 + y**2 + z**2 )

def vec_sqr_length( vec ):
    x, y, z = vec
    return x**2 + y**2 + z**2

def vec_dot( vec1, vec2 ):
    x, y, z = vec1
    a, b, c = vec2
    return x*a + y*b + z*c

def vec_cross( vec1, vec2 ):
    x, y, z = vec1
    a, b, c = vec2
    return ( y*c - z*b, z*a - x*c, x*b - y*a )

class test_vector( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_zeroes( self ):
        vec = vector.zeros()
        for value in vec:
            self.assertEqual(
                value,
                0.0,
                "Vector not zeroed"
                )
    
    def test_normalise( self ):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ], dtype = float )
        vector.normalise( vec )
        self.assertEqual(
            vector.length( vec ),
            1.0,
            "Vector not unit length"
            )

    def test_batch_normalise( self ):
        vecs = numpy.array([
            [ 1.0, 1.0, 1.0 ],
            [ 0.0, 2.0, 0.0 ]
            ])
        vector.normalise( vecs )
        
        for vec in vecs:
            self.assertEqual(
                vec_length( vec ),
                1.0,
                "Vector not unit length"
                )

    def test_squared_length( self ):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ], dtype = float )
        self.assertEqual(
            vector.squared_length( vec ),
            vec_sqr_length( vec ),
            "Squared length incorrect"
            )

    def test_length( self ):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ], dtype = float )

        # normalise the vector ourselves
        vecLength = vec_length( vec )
        vec /= vecLength
        assert vec_length( vec ) == 1.0

        # ensure the calculated length is what we expect
        self.assertEqual(
            vector.length( vec ),
            1.0,
            "Incorrect length calculation"
            )

    def test_batch_lengths( self ):
        #
        # group length calc
        #
        vecs = numpy.array([
            [ 1.0, 1.0, 1.0 ],
            [ 0.0, 2.0, 0.0 ]
            ])
        lengths = vector.length( vecs )
        for vec, length in zip( vecs, lengths ):
            self.assertEqual(
                vec_length( vec ),
                length,
                "Incorrect length calculation"
                )

    def test_set_length( self ):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ], dtype = float )
        vector.set_length( vec, 2.0 )
        self.assertEqual(
            vec_length( vec ),
            2.0,
            "Vector length not set correctly"
            )

    def test_dot( self ):
        vec1 = numpy.array( [1.0, 0.0, 0.0], dtype = float )
        vec2 = numpy.array( [0.0, 1.0, 0.0], dtype = float )
        self.assertEqual(
            vector.dot( vec1, vec2 ),
            0.0,
            "Dot product of adjacent vectors incorrect"
            )

        vec1 = numpy.array( [0.0, 1.0, 0.0], dtype = float )
        vec2 = numpy.array( [0.0, 1.0, 0.0], dtype = float )
        self.assertEqual(
            vector.dot( vec1, vec2 ),
            1.0,
            "Dot product of adjacent vectors incorrect"
            )

        vec1 = numpy.array( [1.0, 1.0, 0.0], dtype = float )
        vec2 = numpy.array( [0.0, 1.0, 0.0], dtype = float )
        self.assertEqual(
            vector.dot( vec1, vec2 ),
            vec_dot( vec1, vec2 ),
            "Dot product of adjacent vectors incorrect"
            )

    def test_cross_product( self ):
        vec1 = numpy.array( [1.0, 0.0, 0.0], dtype = float )
        vec2 = numpy.array( [0.0, 1.0, 0.0], dtype = float )
        result = vector.cross( vec1, vec2 )
        test_result = vec_cross( vec1, vec2 )
        for a, b in zip( result, test_result ):
            self.assertEqual(
                a,
                b,
                "Cross product incorrect"
                )

    def test_interoplation( self ):
        vec1 = numpy.array(
            [ 0.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        vec2 = numpy.array(
            [ 1.0, 1.0, 1.0 ],
            dtype = numpy.float
            )
        result = vector.interpolate( vec1, vec2, 0.5 )
        for value in result:
            self.assertEqual(
                value,
                0.5,
                "Interoplation value incorrect"
                )

    
if __name__ == '__main__':
    unittest.main()
