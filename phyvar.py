#!/usr/bin/env python3
from phyunit import PhyDims


class PhyVar:
    def __init__(self, dims, sym='', name="", desc=""):
        self.dims = dims
        self.sym = sym
        self.name = name
        self.desc = desc

    def change_strs(self, sym=None, name=None, desc=None):
        """
        can used for create units dict.
        """
        if sym is not None:
            self.sym = sym
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc

    def SI_unit(self):
        pass

    # TODO: xref move here
    def __add__(self, other):
        assert self.dims == other.dims

    def __sub__(self, other):
        assert self.dims == other.dims

    # TODO: save operation result var to sqlite
    def __mul__(self, other):
        if isinstance(other, PhyVar):
            return self.__class__(self.dims * other.dims,
                                  self.sym + '*' + other.sym,
                                  name=self.name + '*' + other.name)
        else:
            return self

    def __truediv__(self, other):
        if isinstance(other, PhyVar):
            return self.__class__(self.dims / other.dims,
                                  self.sym + '*' + other.sym,
                                  name=self.name + '*' + other.name)
        else:
            return self


length = PhyVar(PhyDims.from_nums(L=1), sym='l', name="length")
area = PhyVar(PhyDims.from_nums(L=2), sym='S', name='area')
volume = PhyVar(PhyDims.from_nums(L=3), sym='V', name="volume")
mass = PhyVar(PhyDims.from_nums(M=1), sym='m', name='mass')
