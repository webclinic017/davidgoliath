import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import boxcox
import investpy as iv
import datetime
from settings import *
import random
from pandas.plotting import lag_plot, autocorrelation_plot

import os
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")


def binominal_check():
    pass


def retrace_func():
    # window

    # in that window, retrace is bull or bear candle

    # lenght of retrace point compare with high low

    # custom upsampling regression
    # - day to h1/ h4/ h8/ h12
    # - market hours (session)
    # - economic calendar

    pass


# rolling fibocalculator:
# https://stackoverflow.com/questions/40954560/pandas-rolling-apply-custom
# improve 1 candle vs multicandle (2 or more)
def fibocalculator(source="investpy/currenciesdata/", quotes='GBPUSD',
                   interval='Daily', periods=20):

    fiboret_level = (0.236, 0.382, 0.5,
                     0.618, 0.707, 0.786, 0.887)
    fiboexp_level = (-0.382, -0.236, 0, 0.236, 0.5,
                     0.618, 0.786, 1, 1.272, 1.618)

    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    # get period data range and low/high
    df = df.iloc[-periods-1:]

    low = df['Low'].min()
    high = df['High'].max()

    # One candle
    if periods == 1:
        # statistic retrace then random choose in a range

        # interpolation then randomize a retrace point
        pass

    # statistic retrace then random choose in a range

    # window with function

    # multi candles
    low_index = df.loc[df['Low'] == low].index
    high_index = df.loc[df['High'] == high].index

    last_pos = df.index.tolist()[len(df)-1]
    print(df.tail(1).index.values[0])
    # '''
    isUptrend = True if (high_index - low_index > 0) else False

    # process uptrend price level (multi candles or one candle)
    print(isUptrend)
    if isUptrend:
        high_pos = high_index.tolist()[0]
        retrace = df[high_pos-last_pos-1:]['Low'].min()
        # Fibonnaci path
        price_ret = [round((1-level)*(high-low) + low, 4)
                     for level in fiboret_level]
        price_ret.reverse()
        price_ret.append(high)
        price_ret.insert(0, low)

        # Fibonacci Expansion:
        price_exp = [round(level*(high-low) + retrace, 4)
                     for level in fiboexp_level]
    # downtrend
    else:
        low_pos = low_index.tolist()[0]
        retrace = df[low_pos-last_pos-1:]['High'].max()
        # Fibonnaci path
        price_ret = [round(low + level*(high-low), 4)
                     for level in fiboret_level]
        price_ret.reverse()
        price_ret.append(low)
        price_ret.insert(0, high)

        # Fibonacci Expansion:
        price_exp = [round(retrace - level*(high-low), 4)
                     for level in fiboexp_level]
    # return (price_ret, price_exp, isUptrend)
    # '''


def account_linking():
    '''linking to get mt4 infomation'''
    pass


def process_monte_carlo():
    '''Monte Carlo'''
    pass


def process_markov_chain():
    '''Markov Chain'''
    pass


def pp_statistics():
    '''pivot point statistics'''
    pass


def simulate_models():
    # 8-sided dice

    # Binominal Model
    pass


def changed_corr():
    '''get 2 most pos/neg correlation dataset and ...'''
    pass


def bullbear_classifier():
    pass


def price_pattern():
    # normal price

    # mean price

    # median price

    # std

    # skew

    # outliner

    # residual

    pass


def volume_pattern():
    # normal price

    # mean price

    # median price

    # std

    # skew

    # outliner

    # residual

    pass


def custom_pivottbl():
    '''experiment pivot table'''
    pass


def custom_window():
    '''how window data improve traning result'''
    pass


def ds_script():
    '''dataset script'''
    pass


# fibocalculator()
def volume_fill():
    '''fill empty volume data based on month and week volume data'''
    pass


# get data --------------------------
def get_data():
    today = datetime.datetime.today().strftime("%d/%m/%Y")
    df = iv.commodities.get_commodity_historical_data(
        'Gold', '01/01/2010', today)
    # df.to_csv('data/Gold_Daily.csv')
    # process zero volume values --------------------------
    # df = pd.read_csv('data/Gold_Daily.csv')
    # df['Date'] = pd.to_datetime(df['Date'])
    # df.set_index('Date', inplace=True)

    # https://www.geeksforgeeks.org/python-pandas-dataframe-where/

    # volume_fill
    # T.B.D

    rd_period = 200
    zero_df = df.loc[df['Volume'] == 0]
    for item in zero_df.index:
        index = df.index.get_loc(item)
        post_df = df.iloc[index-rd_period:index]
        df.at[item, 'Volume'] = post_df['Volume'].mean()

    df.drop(['Currency'], axis=1, inplace=True)
    df['hl_change'] = (df['High']-df['Low'])/df['Low']
    df['cl_change'] = (df['Close']-df['Low'])/df['Low']
    df['pct_change'] = df['Close'].pct_change()
    df['vol_change'] = df['Volume'].pct_change()

    # # test zero exist
    # print(np.count_nonzero(df['Close'].values))
    # print(np.count_nonzero(df['Volume'].values))
    df.to_csv('data/Gold_Daily_fill.csv')


