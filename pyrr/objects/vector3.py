# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import numpy as np
from multipledispatch import dispatch
from collections import Iterable
from .base import BaseObject, BaseVector, BaseVector3, BaseVector4, BaseMatrix, BaseQuaternion, NpProxy
from .. import vector3

# TODO: add < <= > >= == != operators

class Vector3(BaseVector3):
    _module = vector3
    _shape = (3,)

    x = NpProxy(0)
    y = NpProxy(1)
    z = NpProxy(2)
    xy = NpProxy([0,1])
    xyz = NpProxy([0,1,2])
    xz = NpProxy([0,2])

    ########################
    # Creation
    def __new__(cls, value=None, dtype=None):
        if value is not None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # matrix44
            if obj.shape == (4,4):
                obj = vector3.create_from_matrix44_translation(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Vector3, cls).__new__(cls, obj)

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
    @dispatch(BaseVector3)
    def __add__(self, other):
        return Vector3(super(Vector3, self).__add__(other))

    @dispatch(BaseVector3)
    def __sub__(self, other):
        return Vector3(super(Vector3, self).__sub__(other))

    @dispatch(BaseVector3)
    def __mul__(self, other):
        return Vector3(super(Vector3, self).__mul__(other))

    @dispatch(BaseVector3)
    def __truediv__(self, other):
        return Vector3(super(Vector3, self).__truediv__(other))

    @dispatch(BaseVector3)
    def __div__(self, other):
        return Vector3(super(Vector3, self).__div__(other))

    @dispatch(BaseVector3)
    def __xor__(self, other):
        return self.cross(other)

    @dispatch(BaseVector3)
    def __or__(self, other):
        return self.dot(other)

    @dispatch(BaseVector3)
    def __ne__(self, other):
        return bool(np.any(super(Vector3, self).__ne__(other)))

    @dispatch(BaseVector3)
    def __eq__(self, other):
        return bool(np.all(super(Vector3, self).__eq__(other)))

    ########################
    # Methods and Properties
    @property
    def negative(self):
        return Vector3(-self)

from .vector4 import Vector4
