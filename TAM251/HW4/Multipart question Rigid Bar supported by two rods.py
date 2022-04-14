from sympy import *
from sympy import Matrix as Matrix
import numpy as np

h = 104 # mm
b = 113 # mm
d = 26 # mm
E1 = 174 # MPa
E2 = 231 # MPa
W = 95 # N

#E1 = E1 * 10**6
#E2 = E2 * 10**6

theta1 = atan(h/b)
theta2 = atan(h/(2*b))
#print(theta1)
#print(theta2)


ratiod1d2 = (sin(theta1)/(2*sin(theta2)))

print(N(ratiod1d2))

A = (pi/4)*d**2

L1 = sqrt(h**2 + b**2)
L2 = sqrt(h**2+(2*b)**2)

f1 = L1/(E1*A)
f2 = L2/(E2*A)

print(N(f1))
print(N(f2))

ratioF1F2 = ratiod1d2*(f2/f1)

print(N(ratioF1F2))

F2 = symbols('F2')

F1 = ratioF1F2*F2

eq1 = Eq(b*F1*sin(theta1) - b *(W/2) + F2*2*b*sin(theta2) - 2*b*(W/2), 0)

sol = solve((eq1),(F2))


print(N((sol[0]*ratioF1F2)/A))
print(N(sol[0]/A))




