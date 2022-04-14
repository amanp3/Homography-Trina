import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A specimen has circular cross-sectional area with initial diameter  and a gauge length . 
# A force  elongates the specimen by . The specimen material has yielding strength  and shear modulus .
#Determine the elastic modulus Determine the Poisson ratio :
#Determine the reduction in diameter :


Lo = 200 # mm
d = 30 # mm
P = 121 # kN
delta = 0.3 # mm
sy = 350 # MPa
G = 49 # GPa


stress = P/(pi*.25*(d**2))
strain = delta/Lo

E = stress/strain

v = ((E/G)/2)-1

dD = v*(delta/Lo)*d

print("E GPa= ", (N(E)), "v = ", (N(v)), "dD mm = ", (N(dD)))