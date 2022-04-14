#A particle  starts at time  at the position
 
#The velocity 
#of the particle is written in the polar basis associated with its current position, and is:
#In the above expression,  is in seconds.

#What is the position of  at ?

import sympy
import numpy as np

t = sympy.symbols('t')

x = -3
y = -3
tf = 4

vr = 0
vtheta = 3*2.718281828**(-3*t)

r0 = np.sqrt(x**2+y**2)

r = r0 + sympy.integrate(vr,t)


theta0 = np.arctan(y/x)
theta = theta0 + sympy.integrate(vtheta / r , (t,0,tf))

r = sympy.N(r.subs(t, tf))
theta = sympy.N(theta)

rfinal = r*np.array([sympy.cos(theta), sympy.sin(theta)])
print(rfinal)

