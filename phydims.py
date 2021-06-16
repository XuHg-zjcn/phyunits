#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:37:29 2021

@author: xrj
"""
import numpy as np
from dims import Dims


class PhyDims(Dims):
    def __init__(self, arr, xref=False):
        """

        Parameters
        ----------
        arr : np.array
            length-7 int dims numbers..
        xref : bool, optional
            @ref to Dims.__init__. The default is False.

        Returns
        -------
        None.

        """
        arr = np.array(arr)
        assert arr.shape == (7,),\
            f'array must dim=1, length=7(base dims), but current is {arr.shape}'
        super().__init__(arr, xref)

    @classmethod
    def from_nums(cls, L=0, M=0, T=0, I=0, K=0, n=0, J=0, xref=False):
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
        return cls([L, M, T, I, K, n, J], xref)
