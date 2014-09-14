# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from multipledispatch import dispatch
from .base import BaseObject, BaseQuaternion, BaseMatrix, BaseVector, NpProxy
from .. import quaternion

class Quaternion(BaseQuaternion):
    _module = quaternion
    _shape = (4,)

    x = NpProxy(0)
    y = NpProxy(1)
    z = NpProxy(2)
    w = NpProxy(3)
    xy = NpProxy([0,1])
    xyz = NpProxy([0,1,2])
    xyzw = NpProxy([0,1,2,3])
    xz = NpProxy([0,2])
    xzw = NpProxy([0,2,3])
    xyw = NpProxy([0,1,3])
    xw = NpProxy([0,3])

    ########################
    # Creation
    @classmethod
    def from_x_rotation(cls, theta, dtype=None):
        return cls(quaternion.create_from_x_rotation(theta, dtype))

    @classmethod
    def from_y_rotation(cls, theta, dtype=None):
        return cls(quaternion.create_from_y_rotation(theta, dtype))

    @classmethod
    def from_z_rotation(cls, theta, dtype=None):
        return cls(quaternion.create_from_z_rotation(theta, dtype))

    @classmethod
    def from_axis_rotation(cls, axis, theta, dtype=None):
        return cls(quaternion.create_from_axis_rotation(axis, theta, dtype))

    @classmethod
    def from_matrix(cls, matrix, dtype=None):
        return cls(quaternion.create_from_matrix(matrix, dtype))

    @classmethod
    def from_eulers(cls, eulers, dtype=None):
        return cls(quaternion.create_from_eulers(eulers, dtype))

    @classmethod
    def from_inverse_of_eulers(cls, eulers, dtype=None):
        return cls(quaternion.create_from_inverse_of_eulers(eulers, dtype))

    def __new__(cls, value=None, dtype=None):
        if value is not None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # matrix33, matrix44
            if obj.shape in ((4,4,), (3,3,)) or isinstance(obj, (Matrix33, Matrix44)):
                obj = quaternion.create_from_matrix(obj, dtype=dtype)
        else:
            obj = quaternion.create(dtype=dtype)
        obj = obj.view(cls)
        return super(Quaternion, cls).__new__(cls, obj)

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

    ########################
    # Quaternions
    @dispatch(BaseQuaternion)
    def __mul__(self, other):
        return self.cross(other)

    @dispatch(BaseQuaternion)
    def __or__(self, other):
        return self.dot(other)

    def __invert__(self):
        return self.conjugate

    ########################
    # Matrices
    @dispatch(BaseMatrix)
    def __mul__(self, other):
        return self * Quaternion(other)

    ########################
    # Vectors
    @dispatch(BaseVector)
    def __mul__(self, other):
        return other.__class__(quaternion.apply_to_vector(self, other))

    ########################
    # Methods and Properties
    @property
    def length(self):
        return quaternion.length(self)

    def normalise(self):
        self[:] = quaternion.normalise(self)#self.normalised

    @property
    def normalised(self):
        return Quaternion(quaternion.normalise(self))

    @property
    def angle(self):
        return quaternion.rotation_angle(self)

    @property
    def axis(self):
        return Vector3(quaternion.rotation_axis(self))

    def cross(self, other):
        return Quaternion(quaternion.cross(self, other))

    def dot(self, other):
        return quaternion.dot(self, other)

    @property
    def conjugate(self):
        return Quaternion(quaternion.conjugate(self))

    @property
    def inverse(self):
        return Quaternion(quaternion.inverse(self))

    def power(self, exponent):
        return Quaternion(quaternion.power(self, exponent))

    @property
    def negative(self):
        return Quaternion(quaternion.negate(self))

    @property
    def is_identity(self):
        return quaternion.is_identity(self)

    @property
    def matrix44(self):
        return Matrix44.from_quaternion(self)

    @property
    def matrix33(self):
        return Matrix33.from_quaternion(self)

from .vector3 import Vector3
from .vector4 import Vector4
from .matrix33 import Matrix33
from .matrix44 import Matrix44
