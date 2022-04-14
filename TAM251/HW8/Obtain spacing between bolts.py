#three off set rectangles
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#8.7

h = 171 # mm
t = 42 # mm
d = 13 # mm
taub = 2 # MPa
V = 3 # kN


A = 3*h*t
ybar = ((h/2)*h*t + h*h*t + (h/2)*h*t)/(3*h*t)

Q = (ybar - h/2)*(h*t)
print(Q)

print(ybar)
I1 = (1/12)*(t*h**3) + (t*h)*(ybar-(h/2))**2 
I2 = (1/12)*(t*h**3) + (t*h)*(h-ybar)**2
I3 = (1/12)*(t*h**3) + (t*h)*(ybar-(h/2))**2 

I = I1+I2+I3
print(I)
q = (V*Q)/I
print(q)
Anail = (pi*(d/2)**2)

dS = (taub*Anail)/q

print(N(dS*10**-3)) #mm