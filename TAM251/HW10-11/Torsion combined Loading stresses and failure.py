import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#TORSION VARIANT
#The compressed-air tank has an inner radius  and uniform wall thickness . 
# The gage pressure inside the tank is  and the torque  is applied at the end cap. Use , ,  and .
#Obtain the state of plane stress at point  in the  coordinate system:
#Determine the principal stresses  and  at point :
#Determine the principal plane defined by the rotation :
#Determine the maximum in-plane shear stress :
#Determine the factor of safety against yielding of the material at point  
# on the basis of the Tresca criterion. The material has yielding stress .

#10.8
p = 1373 # kPa
T = 1 # kN.m
t = 11 # mm
r = 209 # mm
sigmaY = 210 # MPa

p = p *10**3
T = T*10**3
t = t*10**-3
r = r*10**-3
sigmaY = sigmaY *10**6

sx = (p*r)/(2*t)
sy = (p*r)/t
txy = -1*(T*(r+t))/((pi/2)*(r+t)**4 - (pi/2)*(r**4))

print(N(sx*10**-6))
print(N(sy*10**-6))
print(N(txy*10**-6))

print("  ")
sx = float(sx)
sy = float(sy)
txy = float(-1*txy)

savg = (sx + sy)/2
a1 = (sx-sy)/2
a2 = txy
R = sqrt(a1**2 + a2**2)

s1 = savg + R
s2 = savg - R

print(N(s1*10**-6))
print(N(s2*10**-6))

thetap = np.arctan2(2*txy, sx-sy)/2
print(N(-thetap * (180/pi)))
tmax = R
print(N(tmax*10**-6))

#smaller of sigmaY/(s1 or s2)
print(" ")
print(N(sigmaY/abs(s1)))
print(N(sigmaY/abs(s2)))