#12.4
import numpy as np
from sympy import *

#Beam  has length , elasticity modulus , cross-section with moment of inertia . 
# The beam is fixed at  and suported by a roller at . 
# The beam is subjected to a uniform distributed load of intensity  over half of its length 
# as shown in the figure below.

#Wall mounted with half lenghth dist load then roller support at end

L = 5 # m
w = 6 # kN/m
Iz = 1 # mm^4


w=w*1000
E=E*10**9
P = symbols('P')

#deflection = 0
eq1 = Eq(0, P*(L**3)/(3*E*Iz) + (-w*((L/2)**4)/(8*E*Iz))+ (-w*((L/2)**3)/(6*E*Iz))*(L/2))
#pretty straightforward, hard part is multiply deflection of distributed load by thetadistance(linear displacement after load)
#theta = 0
#eq2 = Eq(0,P*(L2)/(2EIz) + -w((L/2)**3)/(6E*Iz))

soln = solve((eq1), ('P'), dict= True)

print(soln) #divide by 1000 for N and it asks for MAGNITUDE, ONLY EQ1 works because roller, only deflection is controlled.   