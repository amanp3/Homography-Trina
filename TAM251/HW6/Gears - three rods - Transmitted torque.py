from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#The gear train illustrated below consists of three solid shafts connected by four gears: two gears with radius  
# and two other gears with radius . All three shafts are made of the same material and have the same diameter . 
# The shafts are supported by the smooth journal bearings , , ,  and a motor exerts a torque  at .
#Determine the magnitude of the maximum shear stress developed in the shafts.

R1 = 94 # mm
R2 = 47 # mm
d = 25 # mm
TW = 4038 # N.mm

#rod 1,2,3 are read from top to bottom

T2 = TW*(R1/R2)

T3 = T2*(R1/R2)

J = (pi/2)*(d/2)**4
Tau1 = (TW*(d/2))/(J)
Tau2 = (T2*(d/2))/(J)
Tau3 = (T3*(d/2))/(J)

print(N(Tau1))
print(N(Tau2))
print(N(Tau3))