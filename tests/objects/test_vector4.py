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

    def test_inverse(self):
        v = Vector4([1.,2.,3.,4.])
        self.assertTrue(np.array_equal(v.inverse, [-1.,-2.,-3.,-4.]))

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

    def test_accessors(self):
        v = Vector4(np.arange(self._size))
        self.assertTrue(np.array_equal(v.xy,[0,1]))
        self.assertTrue(np.array_equal(v.xyz,[0,1,2]))
        self.assertTrue(np.array_equal(v.xz,[0,2]))
        self.assertTrue(np.array_equal(v.xyz,[0,1,2]))

        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 1)
        self.assertEqual(v.z, 2)


if __name__ == '__main__':
    unittest.main()
try:
    import unittest2 as unittest
except:
    import unittest