try:
    import unittest2 as unittest
except:
    import unittest
import numpy as np
from pyrr import quaternion, matrix44

class test_matrix_quaternion(unittest.TestCase):
    def test_m44_q_equivalence(self):
        """Test for equivalance of matrix and quaternion rotations.

        Create a matrix and quaternion, rotate each by the same values
        then convert matrix<->quaternion and check the results are the same.
        """
        m = matrix44.create_from_x_rotation(np.pi / 2.)
        mq = quaternion.create_from_matrix(m)

        q = quaternion.create_from_x_rotation(np.pi / 2.)
        qm = matrix44.create_from_quaternion(q)

        self.assertTrue(np.allclose(np.dot([1.,0.,0.,1.], m), [1.,0.,0.,1.]))
        self.assertTrue(np.allclose(np.dot([1.,0.,0.,1.], qm), [1.,0.,0.,1.]))

        self.assertTrue(np.allclose(quaternion.apply_to_vector(q, [1.,0.,0.,1.]), [1.,0.,0.,1.]))
        self.assertTrue(np.allclose(quaternion.apply_to_vector(mq, [1.,0.,0.,1.]), [1.,0.,0.,1.]))

        np.testing.assert_almost_equal(q, mq, decimal=5)
        np.testing.assert_almost_equal(m, qm, decimal=5)


if __name__ == '__main__':
    unittest.main()
