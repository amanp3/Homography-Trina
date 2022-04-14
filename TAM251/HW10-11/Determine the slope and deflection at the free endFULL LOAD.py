import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#11.12
#The cantilever beam  with length  has elasticity modulus , cross-section with moment of inertia  
# and supports a uniform distributed load of 
# intensity  over its entire length and a concentrated force  at midpoint .

P = 13 # kN
L = 7 # m
E = 220 # GPa
Iz = 0.000043 # m^4
#Iz OMEGALUL

P = P *10**3
E = E*10**9
w = P/L

y1 = (P*(L/2)**3)/(3*E*Iz) + (P*(L/2)**3)/(2*E*Iz)
theta1 = (P*(L/2)**2)/(2*E*Iz)
y2 = (-w*L**4)/(8*E*Iz)
theta2 = (-w*L**3)/(6*E*Iz)

y = y1 + y2
print(N(y*10**3))
theta = theta1 + theta2
print(N(theta))