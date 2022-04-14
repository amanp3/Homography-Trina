from sympy import *
from sympy import Matrix as Matrix
import numpy as np
#4.2
#The rigid beam  is supported by a smooth pin , two rods at points  and  and is 
# subjected to a load  as illustrated below. The inclined rod  has stiffness , length  and inclination . 
# The vertical rod  has stiffness  and the same length . Neglect the weight of the beam  
# and assume that when  the rigid bar is in the 
# horizontal position and the rods are stress-free. Assume small rotations.
#Determine the change in length of rod2 , , when . Remember the sign convention for positive and negative length changes

k1 = 250 # N/mm
k2 = 191 # N/mm
L = 200 # mm
theta = 32 # degrees
P = 20 # N

theta = theta *(pi/180)

d2 = symbols('d2')

#d2 = d1*cos(theta)

eq1 = Eq(P*(L/2) - d2*k2*L - d2*k1*cos(theta)*cos(theta)*L,0)

sol = solve((eq1), (d2))

print(sol[0]) #mm

#print(N(cos(theta)*sol[0]))
