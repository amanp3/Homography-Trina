#aq = ap + alpha x rpq + w x (w x rpq)

from sympy import *
from sympy import Matrix as M

w = M([0,0,-2])
alpha = M([0,0,2])

rpq = M([5,2,0])
ap = M([5, 3, 0])

aqx, aqy = symbols('aqx, aqy')
aq = M([aqx, aqy, 0])

eq1 = Eq(aq, ap + alpha.cross(rpq) + w.cross(w.cross(rpq)))

sol = solve((eq1), (aqx, aqy), dict = True)
print(sol)