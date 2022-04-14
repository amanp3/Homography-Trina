from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#aq = ap + alpha x rpq + w x (w x rpq)

#vq = vp + w x rpq
vQx, wz = symbols('vQx, wz')

vQ = Matrix([vQx, 1.6, 0])
w = Matrix([0,0,wz])
rPQ = Matrix([1.9026, -2.18866,0])

eq1 = Eq(vQ, w.cross(rPQ))

sol = solve((eq1))
print(sol)

vQ = Matrix([1.84056, 1.6, 0])
w = Matrix([0,0,0.8409545])

aQx, alphaZ = symbols('aQx, alphaZ')
aQ = Matrix([aQx, -2.7,0])
alpha = Matrix([0,0,alphaZ])

eq2 = Eq(aQ, alpha.cross(rPQ) + w.cross(w.cross(rPQ)))

sol2 = solve(eq2)

print(sol2)