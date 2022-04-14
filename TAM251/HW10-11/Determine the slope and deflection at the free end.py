import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#11.15
#The cantilever beam  with length  has elasticity modulus , cross-section with moment of inertia  
# and supports a uniform distributed load of intensity  over half of its length and a couple moment 
# at the end .

w = 10 # kN/m
L = 6 # m
E = 179 # GPa
Iz = 0.000046 # m^4

w = w *10**3
E = E*10**9
M = (w*L**2)/24

y1 = (-w*(L/2)**4)/(8*E*Iz) - ((w*(L/2)**3)/(6*E*Iz))*(L/2)
theta1 =  (-w*(L/2)**3)/(6*E*Iz)
y2 = (M*L**2)/(2*E*Iz)
theta2 = (M*L)/(E*Iz)

y = y1 + y2

theta = theta1 + theta2

print(N(y*10**3))
print(N(theta))