#vc = vb + w2 x rbc
#vb = va + w1 x rab

from sympy import *
from sympy import Matrix as M

w1 = M([0,0, -142])
rab = M([2.4575, 1.721, 0])
va = M([0,0,0])
rbc = M([6.99, -1.721, 0])

wz, vcx, vbx, vby = symbols('w2, vcx, vbx, vby')

w2 = M([0,0, wz])
vc = M([vcx, 0, 0])
vb = M([vbx, vby,0])


eq1 = Eq(vc, vb + w2.cross(rbc))
eq2 = Eq(vb, va + w1.cross(rab))

sol = solve((eq1, eq2), (wz, vcx, vbx, vby), dict = True)

print(sol)