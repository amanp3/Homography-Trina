import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A composite shaft with length  is made by fitting an aluminum sleeve () over a steel core (), 
# as illustrated below. The composite shaft is fixed against rotation at the wall  and has outside diameter . 
# The steel core has diameter . A torque  is applied at .
#Determine the magnitude of the angle of twist at end , i.e., .


L = 43 # in
Ga = 3000 # ksi
Gs = 11000 # ksi
da = 5 # in
ds = 4 # in
Tb = 1 # kip.in


G1 = Ga
G2 = Gs

J1 = (pi/2)*((da/2)**4-(ds/2)**4)
J2 = (pi/2)*((ds/2)**4)

T2 = ((Tb*L)/(G1*J1))/((L/(G1*J1)) + (L/(G2*J2)))

T1 = Tb - T2

phi1 = (T1*L)/(G1*J1)
phi2 = (T2*L)/(G2*J2)

print(N(phi1))
print(N(phi2)) #rad
