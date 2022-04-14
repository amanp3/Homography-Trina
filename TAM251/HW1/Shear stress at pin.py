import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#A cable and pulley system at  is used to support the rigid bar  
# as indicated below. Bar  is pin-connected at . A box with weight  hangs from point .
#Determine the magnitude of the shear stress at pin  for the equilibrium configuration where . 
# Assume the pin is in  shear and has diameter .

W = 3 # kN
a = 4 # m
b = 6 # m
d = 16 # mm
theta = 60 # degrees

W = W*10**3
d = d*10**-3
theta = theta*(pi/180)


Ay, T = symbols('Ay, T')

eq1 = Eq(a*T*sin(theta)-W*sin(theta)*(a+b),0)
sol = solve(eq1, T)
T = sol[0]

eq2 = Eq(Ay + T-W,0)
sol2 = solve(eq2, Ay)
Ay = sol2[0]

A = pi*(d/2)**2

#uncomment last 2 lines with proper double shear/single shear

#divide tau by 2 for double shear
#tau = (Ay/A) /2 #double shear
#print(N(tau*10**-6))