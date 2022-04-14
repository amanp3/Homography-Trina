import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#HW13.7. Buckling hollow rectangle critical load
#The beam below has an elastic modulus  and a lenth . 
# The cross-section of the beam is a hollow rectangle where , , and .
#Find the critical buckling load for a beam with this cross section under axial load, 
#held in place with fixed-fixed conditions, and the beam lateral deflection is in the -direction.

E = 200 # MPa
L = 4.159 # m
t = 27 # mm
a = 119 # mm
b = 214 # mm

I = (1/12)*a*(b)**3 - (1/12)*(a-2*t)*(b-2*t)**3
print(N(I*10**-6)) 


Pcr1 = (pi**2 * E*I)/(L**2)
Pcr2 = (pi**2 * E*I)/(2*L)**2
Pcr3 = (pi**2 * E*I)/(0.7*L)**2
Pcr4 = (pi**2 * E*I)/(0.5*L)**2

print("2 pin: ", N(Pcr1*10**-9))
print("1 fixed 1 free: ", N(Pcr2*10**-9))
print("1 fixed 1 pin: ", N(Pcr3*10**-9))
print("Both Fixed : ", N(Pcr4*10**-9))
