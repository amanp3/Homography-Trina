from sympy import *
import numpy as np
from sympy import Matrix as Matrix

#3.9
L = 2264 # mm
Ac = 2765 # mm^2
E = 197 # GPa
P = 561 # kN
theta = 42 # degrees

theta = theta * (pi/180)

Cy = symbols('Cy')

eq1 = Eq(-P*(L/2) - P* tan(theta)*(L/2) + L*Cy,0)

sol = solve(eq1,Cy)
Cy= sol[0]
print(Cy)

#force balance at C
#net force x
FBC, FAC = symbols('FBC, FAC')
eq2 = Eq(-FBC*cos(theta) - FAC,0)
eq3 = Eq(Cy + FBC*sin(theta),0)

sol2 = solve((eq2,eq3), (FBC, FAC), dict =True)
print(sol2)