from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#Rod  is fixed at  and perfectly bonded to rod  at , as illustrated below. 
# Rod  has length , diameter  and is made of a material with shear modulus . 
# Rod  has length , diameter  and is made of a material with shear modulus . 
# A torque  is applied at  and a torque  is applied at .
#Determine the magnitude of the angle of twist at end , i.e., .

L1 = 377 # mm
L2 = 335 # mm
d1 = 72 # mm
d2 = 45 # mm
G1 = 30 # GPa
G2 = 34 # GPa
TB = 832 # N.m
TC = 609 # N.m

J1 = (pi/32)*d1**4
J2 = (pi/32)*d2**4

phi1 = ((TC-TB)*L1)/(G1*J1)
phi2 = ((TC)*L2)/(G2*J2)

phi = phi1+phi2

print(N(phi))
