import unittest
import math

import numpy

from pyrr import aabb


class test_aabb( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_from_points( self ):
        """
        points = numpy.array(
            [
                [-1.0,-1.0,-1.0]
                ]
            )
        """
        points = numpy.array( [ [-1.0,-1.0,-1.0 ] ] )
        result = aabb.create_from_points( points )
        
        expected = numpy.tile( points, (2,1) )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Create from points failed"
            )

    def test_centre_point( self ):
        def single_point():
            points = numpy.array( [ [-1.0,-1.0,-1.0 ] ] )
            obj = aabb.create_from_points( points )
            result = aabb.centre_point( obj )

            expected = numpy.array( [-1.0,-1.0,-1.0 ] )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "AABB single point centre point incorrect"
                )
        single_point()

        def multiple_points():
            points = numpy.array(
                [
                    [ 1.0, 1.0, 1.0 ],
                    [-1.0,-1.0,-1.0 ]
                    ]
                )
            obj = aabb.create_from_points( points )
            result = aabb.centre_point( obj )

            expected = numpy.zeros( 3 )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "AABB multiple points centre point incorrect"
                )
        multiple_points()

    def test_create_from_aabbs( self ):
        # -1
        a1 = numpy.array(
            [
                [-1.0,-1.0,-1.0 ],
                [-1.0,-1.0,-1.0 ]
                ]
            )
        # +1
        a2 = numpy.array(
            [
                [ 1.0, 1.0, 1.0 ],
                [ 1.0, 1.0, 1.0 ]
                ]
            )

        # -1 to +1
        result = aabb.create_from_aabbs( numpy.array( [ a1, a2 ] ) )

        expected = numpy.array(
            [
                [-1.0,-1.0,-1.0 ],
                [ 1.0, 1.0, 1.0 ]
                ]
            )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Create from AABBS failed"
            )

    def test_add_point( self ):
        obj = numpy.array(
            [
                [-1.0,-1.0,-1.0],
                [-1.0,-1.0,-1.0]
                ]
            )
        points = numpy.array( [ 1.0, 1.0, 1.0] )

        result = aabb.add_points( obj, points )

        expected = numpy.array(
            [
                [-1.0,-1.0,-1.0 ],
                [ 1.0, 1.0, 1.0 ]
                ]
            )

        self.assertTrue(
            numpy.array_equal( result, expected),
            "Add point failed"
            )

    def test_add_aabbs( self ):
        a1 = numpy.array(
            [
                [-1.0,-1.0,-1.0],
                [-1.0,-1.0,-1.0]
                ]
            )
        a2 = numpy.array(
            [
                [ 1.0, 1.0, 1.0],
                [ 1.0, 1.0, 1.0]
                ]
            )
        result = aabb.add_aabbs( a1, a2 )

        expected = numpy.array(
            [
                [-1.0,-1.0,-1.0 ],
                [ 1.0, 1.0, 1.0 ]
                ]
            )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Add AABB failed"
            )


if __name__ == '__main__':
    unittest.main()

