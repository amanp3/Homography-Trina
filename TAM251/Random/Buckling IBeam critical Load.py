import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#HW13.3. Buckling I-beam critical load
#A column with an elastic modulus , length, , and the cross-section given below is subjected to a compressive load . Consider , , and .

#Determine the moment of inertia  about the neutral axis of the cross section.

#Find the critical value of ,  for each of the following boundary conditions:
#Pinned-pinned
#Fixed-Free
#Pinned-Fixed
#Fixed-Fixed

E = 162 # MPa
L = 1861 # mm
t = 24 # mm
a = 48 # mm
b = 120 # mm

I = (1/12)*b*(2*a+2*t)**3 - (1/12)*(b-t)*(2*a)**3
print(N(I*10**-6)) #Iz


Pcr1 = (pi**2 * E*I)/(L**2)
Pcr2 = (pi**2 * E*I)/(2*L)**2
Pcr3 = (pi**2 * E*I)/(0.7*L)**2
Pcr4 = (pi**2 * E*I)/(0.5*L)**2

print("2 pin: ", N(Pcr1*10**-3))
print("1 fixed 1 free: ", N(Pcr2*10**-3))
print("1 fixed 1 pin: ", N(Pcr3*10**-3))
print("Both Fixed : ", N(Pcr4*10**-3))
