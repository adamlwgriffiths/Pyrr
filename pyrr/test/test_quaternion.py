import unittest
import math

import numpy

from pyrr import quaternion


class test_quaternion( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_identity( self ):
        quat = numpy.array(
            [0.0, 0.0, 0.0, 0.0],
            dtype = float
            )
        quat2 = quat
    
        quaternion.identity( quat )
        self.assertEqual(
            quat[ 0 ],
            1.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 1 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 2 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 3 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertTrue(
            quat2 is quat,
            "Quaternion identity not set in place"
            )
    
        quat = quaternion.identity()
        self.assertEqual(
            quat[ 0 ],
            1.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 1 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 2 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 3 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertTrue(
            quat2 is not quat,
            "Quaternion identity not assigned correctly"
            )

    def test_normalise( self ):
        quat = quaternion.identity()
        quaternion.normalise( quat )
        self.assertEqual(
            quat[ 0 ],
            1.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 1 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 2 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 3 ],
            0.0,
            "Quaternion identity incorrect"
            )
    
        quat[ 0 ] = 2.0
        quaternion.normalise( quat )
        self.assertEqual(
            quat[ 0 ],
            1.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 1 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 2 ],
            0.0,
            "Quaternion identity incorrect"
            )
        self.assertEqual(
            quat[ 3 ],
            0.0,
            "Quaternion identity incorrect"
            )
    
    
if __name__ == '__main__':
    unittest.main()

