from sympy import *
from sympy import Matrix as Matrix
import numpy as np

theta = symbols('theta')

r = 3 + 2*cos(3*theta+3)

theta_final = 1
omega = -2
alpha = -2

rdot = diff(r, theta) * omega
#print(rdot)

rdouble = diff(rdot, theta) * omega + rdot*alpha / omega

ar = rdouble - r* (omega**2)
atheta = r*alpha + 2*rdot*omega

ax = ar*cos(theta_final) - atheta*sin(theta_final)
ay = ar*sin(theta_final) + atheta*cos(theta_final)
ax = ax.subs(theta, theta_final)
ay = ay.subs(theta, theta_final)

print((ax) , (ay))