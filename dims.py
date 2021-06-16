#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:41:59 2021

@author: xrj
"""
import numpy as np
from numbers import Number, Integral


class Dims:
    def __init__(self, arr, xref=False):
        """
        Parameters
        ----------
        arr : np.ndarray
        xref : reference system related, bool, optional
            can't add both side, multipy, division any side
            eg: timestamp, position, The default is False.

        Returns
        -------
        None.

        """
        arr = np.array(arr)
        assert issubclass(arr.dtype.type, np.integer), 'arr must be int'
        self.arr = arr
        self.xref = xref  # don't add

    def __add__(self, other):
        assert self.arr == other.arr, "both dims not same"
        assert not(self.xref and other.xref), "can't add both with 'xref' flag"
        return self.__class__(self.arr, self.xref or self.xref)

    def __sub__(self, other):
        assert self.arr == other.arr, "both dims not same"
        assert not self.xref and other.xref,\
            "can't minuend without 'xref' flag, subtrahend with 'xref' flag"
        return self.__class__(self.arr, self.xref ^ other.xref)

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.copy()
        assert not (self.xref or other.xref),\
            "can't mul any with 'reference system related' flag"
        return self.__class__(self.arr + other.arr, False)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return self.copy()
        assert not(self.xref or other.xref),\
            "can't div any with 'reference system related' flag"
        return self.__class__(self.arr - other.arr, False)

    def __pow__(self, other):
        assert not self.xref,\
            "can't power with 'reference system related' flag"
        if isinstance(other, Integral):
            return self.__class__(self.arr*other, False)
        elif isinstance(other, Number):
            arr2 = self.arr*other
            assert np.all(arr2 % 1 == 0), 'has decimal part'
            return self.__class__(arr2, False)
        else:
            raise TypeError(f'unsupport type {type(other)} for exp')
