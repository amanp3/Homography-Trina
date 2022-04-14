from sympy import *
from sympy import Matrix as Matrix
import numpy as np

dBrass = 24 # mm
dSteel = 15 # mm
Ls = 750 # mm
Lb = 795 # mm
Es = 157 # GPa
Eb = 93 # GPa
P = 48 # kN

F1, F2 = symbols('F1,F2')
Ab = (pi/4)*dBrass**2
As = (pi/4)*dSteel**2

eq1 = Eq((F1*Lb)/(Eb*Ab), (F2*Ls)/(Es*As))
eq2 = Eq(F2, P - 2*F1)

sol = solve((eq1,eq2), (F1, F2))
print(sol)

#F1/Ab
#F2/As

print(N((571392/32129)/Ab)*10**3)
print(N((399408/32129)/As)*10**3) #MPa