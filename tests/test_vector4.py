try:
    import unittest2 as unittest
except:
    import unittest
import numpy as np
from pyrr import vector4

# TODO: add checks for various W values to ensure they are calculated correctly
# TODO: should W component remain 1 as if its a vec3 with hidden value?
# or should it be mathematically correct?


class test_vector4(unittest.TestCase):
    def test_create(self):
        result = vector4.create()
        np.testing.assert_almost_equal(result, [0.,0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_values(self):
        result = vector4.create(1.,2.,3.,4., dtype=np.float32)
        np.testing.assert_almost_equal(result, [1.,2.,3.,4.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_x(self):
        result = vector4.create_unit_length_x()
        np.testing.assert_almost_equal(result, [1.,0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_x_dtype(self):
        result = vector4.create_unit_length_x(dtype=np.float32)
        np.testing.assert_almost_equal(result, [1.,0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_y(self):
        result = vector4.create_unit_length_y()
        np.testing.assert_almost_equal(result, [0.,1.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_y_dtype(self):
        result = vector4.create_unit_length_y(dtype=np.float32)
        np.testing.assert_almost_equal(result, [0.,1.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_z(self):
        result = vector4.create_unit_length_z()
        np.testing.assert_almost_equal(result, [0.,0.,1.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_z_dtype(self):
        result = vector4.create_unit_length_z(dtype=np.float32)
        np.testing.assert_almost_equal(result, [0.,0.,1.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_from_vector3(self):
        result = vector4.create_from_vector3([2.,3.,4.])
        np.testing.assert_almost_equal(result, [2.,3.,4.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_vector3_dtype(self):
        result = vector4.create_from_vector3([2.,3.,4.], dtype=np.float32)
        np.testing.assert_almost_equal(result, [2.,3.,4.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_from_vector3_int_assumed(self):
        result = vector4.create_from_vector3([2,3,4,1])
        np.testing.assert_almost_equal(result, [2,3,4,1], decimal=5)
        self.assertTrue(result.dtype == np.int)

    def test_create_from_matrix44_translation(self):
        mat = np.array([
            [1.,2.,3.,4.,],
            [5.,6.,7.,8.,],
            [9.,10.,11.,12.,],
            [13.,14.,15.,16.,],
        ])
        result = vector4.create_from_matrix44_translation(mat)
        np.testing.assert_almost_equal(result, [13.,14.,15.,16.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix44_translation_dtype_matches(self):
        mat = np.array([
            [1.,2.,3.,4.,],
            [5.,6.,7.,8.,],
            [9.,10.,11.,12.,],
            [13.,14.,15.,16.,],
        ], dtype=np.float32)
        result = vector4.create_from_matrix44_translation(mat)
        np.testing.assert_almost_equal(result, [13.,14.,15.,16.], decimal=5)
        self.assertTrue(result.dtype == np.float32)


    """
    def test_normalise_single_vector(self):
        result = vector4.normalise([1.,1.,1.,1.])
        np.testing.assert_almost_equal(result, [0.57735, 0.57735, 0.57735, 1.], decimal=5)

    def test_normalise_batch(self):
        result = vector4.normalise([
            [1.,1.,1.,1.],
            [-1.,-1.,-1.,1.],
            [0.,2.,7.,1.],
        ])
        expected = [
            [0.57735, 0.57735, 0.57735,1.],
            [-0.57735,-0.57735,-0.57735,1.],
            [0., 0.274721, 0.961524,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_squared_length_single_vector(self):
        result = vector4.squared_length([1.,1.,1.,1.])
        np.testing.assert_almost_equal(result, 3., decimal=5)

    def test_squared_length_batch(self):
        result = vector4.squared_length([
            [1.,1.,1.,1.],
            [-1.,-1.,-1.,1.],
            [0.,2.,7.,1.],
        ])
        expected = [
            3.,
            3.,
            53.,
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_length(self):
        result = vector4.length([1.,1.,1.,1.])
        np.testing.assert_almost_equal(result, 1.73205, decimal=5)

    def test_length_batch(self):
        result = vector4.length([
            [1.,1.,1.,1.],
            [-1.,-1.,-1.,1.],
            [0.,2.,7.,1.],
        ])
        expected = [
            1.73205,
            1.73205,
            7.28011,
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_set_length(self):
        result = vector4.set_length([1.,1.,1.,1.],2.)
        expected = [1.15470,1.15470,1.15470,1.]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_set_length_batch_vector(self):
        result = vector4.set_length([
            [1.,1.,1.,1.],
            [-1.,-1.,-1.,1.],
            [0.,2.,7.,1.],
            ], 2.0)
        expected = [
            [1.15470,1.15470,1.15470,1.],
            [-1.15470,-1.15470,-1.15470,1.],
            [0.,0.54944,1.92304,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_dot_adjacent(self):
        result = vector4.dot([1.,0.,0.,1.], [0.,1.,0.,1.])
        np.testing.assert_almost_equal(result, 0.0, decimal=5)

    def test_dot_parallel(self):
        result = vector4.dot([0.,1.,0.,1.], [0.,1.,0.,1.])
        np.testing.assert_almost_equal(result, 1.0, decimal=5)

    def test_dot_angle(self):
        result = vector4.dot([.2,.2,0.,1.], [2.,-.2,0.,1.])
        np.testing.assert_almost_equal(result, 0.36, decimal=5)

    def test_dot_batch(self):
        result = vector4.dot([
            [1.,0.,0.,1.],
            [0.,1.,0.,1.],
            [.2,.2,0.,1.]
        ],[
            [0.,1.,0.,1.],
            [0.,1.,0.,1.],
            [2.,-.2,0.,1.]
        ])
        expected = [
            0.,
            1.,
            0.36
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_cross_single_vector(self):
        result = vector4.cross([1.,0.,0.,1.], [0.,1.,0.,1.])
        np.testing.assert_almost_equal(result, [0.,0.,1.,1.], decimal=5)

    def test_cross_batch(self):
        result = vector4.cross([
            [1.,0.,0.,1.],
            [0.,0.,1.,1.]
        ],[
            [0.,1.,0.,1.],
            [0.,1.,0.,1.],
        ])
        expected = [
            [0.,0.,1.,1.],
            [-1.,0.,0.,1.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_interoplation( self ):
        result = vector4.interpolate([0.,0.,0.,1.], [1.,1.,1.,1.], 0.5)
        np.testing.assert_almost_equal(result, [.5,.5,.5,1.], decimal=5)

        result = vector4.interpolate([0.,0.,0.,1.], [2.,2.,2.,1.], 0.5)
        np.testing.assert_almost_equal(result, [1.,1.,1.,1.], decimal=5)
    """


if __name__ == '__main__':
    unittest.main()
