import sympy

x = sympy.symbols('x')
v = sympy.symbols('v')
g = -9.8

m = 9
y = -2*sympy.cos(1.5*x)
x0= 2
d = 1 #1 is to the right -1 is the left
v0 = 2
vdot = -2 #incresing is pos decreasing is neg

yprime = sympy.diff(y,x)
xdot = d*sympy.sqrt(v**2 / (1+yprime**2))
ydot = d*sympy.sqrt(v**2 - xdot**2)
xdouble = sympy.diff(xdot, x) * xdot + sympy.diff(xdot, v)*vdot
ydouble = sympy.diff(ydot, x) * xdot + sympy.diff(ydot, v)*vdot - g 

print(m*sympy.N(xdouble.subs(v, v0).subs(x, x0)) , m*sympy.N(ydouble.subs(x, x0).subs(v,v0)))









#1 means ccw 0 means cw
#en_hat_ccw_or_cw = 1

#y_prime = sympy.diff(y, x)
#y_double_prime = sympy.diff(y_prime, x)

#rho = (1+((sympy.N(y_prime.subs(x, x0))**2))**(3/2))/(sympy.N(y_double_prime.subs(x, x0)))

#slope = sympy.N(y_prime.subs(x, x0))
#print(slope)
#theta = sympy.atan(slope)
#print(theta)

#a = np.array([a0, v0**2/rho])

#et_hat = np.array([sympy.cos(theta), sympy.sin(theta)])
#en_hat = np.array([])
#if en_hat_ccw_or_cw == 1:
 #   en_hat = np.array([-1*et_hat[1], et_hat[0]])
#else:
#    en_hat = np.array([et_hat[1], -1*et_hat[0]])

#tangent = a[0]*et_hat
#normal = a[1]*en_hat

#ans = tangent + normal
#ans = ans + np.array([0, -9.8])
#ans = ans * mass
#print(ans)