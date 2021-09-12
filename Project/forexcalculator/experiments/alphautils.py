import os
import pandas as pd
import investpy as iv
from datetime import date
from forexflag import *
import numpy as np
import datetime
import pandas_ta
import re
from pathlib import Path
import matplotlib.pyplot as plt
import math
from operator import itemgetter
from getdata import *

markets = ['indices', 'currencies', 'commodities',
           'rates-bonds', 'equities', 'etfs', 'crypto']


def analysis_bond(filename):
    '''
    # https://stackoverflow.com/questions/32237769/defining-a-white-noise-process-in-python
    '''
    pass


def analysis_currency(filename):
    # folder : currenciesdata and combinedata
    pass


def analysis_index(filename):
    pass


def analysis_commodity(filename):
    pass


def analysis_intermarket(filename):
    pass


def analysis_etf(filename):
    pass


# -------------------------------------------------------
# timeframe and Fibonacci
# Day? how much
# Week? how much
# Month? how much
# https://www.quora.com/Is-anyone-making-money-by-using-deep-learning-in-trading
# https://www.google.com/search?q=lstm+machine+learning&oq=LSTM&aqs=chrome.1.0i131i433j0i20i263j0l8.3356j0j4&sourceid=chrome&ie=UTF-8
# https://www.google.com/search?q=Deep+Q+Learning&oq=Deep+Q+Learning&aqs=chrome..69i57j69i65l2j69i60j69i61j69i60.365j0j7&sourceid=chrome&ie=UTF-8
# https://www.google.com/search?sxsrf=ALeKk02YjANRzQ9U67-s9QZOb2JB99YgdQ:1622172808386&q=Using+CNNs+to+analyze+trading+charts&spell=1&sa=X&ved=2ahUKEwi85YfQuOvwAhUVO3AKHS8iD0oQBSgAegQIARAw&biw=960&bih=915
# Currencies Heat Map
# https://www.investing.com/tools/currency-heatmap


def currenciesheatmap():
    # use Xy or smt???
    # output or ... bổ trợ cho cái khác ???
    pass


# Forex Volatility: -> calculte expected pips and most suitable pair
# https://www.investing.com/tools/forex-volatility-calculator
def vol_sort(volume, order):
    return {k: v for k, v in sorted(volume.items(),
                                    key=itemgetter(order), reverse=True)}


def inner_vol_handle(args):
    quote, df, index, bias, enum = args
    dict_ = {}
    for num, name in enumerate(enum):
        temp = df.loc[index == num+bias]
        dict_[name] = temp['Pips'].mean()
    return dict_


def add_week_of_month(df):
    df['Week'] = pd.to_numeric(df.index.day/7)
    df['Week'] = df['Week'].apply(lambda x: math.ceil(x))
    return df


