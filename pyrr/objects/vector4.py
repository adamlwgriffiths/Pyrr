# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from multipledispatch import dispatch
from collections import Iterable
from .base import BaseObject, BaseVector, BaseVector4, BaseQuaternion, BaseMatrix, NpProxy
from .. import vector4

# TODO: add < <= > >= == != operators

class Vector4(BaseVector4):
    _module = vector4
    _shape = (4,)

    x = NpProxy(0)
    y = NpProxy(1)
    z = NpProxy(2)
    w = NpProxy(3)
    xy = NpProxy([0,1])
    xyz = NpProxy([0,1,2])
    xyzw = NpProxy(slice(0,4))
    xz = NpProxy([0,2])
    xw = NpProxy([0,3])
    xzw = NpProxy([0,2,3])

    ########################
    # Creation
    def __new__(cls, value=None, dtype=None):
        if value is not None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # vector3
            if obj.shape == (3,):
                obj = vector4.create_from_vector3(obj, dtype=dtype)
            # matrix44
            elif obj.shape == (4,4) or isinstance(obj, Matrix44):
                obj = vector4.create_from_matrix44_translation(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Vector4, cls).__new__(cls, obj)

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

    @dispatch(BaseObject)
    def __xor__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('xor', self.__class__.__name__, other.__class__.__name__))

    @dispatch(BaseObject)
    def __or__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('or', self.__class__.__name__, other.__class__.__name__))

    @dispatch(BaseObject)
    def __ne__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('compare', self.__class__.__name__, other.__class__.__name__))

    @dispatch(BaseObject)
    def __eq__(self, other):
        raise ValueError('Cannot {} a {} by a {}'.format('compare', self.__class__.__name__, other.__class__.__name__))

    ########################
    # Vectors
    @dispatch(BaseVector4)
    def __add__(self, other):
        return Vector4(super(Vector4, self).__add__(other.vector4))

    @dispatch(BaseVector4)
    def __sub__(self, other):
        return Vector4(super(Vector4, self).__sub__(other.vector4))

    @dispatch(BaseVector4)
    def __mul__(self, other):
        return Vector4(super(Vector4, self).__mul__(other.vector4))

    @dispatch(BaseVector4)
    def __truediv__(self, other):
        return Vector4(super(Vector4, self).__truediv__(other.vector4))

    @dispatch(BaseVector4)
    def __div__(self, other):
        return Vector4(super(Vector4, self).__div__(other.vector4))

    #@dispatch(BaseVector)
    #def __xor__(self, other):
    #    return self.cross(Vector4(other))

    @dispatch(BaseVector4)
    def __or__(self, other):
        return self.dot(Vector4(other))

    @dispatch(BaseVector4)
    def __ne__(self, other):
        return bool(np.any(super(Vector4, self).__ne__(other.vector4)))

    @dispatch(BaseVector4)
    def __eq__(self, other):
        return bool(np.all(super(Vector4, self).__eq__(other.vector4)))

    ########################
    # Methods and Properties
    @property
    def vector3(self):
        return Vector3(self)

    @property
    def vector4(self):
        return self

    @property
    def negative(self):
        return Vector4(-self)

from .vector3 import Vector3
from .matrix44 import Matrix44
