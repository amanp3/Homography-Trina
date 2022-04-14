#with Moment M given

from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m1 = 2
m2 = 6
I1 = 6
I2 = 32

omega1 = Matrix([0,0,8])
omega2 = Matrix([0,0,1])
vP = Matrix([-8,8, 0])
vQ = Matrix([-8,0, 0])
alpha1 = Matrix([0,0,56])

#aP = alpha1.cross(rOP) + omega1.cross(omega1.cross(rOP))
#aq = ap + alpha2 x rpq + w2 x (w2 x rpq)


aP = Matrix([-120, -8, 0])
rOP = Matrix([1, 1, 0])
rPQ = Matrix([-8, 0, 0])

alpha2z, aQy = symbols('alpha2z, aQy')

alpha2 = Matrix([0,0,alpha2z])
aQ = Matrix([aQy,0,0])


#alpha2.cross(rQP), aP + omega1.cross(omega1.cross(rOP)) + alpha2.cross(rPQ) + omega2.cross(omega2.cross(rPQ))
eq1 = Eq(aQ, aP + alpha2.cross(rPQ) + omega2.cross(omega2.cross(rPQ)))
sol = solve(eq1)

print(sol)