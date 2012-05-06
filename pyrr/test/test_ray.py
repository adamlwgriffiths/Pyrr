import unittest
import math

import numpy

from pyrr import ray


class test_ray( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass


    def test_create_from_line( self ):
        result = ray.create_from_line(
            numpy.array(
                [
                    [ 0.0, 0.0, 0.0 ],
                    [10.0, 0.0, 0.0 ]
                    ],
                dtype = numpy.float
                )
            )

        self.assertEqual(
            result[ 0 ][ 0 ],
            0.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 0 ][ 1 ],
            0.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 0 ][ 2 ],
            0.0,
            "Create ray from line incorrect"
            )
        # length should be normalised
        self.assertEqual(
            result[ 1 ][ 0 ],
            1.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 1 ][ 1 ],
            0.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 1 ][ 2 ],
            0.0,
            "Create ray from line incorrect"
            )

        result = ray.create_from_line(
            numpy.array(
                [
                    [ 0.0,10.0, 0.0 ],
                    [10.0,10.0, 0.0 ]
                    ],
                dtype = numpy.float
                )
            )

        self.assertEqual(
            result[ 0 ][ 0 ],
            0.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 0 ][ 1 ],
            10.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 0 ][ 2 ],
            0.0,
            "Create ray from line incorrect"
            )
        # length should be normalised
        self.assertEqual(
            result[ 1 ][ 0 ],
            1.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 1 ][ 1 ],
            0.0,
            "Create ray from line incorrect"
            )
        self.assertEqual(
            result[ 1 ][ 2 ],
            0.0,
            "Create ray from line incorrect"
            )


if __name__ == '__main__':
    unittest.main()

