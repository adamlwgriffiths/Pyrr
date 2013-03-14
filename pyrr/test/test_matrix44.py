import unittest
import math

import numpy

from nose.tools import ok_

from pyrr import matrix33
from pyrr import matrix44
from pyrr import quaternion
from pyrr import vector3


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_identity( self ):
        result = matrix44.create_identity()

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 identity incorrect"
            )

    def test_perspective_projection_works_fine( self ):
        p = matrix44.create_perspective_projection_matrix( 90, 4.0/3, 0.01, 1000 )

        for point, is_inside in (
            ( (0, 0, 1), False ),
            ( (0, 0, 0), False ),
            ( (0, 0, -0.02), True ),
            ( (0, 0, -1000), True ),
            ( (0, 1.50, -1), False ),
            ( (0, 0, -1001), False ),
            ( (50, 0, -0.02), False ),
            ( (0, 50, -0.02), False ),
                ):
            self.check_projection_classifies_point_correctly(
                p, numpy.array( point + ( 1, ) ), is_inside)

    def check_projection_classifies_point_correctly( self, matrix, point, is_inside ):
        transformed = matrix44.multiply( point, matrix )

        # Avoid division by zero warning
        if transformed[ 3 ] == 0:
            assert not is_inside
        else:
            transformed[ 0:3 ] /= transformed[ 3 ]

            max_coordinate = max( abs( c ) for c in transformed[ 0:3 ] )
            assert is_inside == ( max_coordinate <= 1.0 )


    def test_create_from_translation( self ):
        translation = numpy.array( [ 2.0, 3.0, 4.0 ] )
        mat = matrix44.create_from_translation( translation )
        result = mat[ 3, 0:3 ]

        expected = translation

        # translation goes down the last column in normal matrix
        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 translation not set properly"
            )

    def test_create_from_scale( self ):
        scale = numpy.array( [ 2.0, 3.0, 4.0 ] )

        mat = matrix44.create_from_scale( scale )

        result = mat.diagonal()[ :-1 ]

        expected = scale

        # extract the diagonal scale and ignore the last value
        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 scale not set properly"
            )

    def test_create_matrix33_view( self ):
        mat = matrix44.create_identity()
        result = matrix44.create_matrix33_view( mat )

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 create_matrix33_view incorrect"
            )

    def test_create_from_matrix33( self ):
        mat = matrix33.create_identity()
        result = matrix44.create_from_matrix33( mat )

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 create_from_matrix33 incorrect"
            )

    def test_create_from_quaternion( self ):
        def identity():
            quat = quaternion.create_identity()
            result = matrix44.create_from_quaternion( quat )

            expected = numpy.eye( 4 )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix44 from quaternion incorrect with identity quaternion"
                )
        identity()

        def rotated_x():
            quat = quaternion.create_from_x_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_x_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about X"
                )
        rotated_x()

        def rotated_y():
            quat = quaternion.create_from_y_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_y_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about Y"
                )
        rotated_y()

        def rotated_z():
            quat = quaternion.create_from_z_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_z_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about Z"
                )
        rotated_z()

    def test_apply_to_vector( self ):
        def identity():
            mat = matrix44.create_identity()
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = vec

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix44 apply_to_vector incorrect with identity"
                )
        identity()

        def rotated_x():
            mat = matrix44.create_from_x_rotation( math.pi )
            vec = vector3.unit.y

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about X"
                )
        rotated_x()

        def rotated_y():
            mat = matrix44.create_from_y_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about Y"
                )
        rotated_y()

        def rotated_z():
            mat = matrix44.create_from_z_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about Y"
                )
        rotated_z()

        def translation():
            mat = matrix44.create_identity()
            vec = numpy.array([0.0, 0.0, 0.0])
            mat[3,0:3] = [1.0, 2.0, 3.0]

            result = matrix44.apply_to_vector( mat, vec )

            expected = mat[3,0:3]

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with translation"
                )
        translation()
    
if __name__ == '__main__':
    unittest.main()
