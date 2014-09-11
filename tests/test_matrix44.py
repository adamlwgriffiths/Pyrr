import unittest
import math
import numpy as np
from pyrr import matrix44, quaternion


class test_matrix44(unittest.TestCase):
    def test_create_identity(self):
        result = matrix44.create_identity()
        np.testing.assert_almost_equal(result, np.eye(4), decimal=5)

    def test_create_from_quaternion_unit(self):
        result = matrix44.create_from_quaternion([0.,0.,0.,1.])
        np.testing.assert_almost_equal(result, np.eye(4), decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_quaternion_x(self):
        result = matrix44.create_from_quaternion([1.,0.,0.,0.])
        expected = [
            [1.,0.,0.,0.],
            [0.,-1.,0.,0.],
            [0.,0.,-1.,0.],
            [0.,0.,0.,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_quaternion_y(self):
        result = matrix44.create_from_quaternion([0.,1.,0.,0.])
        expected = [
            [-1.,0.,0.,0.],
            [0.,1.,0.,0.],
            [0.,0.,-1.,0.],
            [0.,0.,0.,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_quaternion_z(self):
        result = matrix44.create_from_quaternion([0.,0.,1.,0.])
        expected = [
            [-1.,0.,0.,0.],
            [0.,-1.,0.,0.],
            [0.,0.,1.,0.],
            [0.,0.,0.,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_quaternion_rotation(self):
        result = matrix44.create_from_quaternion([.57735,.57735,.57735,0.])
        expected = [
            [-0.333333, 0.666667, 0.666667,0.],
            [0.666667, -0.333333, 0.666667,0.],
            [0.666667, 0.666667, -0.333333,0.],
            [0.,0.,0.,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_inverse_of_quaternion(self):
        q = quaternion.create_from_x_rotation(math.pi / 2.0)
        result = matrix44.create_from_inverse_of_quaternion(q)
        self.assertTrue(np.allclose(result, matrix44.create_from_x_rotation(-math.pi / 2.0)))

    def test_create_from_translation( self ):
        result = matrix44.create_from_translation([2.,3.,4.])
        expected = np.eye(4)
        expected[3,:3] = [2.,3.,4.]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_create_from_scale( self ):
        result = matrix44.create_from_scale([2.,3.,4.])
        np.testing.assert_almost_equal(result.diagonal()[:-1], [2.,3.,4.], decimal=5)

    def test_create_matrix33_view( self ):
        mat = matrix44.create_identity()
        result = matrix44.create_matrix33_view(mat)
        np.testing.assert_almost_equal(result, mat[:3,:3], decimal=5)
        mat[0,0] = 2.
        np.testing.assert_almost_equal(result, mat[:3,:3], decimal=5)

    def test_create_from_matrix33( self ):
        mat = np.array([
            [1.,2.,3.],
            [3.,4.,5.],
            [6.,7.,8.]
        ])
        result = matrix44.create_from_matrix33(mat)
        np.testing.assert_almost_equal(result[:3,:3], mat, decimal=5)
        orig = mat.copy()
        mat[0,0] = 2.
        np.testing.assert_almost_equal(result[:3,:3], orig, decimal=5)

    def test_create_perspective_projection_matrix_vector3(self):
        m = matrix44.create_perspective_projection_matrix(90, 1024./768., 1., 10.)

        # the values will be in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
        # to be inside = all(-1. < value < 1.)
        for point, inside in (
            (np.array((0.,0.,0.)), False),
            (np.array((0.,0.,-.5)), False),
            (np.array((0.,0.,-1.)), True),
            (np.array((0.,0.,-2.)), True),
            (np.array((0.,0.,-9.)), True),
            (np.array((0.,0.,-11.)), False),
            (np.array((1.,1.,-5.)), True),
        ):
            p = matrix44.apply_to_vector(m, point[:3])

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def test_create_perspective_projection_matrix_vector4(self):
        m = matrix44.create_perspective_projection_matrix(90, 1024./768., 1., 10.)

        # the values will be in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
        # to be inside = all(-1. < value < 1.)
        for point, inside in (
            (np.array((0.,0.,0.,1.)), False),
            (np.array((0.,0.,-.5,1.)), False),
            (np.array((0.,0.,-1.,1.)), True),
            (np.array((0.,0.,-2.,1.)), True),
            (np.array((0.,0.,-9.,1.)), True),
            (np.array((0.,0.,-11.,1.)), False),
            (np.array((1.,1.,-5.,1.)), True),
        ):
            p = matrix44.apply_to_vector(m, point)
            if p[3] == 0.:
                self.assertFalse(inside)

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def test_create_orthogonal_projection_matrix_vector3(self):
        m = matrix44.create_orthogonal_projection_matrix(-1., 1., -1., 1., 1., 10.)

        for point, inside in (
            # +Z
            (np.array((0.,0.,0.)), False),
            (np.array((0.,0.,1.)), False),
            # -Z but outside near, far
            (np.array((0.,0.,-.5)), False),
            (np.array((0.,0.,-11.)), False),
            (np.array((0.,0.,1.)), False),
            # Valid
            (np.array((0.,0.,-10.)), True),
            (np.array((0.,0.,-1.)), True),
            (np.array((0.,0.,-2.)), True),
            (np.array((0.,0.,-9.)), True),
            (np.array((-1.,-1.,-1.)), True),
            (np.array((-1.,-1.,-10.)), True),
            (np.array((1.,1.,-1.)), True),
            (np.array((1.,1.,-10.)), True),
            # Outside left, right, top, bottom
            (np.array((1.1,1.1,-1.)), False),
            (np.array((-1.1,-1.1,-1.)), False),
            (np.array((1.1,1.1,-10.)), False),
            (np.array((-1.1,-1.1,-10.)), False),
        ):
            p = matrix44.apply_to_vector(m, point)

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def test_create_orthogonal_projection_matrix_vector4(self):
        m = matrix44.create_orthogonal_projection_matrix(-1., 1., -1., 1., 1., 10.)

        for point, inside in (
            # +Z
            (np.array((0.,0.,0.,1.)), False),
            (np.array((0.,0.,1.,1.)), False),
            # -Z but outside near, far
            (np.array((0.,0.,-.5,1.)), False),
            (np.array((0.,0.,-11.,1.)), False),
            (np.array((0.,0.,1.,1.)), False),
            # Valid
            (np.array((0.,0.,-10.,1.)), True),
            (np.array((0.,0.,-1.,1.)), True),
            (np.array((0.,0.,-2.,1.)), True),
            (np.array((0.,0.,-9.,1.)), True),
            (np.array((-1.,-1.,-1.,1.)), True),
            (np.array((-1.,-1.,-10.,1.)), True),
            (np.array((1.,1.,-1.,1.)), True),
            (np.array((1.,1.,-10.,1.)), True),
            # Outside left, right, top, bottom
            (np.array((1.1,1.1,-1.,1.)), False),
            (np.array((-1.1,-1.1,-1.,1.)), False),
            (np.array((1.1,1.1,-10.,1.)), False),
            (np.array((-1.1,-1.1,-10.,1.)), False),
        ):
            p = matrix44.apply_to_vector(m, point)
            if p[3] == 0.:
                self.assertFalse(inside)

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def create_perspective_projection_matrix_from_bounds_vector3(self):
        m = matrix44.create_perspective_projection_matrix_from_bounds(-1.,1.,-1.,1.,1.,10.)

        for point, inside in (
            # +Z
            (np.array((0.,0.,0.)), False),
            (np.array((0.,0.,1.)), False),
            # -Z but outside near, far
            (np.array((0.,0.,-.5)), False),
            (np.array((0.,0.,-11.)), False),
            (np.array((0.,0.,1.)), False),
            # Valid
            (np.array((0.,0.,-10.)), True),
            (np.array((0.,0.,-1.)), True),
            (np.array((0.,0.,-2.)), True),
            (np.array((0.,0.,-9.)), True),
            (np.array((-1.,-1.,-1.)), True),
            (np.array((-1.,-1.,-10.)), True),
            (np.array((1.,1.,-1.)), True),
            (np.array((1.,1.,-10.)), True),
            # Outside left, right, top, bottom
            (np.array((1.1,1.1,-1.)), False),
            (np.array((-1.1,-1.1,-1.)), False),
            (np.array((1.1,1.1,-10.)), False),
            (np.array((-1.1,-1.1,-10.)), False),
        ):
            p = matrix44.apply_to_vector(m, point)

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def create_perspective_projection_matrix_from_bounds_vector4(self):
        m = matrix44.create_perspective_projection_matrix_from_bounds(-1.,1.,-1.,1.,1.,10.)

        for point, inside in (
            # +Z
            (np.array((0.,0.,0.,1.)), False),
            (np.array((0.,0.,1.,1.)), False),
            # -Z but outside near, far
            (np.array((0.,0.,-.5,1.)), False),
            (np.array((0.,0.,-11.,1.)), False),
            (np.array((0.,0.,1.,1.)), False),
            # Valid
            (np.array((0.,0.,-10.,1.)), True),
            (np.array((0.,0.,-1.,1.)), True),
            (np.array((0.,0.,-2.,1.)), True),
            (np.array((0.,0.,-9.,1.)), True),
            (np.array((-1.,-1.,-1.,1.)), True),
            (np.array((-1.,-1.,-10.,1.)), True),
            (np.array((1.,1.,-1.,1.)), True),
            (np.array((1.,1.,-10.,1.)), True),
            # Outside left, right, top, bottom
            (np.array((1.1,1.1,-1.,1.)), False),
            (np.array((-1.1,-1.1,-1.,1.)), False),
            (np.array((1.1,1.1,-10.,1.)), False),
            (np.array((-1.1,-1.1,-10.,1.)), False),
        ):
            p = matrix44.apply_to_vector(m, point)
            if p[3] == 0.:
                self.assertFalse(inside)

            # the values are now in clip space from (-1.,-1.,-1.) -> (1.,1.,1.)
            # to be inside = all(-1. < value < 1.)
            self.assertTrue(inside == (np.amax(np.absolute(p[:3])) <= 1.), (inside, point, p))

    def test_apply_to_vector_identity(self):
        mat = matrix44.create_identity()
        result = matrix44.apply_to_vector(mat, [1.,0.,0.])
        np.testing.assert_almost_equal(result, [1.,0.,0.], decimal=5)

    def test_apply_to_vector_x_rotation(self):
        mat = matrix44.create_from_x_rotation(np.pi)
        result = matrix44.apply_to_vector(mat, [0.,1.,0.])
        np.testing.assert_almost_equal(result, [0.,-1.,0.], decimal=5)

    def test_apply_to_vector_y_rotation(self):
        mat = matrix44.create_from_y_rotation(np.pi)
        result = matrix44.apply_to_vector(mat, [1.,0.,0.])
        np.testing.assert_almost_equal(result, [-1.,0.,0.], decimal=5)

    def test_apply_to_vector_z_rotation(self):
        mat = matrix44.create_from_z_rotation(np.pi)
        result = matrix44.apply_to_vector(mat, [1.,0.,0.])
        np.testing.assert_almost_equal(result, [-1.,0.,0.], decimal=5)

    def test_apply_to_vector_with_translation(self):
        mat = matrix44.create_from_translation([2.,3.,4.])
        result = matrix44.apply_to_vector(mat, [1.,1.,1.])
        np.testing.assert_almost_equal(result, [3.,4.,5.], decimal=5)

    @unittest.skip('Not implemented')
    def test_create_from_eulers(self):
        # just call the function
        # TODO: check the result
        matrix44.create_from_eulers([1,2,3])

    def test_create_from_x_rotation(self):
        mat = matrix44.create_from_x_rotation(-math.pi / 2.)
        self.assertTrue(np.allclose(np.dot([0.,1.,0.,1.], mat), [0.,0.,-1.,1.]))
        self.assertTrue(np.allclose(np.dot([1.,0.,0.,1.], mat), [1.,0.,0.,1.]))
        self.assertTrue(np.allclose(np.dot([0.,0.,1.,1.], mat), [0.,1.,0.,1.]))

    def test_create_from_y_rotation(self):
        mat = matrix44.create_from_y_rotation(-math.pi / 2.)
        self.assertTrue(np.allclose(np.dot([0.,1.,0.,1.], mat), [0.,1.,0.,1.]))
        self.assertTrue(np.allclose(np.dot([1.,0.,0.,1.], mat), [0.,0.,1.,1.]))
        self.assertTrue(np.allclose(np.dot([0.,0.,1.,1.], mat), [-1.,0.,0.,1.]))

    def test_create_from_z_rotation(self):
        mat = matrix44.create_from_z_rotation(-math.pi / 2.)
        self.assertTrue(np.allclose(np.dot([0.,1.,0.,1.], mat), [1.,0.,0.,1.]))
        self.assertTrue(np.allclose(np.dot([1.,0.,0.,1.], mat), [0.,-1.,0.,1.]))
        self.assertTrue(np.allclose(np.dot([0.,0.,1.,1.], mat), [0.,0.,1.,1.]))

    def test_multiply_identity(self):
        m1 = matrix44.create_identity()
        m2 = matrix44.create_identity()
        result = matrix44.multiply(m1, m2)
        self.assertTrue(np.allclose(result, np.dot(m1,m2)))

    def test_multiply_rotation(self):
        m1 = matrix44.create_from_x_rotation(math.pi)
        m2 = matrix44.create_from_y_rotation(math.pi / 2.0)
        result = matrix44.multiply(m1, m2)
        self.assertTrue(np.allclose(result, np.dot(m1,m2)))

    def test_inverse(self):
        m = matrix44.create_from_y_rotation(math.pi)
        result = matrix44.inverse(m)
        self.assertTrue(np.allclose(result, matrix44.create_from_y_rotation(-math.pi)))

    
if __name__ == '__main__':
    unittest.main()
