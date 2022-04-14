import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#11.13
#The cantilever beam  with length  has elasticity modulus  and cross-section with moment of inertia . 
# The beam is fixed to a rigid wall at  and supports a uniform distributed load of intensity  
# over half of its length () and a couple moment 
# at the end .

w = 9 # kN/m
L = 8 # m
E = 194 # GPa
Iz = 0.000054 # m^4

w = w*10**3
E = E*10**9
Mo = (w*L**2)/12

y1 = (-w*L**4)/(8*E*Iz)
y2 = (w*(L/2)**4)/(8*E*Iz) + ((w*(L/2)**3)/(6*E*Iz))*((L/2))
y3 = (-Mo*L**2)/(2*E*Iz)

yc= y1 + y2+y3
print(N(yc*10**3)) #abs