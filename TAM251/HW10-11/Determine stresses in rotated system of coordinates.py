import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#10.6
#The state of plane stress at a point on a body is represented by the element below.
#Determine the equivalent state of plane stress on an element at the same point that is rotated by . 
# Remember that a negative sign indicates a clockwise rotation and a positive sign indicates 
# a counter-clockwise rotation.
#Please note: occasionally the diagram above will not correctly render 
# all of the stress component directions. Please use , , and  for the calculations below.

sx = -17 # MPa
sy = 22 # MPa
txy = 20 # MPa
theta = 34

theta = theta*(pi/180)

savg = (sx+sy)/2
s2 = (sx-sy)/2
s3 = cos(2*theta)
s4 = sin(2*theta)


sxN =savg + s2*s3 + txy*s4
print(N(sxN))
syN = savg - s2*s3 - txy*s4
print(N(syN))
txyN = -s2*s4 + txy*s3
print(N(txyN))
