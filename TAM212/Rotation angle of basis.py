import numpy as np

rcart = [-1.062,-5.426]
rpolar = [3.307, 4.431]

xprime = rpolar[0]
yprime = rpolar[1]

x = rcart[0]
y = rcart[1]

A = np.array([[xprime, -yprime], [yprime, xprime]])

er = np.linalg.solve(A, np.array([x,y]))

theta = np.arctan(np.abs(er[1])/np.abs(er[0]))

if er[0] > 0: 
    if er[1] > 0:
        theta = theta
    elif er[1] < 0:
        theta = 2*np.pi - theta

elif er[0] < 0:
    if er[1] > 0:
        theta = np.pi - theta
    elif er[1] < 0:
        theta = theta + np.pi
print(theta)