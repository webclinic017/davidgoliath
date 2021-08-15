import pandas as pd
import investpy as iv
import datetime
import statsmodels
import numpy as np
from settings import *
import random
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
import warnings
warnings.filterwarnings("ignore")

# how to read visualization chart

'''
today = datetime.datetime.today().strftime("%d/%m/%Y")
df = iv.commodities.get_commodity_historical_data('Gold', '01/01/2010', today)
df.to_csv('data/Gold_Daily.csv')
'''

# read data part
df = pd.read_csv('data/Gold_Daily_fill.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.drop(['Currency'], axis=1, inplace=True)


# find zero volume
def fill_zero_vol(file, rd_period=20):
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.drop(['Currency'], axis=1, inplace=True)

    '''
    # df.apply(lambda s: s.value_counts().get(key=0, default=0), axis=1)

    print(np.count_nonzero(df['Open'].values))
    print(np.count_nonzero(df['Close'].values))
    print(np.count_nonzero(df['Low'].values))
    print(np.count_nonzero(df['High'].values))
    print(np.count_nonzero(df['Volume'].values))

    # find the row have 0 (hardway)
    zero_handle = np.where(df['Volume'].values == 0)[0]
    # mean_vol_zero(zero_handle)
    '''
    # split to smaller data set
    # df = df[-100:]

    zero_df = df.loc[df['Volume'] == 0]
    for item in zero_df.index:
        # update zero_df here, update volume past to future

        # handle mean value
        index = df.index.get_loc(item)
        post_df = df.iloc[index-rd_period:index]
        zero_df.at[item, 'Volume'] = post_df['Volume'].mean()
        df.at[item, 'Volume'] = post_df['Volume'].mean()
    print(zero_df)
    # df.to_csv('data/Gold_Daily_fill.csv')


# gen = test(random.randint(10, 20))
# gen = test(random.randint(3, 5))
def dt_feature():
    '''
    df = pd.read_csv('data/Gold_Daily_fill.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    '''
    temp = pd.DataFrame()
    # date-time feature
    temp['month'] = [df.index[i].month for i in range(len(df))]
    temp['day'] = [df.index[i].day for i in range(len(df))]

    # lag feature
    temp['close'] = [df.Close[i] for i in range(len(df))]
    temp['close_lag1'] = temp['close'].shift(1)
    # temp['close_lag3'] = temp['close'].shift(-2)
    # temp['close_lag2'] = temp['close'].shift(-1)

    temp['vol'] = [df.Volume[i] for i in range(len(df))]
    temp['vol_lag1'] = temp['vol'].shift(1)
    # temp['vol_lag3'] = temp['vol'].shift(-2)
    # temp['vol_lag2'] = temp['vol'].shift(-1)

    # window feature
    choices = (random.randint(2, 200) for _ in range(200))
    choice = list(choices)

    window = temp['close_lag1'].rolling(
        window=random.choice(choice))
    temp['mean_close'] = window.mean()

    window_vol = temp['vol_lag1'].rolling(
        window=random.choice(choice))
    temp['mean_vol'] = window_vol.mean()
    '''
    temp['min'] = window.min()
    temp['max'] = window.max()

    # Expanding Window Statistics
    # https://stackoverflow.com/questions/45370666/what-are-pandas-expanding-window-functions
    window_exp = temp['close_lag1'].expanding()
    temp['mean_close'] = window_exp.mean()
    temp['min'] = window_exp.min()
    temp['max'] = window_exp.max()
    '''
    return temp


def line_plot():
    '''
    df = pd.read_csv('data/Gold_Daily_fill.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    '''
    df['Vol'] = ((df['High']-df['Low'])/df['Low']*100).abs()
    df['cl_change'] = (df['Close']-df['Open'])/df['Close']*100
    # df['pct_change'] = df['Close'].pct_change()*100

    df['Vol'][-200:].plot()
    df['cl_change'][-200:].plot()
    # df['cl_change'][-200:].plot(style='k.')
    # df['pct_change'][-200:].plot()

    # df[-200:].Close.plot()
    # df[-200:].Volume.plot()

    print(df.tail())
    plt.show()
    pass


def stack_line_plot():
    # compare line plots for the same interval,
    # but each line need has same length.

    # temp = df.Close['2010': '2020']
    groups = df.Close.groupby(pd.Grouper(freq='Y'))
    years = pd.DataFrame()
    for name, group in groups:
        print(name.year, len(group.values.ravel()))
    #     years[name.year] = group.values.ravel()
    # print(years)
    pass


def histogram_kde():
    # df.Close.hist()
    # df.Close['2020':'2021'].hist()
    # df.Close['2021'].plot(kind='kde')
    # plt.show()

    # print(df.Close['2021'].describe())
    print(df.info())
    pass


def box_whisker():
    # https://stackoverflow.com/questions/23461713/obtaining-values-used-in-boxplot-using-python-and-matplotlib
    one_year = df.Close['2021']
    groups = one_year.groupby(pd.Grouper(freq='M'))
    months = pd.concat([pd.DataFrame(x[1].values) for x in groups], axis=1)
    months.columns = range(1, months.count(axis=1).max()+1)
    months.boxplot()

    # B = plt.boxplot(months)
    # data = [item.get_ydata()[1] for item in B['whiskers']]
    # print(data)

    # print(months)
    plt.show()
    pass


def heatmap():
    one_year = df.Close['2021']
    # one_year = df.Close['2010':'2020']

    groups = one_year.groupby(pd.Grouper(freq='M'))
    months = pd.concat([pd.DataFrame(x[1].values) for x in groups], axis=1)
    months.columns = range(1, months.count(axis=1).max()+1)
    plt.matshow(months, interpolation=None, aspect='auto')
    plt.show()
    pass


def multiple_scatter_plots():
    lags = 8
    values = pd.DataFrame(df.Close.values)
    columns = [values]
    for i in range(1, (lags+1)):
        columns.append(values.shift(i))
    tmp = pd.concat(columns, axis=1)

    # label columns
    columns = ['t+1']
    for i in range(1, (lags+1)):
        columns.append(f't-{i}')
    tmp.columns = columns

    plt.figure(1)

    for i in range(1, lags+1):
        ax = plt.subplot(240+i)
        ax.set_title(f't+1 vs t-{i}')
        plt.scatter(x=tmp['t+1'].values, y=tmp[f't-{i}'].values)
    plt.show()


# fill_zero_vol('data/Gold_Daily.csv', 200)
# dt_feature()
# line_plot()
# stack_line_plot()
# histogram_kde()
# box_whisker()
# heatmap()

# # wtf is this: lag_plot and autocorrelation_plot
# lag_plot(df.Close)
# autocorrelation_plot(df.Close)
# plt.show()

# multiple_scatter_plots()
