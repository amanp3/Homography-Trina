from sympy import *
from sympy import Matrix as Matrix
import numpy as np

L = 1769 # mm
di = 19 # mm
do = 35 # mm
G = 28 # GPa
T = 1393 # N.m

J = (pi/32)*(do**4-di**4)
tau = (T*(di/2))/J

gamma = tau/G
print(N(gamma))

#also works
#gamma2 = ((T)/(G*J))*(di/2)
#print(N(gamma2))