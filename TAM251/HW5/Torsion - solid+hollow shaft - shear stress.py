from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#In the system below, the shaft is hollow from  to  and solid from  to . The shaft has outer diameter  
# and the hollow segment has inner diameter . 
# The shaft is fixed to a wall at . A torque  is applied at  and a torque  is applied at .

d = 76 # mm
TB = 1167 # N.m
TC = 569 # N.m

di = d/2
J1 = (pi/32)*(d**4-di**4)
J2 = (pi/32)*(d**4)

tau1 = ((TB-TC)*(d/2))/J1
tau2 = ((-1*TC)*(d/2))/J2
print(N(tau1*10**3))
print(N(tau2*10**3))