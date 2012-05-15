import unittest
import math

import numpy

from pyrr import geometric_tests

from pyrr import line
from pyrr import plane


class test_geometric_tests( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass


    def closest_point_on_line( self ):
        new_line = line.create_from_points(
            [ 0.0, 0.0, 0.0 ],
            [10.0, 0.0, 0.0 ]
            )

        point = geometric_tests.closest_point_on_line(
            new_line,
            [ 0.5, 1.0, 0.0 ]
            )
        self.assertEqual(
            point[ 0 ],
            0.5
            )
        self.assertEqual(
            point[ 1 ],
            0.0
            )
        self.assertEqual(
            point[ 2 ],
            0.0
            )

    def test_height_above_plane( self ):
        vectors = numpy.array([
            [ 0.0, 0.0, 1.0 ],
            [ 1.0, 0.0, 1.0 ],
            [ 0.0, 1.0, 1.0 ]
            ])
        new_plane = plane.create_from_points(
            vectors[ 0 ],
            vectors[ 1 ],
            vectors[ 2 ]
            )
        plane.flip_normal( new_plane )

        distance_vector = numpy.array([ 0.0, 0.0, 20.0 ])
        distance = geometric_tests.height_above_plane(
            new_plane,
            distance_vector
            )
        # should be 19.0
        self.assertEqual(
            distance,
            19.0,
            "Height above plane incorrect"
            )

    def test_closest_point_on_plane( self ):
        vectors = numpy.array([
            [ 0.0, 0.0, 1.0 ],
            [ 1.0, 0.0, 1.0 ],
            [ 0.0, 1.0, 1.0 ]
            ])
        new_plane = plane.create_from_points(
            vectors[ 0 ],
            vectors[ 1 ],
            vectors[ 2 ]
            )
        plane.flip_normal( new_plane )

        distance_vector = numpy.array([ 0.0, 0.0, 20.0 ])
        closest_point = geometric_tests.closest_point_on_plane(
            new_plane,
            distance_vector
            )
        # should be # 0, 0, 1
        self.assertEqual(
            closest_point[ 0 ],
            0.0,
            "Closest point on plane incorrect"
            )
        self.assertEqual(
            closest_point[ 1 ],
            0.0,
            "Closest point on plane incorrect"
            )
        self.assertEqual(
            closest_point[ 2 ],
            1.0,
            "Closest point on plane incorrect"
            )

    def test_point_intersect_rectangle( self ):
        rect = numpy.array(
            [
                [0.0, 0.0],
                [5.0, 5.0]
                ]
            )

        point = [ 0.0, 0.0 ]
        self.assertTrue(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )

        point = [ 5.0, 5.0 ]
        self.assertTrue(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )

        point = [ 1.0, 1.0 ]
        self.assertTrue(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )

        point = [-1.0, 1.0 ]
        self.assertFalse(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )

        point = [ 1.0, 10.0 ]
        self.assertFalse(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )

        point = [ 1.0,-1.0 ]
        self.assertFalse(
            numpy.array_equal(
                geometric_tests.point_intersect_rectangle(
                    point,
                    rect
                    ),
                point
                )
            )


if __name__ == '__main__':
    unittest.main()

