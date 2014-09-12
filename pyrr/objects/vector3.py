# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import numpy as np
from multipledispatch import dispatch
from collections import Iterable
from .base import BaseVector, BaseVector3, BaseMatrix, BaseQuaternion, NpProxy
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

            # vector4
            if obj.shape == (4,) or isinstance(obj, Vector4):
                obj = vector3.create_from_vector4(obj, dtype=dtype)
            # matrix44
            elif obj.shape == (4,4):
                obj = vector3.create_from_matrix44_translation(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Vector3, cls).__new__(cls, obj)

    ########################
    # Base operators
    @dispatch((np.ndarray, Iterable))
    def __add__(self, other):
        return Vector3(super(Vector3, self).__add__(other))

    @dispatch((np.ndarray, Iterable))
    def __sub__(self, other):
        return Vector3(super(Vector3, self).__sub__(other))

    @dispatch((np.ndarray, Iterable))
    def __mul__(self, other):
        return Vector3(super(Vector3, self).__mul__(other))

    @dispatch((np.ndarray, Iterable))
    def __truediv__(self, other):
        return Vector3(super(Vector3, self).__truediv__(other))

    @dispatch((np.ndarray, Iterable))
    def __div__(self, other):
        return Vector3(super(Vector3, self).__div__(other))

    ########################
    # Quaternion
    @dispatch(BaseQuaternion)
    def __add__(self, other):
        raise ValueError('Cannot add a quaternion to a vector')

    @dispatch(BaseQuaternion)
    def __sub__(self, other):
        raise ValueError('Cannot subtract a quaternion from a vector')

    @dispatch(BaseQuaternion)
    def __mul__(self, other):
        raise ValueError('Cannot multiply a vector by a quaternion')

    @dispatch(BaseQuaternion)
    def __truediv__(self, other):
        raise ValueError('Cannot divide a vector by a quaternion')

    @dispatch(BaseQuaternion)
    def __div__(self, other):
        raise ValueError('Cannot divide a vector by a quaternion')

    ########################
    # Matrices
    @dispatch(BaseMatrix)
    def __add__(self, other):
        raise ValueError('Cannot add a matrix to a vector')

    @dispatch(BaseMatrix)
    def __sub__(self, other):
        raise ValueError('Cannot subtract a matrix from a vector')

    @dispatch(BaseMatrix)
    def __mul__(self, other):
        raise ValueError('Cannot multiply a vector by a matrix')

    @dispatch(BaseMatrix)
    def __truediv__(self, other):
        raise ValueError('Cannot divide a vector by a matrix')

    @dispatch(BaseMatrix)
    def __div__(self, other):
        raise ValueError('Cannot divide a vector by a matrix')

    ########################
    # Vectors
    @dispatch(BaseVector)
    def __add__(self, other):
        return Vector3(super(Vector3, self).__add__(other[:3]))

    @dispatch(BaseVector)
    def __sub__(self, other):
        return Vector3(super(Vector3, self).__sub__(other[:3]))

    @dispatch(BaseVector)
    def __mul__(self, other):
        return Vector3(super(Vector3, self).__mul__(other[:3]))

    @dispatch(BaseVector)
    def __truediv__(self, other):
        return Vector3(super(Vector3, self).__truediv__(other[:3]))

    @dispatch(BaseVector)
    def __div__(self, other):
        return Vector3(super(Vector3, self).__div__(other[:3]))

    @dispatch(BaseVector)
    def __xor__(self, other):
        return self.cross(other)

    @dispatch(BaseVector)
    def __or__(self, other):
        return self.dot(other)

    ########################
    # Methods and Properties
    @property
    def vector3(self):
        return self

    @property
    def vector4(self):
        return Vector4(self)

    @property
    def negative(self):
        return Vector3(-self)

from .vector4 import Vector4
