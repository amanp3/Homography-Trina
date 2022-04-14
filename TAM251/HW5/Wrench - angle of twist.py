from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#A socket wrench has a handle of length , a shaft of length , and a diameter . 
# It is made of a material with shear modulus  and allowable shear stress .
#Determine the maximum allowable applied force .
#Determine the magnitude of the corresponding twist angle of the shaft.

a = 1310 # mm
b = 1661 # mm
d = 50 # mm
G = 62 # GPa
tall = 20 # MPa

J = (pi/2)*((d/2)**4)

P = (2*tall*J)/(a*d)
print(N(P))

T = P*a

phi = (T*b)/(G*J)
print(N(phi*10**-3))