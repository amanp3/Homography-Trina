import numpy as np
#A block with shear modulus  is bonded to a fixed based and to a horizontal 
# rigid plate to which a force  is applied. Assume ,  and .
#Determine the shear stress "tau" in the bonded interface.
#Determine the horizontal displacement "u" of the rigid plate.

G = 4000 # ksi
P = 605 # kips
Lo = 16 # in
b = 5 # in
t = 4 # in



tau =  P/(Lo*b)
print(tau) #ksi
gamma = tau/G

#u = gamma*t
print(gamma*t) #in