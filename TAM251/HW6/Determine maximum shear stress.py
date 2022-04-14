import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#In the system below, the shaft is solid from  to , hollow from  to  
# and is made of a material with shear modulus . The solid shaft  has diameter , 
# the solid shaft  has diameter  and the tubular shaft  has outer diameter  and inner diameter . 
# A torque  is applied at  and a torque  is applied at  as shown. Ends  and  are fixed to rigid walls. Consider ,  and .

# ASSUMED CONVENTION IS TB TO LEFT AND TC TO RIGHT SO FLIP SIGN IN INPUTS ACCORDINGLY
L1 = 206 # mm
L2 = 618 # mm
L3 = 225 # mm
d1 = 37 # mm
d2 = 55 # mm
G = 50 # GPa
Tb = 1395 # N.m
Tc = -1351 # N.m

J1 = (pi/2)*((d1/2)**4)
J2 = (pi/2)*((d2/2)**4)
J3 = (pi/2)*((d2/2)**4-(d1/2)**4)


T1 = ((((Tc*L3)/(G*J3)) -((Tb*L3)/(G*J3)) - ((Tb*L2)/(G*J2))) / ((L1/(G*J1)) + (L2/(G*J2))+ (L3/(G*J3))))
T2 = Tb+T1
T3 = T1+Tb-Tc

#print(N(T1))
#print(N(T2))
#print(N(T3))

tau1 = (T1*(d1/2))/J1
tau2 = (T2*(d2/2))/J2
tau3 = (T3*(d2/2))/J3

print(N(tau1))
print(N(tau2))
print(N(tau3))

#FINAL ANSWER *10^3