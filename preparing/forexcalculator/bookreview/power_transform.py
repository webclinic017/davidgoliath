# Introduce Power transform
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import boxcox

df = pd.read_csv('data/airline-passengers.csv', header=0)

plt.figure(1)
'''
transform = df['Passengers'].to_numpy()
# line plot
plt.subplot(211)
plt.plot(transform)
# histogram
plt.subplot(212)
plt.hist(transform)
'''
# ---------------------------------------------------
'''
# quadratic growth trend and a histogram ---------
series = [i**2 for i in range(1, 100)]
# line plot
plt.subplot(211)
plt.plot(series)
# histogram
plt.subplot(212)
plt.hist(series)
'''
# ---------------------------------------------------
'''
# Square Root transform ---------
series = [i**2 for i in range(1, 100)]
transform = series = np.sqrt(series)
# line plot
plt.subplot(211)
plt.plot(transform)
# histogram
plt.subplot(212)
plt.hist(transform)
'''
# ---------------------------------------------------
'''
# Square Root transform a time series ---------
transform = df['Passengers'].to_numpy()
temp = pd.DataFrame()
temp['passengers'] = np.sqrt(transform)

# line plot
plt.subplot(211)
plt.plot(temp['passengers'])  # increasing variance from cycle to cycle
# histogram
plt.subplot(212)
plt.hist(temp['passengers'])  # exponential or long-tail distribution
'''
# ---------------------------------------------------
'''
# Log Transform --------- natural logarithm- transform to linear
series = [math.exp(i) for i in range(1, 100)]

# make the series linear and the distribution uniform.
transform = np.log(series)
# line plot
plt.subplot(211)
plt.plot(transform)
# histogram
plt.subplot(212)
plt.hist(transform)
'''
# ---------------------------------------------------
'''
# demonstrates a log transform --------- passengers data
# Line and density plots of the log transformed
temp = pd.DataFrame()
temp['passengers'] = np.log(df['Passengers'])
# line plot
plt.subplot(211)
plt.plot(temp['passengers'])  # linear growth and variance
# histogram
plt.subplot(212)
plt.hist(temp['passengers'])  # Gaussian-like distribution
'''
# ---------------------------------------------------
# Box-Cox Transform ---------
temp = pd.DataFrame()

# # choose the lmbda value first
# temp['passengers'] = boxcox(df['Passengers'], lmbda=0.0)

# auto find tuned value
temp['passengers'], lam = boxcox(df['Passengers'])
print(f'{lam}')
# Line and density plots of the Box-Cox transformed
plt.subplot(211)
plt.plot(temp['passengers'])
plt.subplot(212)
plt.hist(temp['passengers'])
plt.show()
