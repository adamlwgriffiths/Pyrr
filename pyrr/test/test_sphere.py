import unittest
import math

import numpy

from pyrr import sphere

from pyrr import vector


class test_sphere( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_from_points( self ):
        vecs = numpy.array(
            [
                [ 0.0, 0.0, 0.0 ],
                [ 5.0, 5.0, 5.0 ],
                [ 0.0, 0.0, 5.0 ],
                [-5.0, 0.0, 0.0 ],
                ],
            dtype = numpy.float
            )
        # the biggest should be 5,5,5
        lengths = vector.length( vecs )
        expected_radius = lengths.max()

        result = sphere.create_from_points( vecs )
        self.assertEqual(
            result[ 1 ],
            expected_radius,
            "Sphere radius not calculated correctly"
            )
        for value in result[ 0 ]:
            self.assertEqual(
                value,
                0.0,
                "Sphere not centred around origin"
                )



if __name__ == '__main__':
    unittest.main()