def forexvolatility(pairs, timeframe='Daily', periods=10):
    vols = {}
    timeframe_vol = {}
    WEEK_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    MONTH_WEEKS = ['1st', '2nd', '3rd', '4th', '5th']
    YEAR_MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                   'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for quote in pairs:
        # modify read file
        df = pd.read_csv(f'investpy/currenciesdata/{quote}_{timeframe}.csv')
        df = df.iloc[-periods:]
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Monthly/ Weekly/ Daily Volatility
        df['Vol'] = ((df['High']-df['Low'])/df['Low']*100).abs()
        if 'JPY' in quote or 'XAG' in quote:
            df['Pips'] = ((df['High']-df['Low'])*100).abs()
        elif 'XAU' in quote:
            df['Pips'] = ((df['High']-df['Low'])*10).abs()
        else:
            df['Pips'] = ((df['High']-df['Low'])*10000).abs()
        vols.setdefault(quote, [df['Pips'].mean(), df['Pips'].std(),
                                df['Vol'].mean(), df['Vol'].std()])
        # vols.setdefault(quote, df['Pips'].mean())

        df['Year'] = df.index.year
        df['Month'] = df.index.month
        df = add_week_of_month(df)

        # Weekday Volatility In Pips
        if timeframe == "Daily":
            tmp = inner_vol_handle(
                (quote, df, df.index.dayofweek, 0, WEEK_DAYS))

        # Monthweek Volatility In Pips
        elif timeframe == "Weekly":
            tmp = inner_vol_handle(
                (quote, df, df['Week'], 1, MONTH_WEEKS))

        # Yearmonth Volatility In Pips
        else:
            tmp = inner_vol_handle(
                (quote, df, df['Month'], 1, YEAR_MONTHS))
        timeframe_vol.setdefault(quote, tmp)

        # Hourly Volatility Pips/GMT Hours

        # # Economic/ markets events
        # markethours()
        # economiccalendar()

        # rate
        # khác biệt cố hữu trong các động lực kinh tế của mỗi quốc gia
        # -> xu hướng biến động nhiều hơn
        # get_commodities / services (majors)
        # Most agricultura/ commodities such as oil are priced in U.S. dollars
        # Try to draw a chart like this for 8 currencies
        # anti-U.S. dollar or pro-U.S. dollar (kháng/ hỗ Dollar)
        # https://www.babypips.com/learn/forex/crosses-present-more-trading-opportunities
        majors = ['GBP/USD', 'EUR/USD', 'USD/CHF', 'USD/JPY']
        commodity_pairs = ['AUD/USD', 'USD/CAD', 'NZD/USD']

        # cặp chéo
        # https://www.babypips.com/learn/forex/cleaner-trends-and-ranges
        majorcrosses = ['EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'GBP/JPY']
        minorcrosses = ['AUD/CHF', 'AUD/JPY', 'CAD/CHF', 'CAD/JPY',
                        'CHF/JPY', 'EUR/AUD', 'EUR/CAD', 'EUR/NZD',
                        'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD',
                        'NZD/CHF', 'NZD/JPY']
    # improve return json
    return df, vol_sort(vols, 1), timeframe_vol


# improve 1 candle vs multicandle (2 or more)
def fibocalculator(source="investpy/currenciesdata/", quotes='USDCHF',
                   interval='Monthly', periods=15):
    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
    low = df['Low'].min()
    high = df['High'].max()
    # get index
    last_pos = df.index.tolist()[len(df)-1]
    low_index, high_index = df.loc[df['Low'] ==
                                   low].index, df.loc[df['High'] == high].index
    isUptrend = True if (high_index - low_index > 0) else False
    fiboret_level = (0.236, 0.382, 0.5,
                     0.618, 0.707, 0.786, 0.887)
    fiboexp_level = (-0.382, -0.236, 0, 0.236, 0.5,
                     0.618, 0.786, 1, 1.272, 1.618)
    # process uptrend price level
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
    return (price_ret, price_exp, isUptrend)

# Pivot Point Calculator
# https://www.investing.com/tools/pivot-point-calculator


def round_nums(arr):
    res = []
    for num in arr:
        res.append(round(num, 4))
    return res


def pivotpointcalculator(pivotType='Fibonacci',
                         source='investpy/currenciesdata/',
                         quotes='USDCHF', interval='Monthly'):
    ret = []
    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    pOpen, pHigh, pLow, pClose = df.iloc[-1:, 1:5].values.tolist()[0]
    # Classic
    if pivotType is 'Classic':
        pp = (pHigh + pLow + pClose) / 3
        S1 = pp*2 - pHigh
        S2 = pp - (pHigh-pLow)
        S3 = pp - 2*(pHigh-pLow)

        R1 = pp*2 - pLow
        R2 = pp + (pHigh-pLow)
        R3 = pp + 2*(pHigh-pLow)

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # Fibonacci
    if pivotType is 'Fibonacci':
        pp = (pHigh + pLow + pClose) / 3

        R1 = pp + ((pHigh-pLow)*0.382)
        R2 = pp + ((pHigh-pLow)*0.618)
        R3 = pp + ((pHigh-pLow)*1)

        S1 = pp - ((pHigh-pLow)*0.382)
        S2 = pp - ((pHigh-pLow)*0.618)
        S3 = pp - ((pHigh-pLow)*1)

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # Camarilla
    if pivotType is 'Camarilla':
        pp = (pHigh + pLow + pClose) / 3

        S1 = pClose - ((pHigh-pLow) * 1.0833)
        S2 = pClose - ((pHigh-pLow) * 1.1666)
        S3 = pClose - ((pHigh-pLow) * 1.25)
        S4 = pClose - ((pHigh-pLow) * 1.5)

        R1 = pClose + ((pHigh-pLow) * 1.0833)
        R2 = pClose + ((pHigh-pLow) * 1.1666)
        R3 = pClose + ((pHigh-pLow) * 1.25)
        R4 = pClose + ((pHigh-pLow) * 1.5)

        ret = round_nums([R4, R3, R2, R1, pp, S1, S2, S3, S4])
        print(ret)
    # Woodie's
    if pivotType is 'Woodie':
        pp = (pHigh + pLow + 2*pClose) / 4

        R1 = 2*pp - pLow
        R2 = pp + pHigh - pLow
        R3 = (pHigh + 2 * (pp - pLow))

        S1 = 2*pp - pHigh
        S2 = pp - pHigh + pLow
        S3 = (pLow - 2 * (pHigh - pp))

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # DeMark's
    if pivotType is 'DeMark':
        if pClose > pOpen:
            X = 2*pHigh + pLow + pClose
        elif pClose < pOpen:
            X = pHigh + 2*pLow + pClose
        else:
            X = pHigh + pLow + 2*pClose
        pp = X/4
        R1 = X/2 - pLow
        S1 = X/2 - pHigh

        ret = round_nums([R1, pp, S1])
        print(ret)
    return ret


# pivotpointcalculator(pivotType='Classic', source=currency_path,
#                      quotes='XAUUSD', interval='Daily')

def inner_volatility(source='investpy/currenciesdata/', quotes='USDCHF',
                     interval='Monthly', periods=6):

    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
    # pct change
    df['HLL'] = (df['High']-df['Open'])/df['Open']*100
    df['HOL'] = (df['High']-df['Open'])/df['Low']*100
    df['COO'] = (df['Close']-df['Open'])/df['Open']*100
    df['COL'] = (df['Close']-df['Open'])/df['Low']*100
    # entire lenght
    df['HLL'] = (df['High']-df['Low'])/df['Low']*100
    df['HLO'] = (df['High']-df['Low'])/df['Open']*100
    df['CLL'] = (df['Close']-df['Low'])/df['Low']*100
    df['CLO'] = (df['Close']-df['Low'])/df['Open']*100
    # # bull/ bear domination all around
    # df['HCC'] = (df['High']-df['Close'])/df['Close']*100
    # df['PCT'] = (df['Close']-df['Open'])/df['Close']*100

    df = df[-periods:]
    df.drop(['Open', 'High', 'Low', 'Close'], axis=1, inplace=True)
    df.set_index('Date', inplace=True)
    df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_vols.csv')


# ----------------------------------
# https://www.investing.com/tools/market-hours


def markethours():
    '''
    # Overlaps time: Overlapping trading hours contain
    # Volume increase in specific session
    '''
    sessions = ['AUS', 'ASIA', 'EU', 'US']
    now = datetime.datetime.now()
    # split data to minor timeframe

    # read api then check session time
    # print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # the highest volume of traders.

    # Phiên Á thì sao?? AUD, NZD

    # Phiên London

    # Phiên Mỹ

    pass


def cal_mm():
    '''Sharpe Ratio'''
    # https://quant.stackexchange.com/questions/39839/how-to-calculate-sharpe-ratio-from-returns
    # https://www.linkedin.com/pulse/calculating-portfolio-sharpe-ratio-python-f%C3%A1bio-neves/

    '''Kelly's Criterion'''
    # https://www.researchgate.net/publication/320180198_Kelly's_Criterion_in_Portfolio_Optimization_A_Decoupled_Problem

    '''rebalance portfolio'''
    # https://www.youtube.com/watch?v=vuZpIkTPATE&ab_channel=Darwinex
    # https://python-bloggers.com/2020/02/rebalancing-really-2/
    # https://www.quantstart.com/articles/monthly-rebalancing-of-etfs-with-fixed-initial-weights-in-qstrader/
    # https://stackoverflow.com/questions/30745160/portfolio-rebalancing-with-bandwidth-method-in-python
    pass


def preprocessing():
    '''
    fillna by mode or mean value
    '''
    # # show columns params
    # print(data['train_class'].describe())

    # # fillna with mode
    # data['train_class'] = data['train_class'].fillna(
    #     data['train_class'].mode().iloc[0])

    # # fillna with mean
    # data['price'] = data.groupby('fare').transform(
    # lambda x: x.fillna(x.mean()))

    # # Bear Bull identify idea:
    # https://towardsdatascience.com/estimating-probabilities-with-bayesian-modeling-in-python-7144be007815
    # https://docs.pymc.io/notebooks/posterior_predictive.html

    # # consider: long/ short in a series of trial
    # data = stats.bernoulli.rvs(0.5, size=number_of_trial[-1])
    # print(data)
    pass
