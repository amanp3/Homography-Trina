from sympy import *
from sympy import Matrix as M
#vq = vp + w2 x rpq
#vp = vo + w1 x rop

vq = M([3,-4,0])
rpq = M([-2,0,0])
rop = M([-2,3,0])
vo = M([0,0,0])

w1z, w2z, vpx, vpy = symbols('w1z, w2z, vpx, vpy')

w1 = M([0,0,w1z])
w2 = M([0,0,w2z])
vp = M([vpx,vpy,0])

eq1 = Eq(vq, vp + w2.cross(rpq))
eq2 = Eq(vp, vo + w1.cross(rop))

soln = solve((eq1, eq2), (vpx, vpy, w1z, w2z), dict = True)

print(soln)