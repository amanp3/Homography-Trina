import numpy as np
from sympy import *
from sympy import Matrix as Matrix

L = 214 # mm
a = 211 # mm
theta = 0.5 # degrees
alpha = 20 # degrees

theta = theta * np.pi/180
alpha = alpha * np.pi/180

b = a * theta #a*np.tan(theta) small angle
Lfinal = L + b*np.sin(alpha)
E = (Lfinal-L)/L

print(E*10**3)

