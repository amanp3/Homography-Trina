#10.10
import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The cantilever beam of length 3L is subject to concentrated loads  and  and has the thin-walled cross-section illustrated below. 
# The cross-section has uniform thickness  and moment of inertia with respect to the centroidal -axis given by . Use ,  and .
#Determine the numerical value of the shear force and bending moment at a cross-section located at . 
# Remember to use the sign conventions for shear forces and bending moments.
#For the cross-section located at , 
# determine the state of plane stress at point  (i.e., y = 5t) in the  coordinate system.
# Determine the principal stresses  and  at point H:
#Determine the maximum in-plane shear stress  at point H :
#What is the value of the corresponding normal stress when the element is oriented so that the shear stress is maximum?
#Show the principal stresses in a properly oriented element, defined by the rotation . 
# The angle  is defined by the angle between the -axis and the plane where the normal stress corresponds to . 
# Give your answer within the range . Use the "drawing element" in the left side of the picture below.
# Draw a properly oriented stress element to show the shear and normal stresses 
# on the planes of maximum in-plane shear stress, defined by the rotation . 
# The angle  is defined by the angle between the -axis and a plane where the shear stress corresponds to . 
# Give your answer within the range . Use the "drawing element" in the right side of the picture below.

t = 5 * 10**-3 #m
L = 112 *10**-3 #m
P = 5 *10**3 #kN
x = 38 *10**-3 #m

I = 3140*t**4

V = P
M = P*(2*L-x) - 2*P*(3*L-x)
print(N(V*10**-3))
print(N(M))

sx = (abs(M)*(5*t))/I
print(N(sx*10**-6))
sy = 0
print(N(sy*10**-6))
##ybar = (25*t**3 + (5*t - (t/2))*(10*t**2))/(10*t**2 + 10*t**2)
Q1 = (7.5*t)*12*t*5*t
Q2 = 7*t*4*t*10*t
Q = Q1 - Q2
txy = -1*(V*Q)/(I*2*t)
print(N(txy*10**-6))



savg = (sx + sy)/2
a1 = (sx - sy)/2 
a2 = txy
R = sqrt(a1**2 + a2**2)

s1 = savg + R
s2 = savg - R

print(N(s1*10**-6))
print(N(s2*10**-6))

print(N(R))
print(N(savg))

thetap = np.arctan2((2*txy), (sx-sy))/2
print(N(thetap*(180/pi)))

thetas = np.arctan2((-1*(sx-sy)),(2*txy))/2
print(N(thetas*(180/pi)))