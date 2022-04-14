from sympy import *
from sympy import Matrix as M
#vq = vp + w x rpq
#vs = vp + w x rps


vp = M([-12, 0, 0])
rpq = M([-8,15,0])
rps = M([15, 8, 0])

wz, vqy, vsx, vsy = symbols('w, vqy, vsx, vsy')

w = M([0,0,wz])
vq = M([0, vqy,0])
vs = M([vsx,vsy,0])

eq1 = Eq(vq, vp + w.cross(rpq))
eq2 = Eq(vs, vp + w.cross(rps))

soln = solve((eq1, eq2), (wz, vqy, vsx, vsy), dict = True)

print(soln)