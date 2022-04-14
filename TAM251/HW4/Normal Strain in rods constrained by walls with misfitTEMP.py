from sympy import *
from sympy import Matrix as Matrix
import numpy as np

delta = 0.02 # in
L = 13 # in
E = 28000 # ksi
alpha = 0.000005 # /degrees F
A = 2 # in^2
dT = -97 # degrees F


sigmatemp = alpha * E * dT
sigman = (delta * E) / L
#print(sigmatemp)
#print(sigman)

print(sigmatemp + sigman) #ksi

#At its initial temperature, the bar is too long by a distance of 
#  to fit into the gap between the rigid walls, which are separated by a distance . 
# In order to make it fit tightly, the bar is cooled to a very low temperature so that 
# it shrinks enough to fit easily into the gap. After it is fit in the gap, the temperature 
# of the bar is raised to a temperature  below the initial temperature and the bar fits tight between the walls.

#The bar has elastic modulus , thermal expansion coefficient  and cross-sectional area .
#What is the stress  in the bar at this temperature ? Considering , the initial length may be approximated 
#as  in your calculations for simplification.