#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:52:27 2021

@author: xrj
"""
from numbers import Number
from phydims import PhyDims


class PhyUnit:
    def __init__(self, dims, xrate=1,
                 unit='', name="", desc=""):
        if isinstance(dims, PhyDims):
            self.dims = dims
        else:
            self.dims = PhyDims(dims, False)
        self.xrate = xrate  # rate of SI unit
        self.unit = unit    # 'cm', 'kg'
        self.name = name    # 'length', 'killgram'
        self.desc = desc

    # TODO: here
    @classmethod
    def from_str(cls, s):
        pass

    def change_strs(self, unit=None, name=None, desc=None):
        """
        can used for create units dict.
        """
        if unit is not None:
            self.unit = unit
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.__class__(self.dims, self.xrate*other)
        else:
            return self.__class__(self.dims*other.dims, self.xrate*other.xrate)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return self.__class__(self.dims, self.xrate/other)
        else:
            return self.__class__(self.dims/other.dims, self.xrate/other.xrate)

    def __pow__(self, other):
        return self.__class__(self.dims**other, self.xrate**other)


def proc_dict(d):
    for k,v in zip(d.keys(), d.values()):
        v.unit = k

units = {    # L, M, T, I, K, n, J
'm' : PhyUnit([1, 0, 0, 0, 0, 0, 0]),
'kg': PhyUnit([0, 1, 0, 0, 0, 0, 0]),
's' : PhyUnit([0, 0, 1, 0, 0, 0, 0]),
'A' : PhyUnit([0, 0, 0, 1, 0, 0, 0]),
'K' : PhyUnit([0, 0, 0, 0, 1, 0, 0]),
'mol':PhyUnit([0, 0, 0, 0, 0, 1, 0]),
'cd': PhyUnit([0, 0, 0, 0, 0, 0, 1]),
}

units['g'] = units['kg']/1000      # used for magnitude
units['N'] = units['kg']*units['s']
units['Pa'] = units['N']/(units['m']**2)
units['C'] = units['A']*units['s']

proc_dict(units)
