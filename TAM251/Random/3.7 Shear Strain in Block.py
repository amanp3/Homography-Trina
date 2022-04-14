import numpy as np

G = 5000 # ksi
P = 775 # kips
Lo = 14 # in
b = 5 # in
t = 4 # in



tao =  P/(Lo*b)
print(tao)
gamma = tao/G

print(gamma*t)