#8.8
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#Four identical boards are bolted together to form a built-up beam with 
# cross-sectional area as illustrated below. Each board has the cross-section dimensions  and .
#  The bolts have diameter  and are spaced every .
#Determine the average shear stress in each bolt, , where the 
# boards are joined together if the maximum internal shear force in the beam is .


b = 221 # mm
t = 50 # mm
d = 18 # mm
deltaS = 86 # mm
Vy = 5 # kN

I = (1/12)*b*(b+2*t)**3 - (1/12)*(b-2*t)*b**3

print(N(I))
Q = ((b/2) + t/2)*(b*t) #+ 2*(b/4)*(b/2)*t
print(N(Q))

q = (Vy*Q)/I

F = q*deltaS
print(N(F))


taub = F/(2*pi*(d/2)**2)
print(N(taub*10**3))