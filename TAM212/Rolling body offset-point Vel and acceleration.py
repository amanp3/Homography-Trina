from sympy import *
from sympy import Matrix as M
import numpy as np


#vQ = M([7,-7,0])

#r = 3
#w = -vQ[0]/r

#r = -vQ[0]/w
#print(w)
#print(r)

#accel check photos

#find alpha with R
#r = 3
#aQ = [-10,4, 0]

#aQ = np.array(aQ)
#rQC = M([r,0,0])
#A = np.array([[-rQC[0], -rQC[1]+r], [rQC[1], rQC[0]]])
#b= aQ.transpose()

#print(A)
#print(b)
#rref A and b, omega = sqrt(first), alpha = second


#
omega = [0, 0, 8]
aQ = [-12,7, 0]

omega = np.array([omega])

r = abs((aQ[0]+ aQ[1])/ -8**2)
print(r)