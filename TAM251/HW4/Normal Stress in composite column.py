from sympy import *
from sympy import Matrix as Matrix
import numpy as np

E1 = 69 # GPa
E2 = 202 # GPa
d = 25 # mm
D = 44 # mm
L = 749 # mm
P = 99 # kN


F1, F2 = symbols('F1, F2')
A1 = (pi/4)*(d**2)
A2 = (pi/4)*(D**2-d**2)

#d1 = d2
eq1 = Eq(F1, ((F2)/(E2*A2))*E1*A1)
eq2 = Eq(P, F1 + F2)

sol = solve((eq1,eq2), (F1, F2))
print(sol)

#F1 = sol[0]
#F2 = sol[1]

sigma = N(-1*(61875/4463)/A1)
print(sigma*10**3)#MPa