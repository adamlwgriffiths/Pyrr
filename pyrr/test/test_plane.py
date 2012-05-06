import unittest
import math

import numpy

from pyrr import plane

def vec_normalise( vec ):
    x, y, z = vec
    length = math.sqrt( x**2 + y**2 + z**2 )
    return vec / length


class test_plane( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_from_points( self ):
        vecs = numpy.array(
            [
                [ 0.0, 1.0, 0.0 ],
                [ 0.0, 1.0,-1.0 ],
                [ 1.0, 1.0, 1.0 ]
                ],
            dtype = numpy.float
            )
        result = plane.create_from_points(
            vecs[ 0 ],
            vecs[ 1 ],
            vecs[ 2 ]
            )

        # we cant be sure where the position is, we just need to know
        # that the plane exists on the Y = 1 axis
        # with the normal facing along the Y axis
        # the order of the vertices we send determines which
        # way the normal faces
        self.assertEqual(
            result[ (0,1) ],
            vecs[ (0,1) ],
            "Plane position incorrect"
            )
        self.assertTrue(
            result[ (1,1) ] > 0.0,
            "Plane normal incorrect"
            )

    def test_create_from_position( self ):
        vecs = numpy.array(
            [
                [ 0.0, 0.0, 0.0 ],
                [ 0.0, 3.0, 0.0 ],
                [ 3.0, 0.0, 0.0 ]
                ],
            dtype = numpy.float
            )
        result = plane.create_from_position(
            vecs[ 0 ],
            vecs[ 1 ],
            vecs[ 2 ]
            )

        # position should be 0,0,0
        for value, position in zip( result[ 0 ], vecs[ 0 ] ):
            self.assertEqual(
                value,
                position,
                "Plane position incorrect"
                )

        vec_normal = vec_normalise( vecs[ 1 ] )
        # normal should be normalised along Y plane
        for value, normal in zip( result[ 1 ], vec_normal ):
            self.assertEqual(
                value,
                normal,
                "Plane normal incorrect"
                )


        # up vector should be normalised along X plane
        vec_up = vec_normalise( vecs[ 2 ] )
        for value, up in zip( result[ 2 ], vec_up ):
            self.assertEqual(
                value,
                up,
                "Plane up incorrect"
                )

    def test_flip_normal( self ):
        result = numpy.array(
            [
                [ 0.0, 0.0, 0.0 ],
                [ 0.0, 1.0, 0.0 ],
                [ 1.0, 0.0, 0.0 ]
                ],
            dtype = numpy.float
            )

        result2 = plane.flip_normal( result )
        self.assertEqual(
            result[ (0,1) ],
            0.0,
            "Flipping normal has moved plane"
            )
        self.assertTrue(
            result[ (1,1) ] < 0.0,
            "Normal not flipped"
            )
        self.assertEqual(
            result2[ (0,1) ],
            result[ (0,1) ],
            "Normal not flipped in place"
            )
    
if __name__ == '__main__':
    unittest.main()

