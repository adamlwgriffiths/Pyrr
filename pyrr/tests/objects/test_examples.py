from __future__ import absolute_import
try:
    import unittest2 as unittest
except:
    import unittest


class test_oo_examples(unittest.TestCase):
    def test_oo_examples(self):
        from pyrr import Quaternion, Matrix44, Vector3
        import numpy as np

        point = Vector3([1.,2.,3.])
        orientation = Quaternion()
        translation = Vector3()
        scale = Vector3([1.,1.,1.])

        # translate along X by 1
        translation += [1.0, 0.0, 0.0]

        # rotate about Y by pi/2
        rotation = Quaternion.from_y_rotation(np.pi / 2.0)
        orientation = rotation * orientation

        # create a matrix
        # start our matrix off using the scale
        matrix = Matrix44.from_scale(scale)

        # apply our orientation
        # we can multiply matricies and quaternions directly!
        matrix = matrix * orientation

        # apply our translation
        translation = Matrix44.from_translation(translation)
        matrix = matrix * translation

        # transform our point by the matrix
        # vectors are transformable by matrices and quaternions directly
        point = matrix * point

    def test_conversions(self):
        from pyrr import Quaternion, Matrix33, Matrix44, Vector3, Vector4

        v3 = Vector3([1.,0.,0.])
        v4 = Vector4.from_vector3(v3, w=1.0)
        v3, w = Vector3.from_vector4(v4)

        m44 = Matrix44()
        q = Quaternion(m44)
        m33 = Matrix33(q)

        m33 = Matrix44().matrix33
        m44 = Matrix33().matrix44
        q = Matrix44().quaternion
        q = Matrix33().quaternion

        m33 = Quaternion().matrix33
        m44 = Quaternion().matrix44

    def test_operators(self):
        from pyrr import Quaternion, Matrix44, Matrix33, Vector3, Vector4
        import numpy as np

        # matrix multiplication
        m = Matrix44() * Matrix33()
        m = Matrix44() * Quaternion()
        m = Matrix33() * Quaternion()

        # matrix inverse
        m = ~Matrix44.from_x_rotation(np.pi)

        # quaternion multiplication
        q = Quaternion() * Quaternion()
        q = Quaternion() * Matrix44()
        q = Quaternion() * Matrix33()

        # quaternion inverse (conjugate)
        q = ~Quaternion()

        # quaternion dot product
        d = Quaternion() | Quaternion()

        # vector oprations
        v = Vector3() + Vector3()
        v = Vector4() - Vector4()

        # vector transform
        v = Quaternion() * Vector3()
        v = Matrix44() * Vector3()
        v = Matrix44() * Vector4()
        v = Matrix33() * Vector3()

        # dot and cross products
        dot = Vector3() | Vector3()
        cross = Vector3() ^ Vector3()
