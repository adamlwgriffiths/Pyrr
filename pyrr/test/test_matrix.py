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
        vec = numpy.array(
            [ 2.0, 2.0, 2.0 ],
            dtype = numpy.float
            )
        scale = ( 10.0, 2.0, 1.0 )
        scaled = matrix.apply_scale( vec, scale )

        self.assertEqual(
            scaled[ 0 ],
            vec[ 0 ] * scale[ 0 ],
            "Apply scale incorrect"
            )
        self.assertEqual(
            scaled[ 1 ],
            vec[ 1 ] * scale[ 1 ],
            "Apply scale incorrect"
            )
        self.assertEqual(
            scaled[ 2 ],
            vec[ 2 ] * scale[ 2 ],
            "Apply scale incorrect"
            )

    def test_batch_apply_scale( self ):
        vecs = numpy.array(
            [
                [ 2.0, 2.0, 2.0 ],
                [ 4.0, 4.0, 4.0 ],
                [ 1.5,10.0,-4.0 ],
                [ 0.0, 0.0, 0.0 ],
                ],
                dtype = numpy.float
            )
        scale = ( 10.0, 2.0, 1.0 )
        result = matrix.apply_scale( vecs, scale )

        for vec, scaled in zip( vecs, result ):
            self.assertEqual(
                scaled[ 0 ],
                vec[ 0 ] * scale[ 0 ],
                "Apply scale incorrect"
                )
            self.assertEqual(
                scaled[ 1 ],
                vec[ 1 ] * scale[ 1 ],
                "Apply scale incorrect"
                )
            self.assertEqual(
                scaled[ 2 ],
                vec[ 2 ] * scale[ 2 ],
                "Apply scale incorrect"
                )

    def test_apply_direction_scale( self ):
        vec = numpy.array(
            [ 2.0, 1.0, 25.0 ],
            dtype = numpy.float
            )
        direction = numpy.array([ 0.0, 0.0, 1.0 ])
        scaled = matrix.apply_direction_scale(
            vec,
            direction,
            0.0
            )

        self.assertEqual(
            scaled[ 0 ],
            vec[ 0 ],
            "Scale incorrectly applied"
            )
        self.assertEqual(
            scaled[ 1 ],
            vec[ 1 ],
            "Scale incorrectly applied"
            )
        self.assertEqual(
            scaled[ 2 ],
            0.0,
            "Scale incorrectly applied"
            )


    def test_batch_apply_direction_scale( self ):
        vecs = numpy.array(
            [
                [ 0.0, 0.0, 0.0 ],
                [ 0.0, 0.0, 1.0 ],
                [ 1.0, 1.0, 1.0 ],
                [ 2.0, 1.0, 25.0 ]
                ],
            dtype = numpy.float
            )
        direction = numpy.array([ 0.0, 0.0, 1.0 ])
        result = matrix.apply_direction_scale(
            vecs,
            direction,
            0.0
            )

        for vec, scaled in zip( vecs, result ):
            self.assertEqual(
                scaled[ 0 ],
                vec[ 0 ],
                "Scale incorrectly applied"
                )
            self.assertEqual(
                scaled[ 1 ],
                vec[ 1 ],
                "Scale incorrectly applied"
                )
            self.assertEqual(
                scaled[ 2 ],
                0.0,
                "Scale incorrectly applied"
                )

    
if __name__ == '__main__':
    unittest.main()

