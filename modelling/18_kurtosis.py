# kurtosis python
# https://www.google.com/search?q=kurtosis+python&oq=Kurtosis+python&aqs=chrome.0.0l4j0i22i30l6.1736j0j7&sourceid=chrome&ie=UTF-8
# https://en.wikipedia.org/wiki/Kurtosis

''' Statistical functions:
Kurtosis is the fourth central moment
divided by the square of the variance.
If Fisher’s definition is used, then 3.0
is subtracted from the result to give 0.0
for a normal distribution.

If bias is False then the kurtosis is
calculated using k statistics to eliminate
bias coming from biased moment estimators.
'''
# -----------------------------------
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html
# scipy part -----------------------------------

# from scipy.stats import norm, kurtosis
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.pylab as p
import numpy as np
import pandas as pd

'''
# # Discrete vs continuous distribution dataset
# data = stats.norm.rvs(size=1000, random_state=3)
# # reference point
# print(stats.kurtosis(data))
# # print(kurtosis(data, fisher=False))

x = np.linspace(-5, 5, 100)
ax = plt.subplot()
distnames = ['laplace', 'norm', 'uniform', 'cauchy', 'maxwell', 'logistic']
for distname in distnames:
    if distname == 'uniform':
        dist = getattr(stats, distname)(loc=-2, scale=4)
    else:
        dist = getattr(stats, distname)
    data = dist.rvs(size=1000)
    kur = stats.kurtosis(data, fisher=True)
    y = dist.pdf(x)
    ax.plot(x, y, label=f'{distname}, {round(kur, 3)}')
    ax.legend()
plt.show()
'''

# geeksforgeeks part -----------------------------------
x1 = np.linspace(-5, 5, 10000)
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp(-.5*(x1)**2)  # normal distribution
# p.plot(x1, y1, '*')
# print(stats.kurtosis(y1))
# print(stats.kurtosis(y1, fisher=False))
# p.show()

# stackoverflow part -----------------------------------
x_ = np.random.normal(0, 2, 10000)
f, (ax1, ax2) = plt.subplots(1, 2)

# print(f'excess kurtosis of random norm dist(should be 0):\
# {stats.kurtosis(x_)}')
# print(f'skewness of random norm dist (should be 0): {stats.skew(x_)}')

# print(f'excess kurtosis of norm dist (should be 0): {stats.kurtosis(x1)}')
# print(f'skewness of norm dist (should be 0): {stats.skew(x1)}')

# ax1.hist(x_, bins='auto')
# ax1.set_title('probability density (random)')
# ax2.hist(y1, bins='auto')
# ax2.set_title('your dataset')

# plt.tight_layout()
# plt.show()

# pandas part -----------------------------------
# df = pd.read_csv('Data/nba.csv')
# df = pd.read_csv('Data/XAUNZD_Daily.csv')
# print(df.tail())

# # skewness along the index axis
# print(df.kurt(axis=0, skipna=True))

# # skewness of the data over the column axis
# print(df.kurt(axis=1, skipna=True))

# BONUS part -----------------------------------
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstat.html
# https://mathworld.wolfram.com/Cumulant.html
# https://mathworld.wolfram.com/k-Statistic.html
'''
sample size increases, n-th moment and n-th k-statistic converge
In the case of the normal distribution, they converge to zero
'''
rndm = np.random.RandomState(1234)
# print(rndm)
for n in [2, 3, 4, 5, 6, 7]:
    # sample size increases
    x = rndm.normal(size=10**n)
    m, k = stats.moment(x, 3), stats.kstat(x, 3)
    print(f'{m}, {k}, {m-k}')
