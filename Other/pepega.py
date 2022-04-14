import numpy as np
from sympy import *
from sympy import Matrix as Matrix

t1 = 2.38
t3 = 2.69

x1 = 0.09
x3 = 0.01

zeta, wn = symbols('zeta, wn')

eq1 = Eq((x1/x3), exp((2*pi*zeta)/ (sqrt(1-zeta**2))))
eq2 = Eq(t3-t1, (2*pi)/(wn*(1-zeta**2)))



sol = solve((eq1,eq2), (zeta, wn), dict = True)
print(sol)

