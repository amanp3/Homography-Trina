#12.2
import numpy as np
from sympy import *
#Beam  has length , elasticity modulus , cross-section with moment of inertia  and is fixed at both ends  and . 
# The beam is subjected to a uniform distributed load of intensity  over half of its length.
#wall on both sides dist load for fisrt half

L = 8 # m
E = 151 # GPa
Iz = 0.000043 # m^4
w = 9 # kN/m


w=w*1000
E=E*10**9
P,M = symbols('P,M')

#deflection = 0
eq1 = Eq(0, P*(L**3)/(3*E*Iz) + M*(L**2)/(2*E*Iz) + (-w*((L/2)**4)/(8*E*Iz))+ (-w*((L/2)**3)/(6*E*Iz))*(L/2))
 #pretty straightforward, hard part is multiply deflection of distributed load by thetadistance(linear displacement after load)
#theta = 0
eq2 = Eq(0,P*(L**2)/(2*E*Iz) + M*L/(E*Iz) + -w*((L/2)**3)/(6*E*Iz))

soln = solve((eq1,eq2), ('P,M'), dict= True)

print(soln) #divide by 1000 for kN and it asks for MAGNITUDE