import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#8.4 distributed load
b = 67 # mm
a = 627 # mm
w = 13 # kN/m
sigmaAll = 182 # MPa
tauAll = 71 # MPa

F = w*a

M = (F/2)*(a/4) - (F/2)*(a/2)
M=-1*M
h = symbols('h')
Ia = (1/12)*b*h**3
eq1 = Eq(sigmaAll, (M*(h/2))/Ia)

h1 = solve(eq1, h)
print(h1)
h1 = h1[0]
print(N(h1))

eq2 = Eq(tauAll, ((F/2)*((h/2)*b*(h/2)))/(I*b))
h2 = solve(eq2, h)
h2 = h2[0]
print(N(h2))