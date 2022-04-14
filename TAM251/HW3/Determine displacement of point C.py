import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#The rigid bar  has length  and is supported by a deformable rod at  
# and pin-connected at , as indicated below. The deformable rod  has length , 
# elasticity modulus , cross-sectional area  and is attached to a bracket at . 
# Assume the rigid bar is subjected to a concentrated force with magnitude . Consider  and .
#Determine the vertical displacement of point . Assume small rotation approximation.

P = 2 # kN
a = 533 # mm
b = 537 # mm
L = 1095 # mm
E = 183 # GPa
Ac = 905 # mm^2
theta = 63 # degrees

P = P*10**3
a = a*10**-3
b = b*10**-3
L = L *10**-3
E = E*10**9
Ac = Ac*10**-6
theta = theta*(pi/180)

F = (P*L)/(a*sin(theta))

dL = (F*b)/(E*Ac)
h = dL/sin(theta)

dc = (h*L)/a
print(N(dc*10**3)) #mm

#import numpy as np
#from sympy import *
#from sympy import Matrix as Matrix

#P = 3 # kN
#a = 618 # mm
#b = 686 # mm
#L = 1073 # mm
#E = 176 # GPa
#Ac = 958 # mm^2
#theta = 36 # degrees

#theta  = theta * (pi/180)

#FBD = (P*L)/(a*sin(theta))
#print(N(FBD))
#sigma = FBD/Ac

#episilon = sigma/E

#dbd = episilon*b

#dbd = (FBD*b)/(E*Ac) #also works comment out previous 2 lines

#print(N(dbd))

#d = dbd/sin(theta)

#alpha = atan(d/a)

#dc = L*tan(alpha)

#print(N(dc))
