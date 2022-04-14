from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m = 3
v0 = 9
h = 16
vf = 8

W  = .5*m*vf**2 - .5*m*v0**2 - m*9.8*h
print(W)