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
        self.assertTrue(np.array_equal(euler.create(), [0., 0., 0.]))
        self.assertTrue(np.array_equal(euler.create(roll=1., pitch=2., yaw=3.), [1., 2., 3.]))

        # swap indices
        indices = euler.index.yaw, euler.index.pitch, euler.index.roll
        new_indices = indices[1], indices[2], indices[0]
        euler.index.yaw, euler.index.pitch, euler.index.roll = new_indices

        self.assertTrue(np.array_equal(euler.create(roll=1., pitch=2., yaw=3.), [2., 3., 1.]))

        # reset
        euler.index.yaw, euler.index.pitch, euler.index.roll = indices

if __name__ == '__main__':
    unittest.main()
