from sympy import *
from sympy import Matrix as Matrix
import numpy as np

t = symbols('t')

vx = -2*t**2
vy = t**2 - t
tf = 2

rx = integrate(vx, (t, 0, tf))

ry = integrate(vy, (t, 0, tf))

r = sqrt(rx**2 + ry**2)

print(r.evalf())