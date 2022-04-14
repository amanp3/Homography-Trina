#7.12
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#DOOR looking one
#DOESNT WORK

t = 20 # mm
a = 20 # mm
r = 60 # mm
ybar = -6.5678 # mm

x = ((pi/8) - (8/(9*pi)))
ySC = (4*r)/(3*pi)

I1 = (1/12)*(8*t)*(14*t)**3 + (8*t*14*t)*(ybar)**2
I2 = (x)*r**4 + ((1/2)*pi*r**2)*(((a+ybar+ySC))**2)

print(N(I1))
print(N(I2))
I = I1-I2

print(N(I))
