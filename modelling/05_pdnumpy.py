# Probability distribution numpy
'''
1. a Generator
2. Call default_rng
3. Generator uses bits provided by PCG64
4. RandomState
5.

'''
# https://www.google.com/search?q=Probability+distribution+numpy&oq=Probability+distribution+numpy&aqs=chrome..69i57j0i22i30l6.2718j0j7&sourceid=chrome&ie=UTF-8
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import default_rng
from numpy import random as rd
from numpy.random import Generator, PCG64

x = rd.binomial(n=10, p=0.5, size=1000)
# sns.distplot(x, hist=True, kde=False)
# plt.show()

# -------------------- Basic ---------------------------
rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)
# print(vals)
# print(more_vals)

# RandomState---------------
a = rd.random_sample(size=5)
a = rd.rand(1, 3)
# print(a)

# ----- random samples from a normal (Gaussian) distribution --------
mu, sigma = 0, 0.1  # mean and std
a = rd.normal(mu, sigma, 1000)
# sns.distplot(a, hist=False)
# plt.show()

# # Verify the mean and the variance
# print(abs(mu - np.mean(a)))
# print(abs(sigma - np.std(a, ddof=1)))

# # plotting
# count_, bin_, ignored_ = plt.hist(a, 30, density=True)
# plt.plot(bin_, 1/(sigma*np.sqrt(2*np.pi)) *
#          np.exp(-(bin_-mu)**2/(2*sigma**2)), linewidth=2, color='r')
# plt.show()

# ----------- all Probability distribution Types -------------
# https://numpy.org/doc/stable/reference/random/generator.html

# ----------- Generator.integers -------------
# # array
# print(rng.integers(3, size=10))

# # matrix
# print(rng.integers(5, size=(2, 4)))

a = rng.integers(1, [3, 5, 10])
# print(a)

# ----------- Generator.random -------------
# print(rng.random())
# print(rng.random(5,))
# print(rng.random((5, 2)))

# # 3*2 array of random numbers from [-5, 0):
# print(5 * rng.random((3, 2)) - 5)

# ----------- Generator.choice: inplace # replace -------------
# # uniform
# print(rng.choice(5, (3, 2)))

# non-uniform: p stand for probabilities associated with each entry
# print(rng.choice(5, (3, 2), p=[0.1, 0, 0.3, 0.6, 0]))

# uniform/ non-uniform without replacement

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
# print(rng.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3]))

# ----------- Generator.shuffle -------------
arr = np.arange(10)
rng.shuffle(arr)
# print(arr)

arr = np.arange(9).reshape((3, 3))
rng.shuffle(arr)
# print(arr)

# ----------- Generator.permutation -------------
# print(rng.permutation(10))
# print(rng.permutation([1, 4, 9, 12, 15]))
arr = np.arange(9).reshape((3, 3))
# print(arr)
# print(rng.permutation(arr, axis=1))  # columns


# ----------- Generator.beta -------------
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html