# read data
def read_data():
    df = pd.read_csv('data/Gold_Daily_fill.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    # print(df.tail(10))
    temp = pd.DataFrame()
    temp['date'] = [df.index[i] for i in range(len(df))]
    # temp['date'] = pd.to_datetime(temp['date'])
    temp.set_index('date', inplace=True)

    temp['close'] = [df.Close[i] for i in range(len(df))]
    temp['vol'] = [df.Volume[i] for i in range(len(df))]
    temp['hl_change'] = [df.hl_change[i] for i in range(len(df))]
    temp['cl_change'] = [df.cl_change[i] for i in range(len(df))]

    # df.drop(['Currency'], axis=1, inplace=True)
    # print(df.tail(10))
    # print(temp.tail(10))

    '''
    pct_neg = np.sum((temp['pct_change'] < 0).values.ravel())
    pct_pos = np.sum((temp['pct_change'] > 0).values.ravel())
    proba_negpct = pct_neg/(pct_pos+pct_neg)

    vol_neg = np.sum((temp['vol_change'] < 0).values.ravel())
    vol_pos = np.sum((temp['vol_change'] > 0).values.ravel())
    proba_negvol = vol_neg/(vol_pos+vol_neg)
    '''

    # fibonacci

    # pivot

    # news

    return temp


# date-time feature
def dt_feature():
    temp['day'] = [df.index[i].day for i in range(len(df))]
    temp['month'] = [df.index[i].month for i in range(len(df))]
    temp['year'] = [df.index[i].year for i in range(len(df))]
    # print(temp)


# lag feature
def lag_feature():
    temp['close_lag-2'] = temp['close'].shift(-2)
    temp['close_lag-1'] = temp['close'].shift(-1)
    temp['close_lag+1'] = temp['close'].shift(1)

    temp['vol_lag-2'] = temp['vol'].shift(-2)
    temp['vol_lag-1'] = temp['vol'].shift(-1)
    temp['vol_lag+1'] = temp['vol'].shift(1)
    # print(temp.tail(10))
    pass


def window_feature(rd_num=200):
    choices = (random.randint(2, rd_num) for _ in range(rd_num))
    choice = list(choices)
    window_close = temp['close'].shift(1).rolling(window=random.choice(choice))
    window_vol = temp['vol'].shift(1).rolling(window=random.choice(choice))
    # print(window_close, window_vol)
    temp['mean_close'] = window_close.mean()
    temp['mean_vol'] = window_vol.mean()
    # print(temp)
    pass


# dt_feature()
# lag_feature()
# window_feature()
'''
# not useful
def parser(x):
    return datetime.datetime.strptime('190'+x, '%Y-%m')
'''


def resample_up():
    tmp = read_data()[-15:]['hl_change']
    # using 8 hour chart
    upsampled = tmp.resample(rule='8H', closed='left', label='left').mean()
    interpolated = upsampled.interpolate(method='linear')
    # interpolated = upsampled.interpolate(method='spline', order=5)
    # print(interpolated)

    # exactly time
    interpolated.plot()
    plt.show()


# important (D->W possible)
def resample_down():
    tmp = read_data()[-62:]['close']
    downsampled = tmp.resample(rule='W').mean()
    interpolated = downsampled.interpolate(method='linear')
    # print(interpolated)

    # exactly time
    interpolated.plot()
    plt.show()
    pass


# remove noise and improve the signal
def power_transform():
    tmp = read_data()[-62:]['hl_change']
    plt.figure(1)

    plt.subplot(221)
    plt.plot(tmp)
    plt.subplot(222)
    plt.hist(tmp)

    # # when and how square root transform.
    # # - when the trend is quadratic growth.

    # transform = np.sqrt(tmp)
    # plt.subplot(223)
    # plt.plot(transform)
    # plt.subplot(224)
    # plt.hist(transform)

    # # when use log transform
    # # - trends are exponential
    # # - values are positive and non-zero.

    # transform = np.log(tmp)
    # plt.subplot(223)
    # plt.plot(transform)
    # plt.subplot(224)
    # plt.hist(transform)

    # Box-Cox transform
    # - support square root and log

    transform, lam = boxcox(tmp)
    print(lam)
    plt.subplot(223)
    plt.plot(transform)
    plt.subplot(224)
    plt.hist(transform)

    plt.show()
    pass


def super_ma():
    df = pd.read_csv('data/Gold_Daily_fill.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low', 'Close', 'Volume',
            'vol_change'], axis=1, inplace=True)
    # print(df.tail())
    '''
    tmp = read_data()  # [-62:]['hl_change']

    temp = pd.DataFrame()

    rolling = tmp.close.rolling(window=3)
    rolling_mean = rolling.mean()
    temp['close_rolling_mean'] = rolling_mean

    rolling = tmp.vol.rolling(window=3)
    rolling_mean = rolling.mean()
    temp['vol_rolling_mean'] = rolling_mean

    rolling = tmp.hl_change.rolling(window=3)
    rolling_mean = rolling.mean()
    temp['hl_rolling_mean'] = rolling_mean

    rolling = tmp.cl_change.rolling(window=3)
    rolling_mean = rolling.mean()
    temp['cl_rolling_mean'] = rolling_mean

    # print(temp.tail(10))
    temp[-62:].plot()
    plt.show()
    '''
    df[-62:].plot()
    plt.show()
    pass


def fibo_cluster():
    pass


def custom_rsquared():
    pass


# super_ma()
# power_transform()
# resample_down()
# resample_up()
# get_data()
# read_data()
