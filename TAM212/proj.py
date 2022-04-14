import numpy as np

a= np.array([1,-1,0,1])
b= np.array([0.58, -0.58, 0.58,0])

projAontoB = (np.dot(a,b)/(np.linalg.norm(b)**2))*b

print(projAontoB)