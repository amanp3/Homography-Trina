from sympy import *
from sympy import Matrix as M

#vq = vp + w x rpq


vp = M([2,1,0]) #
rpq = M([-2,2,0]) #

wz, v = symbols('wz, v')

vq = M([v,v,0]) #edit based on angle
w = M([0,0,wz]) #

eq1 = Eq(vq, vp + w.cross(rpq))

soln = solve((eq1), (v, wz), dict = True)

print(soln)