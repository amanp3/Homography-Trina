#A beam has the built-up cross section shown below. The rectangular top (in gray pattern) is glued to the 
# "curvy-I" bottom (which has cross section area ). Both parts are made of the same material. Assume .
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

R = 23 # mm
Mz = 1591 # N.m

#7.10

R = 23 # mm
Mz = 1591 # N.m

A1 = (4*R*pi*R)-(pi*R**2)
ybar = ((2*R + R/2)*(pi*R*R))/(pi*R*R + A1)

print(N(ybar))

Ic = (61*pi*R**4)/12 + (A1)*(ybar**2)
I1 = (1/12)*(pi*R)*(R**3) + (pi*R*R)*(2*R+(R/2)-ybar)**2

I = Ic+I1

print(N(I)*10**-6)

sigma = (Mz*(3*R-ybar))/I
print(N(sigma*10**3))