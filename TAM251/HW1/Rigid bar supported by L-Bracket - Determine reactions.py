import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#The rigid bars  and  are pinned to a wall at  and , 
# respectively, and pinned together at . Bar  is subjected to a 
# triangular distributed load with .
#Determine the magnitude of the average shear stress at pin , . 
# Consider a pin in single shear with cross-sectional area .

a = 668 # mm
b = 84 # mm
c = 501 # mm
d = 167 # mm
L = 1671 # mm
w = 5 # kN/m
Ac = 57 # mm^2


a = a/1000
b=b/1000
c=c/1000
d = d/1000
L = L/1000
w = w*10**3
Ac = Ac*10**-6

P = .5*L*w
print(P)
Ax, Bx, Ay, By = symbols('Ax, Bx, Ay, By')

eq1 = Eq(Ax + Bx, 0)
eq2 = Eq(Ay+By-P, 0)
eq3 = Eq(-P*(1/3)*L+ By*(a+b),0)
eq4 = Eq(-Bx*(c+d)+By*(a+b),0)

sol = solve((eq1,eq2,eq3,eq4), (Ax, Bx, Ay, By), dict = True)
print(sol)

#uncomment and replace with real values outputtd in the code
#Bx = 3483.3345
#By = 3094.23869

V = sqrt(Bx**2 + By**2)

tau = V/Ac
print(tau*10**-6)



