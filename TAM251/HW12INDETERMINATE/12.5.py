#12.5
import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#HW12.5. Obtain the tension in the cable
# The cantilever beam  with length  has additional support from cable  with length . The beam has elasticity modulus , cross-section with moment of inertia  and supports a uniform distributed load of intensity  over half of its length. Before the load is applied, the cable is taut, but stress free. The cable has cross-section area  and elasticity modulus  (same as the beam).
# Determine the cable tension T.
#half dist LOAD tension cable at end

L = 8 # m
H = 2 # m
E = 219 # GPa
Iz = 53000000 # mm^4
w = 8 # kN/m
A = 205 # mm^2

thetaw = -w*1000*(L/2)**3/(6*E*Iz*10**-3)
yw = -w*1000*(L/2)**4/(8*E*Iz*10**-3) + L/2*thetaw

T = symbols('T')
yT = T*1000*L**3/(3*E*Iz*10**-3)
e1 = Eq(yT + yw, -T*1000*H/(E*10**9*A*10**-6))
sol = solve(e1,T)
print('T =', sol[0])

