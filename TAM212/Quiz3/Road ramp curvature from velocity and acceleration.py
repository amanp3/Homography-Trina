import numpy as np

v = np.array([0,76,14])
a = np.array([-152,114,-49])

p = np.linalg.norm(v)**3 / np.linalg.norm(np.cross(v,a))

print(p)