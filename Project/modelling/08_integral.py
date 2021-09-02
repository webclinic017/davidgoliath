# integral python
# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(integrate(cos(x), x))
print(integrate(exp(-x), (x, 0, oo)))
print(integrate(exp(-x**2-y**2), (x, -oo, oo), (y, -oo, oo)))
