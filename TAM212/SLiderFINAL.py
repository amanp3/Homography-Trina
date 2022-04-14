from sympy import *
from sympy import Matrix as Matrix
import numpy as np
#vq = vp + w x rpq
#aq = ap + alpha x rpq + w x (w x rpq)
m1 = 2
m2 = 6
I1 = 6
I2 = 32
rOP = Matrix([1,1, 0])
rPQ = Matrix([-8,0, 0])
w1 = Matrix([0,0,8])
w2 = Matrix([0,0,1])
vP = Matrix([-8,8, 0])
vQ = Matrix([-8,0, 0])
alpha1 = Matrix([0,0,56])

ap = alpha1.cross(rOP) + w1.cross(w1.cross(rOP))
print(ap)

#aq = ap + alpha x rpq + w x (w x rpq)

aQx, a