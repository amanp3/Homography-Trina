import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The truss system below is supported by a pin at  and a roller at . When unloaded, truss member  has length . 
# The truss members are made of steel pipes with cross-sectional area  and elasticity modulus . 
# A vertical and a horizontal load of magnitude  are applied at joint . The angle is .
#Determine the horizontal displacement of point . Assume small deformations.

L = 2360 # mm
Ac = 2649 # mm^2
E = 204 # GPa
P = 426 # kN
theta = 41 # degrees

L = L*10**-3
Ac = Ac*10**-6
E = E*10**9
P = P*10**3

theta = theta*(pi/180)

#if vert force down then P/sin(theta) is POS 
#if horiz force to the right then P/cos(theta) is POS
F = P/cos(theta)  + P/sin(theta)
F = F/2
Fx = F*cos(theta)

dc = (Fx*L)/(E*Ac)
print(N(dc*10**3))