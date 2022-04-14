import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#In the system below, the shaft is hollow from  to , solid from  to  and is made of a material with shear modulus . 
# The shaft has outer diameter  and the hollow segment has inner diameter . 
# A torque  is applied at . Ends  and  are fixed to rigid walls. Consider .
#Determine the magnitude of twist angle at , .

d = 49 # mm
L = 181 # mm
G = 64 # GPa
TB = 1359 # N.m

#PHI 1 + PHI 2 = 0 

J1 = (pi/2)*((d/2)**4-(d/4)**4)
J2 = (pi/2)*((d/2)**4)

#T1 = ((TB*L)/(G*J2))/((L/(G*J1)+L/(G*J2)))
#T2 = T1-TB


T2 = ((TB*L)/(G*J1))/((-1*L/(G*J2)) - L/(G*J1))

T1 = T2+TB

phi1 = (T1*L)/(G*J1)
phi2 = (T2*L)/(G*J2)


print(N(phi1))
print(N(phi2))
