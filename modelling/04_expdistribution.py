# Exponential distribution
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# random sampling
# pdf?

# a = np.random.exponential(scale=2, size=(3, 4))
# a = np.random.exponential(5, (2, 3))
# print(a)

# plotting
a = np.random.exponential(size=1000)
# sns.distplot(a, hist=False)
# plt.show()
