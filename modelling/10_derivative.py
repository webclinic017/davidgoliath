# derivative calculator python
# https://www.google.com/search?q=derivative+calculator+python&oq=derivative+calculator+python&aqs=chrome..69i57j0i22i30l2.4221j0j4&sourceid=chrome&ie=UTF-8

import numpy as np
from sympy import Symbol, lambdify

x = Symbol('x')
y = x**3+2*x**2+1
yprime = y.diff(x)
# print(yprime)
f = lambdify(x, yprime, 'numpy')
print(f(np.ones(5)))

# x = np.linspace(0, 10, 1000)
# dx = x[1] - x[0]
# y = x**2 + 1
# dydx = np.gradient(y, dx)
# print(dydx)
