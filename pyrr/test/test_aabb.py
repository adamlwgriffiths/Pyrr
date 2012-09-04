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
        obj = aabb.create_from_points(
            numpy.array(
                [[-1.0,-1.0,-1.0]],
                dtype = numpy.float
                )
            )
        self.assertTrue(
            numpy.array_equal( obj[ 0 ], [-1.0,-1.0,-1.0 ] ),
            "Create from points failed"
            )
        self.assertTrue(
            numpy.array_equal( obj[ 1 ], [-1.0,-1.0,-1.0 ] ),
            "Create from points failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre_point(obj), [-1.0,-1.0,-1.0 ] ),
            "Create from points failed"
            )

    def test_create_from_aabbs( self ):
        a1 = aabb.create_from_points(
            [
                [ 0.0, 0.0, 0.0 ],
                [ 1.0, 1.0,-1.0 ]
                ]
            )
        a2 = aabb.create_from_points(
            [
                [ 0.0, 0.0, 0.0 ],
                [-1.0,-1.0, 1.0 ]
                ]
            )
        a3 = aabb.create_from_aabbs(
            numpy.array(
                [ a1, a2 ]
                )
            )

        self.assertTrue(
            numpy.array_equal(
                a3[ 0 ],
                [-1.0,-1.0,-1.0 ]
                ),
            "Create from AABBS failed"
            )
        self.assertTrue(
            numpy.array_equal(
                a3[ 1 ],
                [ 1.0, 1.0, 1.0 ]
                ),
            "Create from AABBS failed"
            )


    def test_add_point( self ):
        obj = numpy.array(
            [
                [-1.0,-1.0,-1.0],
                [-1.0,-1.0,-1.0]
                ],
            dtype = numpy.float
            )

        aabb.add_points(
            obj,
            numpy.array(
                [[ 1.0,-1.0,-1.0]],
                dtype = numpy.float
                ),
            out = obj
            )
        self.assertTrue(
            numpy.array_equal( obj[ 0 ], [-1.0,-1.0,-1.0] ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( obj[ 1 ], [ 1.0,-1.0,-1.0]  ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre_point( obj ), [ 0.0,-1.0,-1.0] ),
            "Add point failed"
            )

    def test_add_aabbs( self ):
        obj = aabb.create_from_points(
            numpy.array(
                [
                    [-1.0,-1.0,-1.0],
                    [ 1.0,-1.0,-1.0]
                    ],
                dtype = numpy.float
                )
            )

        obj2 = aabb.create_from_bounds( [1.0,-2.0, 1.0], [2.0,-1.0, 1.0] )
        aabb.add_aabbs(
            obj,
            numpy.array( [ obj2 ] ),
            out = obj
            )

        self.assertTrue(
            numpy.array_equal( aabb.minimum(obj), [-1.0,-2.0,-1.0] ),
            "Add AABB failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.maximum(obj), [ 2.0,-1.0, 1.0]  ),
            "Add AABB failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre_point(obj), [ 0.5,-1.5, 0.0] ),
            "Add AABB failed"
            )


if __name__ == '__main__':
    unittest.main()

