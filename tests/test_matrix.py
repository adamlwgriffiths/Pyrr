import unittest
import math

import numpy

from pyrr import matrix


class test_matrix( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_apply_scale( self ):
        vec = numpy.array( [ 2.0, 2.0, 2.0 ] )
        scale = numpy.array( [ 10.0, 2.0, 1.0 ] )
        result = matrix.apply_scale( vec, scale )

        self.assertTrue(
            numpy.array_equal( result, vec * scale ),
            "Apply scale incorrect"
            )

    def test_batch_apply_scale( self ):
        vecs = numpy.array(
            [
                [ 2.0, 2.0, 2.0 ],
                [ 4.0, 4.0, 4.0 ],
                [ 1.5,10.0,-4.0 ],
                [ 0.0, 0.0, 0.0 ],
                ]
            )
        scale = numpy.array( [ 10.0, 2.0, 1.0 ] )
        result = matrix.apply_scale( vecs, scale )

        self.assertTrue(
            numpy.array_equal( result, vecs * scale ),
            "Batch apply scale incorrect"
            )

    def test_apply_direction_scale( self ):
        def apply():
            # squash in the Z direction
            vec = numpy.array( [ 2.0, 1.0, 25.0 ] )
            direction = numpy.array( [ 0.0, 0.0, 1.0 ] )

            result = matrix.apply_direction_scale(
                vec,
                direction,
                0.0
                )

            self.assertTrue(
                numpy.array_equal( result, [ vec[ 0 ], vec[ 1 ], 0.0 ] ),
                "Scale incorrectly applied"
                )
        apply()

        def batch_apply():
            vecs = numpy.array(
                [
                    [ 0.0, 0.0, 0.0 ],
                    [ 0.0, 0.0, 1.0 ],
                    [ 1.0, 1.0, 1.0 ],
                    [ 2.0, 1.0, 25.0 ]
                    ]
                )
            direction = numpy.array( [ 0.0, 0.0, 1.0 ] )

            result = matrix.apply_direction_scale( vecs, direction, 0.0 )

            expected = numpy.array( vecs )
            expected[ :,-1 ] = 0.0

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Batch scale incorrectly applied"
                )
        batch_apply()

    
if __name__ == '__main__':
    unittest.main()

