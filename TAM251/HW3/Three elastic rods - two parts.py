import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#Three circular elastic rods support the rigid bar  as indicated below. 
# Rod  has stiffness  and rods  and  have stiffness . 
# The bottom end of rods  and  are fixed, i.e.,  and . The force  is applied at point .
#Determine the magnitude of the vertical displacement of the rigid bar, :
#Determine the magnitude of the displacement of point , :

k1 = 1000000 # kN/m
k2 = 400000 # kN/m
P = 39 # kN

k1 = k1*10**3
k2 = k2*10**3
P = P*10**3

db = P/(2*k2)

print(N(db*10**3)) #mm

dc = db + P/k1
print(N(dc*10**3)) #mm