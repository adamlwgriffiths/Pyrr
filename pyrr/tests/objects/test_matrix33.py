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


class test_object_matrix33(unittest.TestCase):
    _shape = (3,3)
    _size = np.multiply.reduce(_shape)

    def test_imports(self):
        import pyrr
        pyrr.Matrix33()
        pyrr.matrix33.Matrix33()
        pyrr.objects.matrix33.Matrix33()

        from pyrr import Matrix33
        from pyrr.objects import Matrix33
        from pyrr.objects.matrix33 import Matrix33

    def test_create(self):
        m = Matrix33()
        self.assertTrue(np.array_equal(m, np.zeros(self._shape)))
        self.assertEqual(m.shape, self._shape)

        m = Matrix33(np.arange(self._size))
        self.assertEqual(m.shape, self._shape)

        m = Matrix33([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(m.shape, self._shape)

        m = Matrix33(Matrix33())
        self.assertTrue(np.array_equal(m, np.zeros(self._shape)))
        self.assertEqual(m.shape, self._shape)

    def test_identity(self):
        m = Matrix33.identity()
        self.assertTrue(np.array_equal(m, np.eye(3)))

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
        m1 = Matrix44.identity()
        m = Matrix33.from_matrix44(m1)
        self.assertTrue(np.array_equal(m, np.eye(3)))

        m = Matrix33(m1)
        self.assertTrue(np.array_equal(m, np.eye(3)))

    def test_create_from_scale(self):
        v = Vector3([1,2,3])
        m = Matrix33.from_scale(v)
        self.assertTrue(np.array_equal(m, np.diag([1,2,3])))

    def test_create_from_eulers(self):
        e = Vector3([1,2,3])
        m = Matrix33.from_eulers(e)
        self.assertTrue(np.array_equal(m, matrix33.create_from_eulers([1,2,3])))

    def test_create_from_quaternion(self):
        q = Quaternion()
        m = Matrix33.from_quaternion(q)
        self.assertTrue(np.array_equal(m, np.eye(3)))
        self.assertTrue(np.array_equal(m.quaternion, q))

        m = Matrix33(q)
        self.assertTrue(np.array_equal(m, np.eye(3)))

    def test_create_from_inverse_quaternion(self):
        q = Quaternion.from_x_rotation(0.5)
        m = Matrix33.from_inverse_of_quaternion(q)
        expected = matrix33.create_from_quaternion(quaternion.inverse(quaternion.create_from_x_rotation(0.5)))
        np.testing.assert_almost_equal(np.array(m), expected, decimal=5)
        #self.assertTrue(np.array_equal(m, expected))

    def test_multiply(self):
        m1 = Matrix33(np.arange(self._size))
        m2 = Matrix33(np.arange(self._size)[::-1])
        m = m1 * m2
        self.assertTrue(np.array_equal(m, matrix33.multiply(m2, m1)))

        m1 = Matrix33(np.arange(self._size))
        m2 = Matrix44(np.arange(16))
        m = m1 * m2
        self.assertTrue(np.array_equal(m, matrix33.multiply(matrix33.create_from_matrix44(m2), m1)))

    def test_inverse(self):
        m1 = Matrix33.identity() * Matrix33.from_x_rotation(0.5)
        m = m1.inverse
        self.assertTrue(np.array_equal(m, matrix33.inverse(m1)))

    def test_matrix33(self):
        m1 = Matrix33.identity() * Matrix33.from_x_rotation(0.5)
        m = m1.matrix33
        self.assertTrue(m1 is m)

    def test_matrix44(self):
        m1 = Matrix33.identity() * Matrix33.from_x_rotation(0.5)
        m = m1.matrix44
        self.assertTrue(np.array_equal(m, matrix44.create_from_matrix33(m1)))

    def test_operators_matrix33(self):
        m1 = Matrix33.identity()
        m2 = Matrix33.from_x_rotation(0.5)

        # add
        self.assertTrue(np.array_equal(m1 + m2, matrix33.create_identity() + matrix33.create_from_x_rotation(0.5)))

        # subtract
        self.assertTrue(np.array_equal(m1 - m2, matrix33.create_identity() - matrix33.create_from_x_rotation(0.5)))

        # multiply
        self.assertTrue(np.array_equal(m1 * m2, matrix33.multiply(matrix33.create_from_x_rotation(0.5), matrix33.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m1 / m2)

        # inverse
        self.assertTrue(np.array_equal(~m2, matrix33.inverse(matrix33.create_from_x_rotation(0.5))))

        # ==
        self.assertTrue(Matrix33() == Matrix33())
        self.assertFalse(Matrix33() == Matrix33([1. for n in range(9)]))

        # !=
        self.assertTrue(Matrix33() != Matrix33([1. for n in range(9)]))
        self.assertFalse(Matrix33() != Matrix33())

    def test_operators_matrix44(self):
        m1 = Matrix33.identity()
        m2 = Matrix44.from_x_rotation(0.5)

        # add
        self.assertTrue(np.array_equal(m1 + m2, matrix33.create_identity() + matrix33.create_from_x_rotation(0.5)))

        # subtract
        self.assertTrue(np.array_equal(m1 - m2, matrix33.create_identity() - matrix33.create_from_x_rotation(0.5)))

        # multiply
        self.assertTrue(np.array_equal(m1 * m2, matrix33.multiply(matrix33.create_from_x_rotation(0.5), matrix33.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m1 / m2)

    def test_operators_quaternion(self):
        m = Matrix33.identity()
        q = Quaternion.from_x_rotation(0.7)

        # add
        self.assertRaises(ValueError, lambda: m + q)

        # subtract
        self.assertRaises(ValueError, lambda: m - q)

        # multiply
        self.assertTrue(np.array_equal(m * q, matrix33.multiply(matrix33.create_from_quaternion(quaternion.create_from_x_rotation(0.7)), matrix33.create_identity())))

        # divide
        self.assertRaises(ValueError, lambda: m / q)

    def test_operators_vector3(self):
        m = Matrix33.identity()
        v = Vector3([1,1,1])

        # add
        self.assertRaises(ValueError, lambda: m + v)

        # subtract
        self.assertRaises(ValueError, lambda: m - v)

        # multiply
        self.assertTrue(np.array_equal(m * v, matrix33.apply_to_vector(matrix33.create_identity(), [1,1,1])))

        # divide
        self.assertRaises(ValueError, lambda: m / v)

    def test_operators_vector4(self):
        m = Matrix33.identity()
        v = Vector4([1,1,1,1])

        # add
        self.assertRaises(ValueError, lambda: m + v)

        # subtract
        self.assertRaises(ValueError, lambda: m - v)

        # multiply
        self.assertTrue(ValueError, lambda: m * v)

        # divide
        self.assertRaises(ValueError, lambda: m / v)

    def test_operators_number(self):
        m = Matrix33.identity()
        fv = np.empty((1,), dtype=[('i', np.int16, 1),('f', np.float32, 1)])
        fv[0] = (2, 2.0)

        # add
        self.assertTrue(np.array_equal(m + 1.0, matrix33.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + 1, matrix33.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + np.float(1.), matrix33.create_identity()[:] + 1.0))
        self.assertTrue(np.array_equal(m + fv[0]['f'], matrix33.create_identity()[:] + 2.0))
        self.assertTrue(np.array_equal(m + fv[0]['i'], matrix33.create_identity()[:] + 2.0))

        # subtract
        self.assertTrue(np.array_equal(m - 1.0, matrix33.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - 1, matrix33.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - np.float(1.), matrix33.create_identity()[:] - 1.0))
        self.assertTrue(np.array_equal(m - fv[0]['f'], matrix33.create_identity()[:] - 2.0))
        self.assertTrue(np.array_equal(m - fv[0]['i'], matrix33.create_identity()[:] - 2.0))

        # multiply
        self.assertTrue(np.array_equal(m * 2.0, matrix33.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * 2, matrix33.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * np.float(2.), matrix33.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * fv[0]['f'], matrix33.create_identity()[:] * 2.0))
        self.assertTrue(np.array_equal(m * fv[0]['i'], matrix33.create_identity()[:] * 2.0))

        # divide
        self.assertTrue(np.array_equal(m / 2.0, matrix33.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / 2, matrix33.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / np.float(2.), matrix33.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / fv[0]['f'], matrix33.create_identity()[:] / 2.0))
        self.assertTrue(np.array_equal(m / fv[0]['i'], matrix33.create_identity()[:] / 2.0))

    def test_accessors(self):
        m = Matrix33(np.arange(self._size))
        self.assertTrue(np.array_equal(m.m1,[0,1,2]))
        self.assertTrue(np.array_equal(m.m2,[3,4,5]))
        self.assertTrue(np.array_equal(m.m3,[6,7,8]))

        self.assertTrue(np.array_equal(m.r1,[0,1,2]))
        self.assertTrue(np.array_equal(m.r2,[3,4,5]))
        self.assertTrue(np.array_equal(m.r3,[6,7,8]))

        self.assertTrue(np.array_equal(m.c1,[0,3,6]))
        self.assertTrue(np.array_equal(m.c2,[1,4,7]))
        self.assertTrue(np.array_equal(m.c3,[2,5,8]))

        self.assertEqual(m.m11, 0)
        self.assertEqual(m.m12, 1)
        self.assertEqual(m.m13, 2)
        self.assertEqual(m.m21, 3)
        self.assertEqual(m.m22, 4)
        self.assertEqual(m.m23, 5)
        self.assertEqual(m.m31, 6)
        self.assertEqual(m.m32, 7)
        self.assertEqual(m.m33, 8)

        m.m11 = 1
        self.assertEqual(m.m11, 1)
        self.assertEqual(m[0,0], 1)
        m.m11 += 1
        self.assertEqual(m.m11, 2)
        self.assertEqual(m[0,0], 2)

if __name__ == '__main__':
    unittest.main()
