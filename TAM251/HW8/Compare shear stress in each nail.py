import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#Nails, each having a total shear strength of , are used in a beam that can be constructed either as in Case 1 or as in Case 2. If the nails are spaced at . Each board has the cross-section dimensions  and . The nails have diameter .
#Determine the moment of inertia  of the cross section.
#Determine the largest vertical shear that can be supported in each case so that the fasteners will not fail.
#8.10

b = 46 # in
t = 4 # in
d = 0.78 # in
deltaS = 44 # in
Vmax = 3 # lb

I = (1/12)*b*(2*t+b)**3 - (1/6)*((b-t)/2)*b**3

print(N(I)*10**-3)

Q1 = (b/2 + t/2)*(b*t)

V1 = (Vmax*I)/(deltaS*Q1)
print(N(V1))

Q2 = (b/2 + t/2)*((b-t)/2)*t

V2 = (Vmax*I)/(deltaS*Q2)
print(N(V2))