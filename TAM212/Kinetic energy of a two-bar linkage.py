from sympy import *
from sympy import Matrix as Matrix
import numpy as np


m1 = 4
m2 = 5
rOP = Matrix([1,1,0])
rPQ = Matrix([0,2,0])
omega1 = Matrix([0,0,-1])
omega2 = Matrix([0,0,2])

vP = omega1.cross(rOP)
v2 = vP + omega2.cross(rPQ/2)

normrOP = (rOP[0]**2 + rOP[1]**2)**.5
normrPQ = (rPQ[0]**2 + rPQ[1]**2)**.5
I1 = (m1*normrOP**2)/3
I2 = (m2*normrPQ**2/12)

KE = .5*I1*omega1[2]**2 + .5*I2*omega2[2]**2 + .5*m2*(v2[0]**2+v2[1]**2+v2[2]**2)

print(KE)