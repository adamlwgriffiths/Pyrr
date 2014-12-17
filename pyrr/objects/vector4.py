# -*- coding: utf-8 -*-
"""Represents a 4 dimensional Vector.

The Vector4 class provides a number of convenient functions and
conversions.
::

    import numpy as np
    from pyrr import Quaternion, Matrix33, Matrix44, Vector4

    v = Vector4()
    v = Vector4([1.,2.,3.])

    # explicit creation
    v = Vector4.from_vector3(Vector3([1.,2.,3.]), w=1.0)

    # copy constructor
    v = Vector4(Vector4())

    # add / subtract vectors
    v = Vector4([1.,2.,3.,4.]) + Vector4([4.,5.,6.,7.])

    # rotate a vector by a Matrix
    v = Matrix44.identity() * Vector4([1.,2.,3.,4.])

    # rotate a vector by a Quaternion
    v = Quaternion() * Vector4([1.,2.,3.,4.])

    # get the dot-product of 2 vectors
    d = Vector4([1.,0.,0.,0.]) | Vector4([0.,1.,0.,0.])

    # access specific parts of the vector
    # x value
    x,y,z,w = v.x, v.y, v.z, v.w

    # access groups of values as np.ndarray's
    xy = v.xy
    xyz = v.xyz
    xyzw = v.xyzw
    xz = v.xz
    xw = v.xw
    xyw = v.xyw
    xzw = v.xzw
"""
from __future__ import absolute_import
from numbers import Number
import numpy as np
from multipledispatch import dispatch
from .base import BaseObject, BaseVector4, BaseMatrix44, NpProxy
from .. import vector4

# TODO: add < <= > >= == != operators

class Vector4(BaseVector4):
    _module = vector4
    _shape = (4,)

    #: The X value of this Vector.
    x = NpProxy(0)
    #: The Y value of this Vector.
    y = NpProxy(1)
    #: The Z value of this Vector.
    z = NpProxy(2)
    #: The W value of this Vector.
    w = NpProxy(3)
    #: The X,Y values of this Vector as a numpy.ndarray.
    xy = NpProxy([0,1])
    #: The X,Y,Z values of this Vector as a numpy.ndarray.
    xyz = NpProxy([0,1,2])
    #: The X,Y,Z,W values of this Vector as a numpy.ndarray.
    xyzw = NpProxy(slice(0,4))
    #: The X,Z values of this Vector as a numpy.ndarray.
    xz = NpProxy([0,2])
    #: The X,W values of this Vector as a numpy.ndarray.
    xw = NpProxy([0,3])
    #: The X,Y,W values of this Vector as a numpy.ndarray.
    xyw = NpProxy([0,1,3])
    #: The X,Z,W values of this Vector as a numpy.ndarray.
    xzw = NpProxy([0,2,3])

    ########################
    # Creation
    @classmethod
    def from_vector3(cls, vector, w=0.0, dtype=None):
        """Create a Vector4 from a Vector3.

        By default, the W value is 0.0.
        """
        return cls(vector4.create_from_vector3(vector, w, dtype))

    def __new__(cls, value=None, dtype=None):
        if value is not None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # matrix44
            if obj.shape in ((4,4,)) or isinstance(obj, BaseMatrix44):
                obj = vector4.create_from_matrix44_translation(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Vector4, cls).__new__(cls, obj)

    ########################
    # Basic Operators
    @dispatch(BaseObject)
    def __add__(self, other):
        raise ValueError('Cannot {} a {} to a {}'.format('add', type(other).__name__, type(self).__name__))

    @dispatch(BaseObject)
    def __sub__(self, other):
        raise ValueError('Cannot {} a {} from a {}'.format('subtract', type(other).__name__, type(self).__name__))

    @dispatch(BaseObject)
    def __mul__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('multiply', type(self).__name__, type(other).__name__))

    @dispatch(BaseObject)
    def __truediv__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('divide', type(self).__name__, type(other).__name__))

    @dispatch(BaseObject)
    def __div__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('divide', type(self).__name__, type(other).__name__))

    @dispatch((BaseObject, Number))
    def __xor__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('xor', type(self).__name__, type(other).__name__))

    @dispatch((BaseObject, Number))
    def __or__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('or', type(self).__name__, type(other).__name__))

    @dispatch((BaseObject, Number))
    def __ne__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('compare', type(self).__name__, type(other).__name__))

    @dispatch((BaseObject, Number))
    def __eq__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('compare', type(self).__name__, type(other).__name__))

    ########################
    # Vectors
    @dispatch((BaseVector4, np.ndarray))
    def __add__(self, other):
        return Vector4(super(Vector4, self).__add__(other))

    @dispatch((BaseVector4, np.ndarray))
    def __sub__(self, other):
        return Vector4(super(Vector4, self).__sub__(other))

    @dispatch((BaseVector4, np.ndarray))
    def __mul__(self, other):
        return Vector4(super(Vector4, self).__mul__(other))

    @dispatch((BaseVector4, np.ndarray))
    def __truediv__(self, other):
        return Vector4(super(Vector4, self).__truediv__(other))

    @dispatch((BaseVector4, np.ndarray))
    def __div__(self, other):
        return Vector4(super(Vector4, self).__div__(other))

    #@dispatch(BaseVector)
    #def __xor__(self, other):
    #    return self.cross(Vector4(other))

    @dispatch(BaseVector4)
    def __or__(self, other):
        return self.dot(Vector4(other))

    @dispatch(BaseVector4)
    def __ne__(self, other):
        return bool(np.any(super(Vector4, self).__ne__(other)))

    @dispatch(BaseVector4)
    def __eq__(self, other):
        return bool(np.all(super(Vector4, self).__eq__(other)))

    ########################
    # Number
    @dispatch(Number)
    def __add__(self, other):
        return Vector4(super(Vector4, self).__add__(other))

    @dispatch(Number)
    def __sub__(self, other):
        return Vector4(super(Vector4, self).__sub__(other))

    @dispatch(Number)
    def __mul__(self, other):
        return Vector4(super(Vector4, self).__mul__(other))

    @dispatch(Number)
    def __truediv__(self, other):
        return Vector4(super(Vector4, self).__truediv__(other))

    @dispatch(Number)
    def __div__(self, other):
        return Vector4(super(Vector4, self).__div__(other))

    ########################
    # Methods and Properties
    @property
    def inverse(self):
        """Returns the opposite of this vector.
        """
        return Vector4(-self)

from .matrix44 import Matrix44
