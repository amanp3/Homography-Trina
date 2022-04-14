#12.6
import numpy as np
from sympy import *
import numpy as np

P = 56 # kN
L = 1942 # mm
delta = 2 # mm
E = 155 # GPa
Iz = 128079468 # mm^4

Ry = symbols('Ry')
Yp = -5*P*L**3/6/E/Iz
Yry = 8*Ry*L**3/3/E/Iz
eq1 = Eq(Yp + Yry, -1*delta)
soln = solve((eq1),('Ry'), dict= True)
print(soln)