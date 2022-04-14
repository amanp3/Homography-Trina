import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A beam has the extruded cross section shown below, where .
#Determine the centroid position 
#, i.e. the signed distance from the -axis to  axis, where  is the centroidal axis of the cross section.

#q11 AMONG US CHARACTER 

t = 16 # mm
a = 78 # mm

A1 = 8*t*12*t
A2 = 6*t*2*t

y1 = 0
y2 = t+a


ybar1 = ((y1*A1-y2*A2))/(A1 - A2)
print(ybar1)

