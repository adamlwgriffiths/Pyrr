import unittest
import math

import numpy

from pyrr import plane

def vec_normalise( vec ):
    x, y, z = vec
    length = math.sqrt( x**2 + y**2 + z**2 )
    return vec / length


class test_plane( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_from_points( self ):
        def test_x_y():
            vecs = numpy.array(
                [
                    [ 1.0, 0.0, 0.0 ],
                    [ 0.0, 1.0, 0.0 ],
                    [ 1.0, 1.0, 0.0 ]
                    ],
                dtype = numpy.float
                )
            result = plane.create_from_points(
                vecs[ 0 ],
                vecs[ 1 ],
                vecs[ 2 ]
                )
            expected_normal = numpy.array([ 0.0, 0.0, 1.0 ])
            expected_d = 0

            self.assertTrue(
                numpy.array_equal( result[ :3 ], expected_normal ),
                "Plane normal incorrect"
                )
            self.assertTrue(
                numpy.array_equal( result[ 3 ], expected_d ),
                "Plane distance incorrect"
                )
        test_x_y()

    def test_create_from_position( self ):
        position = numpy.array( [ 1.0, 0.0, 0.0 ] )
        normal = numpy.array( [ 0.0, 3.0, 0.0 ] )

        result = plane.create_from_position(
            position,
            normal
            )

        expected_normal = numpy.array([0.0, 1.0, 0.0] )
        expected_position = numpy.array([0.0, 0.0, 0.0] )

        self.assertTrue(
            numpy.array_equal( result[ :3 ], expected_normal ),
            "Plane normal incorrect"
            )
        self.assertTrue(
            numpy.array_equal( plane.position(result), expected_position ),
            "Plane position incorrect"
            )

    def test_invert_normal( self ):
        p = numpy.array( [ 1.0, 0.0, 0.0, 1.0 ] )

        result = plane.invert_normal( p )

        expected = numpy.array( [-1.0, 0.0, 0.0, -1.0 ] )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Plane normal invert incorrect"
            )
    
if __name__ == '__main__':
    unittest.main()

