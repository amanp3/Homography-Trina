import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#11.9
#The cantilever beam has length  where , elasticity modulus , 
# and cross-section with moment of inertia .
#  A force  and a couple moment  are applied at midpoint as indicated below.

P = 9 # kN
M = 9 # kN.m
L = 7 # m
E = 224 # GPa
Iz = 0.000047 # m^4

P = P * 10**3
M = M* 10**3
E = E*10**9

#0<x<L
x3 = (-P)/(6*E*Iz)
x2 = (P*3*L)/(6*E*Iz) - M/(2*E*Iz)

print(N(x3))
print(N(x2))

#L<x<2L
#x1 terms
theta1 = (P*L**2)/(2*E*Iz)
theta2 = (-M*L)/(E*Iz)

x1 = theta1 + theta2
print(N(x1))

x0 = (-P*L**3)/(2*E*Iz) + (M*L**2)/(E*Iz) + x3*(L**3) + x2*(L**2)
print(N(x0))
#x0 = x3*(L)**3 + x2*(L)**2 - x1*L
#print(N(x0))