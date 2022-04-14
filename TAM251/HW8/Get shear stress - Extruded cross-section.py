import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#8.2
#H shape withe small opening on top and bottom
#Determine the magnitude of the maximum shear stress  when the cross-section is subject to a shear force

b = 22 # mm
t = 8 # mm
Vy = 14 # kN


A = (2*(2*b*b)+ 2*2*b*t)
cent = ((2*(2*b*b*(b+2*t))+ (2*(2*b*t*(2*b+(t/2)+2*t)))))/A
Q = cent*A
print(N(Q))

thickness = 2*b

I1 =  (1/12)*(2*b+2*t+2*b)*(4*t)**3
I2 = 4*((1/12)*b*(2*b)**3 + (2*b*b)*(2*t+b)**2) 
I3 =  4* ((1/12)*(2*b)*(t**3) + ((2*b*t)*((2*b + 2*t +(t/2))**2))) 

print(I1) 
print(I2) 
print(I3)

I = I1 + I2+ I3
print(N(I))

tau = (Vy*Q)/(I*thickness)
print(tau*10**3) #MPa