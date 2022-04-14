#vp = vo + w x rop
from sympy import *
from sympy import Matrix as M

rop = M([-4,14,0])

w = M([0, 0, 0.7])

vo = M([0,0,0])



vpx, vpy = symbols('vpx, vpy')
vp = M([vpx,vpy,0])


eq1 = Eq(vp, vo + w.cross(rop))

sol = solve((eq1), (vpx, vpy), dict = True)

print(sol)