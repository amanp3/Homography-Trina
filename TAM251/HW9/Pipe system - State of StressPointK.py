import numpy as np
from sympy import *
from sympy import Matrix as Matrix
#pointK is y axis

#9.7
a = 341
b = 235
c = 270
Pz = 379 
Py = 332 
p = 736
do = 88
di = 48

p = p/1000

Vy = Py
Vz = Pz

I = (pi/4)*(do/2)**4 - (pi/4)*(di/2)**4
Q = ((4*(do/2))/(3*pi))*(.5*pi*(do/2)**2)-((4*(di/2))/(3*pi))*(.5*pi*(di/2)**2)
J = (pi/2)*(do/2)**4 - (pi/2)*(di/2)**4


#print(Vy)
#print(Vz)

Tx = -1*c*Pz - Py*b
#print(Tx*10**-3)

My = -1*a*Pz
#print(My*10**-3)
Mz = -1*Py*a
#print(Mz*10**-3)


sigmax = (abs(Mz)*(do/2))/I + (p*(di/2))/(2*((do-di)/2))
print(N(sigmax))

sigmaz = (p*(di/2))/((do-di)/2)
print(N(sigmaz))

tauxz = (Pz*Q)/(I*(do-di)) - (abs(Tx)*(do/2))/J
print(N(tauxz))