# linear algebra python
# https://www.google.com/search?q=linear+algebra+python&sxsrf=ALeKk00bAclhj18xCwEbKZ27J5UMzPRTfA%3A1621259417578&ei=mXSiYPXXItqNr7wPzoSXsAY&oq=linear+al&gs_lcp=Cgdnd3Mtd2l6EAMYATIECCMQJzIECAAQQzIECAAQQzIECC4QQzICCAAyBQgAEMsBMgUIABDLATICCAAyAggAMgIILjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoFCAAQkQI6CggAELEDEIMBEEM6CwgAELEDEIMBEJECUOSkAVjptQFg5cABaAFwAngAgAHIAYgBiA2SAQUwLjkuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz
import numpy as np
from numpy import linalg as la
import time


'''
pinv, dot, matmul, multi_dot, arrays vs matrix vs vectors,
vdot, inner, outer, einsum/ einsum_path, matrix_power, kron,
decomposition, cond, det, solve, lstsq, inv
'''


# ---------- dot: product of two arrays -----------
m = np.arange(3) - 3
# print(m)
n = np.arange(3) - 2
# print(n)
# print(np.dot(m, n))
# print(np.dot(2, 3))
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
# print(np.dot(a, b))

a = np.arange(2*3*4).reshape((2, 3, -1))
# b = np.arange(3*4*5*6)[::-1].reshape((5, 4, 6, 3))
# print(a)
# print(b)

# ---------- multi_dot: product of two or more arrays -----------
A = np.random.random((5, 4))
B = np.random.random((4, 3))
C = np.random.random((3, 6))
D = np.random.random((6, 2))
# print(la.multi_dot([A, B, C, D]))

# ---------- vdot: product of two vectors -----------
# complex conjugate: a+bj vs a-bj
a = np.array([1+2j, 3+4j])
b = np.array([5+6j, 7+8j])
# print(np.vdot(a, b))
a = np.array([[1, 4], [5, 6], [5, 6]])
b = np.array([[4, 1], [2, 2], [5, 6]])
# print(np.vdot(a, b))

# ---------- inner: Inner product of two arrays -----------
# scalars: vô hướng
a = np.arange(3) - 1
b = np.arange(3) - 2
# print(np.inner(a, b))
a = np.arange(12).reshape((2, 3, -1))
# print(a)
b = np.arange(2)
# print(b)
# print(np.inner(a, b))

# b = 1 -> b scalar
# print(np.inner(np.eye(3), 1))

# ---------- outer : outer product of two arrays -----------
rl = np.outer(np.ones((5, )), np.linspace(-2, 2, 5))
# print(rl)
# print(np.ones((5, )))
# print(np.linspace(-2, 2, 5))

im = np.outer(1j*np.linspace(2, -2, 5), np.ones((5, )))
# print(im)

# grid for computing a Mandelbrot set
# print(rl + im)

x = np.array(['a', 'b', 'c'], dtype=object)
# print(np.outer(x, [1, 2, 1]))

# ---------- matmul: matrix product of two arrays -----------
a = np.ones([9, 5, 7, 4])
c = np.ones([9, 5, 4, 3])
# print(a)
# print(c)
# # using shape to get dismensions
# print(np.dot(a, c).shape)
# print(np.matmul(a, c).shape)

a = np.array([[1, 0],
              [0, 1]])
b = np.array([[4, 1],
              [2, 2]])
# print(np.matmul(a, b))

a = np.arange(2 * 2 * 4).reshape((2, 2, 4))
b = np.arange(2 * 2 * 4).reshape((2, 4, 2))
# print(np.matmul(a, b).shape)
# print(np.matmul(a, b)[0, 1, 1])
# print(sum(a[0, 1, :]*b[0, :, 1]))

# print(np.matmul([2j, 3j], [2j, 3j]))

a = np.array([2j, 3j])
b = np.array([2j, 3j])
# print(a @ b)

# ---------- tensordot: tensor dot product along specified axes -----------
# axes = 0, 1, 2
# 2 tham số đầu tiên ảnh hưởng chính đến nhân ma trận
a = np.arange(6.).reshape(1, 2, -1)
b = np.arange(4.).reshape(2, 1, -1)
c = np.tensordot(a, b, axes=([1, 0], [0, 1]))
# c = np.tensordot(a, b, axes=([0, 1], [1, 0]))
# print(a)
# print()
# print(b)
# print()
# print(c.shape)
# d = np.zeros((3, 2))
# for i in range(3):
#     for j in range(2):
#         for k in range(1):
#             for n in range(2):
#                 d[i, j] += a[k, n, i] * b[n, k, j]
# print(d)
a = np.array(range(1, 9))
a.shape = (2, 2, 2)
A = np.array(('a', 'b', 'c', 'd'), dtype=object)
A.shape = (2, 2)
# khi nào dùng axes nào = 0, 1, 2
res = np.tensordot(a, A, ((0, 1), (1, 0)))
# print(res.shape)


