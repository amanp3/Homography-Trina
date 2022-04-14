import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A beam with hollow circular cross-section with outer diameter  and inner diameter  is subjected to  of shear force.
#Determine the moment of inertia  about the neutral axis.
#Evaluate the first moment of area  needed to compute the average transverse shear stress 
# at the neutral axis of the cross section (i.e. ).
#Determine the magnitude of the average shear stress  at the neutral axis.
#8.9

D = 204 # mm
d = 114 # mm
V = 70 # kN

I = (pi/4)*(D/2)**4 - (pi/4)*(d/2)**4

print(N(I)*10**-6)

A = (1/2)*(pi*(D/2)**2-pi*(d/2)**2)
#Q = ((.5*(D/2)**2*pi*(D/4)) - .5*(d/2)**2*pi*(d/4)) #*(1/2)*(pi*(D/2)**2-pi*(d/2)**2)
#Q = ((D-d)/4 + (d/2))*(1/2)*(pi*(D/2)**2-pi*(d/2)**2)

Q = (1/2)*(pi*(D/2)**2)*((4*(D/2))/(3*pi)) - ((1/2)*pi*(d/2)**2)*((4*(d/2))/(3*pi))

print(N(Q)*10**-3)

thickness = (D-d)
tau = (V*Q)/(I*thickness)
print(N(tau*10**3))