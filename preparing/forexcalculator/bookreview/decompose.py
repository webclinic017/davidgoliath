# Decompose time series to its components: level, trend, seasonality
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import matplotlib.pyplot as plt
import random

# --------------- Test purpose ---------------
'''
quote = 'VN'
# preprocessing data
df = pd.read_csv(f'data/{quote}.csv', header=0)
df.drop('Currency', axis=1, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# df.sort_index(inplace=True)

result = seasonal_decompose(
    df.Close['2021-06'], model='additive',
    extrapolate_trend='freq', period=5)
# show output
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
result.plot()
plt.show()
'''
# --------------- Test purpose 2 ---------------
'''
# series = [i+random.randrange(10) for i in range(1, 100)]
series = [i**2 for i in range(1, 100)]
# print(series)
# result = seasonal_decompose(series, model='additive', period=1)
result = seasonal_decompose(series, model='multiplicative', period=1)
result.plot()
plt.show()
'''
# --------------- End Test purpose ---------------
series = pd.read_csv('data/airline-passengers.csv', header=0)
# series['Month'] = pd.to_datetime(series['Month'])
series.set_index('Month', inplace=True)
# transform = series['Passengers']
transform = series.values
result = seasonal_decompose(transform, model='multiplicative', period=1)
result.plot()
plt.show()
