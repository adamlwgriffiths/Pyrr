# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from multipledispatch import dispatch
from collections import Iterable
from .base import BaseVector, BaseVector4, BaseQuaternion, BaseMatrix, NpProxy
from .. import vector4

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
        if value != None:
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
    # Base operators
    @dispatch((np.ndarray, Iterable))
    def __add__(self, other):
        return Vector4(super(Vector4, self).__add__(other))

    @dispatch((np.ndarray, Iterable))
    def __sub__(self, other):
        return Vector4(super(Vector4, self).__sub__(other))

    @dispatch((np.ndarray, Iterable))
    def __mul__(self, other):
        return Vector4(super(Vector4, self).__mul__(other))

    @dispatch((np.ndarray, Iterable))
    def __div__(self, other):
        return Vector4(super(Vector4, self).__div__(other))

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
    def __div__(self, other):
        raise ValueError('Cannot divide a vector by a matrix')

    ########################
    # Vectors
    @dispatch(BaseVector)
    def __add__(self, other):
        return Vector4(super(Vector4, self).__add__(Vector4(other)))

    @dispatch(BaseVector)
    def __sub__(self, other):
        return Vector4(super(Vector4, self).__sub__(Vector4(other)))

    @dispatch(BaseVector)
    def __mul__(self, other):
        return Vector4(super(Vector4, self).__mul__(Vector4(other)))

    @dispatch(BaseVector)
    def __div__(self, other):
        return Vector4(super(Vector4, self).__div__(Vector4(other)))

    #@dispatch(BaseVector)
    #def __xor__(self, other):
    #    return self.cross(Vector4(other))

    @dispatch(BaseVector)
    def __or__(self, other):
        return self.dot(Vector4(other))

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
