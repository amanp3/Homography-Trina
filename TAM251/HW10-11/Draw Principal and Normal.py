import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#10.4Draw Principal and Maximum Stress Element

sx = -26
sy = 0
txy = -20

R = sqrt(((sx-sy)/2)**2 + (txy)**2)
savg = (sx+sy)/2

s1 = savg + R
s2 = savg - R

print(s1)
print(s2)

thetap = np.arctan2((2*txy), (sx-sy))/2
print(N(thetap*(180/pi)))


tmax = R

print(tmax)

#thetas = thetap*(180/pi) -45 
#print(N(thetas))
thetas = np.arctan2((-1*(sx-sy)),(2*txy))/2
print(N(thetas*(180/pi)))

print(savg)#if neg then max element sigma arrows go compression


#The state of stress at a point on a body is given by the following stress components: sigma1 sigma2
#1) Determine the principal stresses  and .
#2) Sketch the principal stress element, defined by the rotation thetap1.
#3) Determine the absolute value of the maximum shear stress .
#4) Sketch the maximum shear stress element, defined by the rotation thetas.
