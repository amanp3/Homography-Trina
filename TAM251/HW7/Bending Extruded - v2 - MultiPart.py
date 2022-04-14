import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A beam has the extruded cross section shown below, where .
#Find , i.e., the  distance from the '-axis to the -axis, where  is the centroidal axis of the cross section.
#Determine the moment of inertia  with respect to the centroidal axis .
#7.9


t = 15 # mm
Mz = -1601 # N.m

A1 = (6*t*4*t) - (2*t*4*t)
A2 = (4*t*4*t)

ybarBottom = ((3*t*A1) + (8*t*A2))/(A1+A2)
print(ybarBottom)
ybar = ybarBottom-3*t
print(ybar)

I1 = (1/12)*(4*t)*(4*t)**3 + A2*(8*t - ybarBottom)**2
I2 = ((1/12)*4*t*(6*t)**3 - (1/12)*(2*t)*(4*t)**3)+ A1*(3*t-ybarBottom)**2

I = I1+I2
print(I)

c = ybarBottom
print((Mz*c)/I)