# ---------- einsum/ einsum_path: Einstein summation -----------
# https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum
a = np.arange(6.).reshape(1, 2, -1)
b = np.arange(4.).reshape(2, 1, -1)
# print(np.einsum('ijm,jik', a, b))

a = np.arange(25).reshape(5, 5)
b = np.arange(5)
c = np.arange(6).reshape(2, 3)

# print(np.einsum('ii', a))
# print(np.trace(a))
# print(np.einsum(a, [0, 0]))
# print(np.einsum('ii->i', a))
# print(np.diag(a))

# # Sum over an axis
# print(a)
# print(np.einsum('ij->i', a))
# print(np.sum(a, axis=1))
# print(np.sum(a, axis=0))
# print(np.einsum('...i->...', a))

# # matrix transpose
# print(np.einsum('ji', a))
# print(np.einsum('ij->ji', a))
# print(np.transpose(a))
# print(a.T)
# print(np.einsum(a, [1, 0]))

# # Vector inner products
# print(b)
# print(np.einsum('i,i', b, b))
# print(np.einsum(b, [0], b, [0]))
# print(np.dot(b, b.T))
# print(np.inner(b, b))

# # Matrix vector multiplication
# print(np.einsum('ij,j', a, b))
# print(np.einsum(a, [0, 1], b, [1]))  # ???
# print(np.dot(a, b))
# print(np.einsum('...j,j', a, b))    # ???

# # scalar multiplication
# print(np.einsum(',ij', 3, c))
# print(np.multiply(3, c))

# # Writeable returned arrays
# a = np.zeros((3, 3))
# np.einsum('ii->i', a)[:] = 1
# print(a)

# # Chained array operations. For more complicated contractions
# a = np.ones(64).reshape(2, 4, 8)
# # print(a)
# t0 = time.time()
# path = np.einsum_path('ijk,ilm,njm,nlk,abc->', a, a,
#                       a, a, a, optimize='optimal')[0]
# for item in range(500):
#     # _ = np.einsum('ijk,ilm,njm,nlk,abc->', a, a, a, a, a)
#     # _ = np.einsum('ijk,ilm,njm,nlk,abc->', a, a, a, a, a, optimize='optimal')
#     # _ = np.einsum('ijk,ilm,njm,nlk,abc->', a, a, a, a, a, optimize='greedy')
#     _ = np.einsum('ijk,ilm,njm,nlk,abc->', a, a, a, a, a, optimize=path)
# t1 = time.time()
# print(t1-t0)

# # ---------------- bonus :
# a = np.arange(25).reshape(5, 5)
# # print(a)
# print(np.average(a, axis=0))
# print(np.average(a, axis=1))


# ---------- matrix_power: matrix to power -----------
i = np.array([[0, 1], [-1, 0]])
# i = np.ones((3, 3))
# print(i)
# print(la.matrix_power(i, 0))
# print(la.matrix_power(i, -3))

# q = np.zeros((4, 4))
# q[0:2, 0:2] = -i
# q[2:4, 2:4] = i
# print(la.matrix_power(q, 2))


# ---------- kron: Kronecker product of two arrays -----------
# https://math.stackexchange.com/questions/1874581/why-use-the-kronecker-product
a = np.arange(3)
b = np.arange(3) - 2
# print(a)
# print(b)
# print(np.kron(a.T, b.T))

# print(np.kron([1, 10, 100], [5, 6, 7]))
# print(np.kron([5, 6, 7], [1, 10, 100]))

# # ones, zeros, eye
# print(np.kron(np.eye(2), np.ones((2, 2))))

a = np.arange(100).reshape((2, 5, 2, 5))
b = np.arange(24).reshape((2, 3, 4))
c = np.kron(a, b)
# print(c.shape)

# ---------- cholesky: Cholesky decomposition -----------
# https://www.sciencedirect.com/topics/engineering/cholesky-decomposition
A = np.array([[1, -2j], [2j, 5]])
# print(A)
L = la.cholesky(A)
# print(L)
# print(np.dot(L, L.T.conj()))

