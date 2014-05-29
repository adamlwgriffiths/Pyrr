import unittest
import numpy as np
from pyrr import vector3


class test_vector3(unittest.TestCase):
    def test_create(self):
        result = vector3.create()
        np.testing.assert_almost_equal(result, [0.,0.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_values(self):
        result = vector3.create(1., 2., 3., dtype=np.float32)
        np.testing.assert_almost_equal(result, [1.,2.,3.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_x(self):
        result = vector3.create_unit_length_x()
        np.testing.assert_almost_equal(result, [1.,0.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_x_dtype(self):
        result = vector3.create_unit_length_x(dtype=np.float32)
        np.testing.assert_almost_equal(result, [1.,0.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_y(self):
        result = vector3.create_unit_length_y()
        np.testing.assert_almost_equal(result, [0.,1.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_y_dtype(self):
        result = vector3.create_unit_length_y(dtype=np.float32)
        np.testing.assert_almost_equal(result, [0.,1.,0.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_unit_length_z(self):
        result = vector3.create_unit_length_z()
        np.testing.assert_almost_equal(result, [0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_unit_length_z_dtype(self):
        result = vector3.create_unit_length_z(dtype=np.float32)
        np.testing.assert_almost_equal(result, [0.,0.,1.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_from_vector4(self):
        result = vector3.create_from_vector4([1.,2.,3.,4.])
        np.testing.assert_almost_equal(result, [1.,2.,3.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_vector4_dtype(self):
        result = vector3.create_from_vector4([1.,2.,3.,4.], dtype=np.float32)
        np.testing.assert_almost_equal(result, [1.,2.,3.], decimal=5)
        self.assertTrue(result.dtype == np.float32)

    def test_create_from_vector4_int_assumed(self):
        result = vector3.create_from_vector4([1,2,3,4])
        np.testing.assert_almost_equal(result, [1,2,3], decimal=5)
        self.assertTrue(result.dtype == np.int)

    def test_create_from_vector4_no_side_effects(self):
        vec = [1.,2.,3.,4.]
        result = vector3.create_from_vector4(vec)
        np.testing.assert_almost_equal(result, [1.,2.,3.], decimal=5)
        self.assertTrue(result.dtype == np.float)

        # ensure we can modify each value without affecting the other
        result[0] = 6.
        self.assertFalse(np.array_equal(result, vec[:3]))
        vec[0] = 5.
        self.assertFalse(np.array_equal(result, vec[:3]))

    def test_create_from_matrix44_translation(self):
        mat = np.array([
            [1.,2.,3.,4.,],
            [5.,6.,7.,8.,],
            [9.,10.,11.,12.,],
            [13.,14.,15.,16.,],
        ])
        result = vector3.create_from_matrix44_translation(mat)
        np.testing.assert_almost_equal(result, [13.,14.,15.], decimal=5)
        self.assertTrue(result.dtype == np.float)

    def test_create_from_matrix44_translation_dtype_matches(self):
        mat = np.array([
            [1.,2.,3.,4.,],
            [5.,6.,7.,8.,],
            [9.,10.,11.,12.,],
            [13.,14.,15.,16.,],
        ], dtype=np.float32)
        result = vector3.create_from_matrix44_translation(mat)
        np.testing.assert_almost_equal(result, [13.,14.,15.], decimal=5)
        self.assertTrue(result.dtype == np.float32)
