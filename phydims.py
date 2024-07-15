#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:37:29 2021

@author: xrj
"""
from collections.abc import Iterable

import numpy as np
from dims import Dims


class PhyDims(Dims):
    def __init__(self, L=0, M=0, T=0, I=0, K=0, n=0, J=0):
        """
        Parameters
        ----------
        L : length
        M : mass
        T : time
        I : current
        K : temp
        n : mol
        J : candela
        xref : reference system related flag

        Returns
        -------
        TYPE
            PhyDims object.

        """
        if isinstance(L, Dims):
            arr = L.arr
        elif isinstance(L, Iterable):
            arr = np.array(L)
        else:
            arr = np.array([L, M, T, I, K, n, J])
        assert arr.shape == (7,),\
            f'array must shape==(7,), as 7 base dimension, but current shape={arr.shape}'
        super().__init__(arr)
