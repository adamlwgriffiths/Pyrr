import unittest
import math

import numpy

from pyrr import matrix44
from pyrr import quaternion


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        mat = matrix44.identity()

        self.assertTrue(
            numpy.array_equal(
                mat,
                numpy.eye( 4 )
                ),
            "Not an identity matrix"
            )

    def test_create_from_translation( self ):
        translation = numpy.array( [ 1.0, 2.0, 3.0 ])
        mat = matrix44.create_from_translation( translation )

        # translation goes down the last column in normal matrix
        self.assertTrue(
            numpy.array_equal( mat[ 3, 0:3 ], translation ),
            "Translation not set properly"
            )

    def test_create_from_scale( self ):
        scale = numpy.array( [ 2.0, 3.0, 4.0 ] )

        mat = matrix44.create_from_scale( scale )

        # extract the diagonal scale and ignore the last value
        self.assertTrue(
            numpy.array_equal( mat.diagonal()[ :-1 ], scale ),
            "Scale not set properly"
            )

    def test_to_matrix33( self ):
        mat = matrix44.identity()
        mat = matrix44.to_matrix33( mat )

        self.assertTrue(
            numpy.array_equal( mat, numpy.eye( 3 ) ),
            "Matrix33 not extracted properly"
            )

    def test_create_from_quaternion( self ):
        # identity
        quat = quaternion.identity()
        mat = matrix44.create_from_quaternion( quat )

        self.assertTrue(
            numpy.array_equal( mat, numpy.eye( 4 ) ),
            "Quaternion to Matrix conversion failed with identity quaternion"
            )
    
if __name__ == '__main__':
    unittest.main()

