from sympy import *
import numpy as np
from sympy import Matrix as Matrix

rho = 43
omega = Matrix([0,0,-4])
alpha = Matrix([0,0,9])
rCQ = Matrix([-9,-3,0])


alphaz = alpha[2]
r = (rCQ[0]**2 + rCQ[1]**2 + rCQ[2]**2)**.5

vI = (omega.cross(rCQ)[0]**2 + omega.cross(rCQ)[1]**2)**.5

#inside bottom
ac = Matrix([-1*alphaz*r, (vI**2)/(rho - r), 0])
#outside top
#ac = Matrix([-1*alphaz*r, -(vI**2)/(rho + r), 0])
#outside left
#ac = Matrix([(vI**2)/(rho + r), -1*alphaz*r, 0])
#outside right
#ac = Matrix([-(vI**2)/(rho + r), 1*alphaz*r, 0])

aq = ac + alpha.cross(rCQ) + omega.cross(omega.cross(rCQ))
print(aq)