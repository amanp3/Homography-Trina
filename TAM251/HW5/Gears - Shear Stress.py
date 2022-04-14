from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#Two solid shafts  and  are connected by gears of radius  
# and  as depicted by the 2D illustration below. Both shafts have the same diameter .
#Determine the magnitude of the maximum shear stress at rod , , when a torque  is applied at .

Rb = 74 # mm
Rc = 33 # mm
d = 12 # mm
TD = 26 # N.m

T1 = TD*(Rb/Rc)
J = (pi/2)*(((d/2)**4))

tau = (T1*(d/2))/J

print(N(tau*10**3))
