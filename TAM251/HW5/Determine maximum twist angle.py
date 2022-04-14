from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#The solid shaft has length , radius  and is made of a material with shear modulus  and ultimate shear stress .
#Determine the maximum allowable twist angle  assuming a factor of safety .

L = 1615 # mm
r = 16 # mm
G = 54 # GPa
tu = 55 # MPa
FS = 3

phi = (L*tu)/(G*r)
print(N(phi/FS)*10**-3)