import unittest
import math

import numpy

from pyrr import matrix44


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        mat = matrix44.identity()

        for x in range( 4 ):
            for y in range( 4 ):
                if x == y:
                    # assert the diagonal is 1.0
                    self.assertEqual(
                        mat[ (x, y) ],
                        1.0,
                        "Not an identity matrix"
                        )
                else:
                    # all other values are 0.0
                    self.assertEqual(
                        mat[ (x, y) ],
                        0.0,
                        "Not an identity matrix"
                        )

    def test_set_translation( self ):
        mat = matrix44.identity()
        mat = matrix44.set_translation( mat, [ 1.0, 2.0, 3.0 ] )

        # translation goes down the last column in normal matrix
        self.assertEqual(
            mat[ 3 ][ 0 ],
            1.0,
            "Translation not set properly"
            )
        self.assertEqual(
            mat[ 3 ][ 1 ],
            2.0,
            "Translation not set properly"
            )
        self.assertEqual(
            mat[ 3 ][ 2 ],
            3.0,
            "Translation not set properly"
            )

    
if __name__ == '__main__':
    unittest.main()

