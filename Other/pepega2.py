import numpy as np
from sympy import *
from sympy import Matrix as Matrix

zeta, wn = symbols('zeta, wn')

Mp = 0.538
tp = 0.24

eq1 = Eq(Mp, exp((-1*pi*zeta)/(sqrt(1-zeta**2))))
eq2 = Eq(pi/(wn*(sqrt(1-zeta**2))), tp)

sol = solve((eq1,eq2), (zeta, wn), dict = True)
print(sol)