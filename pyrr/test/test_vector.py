import unittest
import math

import numpy

from pyrr import vector


class test_vector( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_zeroes( self ):
        vec = vector.zeros()

        self.assertTrue(
            numpy.array_equal( vec, [ 0.0, 0.0, 0.0 ] ),
            "Vector zeros not zeroed"
            )
    
    def test_normalise( self ):
        def single_vector():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            result = vector.normalise( vec )

            length = numpy.array(
                [ math.sqrt( numpy.sum( vec ** 2 ) ) ]
                )
            expected = vec / length

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector normalise not unit length"
                )
        single_vector()

        def batch_normalise():
            vec = numpy.array([ 1.0, 1.0, 1.0 ] )
            batch = numpy.tile( vec, (3, 1) )
            result = vector.normalise( batch )
            
            lengths = numpy.array(
                [ math.sqrt( numpy.sum( vec ** 2 ) ) ]
                )
            lengths = numpy.tile( lengths, (3,1) )
            expected = batch / lengths

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Batch vector normalise not unit length"
                )
        batch_normalise()

    def test_squared_length( self ):
        def single_vector():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            result = vector.squared_length( vec )

            expected = numpy.sum( vec ** 2 )

            self.assertEqual(
                result,
                expected,
                "Vector squared length incorrect"
                )
        single_vector()

        def batch_square_length():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            batch = numpy.tile( vec, (3,1) )
            result = vector.squared_length( batch )

            expected = numpy.array(
                [ numpy.sum( vec ** 2 ) ]
                )
            expected = numpy.tile( expected, (3) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector squared length calculation incorrect"
                )
        batch_square_length()

    def test_length( self ):
        def single_vector():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            result = vector.length( vec )

            expected = math.sqrt( numpy.sum( vec ** 2 ) )

            # ensure the calculated length is what we expect
            self.assertEqual(
                result,
                expected,
                "Vector length calculation incorrect"
                )
        single_vector()

        def batch_lengths():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            batch = numpy.tile( vec, (3,1) )
            result = vector.length( batch )

            expected = numpy.array(
                [ math.sqrt( numpy.sum( vec ** 2 ) ) ]
                )
            expected = numpy.tile( expected, (3) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector batch length calculation incorrect"
                )
        batch_lengths()

    def test_set_length( self ):
        def single_vector():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            length = 2.0
            result = vector.set_length( vec, length )

            current_length = numpy.array(
                [ math.sqrt( numpy.sum( vec ** 2 ) ) ]
                )
            expected = (vec / current_length) * 2.0

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector length not set correctly"
                )
        single_vector()

        def batch_vector():
            vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
            length = 2.0
            batch = numpy.tile( vec, (3,1) )
            result = vector.set_length( batch, length )

            current_length = numpy.array(
                [ math.sqrt( numpy.sum( vec ** 2 ) ) ]
                )
            expected = (vec / current_length) * 2.0
            expected = numpy.tile( expected, (3,1) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector length not set correctly"
                )
        batch_vector()

    def test_dot( self ):
        def vec_dot( vec1, vec2 ):
            x1, y1, z1 = vec1
            x2, y2, z2 = vec2
            return x1 * x2 + y1 * y2 + z1 * z2

        def adjacent():
            vec1 = numpy.array( [ 1.0, 0.0, 0.0 ] )
            vec2 = numpy.array( [ 0.0, 1.0, 0.0 ] )

            result = vector.dot( vec1, vec2 )

            expected = numpy.sum( vec1 * vec2 )
            assert expected == 0.0
            assert numpy.array_equal( expected, vec_dot( vec1, vec2 ) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Dot product of adjacent vectors incorrect"
                )
        adjacent()

        def parallel():
            vec1 = numpy.array( [ 0.0, 1.0, 0.0 ] )
            vec2 = numpy.array( [ 0.0, 1.0, 0.0 ] )

            result = vector.dot( vec1, vec2 )

            expected = numpy.sum( vec1 * vec2 )
            assert expected == 1.0
            assert numpy.array_equal( expected, vec_dot( vec1, vec2 ) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Dot product of parallel vectors incorrect"
                )
        parallel()

        def angle():
            vec1 = numpy.array( [ 1.0, 1.0, 0.0 ] )
            vec2 = numpy.array( [ 0.0, 1.0, 0.0 ] )
            result = vector.dot( vec1, vec2 )

            expected = numpy.sum( vec1 * vec2 )
            assert numpy.array_equal( expected, vec_dot( vec1, vec2 ) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Dot product of angled vectors incorrect"
                )
        angle()

        def batch():
            vecs1 = numpy.array([
                # adjacent
                [ 1.0, 0.0, 0.0],
                # parallel
                [ 0.0, 1.0, 0.0 ],
                # angled
                [ 1.0, 1.0, 0.0 ]
                ])
            vecs2 = numpy.array([
                # adjacent
                [ 0.0, 1.0, 0.0],
                # parallel
                [ 0.0, 1.0, 0.0 ],
                # angled
                [ 0.0, 1.0, 0.0 ]
                ])
            result = vector.dot( vecs1, vecs2 )

            expected = numpy.sum( vecs1 * vecs2, axis = -1 )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector dot calculation incorrect"
                )

            # assert individually
            assert numpy.array_equal( result[ 0 ], numpy.sum( vecs1[ 0 ] * vecs2[ 0 ] ) )
            assert numpy.array_equal( result[ 1 ], numpy.sum( vecs1[ 1 ] * vecs2[ 1 ] ) )
            assert numpy.array_equal( result[ 2 ], numpy.sum( vecs1[ 2 ] * vecs2[ 2 ] ) )
        batch()

    def test_cross_product( self ):
        def vec_cross( vec1, vec2 ):
            x1, y1, z1 = vec1
            x2, y2, z2 = vec2
            return [
                y1 * z2 - z1 * y2,
                z1 * x2 - x1 * z2,
                x1 * y2 - y1 * x2
                ]

        def single_vector():
            vec1 = numpy.array( [1.0, 0.0, 0.0] )
            vec2 = numpy.array( [0.0, 1.0, 0.0] )

            result = vector.cross( vec1, vec2 )

            expected = numpy.cross( vec1, vec2 )
            assert numpy.array_equal( expected, vec_cross( vec1, vec2 ) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector cross product incorrect"
                )

        def batch():
            vec1 = numpy.array( [1.0, 0.0, 0.0] )
            vec2 = numpy.array( [0.0, 1.0, 0.0] )
            batch1 = numpy.tile( vec1, (3,1) )
            batch2 = numpy.tile( vec2, (3,1) )

            result = vector.cross( batch1, batch2 )

            expected = numpy.cross( vec1, vec2 )
            expected = numpy.tile( expected, (3,1) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Vector cross product incorrect"
                )
        batch()

    def test_interoplation( self ):
        vec1 = numpy.array( [ 0.0, 0.0, 0.0 ] )
        vec2 = numpy.array( [ 1.0, 1.0, 1.0 ] )

        result = vector.interpolate( vec1, vec2, 0.5 )

        expected = numpy.array( [ 0.5, 0.5, 0.5 ] )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Interoplation value incorrect"
            )

    
if __name__ == '__main__':
    unittest.main()
