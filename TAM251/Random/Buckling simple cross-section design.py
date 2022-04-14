import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#13.6
#A column of length  with modulus of elasticity  has a square 
# cross-section and must support a load of . 
# The boundary conditions for the column are fixed-fixed.
#Find the minimum side length  for the cross section 
# if the column is to have a factor of safety  against failure due to buckling.

P = 564 # N
L = 1.490 # m
E = 201 # GPa
FS = 2.7

E = E * 10**9
s = symbols('s')

I = (1/12)*s*s**3#square
#I = (pi/4)*(s)**4 #s is radius here
P = P*FS

eq1 = Eq(P, (pi**2 * E*I)/(L**2))  #2 pin
eq2 = Eq(P, (pi**2 * E*I)/(2*L)**2) #1 fixed 1 free
eq3 = Eq(P, (pi**2 * E*I)/(0.7*L)**2) #1 fixed 1 pin
eq4 = Eq(P, (pi**2 * E*I)/(0.5*L)**2) #fixed fixed


sol = solve(eq4, s)
print(sol)



#print("2 pin: ", N(Pcr1*10**-3))
#print("1 fixed 1 free: ", N(Pcr2*10**-3))
#print("1 fixed 1 pin: ", N(Pcr3*10**-3))
#print("Both Fixed : ", N(Pcr4*10**-3))