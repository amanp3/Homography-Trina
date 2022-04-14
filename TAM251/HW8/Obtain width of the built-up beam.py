import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#DOESNT WORK
#8.5
#Three identical boards are glued together to form a built-up beam with cross-sectional area as 
# illustrated below. Each board has cross-section dimensions  and . The wood has allowable shear stress 
# and the glue can withstand a maximum shear stress 
#Determine the minimum required width  of the cross-section so that the beam can withstand the prescribed loading condition.

h = 1 # in
a = 34 # in
P = 3 # kips
s1 = 304 # psi
s2 = 211 # psi

b = symbols('b')
Qwood = (3/2)*h*b*(3/4)*h
Qglue = (h/2)*b *(1/4)*h
I = (1/12)*b*(3*h)**3

#wood
eq1 = Eq(s1, ((P/2)*(Qwood))/(I*b))
sol1 = solve(eq1, b)
b1 = sol1[0]

#glue
eq2 = Eq(s2, ((P/2)*(Qglue))/(I*b))
sol2 = solve(eq2, b)
b2= sol2[0]

print(N(b1))
print(N(b2))