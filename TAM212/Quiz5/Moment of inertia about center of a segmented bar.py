from sympy import *
import numpy as np

w = 2
l1 = 5
l2 = 6
l3 = 6
rho1 = 4
rho2 = 1
rho3 = 5

rect1mass = l1*w*rho1
rect2mass = l2*w*rho2
rect3mass = l3*w*rho3

ybar = (rect2mass*(l1+l2)/2 + rect3mass*(l1+l3 + 2*l2)/2) / (rect1mass + rect2mass + rect3mass)
I = (1/12)*(rect1mass*(w**2 + l1**2) + rect2mass*(w**2 + l2**2) + rect3mass*(w**2 + l3**2))
I+= rect1mass*ybar**2 + rect2mass*((l1+l2)/2 - ybar)**2 + rect3mass*((l1+l3+2*l2)/2 - ybar)**2
print(I)