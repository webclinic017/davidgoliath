# euclid norm
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
from numpy import linalg as la
import numpy as np

a = np.arange(9) - 4
# print(np.arange(9))
# print(a)
b = a.reshape((3, 3))
# print(b)
'''
print(la.norm(a))
print(la.norm(b))
print(la.norm(b, 'fro'))
print(la.norm(a, np.inf))
print(la.norm(b, np.inf))
print(la.norm(a, -np.inf))
print(la.norm(b, -np.inf))
print(la.norm(a, 1))
print(la.norm(b, 1))
# print(la.norm(a, -1))
print(la.norm(b, -1))
print(la.norm(a, 2))
print(la.norm(b, 2))
# print(la.norm(a, -2))
print(la.norm(b, -2))
print(la.norm(a, 3))
# print(la.norm(a, -3))
'''
c = np.array([[1, 2, 3], [-1, 1, 4]])
# # using axis compute vector norms
# print(la.norm(c, axis=0))
# print(la.norm(c, axis=1))
# print(la.norm(c, ord=1, axis=1))

# using axis compute matrix norms
m = np.arange(12).reshape(2, 3, -1)
# print(la.norm(m, axis=(1, 2)))
# print(m[0, :, :])
# print(m[1, :, :])
# print(la.norm(m[0, :, :]), la.norm(m[1, :, :]))

m = np.arange(3) - 1
# print(m)
# print(m/la.norm(m))
