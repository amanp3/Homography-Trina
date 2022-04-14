import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The rigid bar  has length  and is supported by a pin at  and 
# is pin-connected to the deformable rod  at . The deformable rod  has a length , 
# elastic modulus , and a circular cross-section with a diameter of . Consider  and .
#Find the maximum load  that rod  can be subjected to in order to avoid buckling of member .

L = 1001 # mm
a = 534 # mm
b = 624 # mm
E = 164 # GPa
d = 25 # mm
theta = 56 # degrees

theta = theta * (pi/180)
I = (pi/4)*(d/2)**4


B = (pi**2 * E*I)/(b**2)

P = (B*a*sin(theta))/L

print(N(P))


