import numpy as np
from sympy import *
from sympy import Matrix as Matrix

P = 3 # kN
a = 625 # mm
b = 554 # mm
L = 1022 # mm
E = 176 # GPa
Ac = 884 # mm^2
theta = 54 # degrees

theta  = theta * (pi/180)

FBD = (P*L)/(a*sin(theta))

sigma = FBD/Ac

episilon = sigma/E

dbd = episilon*b

#dbd = (FBD*b)/(E*Ac) #also works comment out previous 2 lines


d = dbd/sin(theta)

alpha = atan(d/a)

dc = L*tan(alpha)

print(N(dc))