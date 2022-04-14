#9.5
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#For the pipe system below, we assume the cross-section at  is subject to the resultant forces  and . Use the dimensions ,  and .
#The pipe is sectioned through points  and . Use an appropriate free-body diagram to determine all the resultant internal loadings at this cross-section. Remember to use the sign convention consistent with the given coordinate system.


a = 323 # mm
b = 219 # mm
c = 256 # mm
Pz = 411 # N
Py = 401 # N

Vy = Py
Vz = Pz


print(Vy)
print(Vz)

Tx = -1*c*Pz - Py*b
print(Tx*10**-3)

My = -1*a*Pz
print(My*10**-3)
Mz = -1*Py*a
print(Mz*10**-3)