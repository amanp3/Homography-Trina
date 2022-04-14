from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#Rod  is fixed at  and perfectly bonded to rod  at , as illustrated below. 
# Rod  has length , diameter  and is made of a material with shear modulus . 
# Rod  has length , diameter  and is made of a material with shear modulus . 
# A torque  is applied at  and a torque  is applied at .
#Determine the magnitude of the maximum shear stress  that occurs in the composite rod . #tauMaX

L1 = 300 # mm
L2 = 349 # mm
d1 = 60 # mm
d2 = 46 # mm
G1 = 35 # GPa
G2 = 40 # GPa
TB = 912 # N.m
TC = 895 # N.m

J1 = (pi/32)*d1**4
J2 = (pi/32)*d2**4


tau1 = ((TC-TB)*(d1/2))/J1
tau2 = ((TC)*(d2/2))/J2

print(N(tau1*10**3))
print(N(tau2*10**3)) #MPa
