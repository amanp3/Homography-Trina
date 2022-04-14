
import numpy as np
#Beam  has length , elasticity modulus , cross-section with moment of inertia  and is supported by a rigid pin at  
# and rigid rollers at  and . 
# The beam is subjected to a uniform distributed load of intensity  over its entire length.
#pin on left roller in middle and other end with dIst load over whole thing

L = 8 # m
E = 201 # GPa
Iz = 0.000046 # m^4
w = 12 # kN/m


F = w*L
RB = (5/8)*F

print(RB)
