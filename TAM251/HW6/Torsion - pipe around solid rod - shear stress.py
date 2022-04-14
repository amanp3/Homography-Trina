import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A composite shaft with length  is made by fitting an aluminum sleeve () over a steel core (), as illustrated below.
#  The composite shaft is fixed against rotation at the wall  and has outside diameter . The steel core has diameter . 
# A torque  is applied to the composite shaft at .
#Determine the magnitude of the maximum shear stress, , in the steel core .

L = 48 # in
Ga = 4000 # ksi
Gs = 12000 # ksi
da = 6 # in
ds = 5 # in
Tb = 3 # kip.in

JAL = (pi/2)*((da/2)**4-(ds/2)**4)
JS = (pi/2) * (ds/2)**4

phi = (Tb*L)/(Ga*JAL + Gs*JS)
TAL = (phi*Ga*JAL)/L
TS = (phi*Gs*JS)/L

tauMaxAL = (TAL*(da/2))/(JAL)
tauMaxS = (TS*(ds/2))/(JS)

print(N(tauMaxAL))
print(N(tauMaxS)) #ksi