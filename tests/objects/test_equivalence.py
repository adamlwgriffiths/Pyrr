from __future__ import absolute_import, division, print_function
try:
    import unittest2 as unittest
except:
    import unittest
import numpy as np
from pyrr import Quaternion, Matrix44, Matrix33, Vector3, Vector4, euler


class test_matrix_quaternion(unittest.TestCase):
    def test_m44_q_equivalence(self):
        """Test for equivalance of matrix and quaternion rotations.

        Create a matrix and quaternion, rotate each by the same values
        then convert matrix<->quaternion and check the results are the same.
        """
        m = Matrix44.from_x_rotation(np.pi / 2.)
        mq = Quaternion.from_matrix(m)

        q = Quaternion.from_x_rotation(np.pi / 2.)
        qm = Matrix44.from_quaternion(q)

        self.assertTrue(np.allclose(np.dot([1., 0., 0., 1.], m), [1., 0., 0., 1.]))
        self.assertTrue(np.allclose(np.dot([1., 0., 0., 1.], qm), [1., 0., 0., 1.]))

        self.assertTrue(np.allclose(q * Vector4([1., 0., 0., 1.]), [1., 0., 0., 1.]))
        self.assertTrue(np.allclose(mq * Vector4([1., 0., 0., 1.]), [1., 0., 0., 1.]))

        np.testing.assert_almost_equal(np.array(q), np.array(mq), decimal=5)
        np.testing.assert_almost_equal(np.array(m), np.array(qm), decimal=5)

    def test_euler_equivalence(self):
        eulers = euler.create_from_x_rotation(np.pi / 2.)
        m = Matrix33.from_x_rotation(np.pi / 2.)
        q = Quaternion.from_x_rotation(np.pi / 2.)
        qm = Matrix33.from_quaternion(q)
        em = Matrix33.from_eulers(eulers)
        self.assertTrue(np.allclose(qm, m))
        self.assertTrue(np.allclose(qm, em))
        self.assertTrue(np.allclose(m, em))

    def test_quaternion_matrix_conversion(self):
        # https://au.mathworks.com/help/robotics/ref/quat2rotm.html?requestedDomain=www.mathworks.com
        q = Quaternion([0.7071, 0., 0., 0.7071])
        m33 = q.matrix33
        expected = np.array([
            [1., 0., 0.],
            [0.,-0.,-1.],
            [0., 1.,-0.],
        ])
        self.assertTrue(np.allclose(m33, expected))

        # issue #42
        q = Quaternion([0.80087974, 0.03166748, 0.59114721,-0.09018753])
        m33 = q.matrix33
        q2 = Quaternion.from_matrix(m33)
        print(q, q2)
        self.assertTrue(np.allclose(q, q2))

        q3 = Quaternion.from_matrix(m33.T)
        self.assertFalse(np.allclose(q2, q3))


if __name__ == '__main__':
    unittest.main()
