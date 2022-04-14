from sympy import *
from sympy import Matrix as Matrix
import numpy as np


m = 8
r = 2
g = 9.8
#vcf = 22
vc0 = 4
h = 26

vcf = symbols('vcf')

eq1 = Eq(.5*m*(vcf**2) + .5*m*(r**2)*((vcf/r)**2) + m*g*r, .5*m*(vc0**2) + .5*m*(r**2)*((vc0/r)**2) + m*g*h)

sol = solve((eq1), (vcf), dict = True)
print(sol)