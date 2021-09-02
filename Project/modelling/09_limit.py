# Limit of a function python
# https://www.google.com/search?q=Limit+of+a+function+python&oq=Limit+of+a+function+python&aqs=chrome..69i57j0i22i30.1869j0j4&sourceid=chrome&ie=UTF-8
from sympy import limit, Symbol, sin, oo, cos
# from math import pi

x = Symbol('x')
print(limit(sin(3*x)/x, x, 0))
