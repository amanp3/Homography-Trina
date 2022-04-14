from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#vp = vm + w x rmp
#m is instantanious center


rP = Matrix([4,4,0])
vP = Matrix([32,-32,0])
rQ = Matrix([0,-4,0])
vQ = Matrix([0,-16,0])

rmx, rmy, wz= symbols('rmx, rmy, wz')
omega = Matrix([0,0,wz])

rM = Matrix([rmx, rmy, 0])

eq1 = Eq(vP, omega.cross(rP-rM))
eq2 = Eq(vQ, omega.cross(rQ-rM))

sol = solve((eq1, eq2), (rmx, rmy, wz), dict = True)
print(sol)

print(rM)


#omega = Matrix([0,0,2])
#vP = Matrix([-2,-4,0])
#rP = Matrix([2,3,0])

#rmx, rmy = symbols('rmx, rmy')
#rM = Matrix([rmx,rmy,0])

#eq1 = Eq(vP, omega.cross(rP-rM))

#print(solve(eq1))