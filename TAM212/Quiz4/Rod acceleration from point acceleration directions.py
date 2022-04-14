from sympy import *
from sympy import Matrix as M
import numpy as np
#aq = ap + alpha2 x rpq + w2 x (w2 x rpq)

apMAG = 4
aqMAG = 2.5
thetaP = 58
thetaQ = 61
l = 5.5 

thetaP *= np.pi/ 180
thetaQ *= np.pi/ 180

rpq = M([l, 0 ,0])
wz, alphaz = symbols('wz, alphaz')
w = M([0, 0 , wz])
alpha = M([0, 0, alphaz])

#CALL L THE X AXIS
ap = apMAG* M([cos(thetaP), sin(thetaP), 0]) #draw to figure out these in terms of the line
aq = aqMAG * M([cos(np.pi + thetaQ), sin(np.pi + thetaQ), 0]) #''
print(ap) #check vectors
print(aq) #''

eq1 = Eq(aq, ap + alpha.cross(rpq) + w.cross(w.cross(rpq)))

soln = solve((eq1), (wz, alphaz), dict = True)
print(soln)
print('CHECK SIGN USING RHR')


#WORKING CODE FOR ALPHA
#ap = 3
#aq = 4
#thetaP = -54 #cw is pos ccw is neg
#thetaQ = -46
#l = 6

#thetaP *= np.pi/ 180
#thetaQ *= np.pi/ 180

#alpha = (ap*np.sin(thetaP) + aq*np.sin(thetaQ))/l

#print(alpha)