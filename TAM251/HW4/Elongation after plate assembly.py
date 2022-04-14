from sympy import *
from sympy import Matrix as Matrix
import numpy as np
#Certain application requires plates  and  to be attached to each other using glue, 
# as indicated below. During fabrication plate  was made  smaller than needed. 
# Plate  was placed in an oven to increase its length so that it would perfectly match the size of plate 
#The plates were then immediately glued together.
#Plate  has stiffness , plate  has stiffness  and .
#Determine the extensional strain  of plate  after plate  returns to its original temperature.

deltaM = 2 # mm
k1 = 44000 # N/mm
k2 = 12000 # N/mm
L = 2200 # mm

F = deltaM/(k1+k2)

d1 = F*k1
d2 = F*k2

epsilon1 = d1/(L-deltaM)
epsilon2 = d2/(L)

print(N(epsilon1))
print(N(epsilon2)) #smaller number is answer AND CHECK SIGN

#d1k1 = d2k2
#d1 + d2 = dm
#d1 + (k1/k2)*d1 = dm