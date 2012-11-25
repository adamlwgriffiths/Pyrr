import unittest
import math

import numpy

from pyrr import matrix33
from pyrr import matrix44
from pyrr import quaternion


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        result = matrix44.identity()

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 identity incorrect"
            )

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

    def test_to_matrix33( self ):
        mat = matrix44.identity()
        result = matrix44.to_matrix33( mat )

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 to_matrix33 incorrect"
            )

    def test_create_from_matrix33( self ):
        mat = matrix33.identity()
        result = matrix44.create_from_matrix33( mat )

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix33 to_matrix44 incorrect"
            )

    def test_create_from_quaternion( self ):
        # identity
        quat = quaternion.identity()
        result = matrix44.create_from_quaternion( quat )

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 from quaternion incorrect with identity quaternion"
            )
    
if __name__ == '__main__':
    unittest.main()
