from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m1 = 7
m2 = 8
m3 = 4
r2 = Matrix([-1,-5,0])
r3 = Matrix([-8, -1,0])
rC = Matrix([-13,14, 0])

r1x, r1y = symbols('r1x, r1y')

r1 = Matrix([r1x,r1y,0])
m = m1 + m2 +m3

eq1 = Eq(rC*m, m1*r1 + m2*r2 + m3*r3)

sol = solve((eq1), (r1x, r1y), dict = True)
print(sol)