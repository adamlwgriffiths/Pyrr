import unittest
import math

import numpy
from numpy.testing import assert_array_almost_equal

from pyrr import matrix33
from pyrr import quaternion
from pyrr import vector3


class test_matrix33( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_identity( self ):
        result = matrix33.create_identity()

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 identity incorrect"
            )

    def test_create_from_xyz_rotation( self ):
        angle = math.pi / 2.0

        for input, axis, output in (
            ( ( 0, 1, 0 ), 'x', ( 0, 0,-1 ) ),
            ( ( 0, 1, 0 ), 'y', ( 0, 1, 0 ) ),
            ( ( 0, 1, 0 ), 'z', ( 1, 0, 0 ) ),
            ( ( 1, 0, 0 ), 'x', ( 1, 0, 0 ) ),
            ( ( 1, 0, 0 ), 'y', ( 0, 0, 1 ) ),
            ( ( 1, 0, 0 ), 'z', ( 0,-1, 0 ) ),
            ( ( 0, 0, 1 ), 'x', ( 0, 1, 0 ) ),
            ( ( 0, 0, 1 ), 'y', (-1, 0, 0 ) ),
            ( ( 0, 0, 1 ), 'z', ( 0, 0, 1 ) ),
        ):
            input = numpy.array(input)
            fun = getattr(matrix33, 'create_from_%s_rotation' % (axis,))
            matrix = fun(angle)
            result = numpy.dot(input, matrix)
            expected = numpy.array(output)

            assert_array_almost_equal(
                result, expected,
                err_msg='Axis %s, input %s' % ( axis, input, )
            )


    def test_create_from_scale( self ):
        scale = numpy.array( [ 2.0, 3.0, 4.0 ] )

        mat = matrix33.create_from_scale( scale )

        result = mat.diagonal()

        expected = scale

        # extract the diagonal scale and ignore the last value
        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix33 scale not set properly"
            )

    def test_create_from_quaternion( self ):
        def identity():
            quat = quaternion.create_identity()
            result = matrix33.create_from_quaternion( quat )

            expected = numpy.eye( 3 )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix33 from quaternion incorrect with identity quaternion"
                )
        identity()

        def rotated_x():
            quat = quaternion.create_from_x_rotation( math.pi )
            result = matrix33.create_from_quaternion( quat )

            expected = matrix33.create_from_x_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 from quaternion incorrect with PI rotation about X"
                )
        rotated_x()

        def rotated_y():
            quat = quaternion.create_from_y_rotation( math.pi )
            result = matrix33.create_from_quaternion( quat )

            expected = matrix33.create_from_y_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 from quaternion incorrect with PI rotation about Y"
                )
        rotated_y()

        def rotated_z():
            quat = quaternion.create_from_z_rotation( math.pi )
            result = matrix33.create_from_quaternion( quat )

            expected = matrix33.create_from_z_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 from quaternion incorrect with PI rotation about Z"
                )
        rotated_z()

    def test_apply_to_vector( self ):
        def identity():
            mat = matrix33.create_identity()
            vec = vector3.unit.x

            result = matrix33.apply_to_vector( mat, vec )

            expected = vec

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix33 apply_to_vector incorrect with identity"
                )
        identity()

        def rotated_x():
            mat = matrix33.create_from_x_rotation( math.pi )
            vec = vector3.unit.y

            result = matrix33.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 apply_to_vector incorrect with rotation about X"
                )
        rotated_x()

        def rotated_y():
            mat = matrix33.create_from_y_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix33.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 apply_to_vector incorrect with rotation about Y"
                )
        rotated_y()

        def rotated_z():
            mat = matrix33.create_from_z_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix33.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix33 apply_to_vector incorrect with rotation about Y"
                )
        rotated_z()

if __name__ == '__main__':
    unittest.main()
