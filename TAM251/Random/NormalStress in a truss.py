from sympy import *
from sympy import Matrix as Matrix
import numpy as np

theta = 0.6435
A = 3530 # mm^2
P = 26 # kN

F = P/sin(theta)

sigma = F/A * 10**3

print(-1*sigma/2)