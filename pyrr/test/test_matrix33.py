import unittest
import math

import numpy

from pyrr import matrix33
from pyrr import quaternion


class test_matrix33( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        result = matrix33.identity()

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 identity incorrect"
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
        # identity
        quat = quaternion.identity()
        result = matrix33.create_from_quaternion( quat )

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix33 from quaternion incorrect with identity quaternion"
            )
    
if __name__ == '__main__':
    unittest.main()