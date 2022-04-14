import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The cross section below has dimensions 
#The centroid position  is given by:The moment of inertia  with respect to the centroidal axis  is given by:
#Determine the magnitude of the maximum tensile normal stress  when the cross-section is subject to a positive moment 
#Determine the magnitude of the maximum shear stress  when the cross-section is subject to a shear force 

t1 = 5 # mm
t2 = 7 # mm
b = 76 # mm
h = 77 # mm
ybar = 55.66129 # mm
Iz = 937612.62903 # mm^4
Vy = 37 # kN
Mz = 655 # N.m

t1 = t1*10**-3
t2 = t2*10**-3
b = b*10**-3
h = h*10**-3
ybar = ybar*10**-3

Iz = Iz*10**-12
Vy = Vy*10**3

sigmaTensile = (Mz*ybar)/Iz
print(sigmaTensile*10**-6)
sigmaCompressive = (Mz*(h-ybar+t2))/Iz
print(sigmaCompressive*10**-6)

Q = (t2*b)*(h -ybar + (t2/2)) + (2*t1*(h-ybar))*((h-ybar)/2)
#print(Q)
tau = (Vy*Q)/(Iz*2*t1)
print(tau*10**-6)