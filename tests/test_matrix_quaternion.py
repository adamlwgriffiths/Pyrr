import unittest
import numpy as np
from pyrr import quaternion, matrix44, matrix33

class test_matrix_quaternion(unittest.TestCase):
    def test_m44_q_equivalence(self):
        """Test for equivalance of matrix and quaternion rotations.

        Create a matrix and quaternion, rotate each by the same values
        then convert matrix<->quaternion and check the results are the same.
        """
        m = matrix44.create_from_x_rotation(np.pi)
        q = quaternion.create_from_x_rotation(np.pi)
        qm = matrix44.create_from_quaternion(q)
        mq = quaternion.create_from_matrix(m)
        np.testing.assert_almost_equal(q, mq, decimal=5)
        np.testing.assert_almost_equal(m, qm, decimal=5)


if __name__ == '__main__':
    unittest.main()
