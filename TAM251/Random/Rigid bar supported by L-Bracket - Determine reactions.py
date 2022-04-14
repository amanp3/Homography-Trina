from sympy import *
from sympy import Matrix as Matrix
import numpy as np

a = 665 # mm
b = 83 # mm
c = 499 # mm
d = 166 # mm
L = 1662 # mm
w = 6 # kN/m
Ac = 52 # mm^2

a = a/1000
b = b/1000
c = c/1000
d = d/1000
L = L/1000
Ac = Ac/(10**6)

F = .5*w*L 
Ax, Bx, Ay, By = symbols('Ax, Bx, Ay, By')

eq1 = Eq(Ax + Bx,0)
eq2 = Eq(Ay + By - F, 0)
eq3 = Eq(By*(a+b)-F*(L/3),0)
eq4 = Eq(-Bx*(c+d)-By*(a+b),0)

sol = solve((eq1,eq2,eq3,eq4), (Ax, Bx, Ay, By), dict = True)
print(sol)
print(Ac)

#sqrt(bx**2 + by**2)/2 = V 
#V/Ac