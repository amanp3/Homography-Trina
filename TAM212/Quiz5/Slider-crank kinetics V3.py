from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m1 = 2
m2 = 6
I1 = 6
I2 = 34
rOP = Matrix([1,1, 0])
rPQ = Matrix([-8,-2, 0])
omega1 = Matrix([0,0,16])
omega2 = Matrix([0,0,2])
vP = Matrix([-16,16, 0])
vQ = Matrix([-12,0, 0])
M = Matrix([0,0,3937])
Fp = Matrix([-2886,-389,0])
#M is 0,0, k hat

alpha1  = (rOP.cross(Fp) + M)/I1

ap = rOP.cross(alpha1) + alpha1.cross(rOP) - omega1.cross(omega1.cross(rOP))
print(ap)

#idk
#alpha1 = (ap[0] + omega1[2]**2*rOP[1]) / -rOP[1]
#aQ = alpha1.cross(rOP) + omega1.cross(omega1.cross(rOP))

#alpha2 = (np.cross(rPQ/2, Fq) + np.cross(-rPQ/2, Fp)) / I2
#ap = aQ + np.cross(alpha2, -rPQ) + np.cross(omega2, np.cross(omega2,-rPQ))



