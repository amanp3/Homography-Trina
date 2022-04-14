from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#Two solid shafts  and  are connected by gears of radius  and  
# as depicted by the 2D illustration below. Both shafts have 
# the same torsional flexibility . End  is fixed to a rigid wall.
#Determine the magnitude of the angle of rotation at , , when a torque  is applied at . Assume small rotations.


Rb = 101 # mm
Rc = 41 # mm
ft = 0.000005 # (1/N.m)
TD = 666 # N.m

phiDC = TD*ft

TB = TD*(Rb/Rc)
phi1 = TB*ft
phi2 = phi1*(Rb/Rc)

print(N(phiDC+phi2))