import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#When a force  is applied to the end of the rigid lever , 
# cable  develops a normal strain  Use  and .
#Determine the corresponding rotation  in degrees of the lever .

a = 12 # in
b = 8 # in
strain = 0.004

alpha = atan(b/a)

dL = strain*sqrt(a**2 + b**2)

h = dL/(cos(alpha))

theta = h/b

print(N(theta*(180/pi)))