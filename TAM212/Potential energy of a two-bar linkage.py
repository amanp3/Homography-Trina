from sympy import *
from sympy import Matrix as Matrix
import numpy as np

m1 = 6
m2 = 4
rOP = Matrix([-1,3,0])
rPQ = Matrix([2,1,0])

g = 9.8
V = m1*g*(rOP[1]/2) + m2*g*(rOP[1] + rPQ[1]/2)
print(V)