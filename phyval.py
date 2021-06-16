#!/usr/bin/env python3
from phyvar import PhyVar
from phyunit import PhyUnit


class PhyVal:
    def __init__(self, var: PhyVar, data, unit: PhyUnit=None, sym='', name="", desc=""):
        assert var.dims == unit.dims
        self.var = var
        self.data = data
        self.unit = unit or var.SI_unit()
        self.sym = sym
        self.name = name
        self.desc = desc

    def convert_unit(self, unit2: PhyUnit):
        assert self.unit.dims == unit2.dims
        ratio = unit2.xrate / self.unit.xrate
        return self.__class__(self.var, self.data*ratio, unit2,
                              self.sym, self.name, self.desc)

    def __add__(self, other):
        if self.unit != other.unit:
            other = other.convert_unit(self.unit)
        data2 = self.data + other.data
        return self.__class__(self.var, data2, self.unit)

    def __sub__(self, other):
        if self.unit != other.unit:
            other = other.convert_unit(self.unit)
        data2 = self.data - other.data
        return self.__class__(self.var, data2, self.unit)

    def __mul__(self, other):
        if isinstance(other, PhyVal):
            data2 = self.data * other.data
        else:
            data2 = self.data * other
            other = self
        return self.__class__(self.var*other.var, data2, self.unit*other.unit)

    def __truediv__(self, other):
        if isinstance(other, PhyVal):
            data2 = self.data / other.data
        else:
            data2 = self.data / other
        return self.__class__(self.var/other.var, data2, self.unit/other.unit)
