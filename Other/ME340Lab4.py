import numpy as np
from sympy import *
from sympy import Matrix as Matrix

#timeStart = 0
#tr = 0
#tp = 2.2

#tr = tr - timeStart
#tp = tp - timeStart
#eq1 = Eq((pi - acos(zeta))/(wn*sqrt(1-zeta**2)), tr)
#eq2 = Eq(pi/(wn*(sqrt(1-zeta**2))), tp)


zeta, wn, m = symbols('zeta, wn, m')

ts2 = 1.7 #2% settling time
tp = 0.2

eq1 = Eq(ts2, 4/(zeta*wn))
eq2 = Eq(pi/(wn*(sqrt(1-zeta**2))), tp)

sol = solve((eq1,eq2), (zeta, wn), dict = True)
print(sol)






#eq3 = Eq(0.5, 2*pi*sqrt(m/384.62))

#sol2 = solve(eq3, m)
#print(sol2)


