import unittest
import numpy as np
from pyrr import quaternion


class test_quaternion(unittest.TestCase):
    def test_create(self):
        result = quaternion.create()
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_x_rotation(self):
        result = quaternion.create_from_x_rotation(np.pi)
        np.testing.assert_almost_equal(result, [1.,0.,0.,0.], decimal=3)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_y_rotation(self):
        result = quaternion.create_from_y_rotation(np.pi)
        np.testing.assert_almost_equal(result, [0.,1.,0.,0.], decimal=3)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_z_rotation(self):
        result = quaternion.create_from_z_rotation(np.pi)
        np.testing.assert_almost_equal(result, [0.,0.,1.,0.], decimal=3)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_axis_rotation(self):
        # wolfram alpha can be awesome sometimes
        result = quaternion.create_from_axis_rotation([0.57735, 0.57735, 0.57735],np.pi)
        np.testing.assert_almost_equal(result, [5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17], decimal=3)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_axis_rotation_non_normalised(self):
        result = quaternion.create_from_axis_rotation([1.,1.,1.], np.pi)
        np.testing.assert_almost_equal(result, [5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17], decimal=3)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix_unit(self):
        result = quaternion.create_from_matrix(np.eye(3))
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix_x(self):
        result = quaternion.create_from_matrix([
            [1.,0.,0.],
            [0.,-1.,0.],
            [0.,0.,-1.],
        ])
        np.testing.assert_almost_equal(result, [1.,0.,0.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix_y(self):
        result = quaternion.create_from_matrix([
            [-1.,0.,0.],
            [0.,1.,0.],
            [0.,0.,-1.],
        ])
        np.testing.assert_almost_equal(result, [0.,1.,0.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix_z(self):
        result = quaternion.create_from_matrix([
            [-1.,0.,0.],
            [0.,-1.,0.],
            [0.,0.,1.],
        ])
        np.testing.assert_almost_equal(result, [0.,0.,1.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    """
    @unittest.skip('Not implemented')
    def test_create_from_eulers(self):
        pass

    @unittest.skip('Not implemented')
    def test_create_from_inverse_of_eulers(self):
        pass

    @unittest.skip('Not implemented')
    def test_cross(self):
        pass
    """

    def test_is_zero_length(self):
        result = quaternion.is_zero_length([1.,0.,0.,0.])
        self.assertFalse(result)

    def test_is_zero_length_zero(self):
        result = quaternion.is_zero_length([0.,0.,0.,0.])
        self.assertTrue(result)

    def test_is_non_zero_length(self):
        result = quaternion.is_non_zero_length([1.,0.,0.,0.])
        self.assertTrue(result)

    def test_is_non_zero_length_zero(self):
        result = quaternion.is_non_zero_length([0.,0.,0.,0.])
        self.assertFalse(result)

    def test_squared_length_identity(self):
        result = quaternion.squared_length([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, 1., decimal=5)

    def test_squared_length(self):
        result = quaternion.squared_length([1.,1.,1.,1.])
        np.testing.assert_almost_equal(result, 4., decimal=5)

    def test_squared_length_batch(self):
        result = quaternion.squared_length([
            [0.,0.,0.,1.],
            [1.,1.,1.,1.],
        ])
        np.testing.assert_almost_equal(result, [1.,4.], decimal=5)

    def test_length_identity(self):
        result = quaternion.length([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, 1., decimal=5)

    def test_length(self):
        result = quaternion.length([1.,1.,1.,1.])
        np.testing.assert_almost_equal(result, 2., decimal=5)

    def test_length_batch(self):
        result = quaternion.length([
            [0.,0.,0.,1.],
            [1.,1.,1.,1.],
        ])
        np.testing.assert_almost_equal(result, [1.,2.], decimal=5)

    def test_normalise_identity(self):
        # normalise an identity quaternion
        result = quaternion.normalise([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)

    def test_normalise_non_identity(self):
        # normalise an identity quaternion
        result = quaternion.normalise([1.,2.,3.,4.])
        np.testing.assert_almost_equal(result, [1./np.sqrt(30.),np.sqrt(2./15.),np.sqrt(3./10.),2.*np.sqrt(2./15.)], decimal=5)

    def test_normalise_batch(self):
        # normalise an identity quaternion
        result = quaternion.normalise([
            [0.,0.,0.,1.],
            [1.,2.,3.,4.],
        ])
        expected = [
            [0.,0.,0.,1.],
            [1./np.sqrt(30.),np.sqrt(2./15.),np.sqrt(3./10.),2.*np.sqrt(2./15.)],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_rotation_angle(self):
        result = quaternion.rotation_angle([5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17])
        np.testing.assert_almost_equal(result, np.pi, decimal=5)

    def test_rotation_axis(self):
        result = quaternion.rotation_axis([5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17])
        np.testing.assert_almost_equal(result, [0.57735, 0.57735, 0.57735], decimal=5)

    def test_dot_adjacent(self):
        result = quaternion.dot([1.,0.,0.,0.], [0.,1.,0.,0.])
        np.testing.assert_almost_equal(result, 0.0, decimal=5)

    def test_dot_parallel(self):
        result = quaternion.dot([0.,1.,0.,0.], [0.,1.,0.,0.])
        np.testing.assert_almost_equal(result, 1.0, decimal=5)

    def test_dot_angle(self):
        result = quaternion.dot([.2,.2,0.,0.], [2.,-.2,0.,0.])
        np.testing.assert_almost_equal(result, 0.36, decimal=5)

    def test_dot_batch(self):
        result = quaternion.dot([
            [1.,0.,0.,0.],
            [0.,1.,0.,0.],
            [.2,.2,0.,0.]
        ],[
            [0.,1.,0.,0.],
            [0.,1.,0.,0.],
            [2.,-.2,0.,0.]
        ])
        expected = [0.,1.,0.36]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_conjugate(self):
        #result = quaternion.conjugate([5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17])
        result = quaternion.conjugate([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)

    def test_conjugate_rotation(self):
        result = quaternion.conjugate([5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17])
        np.testing.assert_almost_equal(result, [-0.57735, -0.57735, -0.57735, 6.12323e-17], decimal=5)

    """
    @unittest.skip('Not implemented')
    def test_power(self):
        pass
    """

    def test_inverse(self):
        result = quaternion.inverse([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)

    def test_inverse_rotation(self):
        result = quaternion.inverse([5.77350000e-01, 5.77350000e-01, 5.77350000e-01, 6.12323400e-17])
        np.testing.assert_almost_equal(result, [-0.577351, -0.577351, -0.577351, 6.12324e-17], decimal=5)

    def test_inverse_non_unit(self):
        q = [1,2,3,4]
        result = quaternion.inverse(q)
        expected = quaternion.conjugate(q) / quaternion.length(q)
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_negate_unit(self):
        result = quaternion.negate([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, [0.,0.,0.,-1.], decimal=5)

    def test_negate(self):
        result = quaternion.negate([1.,2.,3.,4.])
        np.testing.assert_almost_equal(result, [-1.,-2.,-3.,-4.], decimal=5)

    def test_apply_to_vector_unit_x(self):
        result = quaternion.apply_to_vector([0.,0.,0.,1.],[1.,0.,0.])
        np.testing.assert_almost_equal(result, [1.,0.,0.], decimal=5)

    def test_apply_to_vector_x(self):
        quat = quaternion.create_from_x_rotation(np.pi)
        result = quaternion.apply_to_vector(quat,[0.,1.,0.])
        np.testing.assert_almost_equal(result, [0.,-1.,0.], decimal=5)

    def test_apply_to_vector_y(self):
        quat = quaternion.create_from_y_rotation(np.pi)
        result = quaternion.apply_to_vector(quat,[1.,0.,0.])
        np.testing.assert_almost_equal(result, [-1.,0.,0.], decimal=5)

    def test_apply_to_vector_z(self):
        quat = quaternion.create_from_z_rotation(np.pi)
        result = quaternion.apply_to_vector(quat,[1.,0.,0.])
        np.testing.assert_almost_equal(result, [-1.,0.,0.], decimal=5)

if __name__ == '__main__':
    unittest.main()
