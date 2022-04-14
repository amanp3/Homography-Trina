from sympy import *
from sympy import Matrix as M

#va = vp + w1 x rpa
#va = vq + w2 x rqa

rpa = M([2,3,0])
vp = M([-2,1,0])
rqa = M([-2,1,0])
vq = M([-3,2,0])

vax, vay, w1z, w2z = symbols('vax, vay, w1z, w2z')
va = M([vax, vay, 0])
w1 = M([0,0,w1z])
w2 = M([0,0,w2z])

eq1 = Eq(va, vp + w1.cross(rpa))
eq2 = Eq(va, vq + w2.cross(rqa))

soln = solve((eq1, eq2), (vax, vay, w1z, w2z), dict = True)

print(soln)