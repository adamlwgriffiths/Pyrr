import unittest
import math

import numpy

from pyrr import aabb


class test_ray( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_add_point( self ):
        obj = aabb.empty()

        aabb.add_point( obj, [-1.0,-1.0,-1.0] )
        self.assertTrue(
            numpy.array_equal( obj[ 0 ], [-1.0,-1.0,-1.0 ] ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( obj[ 1 ], [-1.0,-1.0,-1.0 ] ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre(obj), [-1.0,-1.0,-1.0 ] ),
            "Add point failed"
            )

        aabb.add_point( obj, [ 1.0,-1.0,-1.0] )
        self.assertTrue(
            numpy.array_equal( obj[ 0 ], [-1.0,-1.0,-1.0] ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( obj[ 1 ], [ 1.0,-1.0,-1.0]  ),
            "Add point failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre( obj ), [ 0.0,-1.0,-1.0] ),
            "Add point failed"
            )

    def test_add_aabb( self ):
        obj = aabb.empty()
        aabb.add_point( obj, [-1.0,-1.0,-1.0] )
        aabb.add_point( obj, [ 1.0,-1.0,-1.0] )

        obj2 = aabb.create_from_bounds( [1.0,-2.0, 1.0], [2.0,-1.0, 1.0] )
        aabb.add_aabb( obj, obj2 )

        self.assertTrue(
            numpy.array_equal( aabb.minimum, [-1.0,-2.0,-1.0] ),
            "Add AABB failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.maximum, [ 2.0,-1.0, 1.0]  ),
            "Add AABB failed"
            )
        self.assertTrue(
            numpy.array_equal( aabb.centre, [ 0.5,-1.5, 0.0] ),
            "Add AABB failed"
            )


if __name__ == '__main__':
    unittest.main()

