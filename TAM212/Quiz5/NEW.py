from sympy import *
from sympy import Matrix as Matrix

aP = Matrix([-120, -8, 0])
rOP = Matrix([1, 1, 0])
rPQ = Matrix([-8, 0, 0])
#omega1 = Matrix([0,0,8])
omega2 = Matrix([0,0,1])

alpha2z, aQz = symbols('alpha2z, aQz')

alpha2 = Matrix([0,0,alpha2z])
aQ = Matrix([0,aQz,0])


#alpha2.cross(rQP), aP + omega1.cross(omega1.cross(rOP)) + alpha2.cross(rPQ) + omega2.cross(omega2.cross(rPQ))
eq1 = Eq(aQ, aP + alpha2.cross(rPQ) + omega2.cross(omega2.cross(rPQ)))

print(solve(eq1))
