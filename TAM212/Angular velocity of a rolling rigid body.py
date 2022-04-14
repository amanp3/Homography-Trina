from sympy import *
import numpy as np
from sympy import Matrix as Matrix

rCQ = Matrix([8,-15,0])
vQ = Matrix([8,-32,0])

vx, wz = symbols('vx, wz')

vc = Matrix([vx,0,0])
w = Matrix([0,0,wz])

eq1 = Eq(vQ, vc + w.cross(rCQ))

sol = solve((eq1), (vx, wz), dict =True)

print(sol)