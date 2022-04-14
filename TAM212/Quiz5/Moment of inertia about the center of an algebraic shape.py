from sympy import *
import numpy as np

p = 6
x, y = symbols('x, y')
y1 = 1*x**2 - 4*x - 6
y2 = 1*x**2 + 2

x1 = -1
x2 = 2

A = integrate((y2- y1), (x, x1, x2))
M = p * A
#print(A)
print(M)
Mx = (p/2)*(integrate((y2**2 - y1**2), (x, x1, x2)))
#print(Mx)

My = p*(integrate((x*(y2 - y1)), (x, x1, x2)))
#print(My)

x_bar = My/M
y_bar = Mx/M
#print(x_bar)
#print(y_bar)

r = sqrt((x - x_bar)**2 + (y - y_bar)**2)
print(x_bar, y_bar)

Ic = p*integrate(integrate((r**2), (y, y1, y2)), (x, x1,x2))
print(Ic)