#The basketball pole  is fixed at  and is subject to a force  as indicated below.
#The rod is sectioned through point . Use a free-body diagram of segment  to determine the resultant internal loading at .
#  Remember to use the sign convention consistent with the given coordinate system Shear force
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#9.2
a = 672 # mm
L = 2985 # mm
P = 1044 # N
theta = 49 # degrees
b = 1194 # mm

theta = theta*(pi/180)

Vy = P*sin(theta)
Fx = -1*P*cos(theta)
print(N(Vy))
print(N(Fx))


Mz = -1*(L-b)*P*sin(theta) - P*cos(theta)*a
print(N(Mz*10**-6))