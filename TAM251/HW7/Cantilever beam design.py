#The cantilever beam illustrated below is subject to an uniform distributed load with magnitude 
#  and a couple moment with magnitude . Assume . The beam cross section has dimensions , , , and 
# . The beam is made of a material with allowable tensile stress  and allowable compressive stress .
#q13
import numpy as np
from sympy import *
from sympy import Matrix as Matrix



a = 1873 # mm
b = 241 # mm
h = 140 # mm
t1 = 24 # mm
t2 = 23 # mm
sigmaT = 11 # MPa
sigmaC = 15 # MPa

y = ((h+t2)*b*(0.5*(h+t2)) - (h*(b-2*t1)*(0.5*h)))/((h+t2)*b - (b-2*t1)*h)

print(y)
iz1 = ((b)*(h+t2)**3)/12 + (b*(h+t2))*(y - 0.5*(h+t2))**2
iz2 = -1*((b-2*t1)*(h**3)*(1/12) + (b-2*t1)*h*(y - 0.5*h)**2)
iz = iz1 + iz2
print(iz*10**-6)

wc = (sigmaC*iz)/(1.5*y*a**2)
wt = (sigmaT*iz)/(1.5*(h+t2-y)*a**2)

print(wc, wt)

