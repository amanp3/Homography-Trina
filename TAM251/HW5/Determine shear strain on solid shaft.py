from sympy import *
from sympy import Matrix as Matrix
import numpy as np

#The solid circular shaft has length , diameter  and torsional stiffness .
#Determine the maximum shear strain in the shaft when the applied torque is .

L = 1774 # mm
d = 33 # mm
kt = 4 # kN.m
T = 1293 # N.m

phi = T/kt

gamma = (phi*(d/2))/L

print(gamma) #10**-3
