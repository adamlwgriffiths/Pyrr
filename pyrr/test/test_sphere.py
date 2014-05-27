import unittest
import math

import numpy

from pyrr import sphere

from pyrr import vector


class test_sphere( unittest.TestCase ):
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
        result = sphere.create_from_points( vecs )

        # centred around 0,0,0
        # with MAX LENGTH as radius
        lengths = vector.length( vecs )
        expected = numpy.array( [ 0.0, 0.0, 0.0, lengths.max() ] )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Sphere not calculated correctly"
            )


if __name__ == '__main__':
    unittest.main()
