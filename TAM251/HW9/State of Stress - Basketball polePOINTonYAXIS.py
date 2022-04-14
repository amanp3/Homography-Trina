import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The basketball pole  is fixed at  and is subject to a force  as indicated below.
#The circular cross-section has outer diameter  and inner diameter . Assume , , ,  and .
#Determine the state of stress at point : evaluate the stresses (remember to use sign convention) and 
# draw the representative stress element.

#9.4

a = 673
b = 899
L = 2997
do = 88
di = 48
P = 998
theta = 37


theta = theta*(pi/180)
A = pi*((do/2)**2 - (di/2)**2)
I = (pi/4)*(do/2)**4 -(pi/4)*(di/2)**4

Q = ((4*(do/2))/(3*pi)) * (.5*pi*((do/2)**2)) - ((4*(di/2))/(3*pi)) * (.5*pi*((di/2)**2))

Vy = P*sin(theta)
Fx = -1*P*cos(theta)
Mz = -1*(L-b)*P*sin(theta) - P*cos(theta)*a
Fx = abs(Fx)
Mz = abs(Mz)
My = 0
Mx = 0

sigmax = -1*Fx/A - (Mz/I)*(do/2)

print(N(sigmax))




