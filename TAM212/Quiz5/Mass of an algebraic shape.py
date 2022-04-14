from sympy import *

x = symbols('x')

y1 = 2*x**2 + 4*x - 19
y2 = -1*x**2 + 2*x + 2
x1 = 1
x2 = 2
p = 3

ans = p * integrate((y2 - y1), (x, x1, x2))
print(ans)
