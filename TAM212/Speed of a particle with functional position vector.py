from sympy import *
from sympy import Matrix as Matrix
import numpy as np

t = symbols('t')

tf = 1
rx = -3*sin(-1*t)
ry = 1*sin(-3*t)
rz = 1*exp(-1*t)

v = sqrt(diff(rx)**2 + diff(ry)**2 + diff(rz)**2)

v = v.subs(t, tf)
print(v.evalf())