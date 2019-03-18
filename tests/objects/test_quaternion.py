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


class test_object_quaternion(unittest.TestCase):
    _shape = (4,)
    _size = np.multiply.reduce(_shape)

    def test_imports(self):
        import pyrr
        pyrr.Quaternion()
        pyrr.quaternion.Quaternion()
        pyrr.objects.quaternion.Quaternion()

        from pyrr import Quaternion
        from pyrr.objects import Quaternion
        from pyrr.objects.quaternion import Quaternion

    def test_create(self):
        q = Quaternion()
        self.assertTrue(np.array_equal(q, [0., 0., 0., 1.]))
        self.assertEqual(q.shape, self._shape)

        q = Quaternion([1., 2., 3., 4.])
        self.assertTrue(np.array_equal(q, [1., 2., 3., 4.]))
        self.assertEqual(q.shape, self._shape)

        q = Quaternion(Quaternion([1., 2., 3., 4.]))
        self.assertTrue(np.array_equal(q, [1., 2., 3., 4.]))
        self.assertEqual(q.shape, self._shape)

    def test_from_x_rotation(self):
        # 180 degree turn around X axis
        q = Quaternion.from_x_rotation(np.pi)
        self.assertTrue(np.allclose(q, [1., 0., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0.,-1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 0.,-1.]))

        # 90 degree rotation around X axis
        q = Quaternion.from_x_rotation(np.pi / 2.)
        self.assertTrue(np.allclose(q, [np.sqrt(0.5), 0., 0., np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 0., 1.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0.,-1., 0.]))

        # -90 degree rotation around X axis
        q = Quaternion.from_x_rotation(-np.pi / 2.)
        self.assertTrue(np.allclose(q, [-np.sqrt(0.5), 0., 0., np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 0.,-1.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 1., 0.]))

    def test_from_y_rotation(self):
        # 180 degree turn around Y axis
        q = Quaternion.from_y_rotation(np.pi)
        self.assertTrue(np.allclose(q, [0., 1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [-1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 0.,-1.]))

        # 90 degree rotation around Y axis
        q = Quaternion.from_y_rotation(np.pi / 2.)
        self.assertTrue(np.allclose(q, [0., np.sqrt(0.5), 0., np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [0., 0.,-1.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [1., 0., 0.]))

        # -90 degree rotation around Y axis
        q = Quaternion.from_y_rotation(-np.pi / 2.)
        self.assertTrue(np.allclose(q, [0., -np.sqrt(0.5), 0., np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [0., 0., 1.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [-1., 0., 0.]))

    def test_from_z_rotation(self):
        # 180 degree turn around Z axis
        q = Quaternion.from_z_rotation(np.pi)
        self.assertTrue(np.allclose(q, [0., 0., 1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [-1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0.,-1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 0., 1.]))

        # 90 degree rotation around Z axis
        q = Quaternion.from_z_rotation(np.pi / 2.)
        self.assertTrue(np.allclose(q, [0., 0., np.sqrt(0.5), np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [0., 1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [-1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 0., 1.]))

        # -90 degree rotation around Z axis
        q = Quaternion.from_z_rotation(-np.pi / 2.)
        self.assertTrue(np.allclose(q, [0., 0., -np.sqrt(0.5), np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [0.,-1., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0., 0., 1.]))

    def test_from_axis_rotation(self):
        q = Quaternion.from_axis_rotation([1., 0., 0.], np.pi / 2.)
        self.assertTrue(np.allclose(q, [np.sqrt(0.5), 0., 0., np.sqrt(0.5)]))
        self.assertTrue(np.allclose(q * Vector3([1., 0., 0.]), [1., 0., 0.]))
        self.assertTrue(np.allclose(q * Vector3([0., 1., 0.]), [0., 0., 1.]))
        self.assertTrue(np.allclose(q * Vector3([0., 0., 1.]), [0.,-1., 0.]))

    def test_from_axis(self):
        source = np.array([np.pi / 2, 0, 0])
        result = Quaternion.from_axis(source)
        expected = np.array([np.sqrt(0.5), 0, 0, np.sqrt(0.5)])
        self.assertTrue(np.allclose(result, expected))

        source = np.array([0, np.pi, 0])
        result = Quaternion.from_axis(source)
        expected = np.array([0, 1, 0, 0])
        self.assertTrue(np.allclose(result, expected))

        source = np.array([0, 0, 2 * np.pi])
        result = Quaternion.from_axis(source)
        expected = np.array([0, 0, 0, -1])
        self.assertTrue(np.allclose(result, expected))

    @unittest.skip('Not implemented')
    def test_from_eulers(self):
        pass

    @unittest.skip('Not implemented')
    def test_from_inverse_of_eulers(self):
        pass

    def test_length(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.length, quaternion.length(q)))

    def test_normalize(self):
        q = Quaternion([1., 2., 3., 4.])
        self.assertFalse(np.allclose(q.length, 1.))

        q.normalize()
        self.assertTrue(np.allclose(q.length, 1.))

    def test_normalized(self):
        q1 = Quaternion([1., 2., 3., 4.])
        self.assertFalse(np.allclose(q1.length, 1.))

        q2 = q1.normalized
        self.assertFalse(np.allclose(q1.length, 1.))
        self.assertTrue(np.allclose(q2.length, 1.))

    def test_angle(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertEqual(q.angle, quaternion.rotation_angle(q))

    def test_axis(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.axis, quaternion.rotation_axis(q)))

    def test_cross(self):
        q1 = Quaternion.from_x_rotation(np.pi / 2.0)
        q2 = Quaternion.from_y_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q1.cross(q2), quaternion.cross(q1, q2)))

    def test_dot(self):
        q1 = Quaternion.from_x_rotation(np.pi / 2.0)
        q2 = Quaternion.from_y_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q1.dot(q2), quaternion.dot(q1, q2)))

    def test_conjugate(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.conjugate, quaternion.conjugate(q)))

    def test_inverse(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.inverse, quaternion.inverse(q)))

    def test_exp(self):
        source = Quaternion.from_eulers([0, np.pi / 2, 0])
        result = source.exp()
        expected = np.array([0, 1.31753841, 0, 1.54186346])
        self.assertTrue(np.allclose(result, expected))

    def test_power(self):
        q1 = Quaternion.from_x_rotation(np.pi / 2.0)
        q2 = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q1.power(2.0), quaternion.power(q2, 2.0)))

    def test_negative(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.negative, quaternion.negate(q)))

    def test_is_identity(self):
        self.assertTrue(quaternion.is_identity(Quaternion()))
        self.assertTrue(quaternion.is_identity(Quaternion([0., 0., 0., 1.])))
        self.assertFalse(quaternion.is_identity(Quaternion([1., 0., 0., 0.])))

    def test_matrix33(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.matrix33, matrix33.create_from_quaternion(q)))

    def test_matrix44(self):
        q = Quaternion.from_x_rotation(np.pi / 2.0)
        self.assertTrue(np.allclose(q.matrix44, matrix44.create_from_quaternion(q)))

    def test_operators_matrix33(self):
        q = Quaternion()
        m = Matrix33.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: q + m)

        # subtract
        self.assertRaises(ValueError, lambda: q - m)

        # multiply
        self.assertTrue(np.array_equal(q * m, quaternion.cross(quaternion.create(), quaternion.create_from_matrix(matrix33.create_from_x_rotation(0.5)))))

        # divide
        self.assertRaises(ValueError, lambda: q / m)

    def test_operators_matrix44(self):
        q = Quaternion()
        m = Matrix44.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: q + m)

        # subtract
        self.assertRaises(ValueError, lambda: q - m)

        # multiply
        self.assertTrue(np.array_equal(q * m, quaternion.cross(quaternion.create(), quaternion.create_from_matrix(matrix44.create_from_x_rotation(0.5)))))

        # divide
        self.assertRaises(ValueError, lambda: q / m)

    def test_operators_quaternion(self):
        q1 = Quaternion()
        q2 = Quaternion.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: q1 + q2)

        # subtract
        # we had to add this to enable np.array_equal to work
        # as it uses subtraction
        #self.assertRaises(ValueError, lambda: q1 - q2)

        # multiply
        self.assertTrue(np.array_equal(q1 * q2, quaternion.cross(quaternion.create(), quaternion.create_from_x_rotation(0.5))))

        # divide
        self.assertRaises(ValueError, lambda: q1 / q2)

        # or
        self.assertTrue(np.array_equal(q1 | q2, quaternion.dot(quaternion.create(), quaternion.create_from_x_rotation(0.5))))

        # inverse
        self.assertTrue(np.array_equal(~q2, quaternion.conjugate(quaternion.create_from_x_rotation(0.5))))

        # ==
        self.assertTrue(Quaternion() == Quaternion())
        self.assertFalse(Quaternion() == Quaternion([0., 0., 0., 0.]))

        # !=
        self.assertTrue(Quaternion() != Quaternion([1., 1., 1., 1.]))
        self.assertFalse(Quaternion() != Quaternion())

    def test_operators_vector3(self):
        q = Quaternion.from_x_rotation(0.5)
        v = Vector3([1., 0., 0.])

        # add
        self.assertRaises(ValueError, lambda: q + v)

        # subtract
        self.assertRaises(ValueError, lambda: q - v)

        # multiply
        self.assertTrue(np.array_equal(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(0.5), [1., 0., 0.])))

        # divide
        self.assertRaises(ValueError, lambda: q / v)

    def test_operators_vector4(self):
        q = Quaternion.from_x_rotation(0.5)
        v = Vector4([1., 0., 0., 1.])

        # add
        self.assertRaises(ValueError, lambda: q + v)

        # subtract
        self.assertRaises(ValueError, lambda: q - v)

        # multiply
        self.assertTrue(np.array_equal(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(0.5), [1., 0., 0., 1.])))

        # divide
        self.assertRaises(ValueError, lambda: q / v)


    def test_apply_to_vector_non_unit(self):
        q = Quaternion.from_x_rotation(np.pi)

        # zero length
        v = Vector3([0., 0., 0.])
        self.assertTrue(np.allclose(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(np.pi), [0., 0., 0.])))

        # >1 length
        v = Vector3([2., 0., 0.])
        self.assertTrue(np.allclose(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(np.pi), [2., 0., 0.])))
        v = Vector3([0., 2., 0.])
        self.assertTrue(np.allclose(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(np.pi), [0., 2., 0.])))
        v = Vector3([0., 0., 2.])
        self.assertTrue(np.allclose(q * v, quaternion.apply_to_vector(quaternion.create_from_x_rotation(np.pi), [0., 0., 2.])))


    def test_accessors(self):
        q = Quaternion(np.arange(self._size))
        self.assertTrue(np.array_equal(q.xy, [0, 1]))
        self.assertTrue(np.array_equal(q.xyz, [0, 1, 2]))
        self.assertTrue(np.array_equal(q.xyzw, [0, 1, 2, 3]))

        self.assertTrue(np.array_equal(q.xz, [0, 2]))
        self.assertTrue(np.array_equal(q.xyz, [0, 1, 2]))
        self.assertTrue(np.array_equal(q.xyw, [0, 1, 3]))
        self.assertTrue(np.array_equal(q.xw, [0, 3]))

        self.assertEqual(q.x, 0)
        self.assertEqual(q.y, 1)
        self.assertEqual(q.z, 2)
        self.assertEqual(q.w, 3)

        q.x = 1
        self.assertEqual(q.x, 1)
        self.assertEqual(q[0], 1)
        q.x += 1
        self.assertEqual(q.x, 2)
        self.assertEqual(q[0], 2)

    def test_equality(self):
        q1 = Quaternion([0, 0, 0, 1])
        q2 = Quaternion([0, 0, 0, 1])
        q3 = Quaternion([0, 0, 1, -1])
        self.assertEqual(q1, q2)
        self.assertNotEqual(q1, q3)
        self.assertNotEqual(q2, q3)

    def test_equality_negative(self):
        q1 = Quaternion([0, 0, 0, 1])
        q2 = Quaternion([0, 0, 0, -1])
        q3 = Quaternion([0, 0, 1, -1])
        self.assertEqual(q1, q2)
        self.assertNotEqual(q1, q3)

if __name__ == '__main__':
    unittest.main()
