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
from pyrr import vector4


class test_object_vector4(unittest.TestCase):
    _shape = (4,)
    _size = np.multiply.reduce(_shape)

    def test_imports(self):
        import pyrr
        pyrr.Vector4()
        pyrr.vector4.Vector4()
        pyrr.objects.vector4.Vector4()

        from pyrr import Vector4
        from pyrr.objects import Vector4
        from pyrr.objects.vector4 import Vector4

    def test_create(self):
        v = Vector4()
        self.assertTrue(np.array_equal(v, [0.,0.,0.,0.]))
        self.assertEqual(v.shape, self._shape)

        v = Vector4([1.,2.,3.,4.])
        self.assertTrue(np.array_equal(v, [1.,2.,3.,4.]))
        self.assertEqual(v.shape, self._shape)

        v = Vector4.from_vector3([1.,2.,3.], w=0.0)
        self.assertTrue(np.array_equal(v, [1.,2.,3.,0.]))
        self.assertEqual(v.shape, self._shape)

        v = Vector4(Vector4())
        self.assertTrue(np.array_equal(v, [0.,0.,0.,0.]))
        self.assertEqual(v.shape, self._shape)

        m = Matrix44.from_translation([1.,2.,3.])
        v = Vector4.from_matrix44_translation(m)
        self.assertTrue(np.array_equal(v, [1.,2.,3.,1.]))

        m = Matrix44.from_translation([1.,2.,3.])
        v = Vector4(m)
        self.assertTrue(np.array_equal(v, [1.,2.,3.,1.]))

    def test_inverse(self):
        v = Vector4([1.,2.,3.,4.])
        self.assertTrue(np.array_equal(v.inverse, [-1.,-2.,-3.,-4.]))

    def test_normalize(self):
        v = Vector4([1.,1.,1.,1.])
        np.testing.assert_almost_equal(np.array(v.normalized), [0.5, 0.5, 0.5, 0.5], decimal=5)

        v.normalize()
        np.testing.assert_almost_equal(np.array(v), [0.5, 0.5, 0.5, 0.5], decimal=5)

    def test_operators_matrix33(self):
        v = Vector4()
        m = Matrix33.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: v + m)

        # subtract
        self.assertRaises(ValueError, lambda: v - m)

        # multiply
        self.assertRaises(ValueError, lambda: v - m)

        # divide
        self.assertRaises(ValueError, lambda: v / m)

    def test_operators_matrix44(self):
        v = Vector4()
        m = Matrix44.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: v + m)

        # subtract
        self.assertRaises(ValueError, lambda: v - m)

        # multiply
        self.assertRaises(ValueError, lambda: v * m)

        # divide
        self.assertRaises(ValueError, lambda: v / m)

    def test_operators_quaternion(self):
        v = Vector4()
        q = Quaternion.from_x_rotation(0.5)

        # add
        self.assertRaises(ValueError, lambda: v + q)

        # subtract
        self.assertRaises(ValueError, lambda: v - q)

        # multiply
        self.assertRaises(ValueError, lambda: v * q)

        # divide
        self.assertRaises(ValueError, lambda: v / q)

    def test_operators_vector3(self):
        v1 = Vector4()
        v2 = Vector3([1.,2.,3.])

        # add
        self.assertRaises(ValueError, lambda: v1 + v2)

        # subtract
        self.assertRaises(ValueError, lambda: v1 - v2)

        # multiply
        self.assertRaises(ValueError, lambda: v1 * v2)

        # divide
        #self.assertRaises(ValueError, lambda: v1 / v2)

        # or
        self.assertRaises(ValueError, lambda: v1 | v2)

        # xor
        #self.assertRaises(ValueError, lambda: v1 ^ v2)

        # ==
        self.assertRaises(ValueError, lambda: Vector4() == Vector3())

        # !=
        self.assertRaises(ValueError, lambda: Vector4() != Vector3([1.,1.,1.]))

    def test_operators_vector4(self):
        v1 = Vector4()
        v2 = Vector4([1.,2.,3.,4.])

        # add
        self.assertTrue(np.array_equal(v1 + v2, [1.,2.,3.,4.]))

        # subtract
        self.assertTrue(np.array_equal(v1 - v2, [-1.,-2.,-3.,-4]))

        # multiply
        self.assertTrue(np.array_equal(v1 * v2, [0.,0.,0.,0.]))

        # divide
        self.assertTrue(np.array_equal(v1 / v2, [0.,0.,0.,0.]))

        # or
        self.assertTrue(np.array_equal(v1 | v2, vector4.dot([0.,0.,0.,0.], [1.,2.,3.,4.])))

        # xor
        #self.assertTrue(np.array_equal(v1 ^ v2, vector4.cross([0.,0.,0.,0.], [1.,2.,3.,4.])))

        # ==
        self.assertTrue(Vector4() == Vector4())
        self.assertFalse(Vector4() == Vector4([1.,1.,1.,1.]))

        # !=
        self.assertTrue(Vector4() != Vector4([1.,1.,1.,1.]))
        self.assertFalse(Vector4() != Vector4())

    def test_operators_number(self):
        v1 = Vector4([1.,2.,3.,4.])
        fv = np.empty((1,), dtype=[('i', np.int16, 1),('f', np.float32, 1)])
        fv[0] = (2, 2.0)

        # add
        self.assertTrue(np.array_equal(v1 + 1., [2., 3., 4., 5.]))
        self.assertTrue(np.array_equal(v1 + 1, [2., 3., 4., 5.]))
        self.assertTrue(np.array_equal(v1 + np.float(1.), [2., 3., 4., 5.]))
        self.assertTrue(np.array_equal(v1 + fv[0]['f'], [3., 4., 5., 6.]))
        self.assertTrue(np.array_equal(v1 + fv[0]['i'], [3., 4., 5., 6.]))

        # subtract
        self.assertTrue(np.array_equal(v1 - 1., [0., 1., 2., 3.]))
        self.assertTrue(np.array_equal(v1 - 1, [0., 1., 2., 3.]))
        self.assertTrue(np.array_equal(v1 - np.float(1.), [0., 1., 2., 3.]))
        self.assertTrue(np.array_equal(v1 - fv[0]['f'], [-1., 0., 1., 2.]))
        self.assertTrue(np.array_equal(v1 - fv[0]['i'], [-1., 0., 1., 2.]))

        # multiply
        self.assertTrue(np.array_equal(v1 * 2., [2., 4., 6., 8.]))
        self.assertTrue(np.array_equal(v1 * 2, [2., 4., 6., 8.]))
        self.assertTrue(np.array_equal(v1 * np.float(2.), [2., 4., 6., 8.]))
        self.assertTrue(np.array_equal(v1 * fv[0]['f'], [2., 4., 6., 8.]))
        self.assertTrue(np.array_equal(v1 * fv[0]['i'], [2., 4., 6., 8.]))

        # divide
        self.assertTrue(np.array_equal(v1 / 2., [.5, 1., 1.5, 2.]))
        self.assertTrue(np.array_equal(v1 / 2, [.5, 1., 1.5, 2.]))
        self.assertTrue(np.array_equal(v1 / np.float(2.), [.5, 1., 1.5, 2.]))
        self.assertTrue(np.array_equal(v1 / fv[0]['f'], [.5, 1., 1.5, 2.]))
        self.assertTrue(np.array_equal(v1 / fv[0]['i'], [.5, 1., 1.5, 2.]))

        # or
        self.assertRaises(ValueError, lambda: v1 | .5)
        self.assertRaises(ValueError, lambda: v1 | 5)
        self.assertRaises(ValueError, lambda: v1 | np.float(2.))
        self.assertRaises(ValueError, lambda: v1 | fv[0]['f'])
        self.assertRaises(ValueError, lambda: v1 | fv[0]['i'])

        # xor
        self.assertRaises(ValueError, lambda: v1 ^ .5)
        self.assertRaises(ValueError, lambda: v1 ^ 5)
        self.assertRaises(ValueError, lambda: v1 ^ np.float(2.))
        self.assertRaises(ValueError, lambda: v1 ^ fv[0]['f'])
        self.assertRaises(ValueError, lambda: v1 ^ fv[0]['i'])

        # ==
        self.assertRaises(ValueError, lambda: v1 == .5)
        self.assertRaises(ValueError, lambda: v1 == 5)
        self.assertRaises(ValueError, lambda: v1 == np.float(2.))
        self.assertRaises(ValueError, lambda: v1 == fv[0]['f'])
        self.assertRaises(ValueError, lambda: v1 == fv[0]['i'])

        # !=
        self.assertRaises(ValueError, lambda: v1 != .5)
        self.assertRaises(ValueError, lambda: v1 != 5)
        self.assertRaises(ValueError, lambda: v1 != np.float(2.))
        self.assertRaises(ValueError, lambda: v1 != fv[0]['f'])
        self.assertRaises(ValueError, lambda: v1 != fv[0]['i'])

    def test_bitwise(self):
        v1 = Vector4([1.,0.,0.,1.])
        v2 = Vector4([0.,1.,0.,1.])

        # or (dot)
        self.assertTrue(np.array_equal(v1 | v2, vector4.dot(v1, v2)))

    def test_accessors(self):
        v = Vector4(np.arange(self._size))
        self.assertTrue(np.array_equal(v.xy,[0,1]))
        self.assertTrue(np.array_equal(v.xyz,[0,1,2]))
        self.assertTrue(np.array_equal(v.xz,[0,2]))
        self.assertTrue(np.array_equal(v.xyz,[0,1,2]))

        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 1)
        self.assertEqual(v.z, 2)

        v.x = 1
        self.assertEqual(v.x, 1)
        self.assertEqual(v[0], 1)
        v.x += 1
        self.assertEqual(v.x, 2)
        self.assertEqual(v[0], 2)

if __name__ == '__main__':
    unittest.main()
