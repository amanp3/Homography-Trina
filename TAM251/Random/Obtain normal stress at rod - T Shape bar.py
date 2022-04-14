from sympy import *
from sympy import Matrix as Matrix
import numpy as np


a = 270 # mm
b = 292 # mm
c = 166 # mm
d = 341 # mm
e = 237 # mm
P1 = 50 # kN
P2 = 61 # kN
theta = 35 # degrees
dab = 25 # mm

theta = theta*(pi/180)
#P = P1+P2

M = P1*b +P2*(c+b)

f = symbols('f')


#eq1 = Eq(cx - f*cos(theta))
#eq2 = Eq(cy - P - f*sin(theta))
eq1 = Eq(-M + (e+d+a*sin(theta))*f*cos(theta), 0)

#sol_dict = solve((eq1,eq2,eq3), (f, cx, cy))
#print(f'f = {sol_dict[f]}')
#print(f'cx = {sol_dict[cx]}')
#print(f'cy = {sol_dict[cy]}')

#F = {sol_dict[f]}
#Cx = {sol_dict[cx]}
#Cy = {sol_dict[cy]}


#F = N(F)

#print(F)

sol = solve(eq1, f, dict = True)
print(sol)

#stress = F/(pi*(dab/2)**2)

#f goes in here
print(N(21269/((135*sin(7*pi/36) + 289)*cos(7*pi/36))/(3.1416*(dab/2)**2)))
print('Force:')
print(N(21269/((135*sin(7*pi/36) + 289)*cos(7*pi/36))))