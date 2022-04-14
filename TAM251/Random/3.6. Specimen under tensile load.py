import numpy as np
from sympy import *
from sympy import Matrix as Matrix


Lo = 200 # mm
d = 28 # mm
P = 134 # kN
delta = 0.1 # mm
sy = 350 # MPa
G = 189 # GPa


stress = P/(pi*.25*(d**2))
strain = delta/Lo

E = stress/strain

v = ((E/G)/2)-1

dD = v*(delta/Lo)*d

print("E GPa= " + str(N(E)), "v = " + str(N(v)), "dD mm = " + str(N(dD)))