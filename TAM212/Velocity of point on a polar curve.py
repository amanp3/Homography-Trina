from sympy import *
from sympy import Matrix as Matrix
import numpy as np

theta = symbols('theta')

r = 4 + 1*sin(-3*theta+2)

theta_final = -4
omega = -3


rdot = diff(r, theta) * omega

ver = rdot
vetheta = r*omega


vx = ver*cos(theta_final) - vetheta*sin(theta_final)
vy = ver*sin(theta_final) + vetheta*cos(theta_final)
vx = vx.subs(theta, theta_final)
vy = vy.subs(theta, theta_final)

print(N(vx) , N(vy))



