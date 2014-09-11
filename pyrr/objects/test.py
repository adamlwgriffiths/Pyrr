from __future__ import absolute_import

if __name__ == '__main__':
    import numpy as np
    import math

    from .matrix33 import Matrix33
    from .matrix44 import Matrix44
    from .vector3 import Vector3
    from .vector4 import Vector4
    from .quaternion import Quaternion

    m1 = Matrix44.identity()
    m2 = Matrix44.perspective_projection(90, 640./480., 1., 10.)
    v1 = Vector3([1,2,3])

    print m1 * v1
    print m1 * m2

    try:
        m1 + v1
    except Exception as e:
        print e

    try:
        m1 - v1
    except Exception as e:
        print e


    try:
        m1 + m2
    except Exception as e:
        print e

    try:
        m1 += v1
    except Exception as e:
        print e


    try:
        m1 += m2
    except Exception as e:
        print e

    try:
        Matrix44([1,2,3])
    except Exception as e:
        print e


    #print m1 / m2
    #print m1 / v1


    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 3
    assert np.array_equal(v1.xy, [1,2]), v1.xy
    assert np.array_equal(v1.xyz, [1,2,3]), v1.xyz
    assert np.array_equal(v1.xz, [1,3]), v1.xz

    assert np.array_equal(m1.m1, m1[0]), m1.m1
    assert np.array_equal(m1.m11, m1[0][0]), m1.m11


    m1 = Matrix33.identity()
    m2 = Matrix33.from_scale([1,2,3])


    m1 = Matrix33.identity()
    m2 = Matrix44.identity()

    assert np.array_equal(m1 * m2, Matrix33.identity())

    try:
        m1 / m2
    except Exception as e:
        print e


    try:
        m1 /= m2
    except Exception as e:
        print e
    else:
        print 'uh oh! didnt error!'

    print repr(m1)

    assert np.array_equal(~m1, m1.inverse)

    q = Quaternion()
    assert np.array_equal(q, [0, 0, 0, 1])

    q = Quaternion.from_x_rotation(math.pi)
    assert np.array_equal(~q, q.conjugate)


    # conversion
    m1 = Matrix33(Quaternion())
    m1 = Matrix44(Quaternion())

    q = Quaternion(Matrix33())
    q = Quaternion(Matrix44())
    q = Quaternion(Vector4())

    # copying values
    m1 = Matrix44()
    m2 = Matrix44(m1)
    m1[0,0] = 5
    assert m2[0,0] == 5
    assert m2.m11 == 5

    m1.m11 = 6
    assert m2[0,0] == 6
    assert m2.m11 == 6

    m1 = Matrix44(np.arange(16))
    assert np.array_equal(m1.m1, [0,1,2,3])
    assert np.array_equal(m1.m2, [4,5,6,7])
    assert np.array_equal(m1.m3, [8,9,10,11])
    assert np.array_equal(m1.m4, [12,13,14,15])

    assert np.array_equal(m1.r1, [0,1,2,3])
    assert np.array_equal(m1.r2, [4,5,6,7])
    assert np.array_equal(m1.r3, [8,9,10,11])
    assert np.array_equal(m1.r4, [12,13,14,15])

    assert np.array_equal(m1.c1, [0,4,8,12])
    assert np.array_equal(m1.c2, [1,5,9,13])
    assert np.array_equal(m1.c3, [2,6,10,14])
    assert np.array_equal(m1.c4, [3,7,11,15])

    assert m1.m11 == 0
    assert m1.m12 == 1
    assert m1.m13 == 2
    assert m1.m14 == 3
    assert m1.m21 == 4
    assert m1.m22 == 5
    assert m1.m23 == 6
    assert m1.m24 == 7
    assert m1.m31 == 8
    assert m1.m32 == 9
    assert m1.m33 == 10
    assert m1.m34 == 11
    assert m1.m41 == 12
    assert m1.m42 == 13
    assert m1.m43 == 14
    assert m1.m44 == 15

    v1 = Vector3([0,0,1])
    v2 = Vector3([1,0,0])
    assert v1.length == 1
    assert v1.squared_length == 1
    assert v1.dot(v1) == 1.
    assert v1.dot(v2) == 0.

    assert v1 | v2 == v1.dot(v2)
    assert np.array_equal(v1 ^ v2, v1.cross(v2))



    v1 = Vector3([-1, 2, -3])
    assert np.array_equal(abs(v1), [1,2,3])
    assert type(abs(v1)) == Vector3


    v1 = Vector4([1,0,0,0])
    v2 = Vector3([1,0,0])
    assert v1 | v2 == 1.0
    assert v2 | v1 == 1.0

    v1 = Vector4([1,0,0,0])
    v2 = Vector3([0,1,0])
    assert np.array_equal(v1 ^ v2, [0,0,1,1])
    assert np.array_equal(v2 ^ v1, [0,0,-1])



    import pyrr
    m1 = pyrr.Matrix44()

    import pyrr.vector3
    pyrr.vector3.Vector3()
