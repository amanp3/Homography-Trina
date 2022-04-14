#no momment, no forces, given aQ
#alpha1 if given comment out
from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m1 = 4
m2 = 3
I1 = 3
I2 = 16.25
rOP = Matrix([-1,1, 0])
rPQ = Matrix([1,-8, 0])
omega1 = Matrix([0,0,8])
omega2 = Matrix([0,0,1])
vP = Matrix([-8,-8, 0])
vQ = Matrix([0,-7, 0])
#alpha1 = 71
aQ = Matrix([0,-126,0])

#aq = ap + alpha x rpq + w x (w x rpq)

alpha1z, alpha2z = symbols('alpha1, alpha2')
alpha1 = Matrix([0,0,alpha1z])
alpha2 = Matrix([0,0,alpha2z])

eq1 = Eq(aQ, alpha1.cross(rOP) + omega1.cross(omega1.cross(rOP)) + alpha2.cross(rPQ) + omega2.cross(omega2.cross(rPQ)))
sol = solve((eq1), (alpha1z, alpha2z), dict = True)

print(sol)