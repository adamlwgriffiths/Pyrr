try:
    import unittest2 as unittest
except:
    import unittest
import numpy as np
from pyrr import euler

class test_euler(unittest.TestCase):
    def test_import(self):
        import pyrr
        pyrr.euler
        from pyrr import euler

    def test_create(self):
        self.assertTrue(np.array_equal(euler.create(), [0.,0.,0.]))
        self.assertTrue(np.array_equal(euler.create(1.,2.,3.), [1.,2.,3.]))

    def test_pitch(self):
        self.assertEqual(euler.pitch([1.,2.,3.]), 1.)

    def test_roll(self):
        self.assertEqual(euler.roll([1.,2.,3.]), 2.)

    def test_yaw(self):
        self.assertEqual(euler.yaw([1.,2.,3.]), 3.)



if __name__ == '__main__':
    unittest.main()

