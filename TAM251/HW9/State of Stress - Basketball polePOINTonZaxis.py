import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The basketball pole  is fixed at  and is subject to a force  as indicated below.
#The circular cross-section has outer diameter  and inner diameter . Assume , , ,  and .
#Determine the state of stress at point : evaluate the stresses (remember to use sign convention) and 
# draw the representative stress element.
#9.3

a = 648/1000
b = 1469/1000
L = 2938/1000
do = 87/1000
di = 47/1000
P = 1075
theta = 33

theta = theta*(pi/180)
A = pi*((do/2)**2 - (di/2)**2)
I = (pi/4)*(do/2)**4 -(pi/4)*(di/2)**4

Q = ((4*(do/2))/(3*pi)) * (.5*pi*((do/2)**2)) - ((4*(di/2))/(3*pi)) * (.5*pi*((di/2)**2))

Vy = P*sin(theta)
Fx = -1*P*cos(theta)
Mz = -1*(L-b)*P*sin(theta) - P*cos(theta)*a
My = 0
Mx = 0
sigmax = Fx/A + (My*(do/2)/I)
print(N(sigmax*10**-3))



tau = (Vy*Q)/(I*(do - di)) #why tau negative --> bc look which way shear is it is opposite of pos y direction
print(N(tau*10**-3))
#diagram top face tau in neg y
