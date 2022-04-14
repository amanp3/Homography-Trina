import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The gear train illustrated below consists of three solid shafts with diameter  
# connected by four gears: two gears with radius  and two other gears with radius . 
# The shafts are supported by the smooth journal bearings , , , , 
# fixed at  and are made with a material that has shear modulus . Consider .
#Determine the magnitude of the angle of rotation at , , when a torque  is applied as shown. Assume small rotations.

d = 35 # mm
R1 = 94 # mm
R2 = 47 # mm
G = 80 # GPa
L = 134 # mm
TE = 479 # N.m

T3 = TE
T2 = T3*(R2/R1)
T1 = T2*(R2/R1)

J = (pi/2)*(d/2)**4

phi1 = (T1*L)/(G*J)
phi2 = (T2*L)/(G*J)
phi3 = (T3*L)/(G*J)


phi2T = (phi1*R2)/(R1)
phiA1 = phi2T*(R2/R1)

phiA2 = phi2*(R2/R1)

phiE = (T3*L)/(G*J)


print(N(phiA1))
print(N(phiA2))
print(N(phiE))
print(N(phiA1+phiA2+phiE))
