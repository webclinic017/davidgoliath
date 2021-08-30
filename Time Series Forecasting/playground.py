import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import investpy as iv
# import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

quote = 'VN'
'''
# get investing data
start = '01/01/1990'
today = '13/07/2021'
df = iv.indices.get_index_historical_data(quote, 'vietnam', start, today)
df.to_csv(f'data/{quote}.csv')
'''
# preprocessing data
df = pd.read_csv(f'data/{quote}.csv', header=0)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# consider regret Volume columns
df.drop('Currency', axis=1, inplace=True)
'''
# --------------------- COMMON INFO ------------------
# print(df['2020-04-01':'2021'].describe())
# print(df['2020'].info())
# print(df.index)
# print(df.size)
'''
# ----------------------------------------------------
'''
# --------------------- GROUP BY YEAR ------------------
# get a range values
df = df.Close['2000':'2021']
groups = df.groupby(pd.Grouper(freq='Y'))
for name, group in groups:
    print(name.year, len(group.values.ravel()))
    pass
# df.plot()
# plt.show()
'''
# ----------------------------------------------------
'''
# ------------ LAG: SHIFT, ROLLING, CONCAT ------------------
df = df.Close['2000':'2021']
width = 20
shifted = df.shift(width-1)
window = shifted.rolling(window=width)
tmp = pd.concat([window.min(), window.max(), window.mean(), df], axis=1)
tmp.columns = ['min', 'max', 'mean', 'close']
# print(tmp.describe())
# print(tmp.tail(10))
'''
# ------------------------Data Visualization-------------------------
# ------------ 1. Basic, dash plot ------------------
# ------------ 2. Stacked line plots ------------------
# ------------ 3. Histograms and Density Plots  ------------------
# ------------ 4. Box and Whisker Plots ------------------
# ------------ 5. Heat Maps ------------------
# ------------ 6. Lag Scatter Plots ------------------
# ------------ 7. Autocorrelation Plots ------------------
