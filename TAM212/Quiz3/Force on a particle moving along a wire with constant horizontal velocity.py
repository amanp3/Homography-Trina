import sympy

x = sympy.symbols('x')
g = -9.8

y = -1*sympy.sin(2*x)
vx = 1
m = 7
x0= 4
vy = sympy.diff(y,x) *vx
ay = sympy.diff(vy,x) * vx - g
F = m*ay

print(0 , sympy.N(F.subs(x, x0)))