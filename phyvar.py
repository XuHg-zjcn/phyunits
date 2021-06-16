#!/usr/bin/env python3
from phyunit import PhyDims


class PhyVar:
    def __init__(self, dims, sym='', name="", desc="", xref=False):
        """
        xref : reference system related, bool, optional
            can't add both side, multipy, division any side
            eg: timestamp, position, The default is False.
        """
        self.dims = dims
        self.sym = sym
        self.name = name
        self.desc = desc
        self.xref = xref

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

    def _xref2(self, xref2):
        if self.xref == xref2:
            return self
        else:
            return self.__class__(self.dims, self.sym, self.name, self.desc, xref2)

    # TODO: xref move here
    def __add__(self, other):
        assert self.dims == other.dims, "both dims not same"
        assert not(self.xref and other.xref), "can't add both with 'xref' flag"
        return self._xref2(self.xref or other.xref)

    def __sub__(self, other):
        assert self.dims == other.dims, "both dims not same"
        assert not self.xref and other.xref,\
            "can't minuend without 'xref' flag, subtrahend with 'xref' flag"
        return self._xref2(self.xref ^ other.xref)

    # TODO: save operation result var to sqlite
    def __mul__(self, other):
        assert not (self.xref or other.xref),\
            "can't mul any with 'reference system related' flag"
        if isinstance(other, PhyVar):
            return self.__class__(self.dims * other.dims,
                                  sym=self.sym + '*' + other.sym,
                                  name=self.name + '*' + other.name)
        else:
            return self

    def __truediv__(self, other):
        assert not(self.xref or other.xref),\
            "can't div any with 'reference system related' flag"
        if isinstance(other, PhyVar):
            return self.__class__(self.dims / other.dims,
                                  sym=self.sym + '*' + other.sym,
                                  name=self.name + '*' + other.name)
        else:
            return self

    def __pow__(self, power):
        assert not self.xref,\
            "can't power with 'reference system related' flag"
        return self.__class__(self.dims ** power,
                              sym=self.sym + '^' + str(power),
                              name=self.name + '^' + str(power))


length = PhyVar(PhyDims.from_nums(L=1), sym='l', name="length")
area = PhyVar(PhyDims.from_nums(L=2), sym='S', name='area')
volume = PhyVar(PhyDims.from_nums(L=3), sym='V', name="volume")
mass = PhyVar(PhyDims.from_nums(M=1), sym='m', name='mass')
