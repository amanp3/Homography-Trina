import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The cross section below has dimensions , , , and .
#Determine the centroid position 
#Determine the moment of inertia  with respect to the centroidal axis .
#Determine the magnitude of the maximum normal stress, , when the cross-section is subject to a moment 
#7.8

h = 159 # mm
b = 236 # mm
t1 = 23 # mm
t2 = 21 # mm
Mz = 1454 # N.m

ybar = (h+t2+t2)/2
print(ybar)


I1 = (1/12)*(h+t2+t2)**3*(t1+b+t1) 
I2 = (1/12)*(h)**3*(b)

I = I1-I2
print(I*10**(-6))

sigma = (Mz*ybar)/I
print(sigma*10**3)