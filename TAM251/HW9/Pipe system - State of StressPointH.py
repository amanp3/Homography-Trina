#9.6
import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#pointH is z axis

a = 369
b = 242
c = 266
Pz = 426 
Py = 415 
p = 710
do = 87
di = 67

I = (pi/4)*((do/2)**4) - (pi/4)*((di/2)**4)
Q = ((4*(do/2))/(3*pi)) * (.5*pi*((do/2)**2)) - ((4*(di/2))/(3*pi)) * (.5*pi*((di/2)**2))
J = (pi/2)*(do/2)**4 - (pi/2)*(di/2)**4

Vy = Py
Vz = Pz

#print(Vy)
#print(Vz)

Tx = -1*c*Pz - Py*b
#print(Tx*10**-3)

My = -1*a*Pz
#print(My*10**-3)
Mz = -1*Py*a
#print(Mz*10**-3)

sigmax = (abs(My)/I)*(do/2)


sigmaa = ((p/1000)*(di/2))/((do-di))

sigmaxTotal = -sigmax + sigmaa
print(N(sigmaxTotal))


sigmah = ((p/1000)*(di/2))/((do-di)/2)
print(N(sigmah))#y


tauxy = (Vy*Q)/(I*(do-di))
tauMx = (Tx*(do/2))/(J)

print(N(-tauxy-tauMx))