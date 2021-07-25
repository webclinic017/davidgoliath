import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
import investpy as iv
import datetime as dt
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

# global starttime
start = '01/01/2010'
today = dt.date.today().strftime("%d/%m/%Y")

quote = 'XAU/USD'
'''
series = pd.read_csv('data/daily-min-temperatures.csv', header=0)
series['Date'] = pd.to_datetime(series['Date'])
series.set_index('Date', inplace=True)

autocorrelation_plot(series)
plt.show()
'''

# ---------------------------------------------------
'''
# read data
df = iv.currency_crosses.get_currency_cross_historical_data(
    quote, start, today)
quote = quote.replace('/', '')
df.to_csv(f'data/{quote}.csv')
'''
if '/' in quote:
    quote = quote.replace('/', '')
df = pd.read_csv(f'data/{quote}.csv', header=0)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

'''
# # test data 3: have problem with range
# (- year not have same day count (260 -262 -259))
# get the same day count -> mean of day length

# tempo handle --------

df.drop(df['2015-12'].tail(1).index, inplace=True)
df.drop(df['2016-12'].tail(1).index, inplace=True)
# end tempo handle --------
'''

# # test 2 months data
# temp = df.Close['2021-05': '2021-06']

# # original test data
# temp = df.Close['2021-06']

# temp = df.Close['2015': '2016']
temp = df.Close['2015']

# ----------- Common api
# print(temp.describe())
# print(temp.size)
# print(temp.index)
# print(type(temp))

# ---------- Lag Features: Pandas shift and concat

# tmp = pd.concat([temp.shift(3), temp.shift(2),
#                 temp.shift(1), temp], axis=1)
# tmp.columns = ['t-2', 't-1', 't', 't+1']
# print(tmp)

# ----------  Rolling Window Statistics (rolling)

# shifted = temp.shift(1)  # backward
# window = shifted.rolling(window=2)
# means = window.mean()
# tmps = pd.concat([means, temp], axis=1)
# tmps.columns = ['mean', 't']
# print(tmps)

# ---------- Rolling Window Statistics 2 (width ...)

# width = 3
# shifted = temp.shift(width-1)
# window = shifted.rolling(window=width)
# df = pd.concat([window.min(), window.max(), window.mean(), temp], axis=1)
# df.columns = ['min', 'max', 'mean', 't+1']
# print(df.tail())

# ------------------------------------- Data Visualization
# # basic plot ---------
# temp.plot()

# # dash plot ---------
# temp.plot(style='ko')
# temp.plot(style='k--')

# -------------------------------------

# # # Stacked line plots ---------
# # all document data
# groups = temp.groupby(pd.Grouper(freq='Y'))

# years = pd.DataFrame()
# '''
# # ------------- not the good way ------------
# day_count = []
# # get min days first ---------
# for name, group in groups:
#     day_count.append(len(group.values))
# print(min(day_count))
# # ------------- not the good way ------------
# '''
# for name, group in groups:
#     years[name.year] = group.values.ravel()
# years.plot(subplots=True, legend=False)

# -------------------------------------------------------
# # Histograms and Density Plots ---------
# temp.hist()
# temp.plot(kind='kde')

# -------------------------------------------------------
# # Box and Whisker Plots --------- One year
# one_year = df.Close['2020']
# groups = one_year.groupby(pd.Grouper(freq='M'))
# months = pd.concat([pd.DataFrame(x[1].values) for x in groups], axis=1)
# months.columns = range(1, 13)
# months.boxplot()

# # -------------------------------------------------------
# # # Heat Maps --------- year
# groups = temp.groupby(pd.Grouper(freq='Y'))
# years = pd.DataFrame()

# for name, group in groups:
#     years[name.year] = group.values.ravel()
# years = years.T
# plt.matshow(years, interpolation=None, aspect='auto')

# # Heat Maps --------- month
# groups = temp.groupby(pd.Grouper(freq='M'))
# months = pd.concat([pd.DataFrame(x[1].values) for x in groups], axis=1)
# months.columns = range(1, 13)
# plt.matshow(months, interpolation=None, aspect='auto')

# # -------------------------------------------------------

# # Lag Scatter Plots --------- month
# lag_plot(df.Close['2020'])

# # -------------------------------------------------------
# # Autocorrelation Plots --------- month
# autocorrelation_plot(df.Close['2020'])
# plt.show()
