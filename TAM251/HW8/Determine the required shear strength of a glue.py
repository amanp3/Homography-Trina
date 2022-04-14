import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#Four boards are glued together to form a built-up beam with cross-sectional area as illustrated below where .
#ibeam shape

b = 32 # mm
V = 5 # kN

#SEAM 2
I1 = (1/12)*(3*b)*(4*b)**3
I2 = (1/12)*(b)*(2*b)**3
I3 = I2

I = I1-I2-I3

Q = (b+b/2)*(3*b*b)

tau = (V*Q)/(I*b)
print(tau*10**3) #MPa


#SEAM 1


I1 = (1/12)*(3*b)*(4*b)**3
I2 = (1/12)*(b)*(2*b)**3
I3 = I2

I = I1-I2-I3

Q = (b+b/2)*(b*b)

tau = (V*Q)/(I*b)
print(tau*10**3) #MPa