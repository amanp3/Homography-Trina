from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m = 5
l = 5
F1 = Matrix([-4,-3,0])
F2 = Matrix([1,-5,0])
M = Matrix([0,0,-2])
l1 = Matrix([-2.5,0,0])
l2 = Matrix([2.5,0,0])

r2 = Matrix([5,0,0])

print(r2.cross(F2))

rx,ry = symbols('rx,ry')

Fx = Matrix([3,8,0])
r1 = Matrix([rx,ry,0])


eq1 = Eq(-27, r1.cross(Fx))
print(solve(eq1))













#Mtotal = l1.cross(F1) + l2.cross(F2) + M

#rx = symbols('rx')
#D = Matrix([3,8,0])
#r = Matrix([rx,0,0])

#eq1 = Eq(Mtotal, r.cross(D))


#sol = solve((eq1), (r), dict = True)

#print(sol)