import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A load  is applied to the top of the composite support column while a load  
# is applied to the junction between the bottom and middle columns, as shown in the the figure below.
#  All collumns are made of the same material with elastic modulus .
#Find the MAGNITUDE of the displacement  of point D at the top of the column. Use:

P = 87 #kips
E = 29 * 10**3 #ksi
L1 = 18 
L2 = 18 #in
L3 = 18/3 

A3 = 96
A2 = (3/2)*A3
A1 = 3*A3


d = -(P*L3)/(E*A3) - (P*L2)/(E*A2) + (P*L1)/(E*A1)
print(d*10**3) #magnitude