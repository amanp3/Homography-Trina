import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#11.14
#A horizontal beam is supported by a rigid pin at  and a rod at . 
# Both beam and rod are made of the same material, with elasticity modulus . 
# The beam has moment of inertia  and the rod has cross-sectional area . Assume  , and .

P = 5 # kN
E = 237 # GPa
A = 192 # mm^2
L = 7 # m
H = 2 # m
Iz = 47000000 # mm^4

P = P*10**3
E = E*10**9
A = A*10**-6
Iz = Iz*10**-12

y1 = (-P*L**3)/(48*E*Iz)
y2 = ((-P/2)*H)/(E*A)

y = y1 + y2/2

print(N(y*10**3))