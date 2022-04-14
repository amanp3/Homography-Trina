import numpy as np
#v=w x r
#vp = vc + w x r_cp
#ap = ac + alpha x rcp + w x (w x rcp)

A = np.array([-1, -3, -1])
B = np.array([5, 1, 1])

#print(np.cross(A,B))


#vq = vp + w x rpq
vp = np.array([3,-2,0])
w = np.array([0, 0, 1])
rpq = np.array([-5, -4, 0])

vq = vp + np.cross(w, rpq)

#print(vq)

#aq = ap + alpha x rpq + w x (w x rpq)
ap = np.array([1,-2,0])
alpha = np.array([0,0,-1])
w = np.array([0,0,0])
rpq = np.array([-5,-2,0])

aq = ap + np.cross(alpha, rpq) + np.cross(w, np.cross(w, rpq))
#print(aq)

from sympy import *
from sympy import Matrix as M


#v = w x r
vy, wz = symbols('vy, wz')
v = M([-4.8, vy, 0])
w = M([0,0,wz])

r = M([0.4285836, 0.257519, 0])

eq1 = Eq(v, w.cross(r))

sol = solve((eq1),(vy,wz), dict = True)
#print(sol)

#v = w x r
