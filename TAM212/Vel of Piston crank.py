from sympy import *
from sympy import Matrix as Matrix
import numpy as np

rAB = Matrix([1.33962, 1.046625, 0])
w = Matrix([0,0,-153])

vB = w.cross(rAB)

rBC = Matrix([8.6368, -1.046625,0])

vCx, w2z= symbols('vCx, w2z')

vC = Matrix([vCx, 0, 0])
w2 = Matrix([0,0,w2z])

eq1 =  Eq(vC, vB + w2.cross(rBC))

sol = solve(eq1)
print(sol)