# if array_like
A = [[1, -2j], [2j, 5]]
# print(type(la.cholesky(A)))
# print(type(la.cholesky(np.matrix(A))))

# ---------- qr: qr decomposition -----------
# https://math.stackexchange.com/questions/198479/why-is-qr-factorization-useful-and-important
# https://en.wikipedia.org/wiki/Least_squares
# https://en.wikipedia.org/wiki/Orthonormality

a = np.random.randn(3, 2)
q, r = la.qr(a)
# print(q, r)
# print(r)
# print(np.allclose(a, np.dot(q, r)))
# print(la.qr(a, mode='r'))

A = np.array([[0, 1], [1, 1], [1, 1], [2, 1]])
b = np.array([1, 0, 2, 1])
q, r = la.qr(A)
p = np.dot(q.T, b)
# print(np.dot(np.linalg.inv(r), p))
# print(la.lstsq(A, b, rcond=None)[0])


# ---------- svd: svd decomposition -----------
# https://stats.stackexchange.com/questions/19607/what-is-the-point-of-singular-value-decomposition
a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
b = np.random.randn(2, 7, 8, 3) + 1j*np.random.randn(2, 7, 8, 3)
u, s, vh = np.linalg.svd(a, full_matrices=True)
# print(u, s, vh)
# print(u.shape, s.shape, vh.shape)
# print(np.allclose(a, np.dot(u[:, :6] * s, vh)))
smat = np.zeros((9, 6), dtype=complex)
smat[:6, :6] = np.diag(s)
# print(np.allclose(a, np.dot(u, np.dot(smat, vh))))

u, s, vh = np.linalg.svd(a, full_matrices=False)
# print(np.allclose(a, np.dot(u * s, vh)))
smat = np.diag(s)
# print(np.allclose(a, np.dot(u, np.dot(smat, vh))))

# ---------- eig: eigenvalues and right eigenvectors -----------
# print(np.diag((1, 2, 3)))
w, v = la.eig(np.diag((1, 2, 3)))
# # columns vector
# print(w)
# # diag matrix
# print(v)
w, v = la.eig(np.array([[1, -1], [1, 1]]))
# print(w)
# print(v)

# ---------- eigh: Hermitian eigenvalues and eigenvectors -----------
# ---------- eigvals: eigenvalues of a general matrix -----------
# ---------- eigvalsh: Hermitian eigenvalues of a general matrix ----
# ---------- norm: Matrix or vector norm 02_part -----------
# ---------- cond: condition number -----------
a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
# print(la.cond(a))
# print(la.cond(a, 'fro'))
# print(la.cond(a, np.inf))

# ---------- det: determinant  -----------
a = np.array([[1, 2], [3, 4]])
# a = np.array([[[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]]])
# print(la.det(a))
# ---------- matrix_rank: matrix rank of array -----------
# ---------- slogdet: sign and logarithm determinant  -----------
(sign, logdet) = la.slogdet(a)
# print(sign)
# print(logdet)
# print(sign*np.exp(logdet))  # = det
# ---------- trace: sum along diagonals -----------
# print(np.trace(a))

# ---------- solve: Solve a linear matrix equation -----------
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = la.solve(a, b)
# print(x)
# print(np.allclose(np.dot(a, x), b))

# ---------- tensorsolve: Solve the tensor equation -----------
a = np.eye(2*3*4)
a.shape = (2*3, 4, 2, 3, 4)
b = np.random.randn(2*3, 4)
x = la.tensorsolve(a, b)
# print(x.shape)
# print(np.allclose(np.tensordot(a, x, axes=3), b))

# ---------- lstsq: least-squares solution -----------
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack([x, np.ones(len(x))]).T
m, c = la.lstsq(A, y, rcond=None)[0]
# print(m, c)

# ---------- inv: inverse of a matrix -----------
a = np.array([[1., 2.], [3., 4.]])
# print(type(a))
ainv = la.inv(a)
# print(ainv)
# print(np.allclose(np.dot(a, ainv), np.eye(2)))
# print(la.inv(np.matrix(a)))
a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
# print(la.inv(a))

# ---------- pinv: pseudo inverse of a matrix -----------
a = np.random.randn(3, 2)
B = la.pinv(a)
# print(np.allclose(a, np.dot(a, np.dot(B, a))))
# print(np.allclose(B, np.dot(B, np.dot(a, B))))
