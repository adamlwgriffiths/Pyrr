# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from multipledispatch import dispatch
from .base import BaseMatrix, BaseMatrix33, BaseMatrix44, BaseQuaternion, BaseVector, NpProxy
from .. import matrix33

class Matrix33(BaseMatrix33):
    _module = matrix33
    _shape = (3,3,)

    # m<c> style access
    m1 = NpProxy(0)
    m2 = NpProxy(1)
    m3 = NpProxy(2)

    # m<r><c> access
    m11 = NpProxy((0,0))
    m12 = NpProxy((0,1))
    m13 = NpProxy((0,2))
    m21 = NpProxy((1,0))
    m22 = NpProxy((1,1))
    m23 = NpProxy((1,2))
    m31 = NpProxy((2,0))
    m32 = NpProxy((2,1))
    m33 = NpProxy((2,2))

    # rows
    r1 = NpProxy(0)
    r2 = NpProxy(1)
    r3 = NpProxy(2)

    # columns
    c1 = NpProxy((slice(0,3),0))
    c2 = NpProxy((slice(0,3),1))
    c3 = NpProxy((slice(0,3),2))

    ########################
    # Creation
    @classmethod
    def from_matrix44(cls, matrix, dtype=None):
        return cls(matrix33.create_from_matrix44(matrix, dtype))

    def __new__(cls, value=None, dtype=None):
        if value != None:
            obj = value
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)

            # matrix44
            if obj.shape == (4,4) or isinstance(obj, Matrix44):
                obj = matrix33.create_from_matrix44(obj, dtype=dtype)
            # quaternion
            elif obj.shape == (4,) or isinstance(obj, Quaternion):
                obj = matrix33.create_from_quaternion(obj, dtype=dtype)
        else:
            obj = np.zeros(cls._shape, dtype=dtype)
        obj = obj.view(cls)
        return super(Matrix33, cls).__new__(cls, obj)

    ########################
    # Base operators
    @dispatch((np.ndarray, list, tuple))
    def __add__(self, other):
        return Matrix33(super(Matrix44, self).__add__(other))

    @dispatch((np.ndarray, list, tuple))
    def __sub__(self, other):
        return Matrix33(super(Matrix44, self).__sub__(other))

    @dispatch((np.ndarray, list, tuple))
    def __mul__(self, other):
        return Matrix33(matrix33.multiply(self, other))

    @dispatch((np.ndarray, list, tuple))
    def __div__(self, other):
        return Matrix33(super(Matrix44, self).__div__(other))

    ########################
    # Matrices
    @dispatch(BaseMatrix)
    def __add__(self, other):
        raise TypeError('Cannot add a matrix to a matrix')

    @dispatch(BaseMatrix)
    def __sub__(self, other):
        raise TypeError('Cannot subtract a matrix from a matrix')

    @dispatch(BaseMatrix33)
    def __mul__(self, other):
        return Matrix33(matrix33.multiply(self, other))

    @dispatch(BaseMatrix44)
    def __mul__(self, other):
        return Matrix33(matrix33.multiply(self, other.matrix33))

    @dispatch(BaseMatrix)
    def __div__(self, other):
        raise TypeError('Cannot divide a matrix by a matrix')

    def __invert__(self):
        return self.inverse

    ########################
    # Quaternions
    @dispatch(BaseQuaternion)
    def __add__(self, other):
        raise TypeError('Cannot add a quaternion to a matrix')

    @dispatch(BaseQuaternion)
    def __sub__(self, other):
        raise TypeError('Cannot subtract a quaternion from a matrix')

    @dispatch(BaseQuaternion)
    def __mul__(self, other):
        m = other.matrix33
        return self * m

    @dispatch(BaseQuaternion)
    def __div__(self, other):
        raise TypeError('Cannot divide a matrix by a quaternion')
        
    ########################
    # Vectors
    @dispatch(BaseVector)
    def __add__(self, other):
        raise TypeError('Cannot add a vector to a matrix')

    @dispatch(BaseVector)
    def __sub__(self, other):
        raise TypeError('Cannot subtract a vector from a matrix')

    @dispatch(BaseVector)
    def __mul__(self, other):
        return other.__class__(matrix33.apply_to_vector(self, other))

    @dispatch(BaseVector)
    def __div__(self, other):
        raise TypeError('Cannot divide a matrix by a vector')

    ########################
    # Methods and Properties
    @property
    def matrix33(self):
        return self

    @property
    def matrix44(self):
        return Matrix44(self)

    @property
    def quaternion(self):
        return Quaternion(self)

    @property
    def inverse(self):
        return Matrix33(matrix33.inverse(self))

from .matrix44 import Matrix44
from .quaternion import Quaternion
