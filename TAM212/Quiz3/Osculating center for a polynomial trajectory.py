import numpy as np
import sympy

t = sympy.symbols('t')
rx = 3* t**2 - 3*t - 3
ry = -2*t
t0 = 3

vx = sympy.diff(rx,t)
vy = sympy.diff(ry,t)
ax = sympy.diff(vx,t)
ay = sympy.diff(vy,t)

x = sympy.N(rx.subs(t, t0))
y = sympy.N(ry.subs(t, t0))
r = np.array([x,y])
vx = sympy.N(vx.subs(t, t0))
vy = sympy.N(vy.subs(t, t0))
v = np.array([vx, vy])
vmag = sympy.sqrt(vx**2 +vy**2)
ax = sympy.N(ax.subs(t, t0))
ay = sympy.N(ay.subs(t, t0))
a = np.array([ax, ay])

at = a - (np.dot(a,v)/vmag**2)*v

atmag = sympy.sqrt(at[0]**2 + at[1]**2)

en = at/atmag


rho = vmag**2/atmag
print(rho)
rfinal = r + rho*en

print(rfinal)












#input r v a as vectors at time t
#r = np.array([-3, -14, 0])
#v = np.array([2, -12, 0])
#a = np.array([2, -6, 0])

#unit_binormal = (np.cross(v, a))/(np.linalg.norm(np.cross(v, a)))
#unit_tangent = (v)/np.linalg.norm(v)
#unit_normal = np.cross(unit_binormal, unit_tangent)

#write y as a function of x (x and y are components of r equation)
#find y_prime and y_double_prime and plug in t
#y_prime = -1.5
#y_double_prime = -0.02778

#rho = ((1 + y_prime**2)**(3/2))/(y_double_prime)

#print(unit_normal)
#print(rho)

#ans = r + rho*unit_normal
#print(ans)