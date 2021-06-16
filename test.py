#!/usr/bin/env python3
from __init__ import PhyVal, PhyVar, PhyUnit
from phyvar import volume, mass
from phyunit import units

globals().update(units)
m0 = PhyVal(mass, 1, kg)
V0 = PhyVal(volume, 1, m**3)
ρ0 = m0/V0
print(ρ0.unit.dims.arr)
