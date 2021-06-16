#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:41:59 2021

@author: xrj
"""
import numpy as np
from numbers import Number, Integral


class Dims:
    def __init__(self, *args):
        arr = np.array(args[0] if len(args) == 1 else args)
        assert issubclass(arr.dtype.type, np.integer), 'arr must be int'
        self.arr = arr

    def __add__(self, other):
        assert self == other, "both dims not same"
        return self

    def __sub__(self, other):
        assert self == other, "both dims not same"

    def __mul__(self, other):
        if isinstance(other, Number):
            return self
        return Dims(self.arr + other.arr)

    def __truediv__(self, other):
        return Dims(self.arr - other.arr)

    def __pow__(self, other):
        if isinstance(other, Integral):
            return Dims(self.arr*other)
        elif isinstance(other, Number):
            arr2 = self.arr*other
            assert np.all(arr2 % 1 == 0), 'has decimal part'
            return Dims(arr2)
        else:
            raise TypeError(f'unsupport type {type(other)} for exp')

    def __eq__(self, other):
        return all(self.arr == other.arr)