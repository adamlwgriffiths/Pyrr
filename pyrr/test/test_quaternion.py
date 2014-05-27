import unittest
import math

import numpy

from pyrr import quaternion
from pyrr import vector3


class test_quaternion( unittest.TestCase ):
    def test_create( self ):
        result = quaternion.create()

        expected = numpy.array( [ 0.0, 0.0, 0.0, 1.0 ] )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Quaternion identity incorrect"
            )

    def test_normalise( self ):
        def identity():
            # normalise an identity quaternion
            quat = quaternion.create()
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
            quat = quaternion.create()
            result = quaternion.length( quat )

            expected = 1.0

            self.assertEqual(
                result,
                expected,
                "Identity quaternion length calculation incorrect"
                )
        identity()

        def identity_batch():
            quat = quaternion.create()
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
            quat = quaternion.create()
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


    def test_apply_to_vector( self ):
        def identity():
            quat = quaternion.create()
            vec = vector3.unit.x

            result = quaternion.apply_to_vector( quat, vec )

            expected = vec

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Quaternion apply_to_vector incorrect with identity"
                )
        identity()

        def rotated_x():
            quat = quaternion.create_from_x_rotation( math.pi )
            vec = vector3.unit.y

            result = quaternion.apply_to_vector( quat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Quaternion apply_to_vector incorrect with rotation about X"
                )
        rotated_x()

        def rotated_y():
            quat = quaternion.create_from_y_rotation( math.pi )
            vec = vector3.unit.x

            result = quaternion.apply_to_vector( quat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Quaternion apply_to_vector incorrect with rotation about Y"
                )
        rotated_y()

        def rotated_z():
            quat = quaternion.create_from_z_rotation( math.pi )
            vec = vector3.unit.x

            result = quaternion.apply_to_vector( quat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Quaternion apply_to_vector incorrect with rotation about Y"
                )
        rotated_z()


if __name__ == '__main__':
    unittest.main()

