# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from multipledispatch import dispatch
from collections import Iterable
from .base import BaseObject, BaseMatrix, BaseMatrix33, BaseMatrix44, BaseQuaternion, BaseVector, NpProxy
from .. import matrix44

class Matrix44(BaseMatrix44):
    _module = matrix44
    _shape = (4,4,)

    # m<c> style access
    m1 = NpProxy(0)
    m2 = NpProxy(1)
    m3 = NpProxy(2)
    m4 = NpProxy(3)

    # m<r><c> access
    m11 = NpProxy((0,0))
    m12 = NpProxy((0,1))
    m13 = NpProxy((0,2))
    m14 = NpProxy((0,3))
    m21 = NpProxy((1,0))
    m22 = NpProxy((1,1))
    m23 = NpProxy((1,2))
    m24 = NpProxy((1,3))
    m31 = NpProxy((2,0))
    m32 = NpProxy((2,1))
    m33 = NpProxy((2,2))
    m34 = NpProxy((2,3))
    m41 = NpProxy((3,0))
    m42 = NpProxy((3,1))
    m43 = NpProxy((3,2))
    m44 = NpProxy((3,3))

    # rows
    r1 = NpProxy(0)
    r2 = NpProxy(1)
    r3 = NpProxy(2)
    r4 = NpProxy(3)

    # columns
    c1 = NpProxy((slice(0,4),0))
    c2 = NpProxy((slice(0,4),1))
    c3 = NpProxy((slice(0,4),2))
    c4 = NpProxy((slice(0,4),3))

    ########################
    # Creation
    @classmethod
    def from_matrix33(cls, matrix, dtype=None):
        return cls(matrix44.create_from_matrix33(matrix, dtype))

    @classmethod
    def perspective_projection(cls, fovy, aspect, near, far, dtype=None):
        return cls(matrix44.create_perspective_projection_matrix(fovy, aspect, near, far, dtype))

    @classmethod
    def perspective_projection_bounds(cls, left, right, top, bottom, near, far, dtype=None):
        return cls(matrix44.create_perspective_projection_matrix_from_bounds(left, right, top, bottom, near, far, dtype))

    @classmethod
    def orthogonal_projection(cls, left, right, top, bottom, near, far, dtype=None):
        return cls(matrix44.create_orthogonal_projection_matrix(left, right, top, bottom, near, far, dtype))

    @classmethod
    def from_translation(cls, translation, dtype=None):
        return cls(matrix44.create_from_translation(translation, dtype=dtype))

    @classmethod
    def from_quaternion(cls, quat, dtype=None):
        return cls(matrix44.create_from_quaternion(quat, dtype=dtype))

    def __new__(cls, value=None, dtype=None):
        if value is not None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # matrix33
            if obj.shape == (3,3) or isinstance(obj, Matrix33):
                obj = matrix44.create_from_matrix33(obj, dtype=dtype)
            # quaternion
            elif obj.shape == (4,) or isinstance(obj, Quaternion):
                obj = matrix44.create_from_quaternion(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Matrix44, cls).__new__(cls, obj)

    ########################
    # Basic Operators
    @dispatch(BaseObject)
    def __add__(self, other):
        raise ValueError('Cannot {} a {} to a {}'.format('add', other.__class__.__name__, self.__class__.__name__))

    @dispatch(BaseObject)
    def __sub__(self, other):
        raise ValueError('Cannot {} a {} from a {}'.format('subtract', other.__class__.__name__, self.__class__.__name__))

    @dispatch(BaseObject)
    def __mul__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('multiply', self.__class__.__name__, other.__class__.__name__))

    @dispatch(BaseObject)
    def __truediv__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('divide', self.__class__.__name__, other.__class__.__name__))

    @dispatch(BaseObject)
    def __div__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('divide', self.__class__.__name__, other.__class__.__name__))

    def __invert__(self):
        return self.inverse

    ########################
    # Matrices
    @dispatch(BaseMatrix)
    def __mul__(self, other):
        return Matrix44(matrix44.multiply(self, other.matrix44))

    ########################
    # Quaternions
    @dispatch(BaseQuaternion)
    def __mul__(self, other):
        m = other.matrix44
        return self * m

    ########################
    # Vectors
    @dispatch(BaseVector)
    def __mul__(self, other):
        return other.__class__(matrix44.apply_to_vector(self, other))

    ########################
    # Methods and Properties
    @property
    def matrix33(self):
        return Matrix33(self)

    @property
    def matrix44(self):
        return self

    @property
    def quaternion(self):
        return Quaternion(self)

    @property
    def inverse(self):
        return Matrix44(matrix44.inverse(self))

    @property
    def translation(self):
        return Vector4(self[3,0:4])

from .matrix33 import Matrix33
from .quaternion import Quaternion
