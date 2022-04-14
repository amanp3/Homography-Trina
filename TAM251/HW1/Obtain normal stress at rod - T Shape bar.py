import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The T bracket  is supported by a pin at  and attached to a 
# deformable rod at . The external forces  and  are applied at  and , 
# respectively. Rod  has a circular cross-section with diameter , 
# length  and orientation  as illustrated below. Consider the following dimensions: , ,  and .

a = 320 # mm
b = 288 # mm
c = 177 # mm
d = 241 # mm
e = 244 # mm
P1 = 81 # kN
P2 = 78 # kN
theta = 27 # degrees
dab = 36 # mm


a = a*10**-3
b = b*10**-3
c = c*10**-3
d = d*10**-3
e = e*10**-3
P1 = P1*10**3
P2 = P2*10**3
dab = dab*10**-3



theta = theta*(pi/180)

F = symbols('F')

eq1 = Eq(-P1*b - P2*(b+c) + F*cos(theta)*(e+d+a*sin(theta)), 0)
sol = solve(eq1, F)
F = sol[0]

A = pi*(dab/2)**2

sigmaAB = F/A

print(N(sigmaAB*10**-6))