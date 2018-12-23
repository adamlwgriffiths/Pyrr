from __future__ import absolute_import
try:
    import unittest2 as unittest
except:
    import unittest
import numpy as np
from pyrr.objects.matrix33 import Matrix33
from pyrr.objects.matrix44 import Matrix44
from pyrr.objects.quaternion import Quaternion
from pyrr.objects.vector3 import Vector3
from pyrr.objects.vector4 import Vector4
from pyrr import matrix33
from pyrr import matrix44
from pyrr import quaternion


class test_object_matrix44(unittest.TestCase):
    _shape = (4,4)
    _size = np.multiply.reduce(_shape)

    def test_imports(self):
        import pyrr
        pyrr.Matrix44()
        pyrr.matrix44.Matrix44()
        pyrr.objects.matrix44.Matrix44()

        from pyrr import Matrix44
        from pyrr.objects import Matrix44
        from pyrr.objects.matrix44 import Matrix44

    def test_create(self):
        m = Matrix44()
        self.assertTrue(np.array_equal(m, np.zeros(self._shape)))
        self.assertEqual(m.shape, self._shape)

        m = Matrix44(np.arange(self._size))
        self.assertEqual(m.shape, self._shape)

        m = Matrix44([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        self.assertEqual(m.shape, self._shape)

        m = Matrix44(Matrix44())
        self.assertTrue(np.array_equal(m, np.zeros(self._shape)))
        self.assertEqual(m.shape, self._shape)

    def test_identity(self):
        m = Matrix44.identity()
        self.assertTrue(np.array_equal(m, np.eye(4)))

    @unittest.skip('Not implemented')
    def test_perspective_projection(self):
        pass

    @unittest.skip('Not implemented')
    def test_perspective_projection_bounds(self):
        pass

    @unittest.skip('Not implemented')
    def test_orthogonal_projection(self):
        pass

    @unittest.skip('Not implemented')
    def test_from_translation(self):
        pass

    def test_create_from_matrix44(self):
        m1 = Matrix33.identity()
        m = Matrix44.from_matrix33(m1)
        self.assertTrue(np.array_equal(m, np.eye(4)))

        m = Matrix44(m1)
        self.assertTrue(np.array_equal(m, np.eye(4)))

    def test_create_from_scale(self):
        v = Vector3([1,2,3])
        m = Matrix44.from_scale(v)
        self.assertTrue(np.array_equal(m, np.diag([1,2,3,1])))

    def test_create_from_eulers(self):
        e = Vector3([1,2,3])
        m = Matrix44.from_eulers(e)
        self.assertTrue(np.array_equal(m, matrix44.create_from_eulers([1,2,3])))

    def test_create_from_quaternion(self):
        q = Quaternion()
        m = Matrix44.from_quaternion(q)
        self.assertTrue(np.array_equal(m, np.eye(4)))
        self.assertTrue(np.array_equal(m.quaternion, q))

        m = Matrix44(q)
        self.assertTrue(np.array_equal(m, np.eye(4)))

    def test_create_from_inverse_quaternion(self):
        q = Quaternion.from_x_rotation(0.5)
        m = Matrix44.from_inverse_of_quaternion(q)
        expected = matrix44.create_from_quaternion(quaternion.inverse(quaternion.create_from_x_rotation(0.5)))
        np.testing.assert_almost_equal(np.array(m), expected, decimal=5)
        #self.assertTrue(np.array_equal(m, expected))

    def test_multiply(self):
        m1 = Matrix44(np.arange(self._size))
        m2 = Matrix44(np.arange(self._size)[::-1])
        m = m1 * m2
        self.assertTrue(np.array_equal(m, matrix44.multiply(m2, m1)))

        m1 = Matrix44(np.arange(self._size))
        m2 = Matrix33(np.arange(9))
        m = m1 * m2
        self.assertTrue(np.array_equal(m, matrix44.multiply(matrix44.create_from_matrix33(m2), m1)))

    def test_inverse(self):
        m1 = Matrix44.identity() * Matrix44.from_x_rotation(0.5)
        m = m1.inverse
        self.assertTrue(np.array_equal(m, matrix44.inverse(m1)))

    def test_matrix33(self):
        m1 = Matrix44.identity() * Matrix44.from_x_rotation(0.5)
        m = m1.matrix33
        self.assertTrue(np.array_equal(m, matrix33.create_from_matrix44(m1)))

    def test_matrix44(self):
        m1 = Matrix44.identity() * Matrix44.from_x_rotation(0.5)
        m = m1.matrix44
        self.assertTrue(m1 is m)

    def test_operators_matrix33(self):
        m1 = Matrix44.identity()
        m2 = Matrix33.from_x_rotation(0.5)

        # add
        self.assertTrue(np.array_equal(m1 + m2, matrix44.create_identity() + matrix44.create_from_x_rotation(0.5)))

        # subtract
        self.assertTrue(np.array_equal(m1 - m2, matrix44.create_identity() - matrix44.create_from_x_rotation(0.5)))

        # multiply
        self.assertTrue(np.array_equal(m1 * m2, matrix44.multiply(matrix44.create_from_x_rotation(0.5), matrix44.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m1 / m2)

    def test_operators_matrix44(self):
        m1 = Matrix44.identity()
        m2 = Matrix44.from_x_rotation(0.5)

        # add
        self.assertTrue(np.array_equal(m1 + m2, matrix44.create_identity() + matrix44.create_from_x_rotation(0.5)))

        # subtract
        self.assertTrue(np.array_equal(m1 - m2, matrix44.create_identity() - matrix44.create_from_x_rotation(0.5)))

        # multiply
        self.assertTrue(np.array_equal(m1 * m2, matrix44.multiply(matrix44.create_from_x_rotation(0.5), matrix44.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m1 / m2)

        # inverse
        self.assertTrue(np.array_equal(~m2, matrix44.inverse(matrix44.create_from_x_rotation(0.5))))

        # ==
        self.assertTrue(Matrix44() == Matrix44())
        self.assertFalse(Matrix44() == Matrix44([1. for n in range(16)]))

        # !=
        self.assertTrue(Matrix44() != Matrix44([1. for n in range(16)]))
        self.assertFalse(Matrix44() != Matrix44())

    def test_operators_quaternion(self):
        m = Matrix44.identity()
        q = Quaternion.from_x_rotation(0.7)

        # add
        self.assertRaises(ValueError, lambda: m + q)

        # subtract
        self.assertRaises(ValueError, lambda: m - q)

        # multiply
        self.assertTrue(np.array_equal(m * q, matrix44.multiply(matrix44.create_from_quaternion(quaternion.create_from_x_rotation(0.7)), matrix44.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m / q)

    def test_operators_vector3(self):
        m = Matrix44.identity()
        v = Vector3([1,1,1])

        # add
        self.assertRaises(ValueError, lambda: m + v)

        # subtract
        self.assertRaises(ValueError, lambda: m - v)

        # multiply
        self.assertTrue(np.array_equal(m * v, matrix44.apply_to_vector(matrix44.create_identity(), [1,1,1])))

        # divide
        self.assertRaises(ValueError, lambda: m / v)

    def test_operators_vector4(self):
        m = Matrix44.identity()
        v = Vector4([1,1,1,1])

        # add
        self.assertRaises(ValueError, lambda: m + v)

        # subtract
        self.assertRaises(ValueError, lambda: m - v)

        # multiply
        self.assertTrue(np.array_equal(m * v, matrix44.apply_to_vector(matrix44.create_identity(), [1,1,1,1])))

        # divide
        self.assertRaises(ValueError, lambda: m / v)

    def test_operators_number(self):
        m = Matrix44.identity()
        fv = np.empty((1,), dtype=[('i', np.int16, 1),('f', np.float32, 1)])
        fv[0] = (2, 2.0)

        # add
        self.assertTrue(np.array_equal(m + 1.0, matrix44.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + 1, matrix44.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + np.float(1.), matrix44.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + fv[0]['f'], matrix44.create_identity()[:] + 2.0))
        self.assertTrue(np.array_equal(m + fv[0]['i'], matrix44.create_identity()[:] + 2.0))

        # subtract
        self.assertTrue(np.array_equal(m - 1.0, matrix44.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - 1, matrix44.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - np.float(1.), matrix44.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - fv[0]['f'], matrix44.create_identity()[:] - 2.0))
        self.assertTrue(np.array_equal(m - fv[0]['i'], matrix44.create_identity()[:] - 2.0))

        # multiply
        self.assertTrue(np.array_equal(m * 2.0, matrix44.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * 2, matrix44.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * np.float(2.), matrix44.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * fv[0]['f'], matrix44.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * fv[0]['i'], matrix44.create_identity()[:] * 2.0))

        # divide
        self.assertTrue(np.array_equal(m / 2.0, matrix44.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / 2, matrix44.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / np.float(2.), matrix44.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / fv[0]['f'], matrix44.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / fv[0]['i'], matrix44.create_identity()[:] / 2.0))

    def test_accessors(self):
        m = Matrix44(np.arange(self._size))
        self.assertTrue(np.array_equal(m.m1,[0,1,2,3]))
        self.assertTrue(np.array_equal(m.m2,[4,5,6,7]))
        self.assertTrue(np.array_equal(m.m3,[8,9,10,11]))
        self.assertTrue(np.array_equal(m.m4,[12,13,14,15]))

        self.assertTrue(np.array_equal(m.r1,[0,1,2,3]))
        self.assertTrue(np.array_equal(m.r2,[4,5,6,7]))
        self.assertTrue(np.array_equal(m.r3,[8,9,10,11]))
        self.assertTrue(np.array_equal(m.r4,[12,13,14,15]))

        self.assertTrue(np.array_equal(m.c1,[0,4,8,12]))
        self.assertTrue(np.array_equal(m.c2,[1,5,9,13]))
        self.assertTrue(np.array_equal(m.c3,[2,6,10,14]))
        self.assertTrue(np.array_equal(m.c4,[3,7,11,15]))

        self.assertEqual(m.m11, 0)
        self.assertEqual(m.m12, 1)
        self.assertEqual(m.m13, 2)
        self.assertEqual(m.m14, 3)
        self.assertEqual(m.m21, 4)
        self.assertEqual(m.m22, 5)
        self.assertEqual(m.m23, 6)
        self.assertEqual(m.m24, 7)
        self.assertEqual(m.m31, 8)
        self.assertEqual(m.m32, 9)
        self.assertEqual(m.m33, 10)
        self.assertEqual(m.m34, 11)
        self.assertEqual(m.m41, 12)
        self.assertEqual(m.m42, 13)
        self.assertEqual(m.m43, 14)
        self.assertEqual(m.m44, 15)

        m.m11 = 1
        self.assertEqual(m.m11, 1)
        self.assertEqual(m[0,0], 1)
        m.m11 += 1
        self.assertEqual(m.m11, 2)
        self.assertEqual(m[0,0], 2)

    def test_decompose(self):
        # define expectations for multiple cases
        testsets = [
            (
                Vector3([1, 1, 2], dtype='f4'),
                Quaternion.from_y_rotation(np.pi, dtype='f4'),
                Vector3([10, 0, -5], dtype='f4'),
                Matrix44([
                    [-1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, -2, 0],
                    [10, 0, -5, 1],
                ], dtype='f4')
            ),
            (
                Vector3([-1, 3, .5], dtype='f4'),
                Quaternion.from_axis_rotation(Vector3([.75, .75, 0], dtype='f4').normalized, np.pi, dtype='f4').normalized,
                Vector3([1, -1, 1], dtype='f4'),
                Matrix44([
                    [0, -1, 0, 0],
                    [3, 0, 0, 0],
                    [0, 0, -.5, 0],
                    [1, -1, 1, 1],
                ], dtype='f4')
            ),
        ]

        for expected_scale, expected_rotation, expected_translation, expected_model in testsets:
            # compose model matrix using original inputs
            s = Matrix44.from_scale(expected_scale, dtype='f4')
            r = Matrix44.from_quaternion(expected_rotation, dtype='f4')
            t = Matrix44.from_translation(expected_translation, dtype='f4')
            m = t * r * s

            # check that it's the same as the expected matrix
            np.testing.assert_almost_equal(np.array(m), np.array(expected_model))
            self.assertTrue(m.dtype == expected_model.dtype)
            self.assertTrue(isinstance(m, expected_model.__class__))

            # decompose this matrix and recompose the model matrix from the decomposition
            ds, dr, dt = m.decompose()
            ds = Matrix44.from_scale(ds, dtype='f4')
            dr = Matrix44.from_quaternion(dr, dtype='f4')
            dt = Matrix44.from_translation(dt, dtype='f4')
            dm = dt * dr * ds

            # check that it's the same as the original matrix
            np.testing.assert_almost_equal(np.array(m), np.array(dm))
            self.assertTrue(m.dtype == dm.dtype)
            self.assertTrue(isinstance(dm, m.__class__))

if __name__ == '__main__':
    unittest.main()
