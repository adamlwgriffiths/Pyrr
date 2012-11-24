import unittest
import math

import numpy

from pyrr import quaternion


class test_quaternion( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        result = quaternion.identity()

        expected = numpy.array( [ 0.0, 0.0, 0.0, 1.0 ] )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Quaternion identity incorrect"
            )

    def test_normalise( self ):
        def identity():
            # normalise an identity quaternion
            quat = quaternion.identity()
            result = quaternion.normalise( quat )

            expected = numpy.array( [ 0.0, 0.0, 0.0, 1.0 ] )
            assert numpy.array_equal(
                expected,
                quat / math.sqrt( numpy.sum( quat ** 2 ) )
                )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Normalise identity quaternion incorrect"
                )
        identity()
    
        def non_identity():
            # normalise a quaternion of length 2.0
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            result = quaternion.normalise( quat )

            expected = quat / math.sqrt( numpy.sum( quat ** 2 ) )

            # check the length is 1.0
            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Normalise quaternion incorrect"
                )
        non_identity()

        def non_identity_batch():
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            batch = numpy.tile( quat, ( 3, 1 ) )
            result = quaternion.normalise( batch )

            expected = quat / math.sqrt( numpy.sum( quat ** 2 ) )
            expected = numpy.tile( expected, (3, 1) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Quaternion batch length calculation incorrect"
                )
        non_identity_batch()

    def test_length( self ):
        def identity():
            quat = quaternion.identity()
            result = quaternion.length( quat )

            expected = 1.0

            self.assertEqual(
                result,
                expected,
                "Identity quaternion length calculation incorrect"
                )
        identity()

        def identity_batch():
            quat = quaternion.identity()
            batch = numpy.tile( quat, (2,1) )
            result = quaternion.length( batch )

            expected = numpy.array(
                [ math.sqrt( numpy.sum( quat ** 2 ) ) ]
                )
            expected = numpy.tile( expected, (2) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Identity quaternion batch length calculation incorrect"
                )
        identity_batch()

        def non_identity():
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            result = quaternion.length( quat )

            expected = math.sqrt( numpy.sum( quat ** 2 ) )
            self.assertEqual(
                result,
                expected,
                "Quaternion length calculation incorrect"
                )
        non_identity()

        def non_identity_batch():
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            batch = numpy.tile( quat, ( 3, 1 ) )
            result = quaternion.length( batch )

            expected = numpy.array(
                [ math.sqrt( numpy.sum( quat ** 2 ) ) ]
                )
            expected = numpy.tile( expected, (3) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Quaternion batch length calculation incorrect"
                )
        non_identity_batch()

    def test_squared_length( self ):
        def identity():
            quat = quaternion.identity()
            result = quaternion.squared_length( quat )

            expected = 1.0

            self.assertEqual(
                result,
                expected,
                "Quaternion identity squared length calculation incorrect"
                )
        identity()

        def non_identity():
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            result = quaternion.squared_length( quat )

            expected = numpy.sum( quat ** 2 )

            self.assertEqual(
                result,
                expected,
                "Quaternion squared length calculation incorrect"
                )
        non_identity()

        def non_identity_batch():
            quat = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
            batch = numpy.tile( quat, ( 3, 1 ) )
            result = quaternion.squared_length( batch )

            expected = numpy.array(
                [ numpy.sum( quat ** 2 ) ]
                )
            expected = numpy.tile( expected, (3) )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Quaternion batch squared length calculation incorrect"
                )
        non_identity_batch()

if __name__ == '__main__':
    unittest.main()

