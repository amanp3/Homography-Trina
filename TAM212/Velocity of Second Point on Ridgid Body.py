from sympy import *
from sympy import Matrix as M
import numpy as np

#vQ = vP + w x rPQ

#rPQ = M([-1, -3, 0])
#vP = M([-4, 0 , 0])
#w = M([0,0,2])

#vQx, vQy = symbols('vQx, vQy')
#vQ = M([vQx, vQy, 0])

#eq1 = Eq(vQ, vP + w.cross(rPQ))

#print(solve(eq1))
rPQ = Matrix([2,4,0])
aP = Matrix([-5,-4,0])
alpha = Matrix([0,0,-2])
w = Matrix([0,0,1])

#aQ = aP + alpha x rPQ + w x(w x rPQ)
aQx, aQy = symbols('aQx, aQy')
aQ = Matrix([aQx,aQy,0])
eq1 = Eq(aQ, aP + alpha.cross(rPQ) + w.cross(w.cross(rPQ)))

print(solve((eq1), (aQx, aQy), dict = True))


