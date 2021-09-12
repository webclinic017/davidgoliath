import random as rd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.stattools import adfuller
import numpy as np
from sklearn.metrics import mean_squared_error

# seed random number generator
rd.seed(1)
'''
series = [rd.randrange(10) for i in range(1000)]
plt.plot(series)
plt.show()
'''
#  for _ in range(10)
random_walk = [-1 if rd.random() < 0.5 else 1]
for i in range(1, 1000):
    movement = -1 if rd.random() < 0.5 else 1
    value = random_walk[i-1] + movement
    random_walk.append(value)
# print(random_walk)
# ----------------------------------------
# Predicting a Random Walk
# ---------------------

# prepare dataset
train_size = int(len(random_walk) * 0.66)
train, test = random_walk[0:train_size], random_walk[train_size:]

# persistence
predictions = []
history = train[-1]
for i in range(len(test)):
    # # Persistence or the naive forecast
    # yhat = history
    # ------------------------------
    # - in real, never have 1 or -1
    yhat = history + (-1 if rd.random() < 0.5 else 1)
    predictions.append(yhat)
    history = test[i]
rmse = np.sqrt(mean_squared_error(test, predictions))
'''
- RMSE=1 ~ variation from one time step to the next is always going
to be 1, either in the positive or negative direction.
'''
print(f'Persistence RMSE: {rmse:.3f}')

# ----------------------------------------
# stationary transform
# ---------------------
'''
# take difference to get stationary time series
diff = []
for i in range(1, len(random_walk)):
    value = random_walk[i] - random_walk[i-1]
    diff.append(value)
# print(diff)

# # diff plotting
# plt.plot(diff)
'''
# ---------------------
'''
+ no significant relationship between obs and its lag
+ small correlations close to zero and below the 95%
and 99% confidence levels
'''
# # autocorrelation plotting
# autocorrelation_plot(diff)

# ----------------------------------------
'''
the shape and movement looks
like a realistic time series for the stock price
'''
# ------------------
# # random_walk plot
# plt.plot(random_walk)

# # how to read autocorrelation chart
# autocorrelation_plot(random_walk)
# ----------------------------------------
'''
# statistical test
result = adfuller(random_walk)

# test statistic > all of the critical values
print(f'ADF statistic: {result[0]:.6f}')
print(f'p-value: {result[1]:.6f}')
print('Critial value:')

# confidence levels
for key, value in result[4].items():
    print(f'\t{key}: {value:.3f}')
'''
plt.show()
