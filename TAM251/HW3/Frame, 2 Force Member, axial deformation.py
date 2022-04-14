import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The frame below supports a force with magnitude  applied at a distance  
# above point  as illustrated in the figure below. Assume the bar  
# is rigid and that the circular rod  has diameter  and elastic modulus . 
# The original length of rod  is .
#Determine the internal force in rod , . Remember the sign convention for positive and negative axial forces.
#Determine the axial deformation of rod , . Remember the sign convention for positive and negative deformations.

P = 77 # kN
d = 21 # mm
E = 98 # GPa
L = 676 # mm
a = 208 # mm
b = 395 # mm
alpha = 44 # degrees

P = P*10**3
d = d*10**-3
E = E*10**9
L = L*10**-3
a = a*10**-3
b = b*10**-3

alpha = alpha * (pi/180)

FBC = (P* b)/((a+b)*cos(alpha))

A = (pi/4)*d**2

d = (FBC*L)/(E*A)
print(N(FBC*10**-3)) #kN
print(N(d*10**3)) #mm