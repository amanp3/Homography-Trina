from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#Rods  1 and  2 were supposed to fit exactly between the rigid walls at  and , 
# as indicated in the figure below. However, rod  was manufactured a small amount, ,
#  too long. A technician decides to lower the temperature of rod  by  so that he can 
# insert it in the space between  and . When rod  returns to its initial temperature, 
# the length of each rod is no longer the same as the original one, and the resulting 
# strain is often called "residual strain"".
#Rod  has Young modulus  and cross-sectional area . Rod  has Young modulus  and same 
# cross-sectional area . Rod  has an initial length .
#Determine the resulting "residual" normal strain  in rod 1 when .

E1 = 67 # GPa
E2 = 207 # GPa
A = 1764 # mm^2
L = 782 # mm
deltaM = 0.6 # mm

#d1+d2 =dm

F = symbols('F')

eq1 = Eq((F*L)/(E1*A) + (F*(L+deltaM))/(E2*A), deltaM)

sol = solve(eq1, F)

F = sol[0]

strain1 = ((F*L)/(E1*A))/L
strain2 = ((F*(L+deltaM))/(E2*A))/(L+deltaM)

print(N(-strain1))
print(N(-strain2))