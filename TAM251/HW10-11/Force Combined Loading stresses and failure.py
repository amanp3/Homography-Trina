import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#FORCE ONE
#The compressed-air tank has an inner radius  and uniform wall thickness . 
# The gage pressure inside the tank is  and the centric axial load  is applied at the end cap. Use , ,  and .
#Obtain the state of plane stress at point  in the  coordinate system:
#Determine the principal stresses  and  at point :
#Determine the principal plane defined by the rotation :
#Determine the factor of safety against yielding of the material at point  
# on the basis of the Von-Mises criterion. The material has yielding stress .

#10.7
p = 1369 # kPa
F = 10 # kN
t = 18 # mm
r = 360 # mm
sigmaY = 215 # MPa


p= p*10**3
F = F*10**3
t = t*10**-3
r = r*10**-3
sigmaY = sigmaY*10**6

sx = F/((pi*(r+t)**2) - (pi*(r**2))) + (p*r)/(2*t)
sx = float(sx)
print(N(sx*10**-6))

sy = (p*r)/t
sy = float(sy)
print(N(sy*10**-6))

txy = 0
print(N(txy*10**-6))


savg = (sx + sy)/2
a1 = (sx - sy)/2 
a2 = txy
R = sqrt(a1**2 + a2**2)

s1 = savg + R
s2 = savg - R

print(N(s1*10**-6))
print(N(s2*10**-6))

thetap = np.arctan2((2*txy), (sx-sy))/2
print(N(thetap*(180/pi)))

#vonMises
vM = (s1**2 - (s1*s2)+ s2**2)**.5
print(N(sigmaY/vM))

