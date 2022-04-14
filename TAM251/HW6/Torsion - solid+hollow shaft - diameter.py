#In the system below, the shaft is solid from  to  and hollow from  to . 
# The hollow segment has inner diameter  mm. The shaft is fixed to a wall at . 
# A torque  is applied at  and a torque  is applied at . The shafts both have a shear modulus  and a length .
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

di = 26 # mm
TB = 1480 # N.m
TC = 449 # N.m
G = 114 # MPa
L = 1012 # mm
tauMax = 11 # MPa



T1 = TB-TC
T2 = -1*TC

print(T1)
print(T2)

d = symbols('d')
J = (pi/2)*(d/2)**4
eq1 = Eq(tauMax, (T1*(d/2))/J)

sol = solve(eq1, d)

print(N(sol[0]*10))

d = sol[0]*10
J1 = (pi/2)*(d/2)**4
J2 = (pi/2)*((d/2)**4-(di/2)**4)

phi1 = (T1*L)/(G*J1)
phi2 = (T2*L)/(G*J2)

print(N(phi1))
print(N(phi2))

print(N((phi1+phi2)*10**3))