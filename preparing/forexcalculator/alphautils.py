import os
import quandl
import pandas as pd
import investpy as iv
import datamine as cme
from fredapi import Fred
from datetime import date
from forexflag import *
import numpy as np
import datetime
import pandas_ta
import re
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf

style.use('fivethirtyeight')

quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'
fred = Fred(api_key='fc9753be1dab36c5773160e0fdf05ba7')

# ---------- investpy items -----------
markets = ['indices', 'currencies', 'commodities',
           'rates-bonds', 'equities', 'etfs', 'crypto']
PCT_TYPES = ['COO', 'HLL', 'HCC', 'OLL', 'HOL', 'CLO', 'COL', 'HLO']
# global starttime
starttime = '01/01/2010'
today = date.today().strftime("%d/%m/%Y")

# --------- investpy market folder path
index_path = f'investpy/{markets[0]}data'
currency_path = f'investpy/{markets[1]}data'
commodity_path = f'investpy/{markets[2]}data'
bond_path = f'investpy/{markets[3]}data'
equity_path = f'investpy/{markets[4]}data'
etf_path = f'investpy/{markets[5]}data'
crypto_path = f'investpy/{markets[6]}data'
combine_path = 'investpy/combinedata/'
# --------- end investpy market folder path
# ----------------------------------------------------------
# common function: for RAW DATA
# ----------------------------------------------------------


def analysis_currency(filename):
    # folder : currenciesdata and combinedata
    pass


def analysis_bond(filename):
    # processing data: bond spread
    # https://pypi.org/project/nelson-siegel-svensson/0.1.0/
    # https://pypi.org/project/yield-curve-dynamics/
    pass


def analysis_index(filename):
    pass


def analysis_commodity(filename):
    pass


def analysis_intermarket(filename):
    pass


def combine_params(filename, params, interval):
    check_data(combine_path, f'{filename}_{interval}.csv')
    main_df = pd.DataFrame()
    for ticker, info in params.items():
        ticker = replace_specchar(ticker, '/', '')
        df = pd.read_csv(f'investpy/{info[0]}data/{ticker}_{interval}.csv')
        df.set_index('Date', inplace=True)
        df.rename(columns={'Close': ticker}, inplace=True)
        df = df.filter([ticker])
        main_df = df if main_df.empty else main_df.join(df, how='outer')
        # fillna or dropna
    main_df.to_csv(combine_path + f'{filename}_{interval}.csv')


# dump same thing in an list
def dump_things(filename, things, intervals):
    for thing, info in things.items():
        market, country, infunc = info
        for interval in intervals:
            infunc(thing, interval, country)
    for interval in intervals:
        combine_params(filename, things, interval)


def make_market(params, isReload=True):
    intervals = ['Daily', 'Weekly', 'Monthly']
    filename, data, info, outfunc = params
    thing_pairs = dict(zip(data, info))
    if isReload:
        dump_things(filename, thing_pairs, intervals)
    else:
        outfunc(combine_path + f'{filename}_{interval}.csv')
        # read data


def norm_data():
    # numpy processing
    pass


def append_preparing(path):
    df = pd.read_csv(path)
    cur_date = df[-1:]['Date'].tolist()[0]
    df = df[:-1]
    df.set_index('Date', inplace=True)
    df.to_csv(path)
    if cur_date == date.today().strftime('%Y-%m-%d'):
        return None
    else:
        dayRe = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
        mo = dayRe.search(cur_date)
        starttime = mo.group(3) + "/" + mo.group(2) + "/" + mo.group(1)
        return starttime


def check_data(folder_part, filename):
    if os.path.exists(folder_part+filename):
        print(f'{folder_part+filename} already exist!')
        return True
    else:
        if os.path.exists(folder_part):
            print(f'{folder_part} already exist!')
        else:
            os.makedirs(folder_part)
        return False


def replace_specchar(obj, char, newchar):
    tmp = obj
    if char in obj:
        tmp = obj.replace(char, newchar)
    return tmp


# ----------------------------------------------------------
# common function: for RAW DATA
# ----------------------------------------------------------
# Fred part --------------------------------
def get_economic_fred(currency, item):
    economic_path = f'fred/{currency}/'
    # check_data(economic_path)
    df = fred.get_series(item,
                         observation_start=starttime, observation_end=today)
    print(df.tail())
    pass


# quandl part --------------------------------
def get_economic_quandl(currency, field, item):
    economic_path = f'quandl/{currency}/'
    check_data(economic_path, f'{item}.csv')
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    print(df.tail())
    # df.to_csv(economic_path + f'{item}.csv')


def get_quandl_data(market, field, currency, item):
    # need optimize folder name
    quandl_part = f'quandl/{market}data/{currency}/'
    # create folder
    check_data(quandl_part, f'{item}.csv')
    # request data then save to file, start_date, end_date
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    print(df.tail())
    # df.to_csv(quandl_part + f'{item}.csv')
    # return quandl_part + f'{item}.csv'


def get_yahoofinance_data():
    # Data Model: [date, open, high, low, close, volume, currency]
    # check types
    # use true get historical data function
    gold = yf.download('GC=F', start="2021-01-01", end="2021-06-08")
    # print(type(gold))
    gold.to_csv('yahoofinance/gold.csv')
    pass


# get_yahoofinance_data()


def read_data(file):
    df = pd.read_csv(file)
    # return None


# --------------------- indices ----------------------------------
def get_indices(index, interval, country):
    index_ = replace_specchar(index, '/', '_')
    path = index_path + f'/{index_}_{interval}.csv'
    if not check_data(index_path, f'/{index_}_{interval}.csv'):
        df = iv.indices.get_index_historical_data(
            index=index, country=country, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df.to_csv(path)
    else:
        new_start = append_preparing(path)
        if new_start is not None:
            df = iv.indices.get_index_historical_data(
                index=index, country=country, from_date=new_start,
                to_date=today, order='ascending', interval=interval)
            df.to_csv(path, mode='a', header=False)


def get_currency_indices(isReload=True):
    data = ['US Dollar Index', 'PHLX Euro',
            'PHLX Australian Dollar', 'PHLX Canadian Dollar',
            'PHLX Swiss Franc', 'PHLX British Pound',
            'PHLX Yen', 'PHLX New Zealand Dollar']
    info = [[markets[0], 'united states', get_indices]]*len(data)
    params = ['currencyindex', data, info, analysis_index]
    make_market(params, isReload)


# ------------------- bonds -----------------------------
def get_bonds(bond, interval, country):
    path = bond_path + f'/{bond}_{interval}.csv'
    if not check_data(bond_path, f'/{bond}_{interval}.csv'):
        df = iv.bonds.get_bond_historical_data(
            bond=bond, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df.to_csv(path)
    else:
        new_start = append_preparing(path)
        if new_start is not None:
            df = iv.bonds.get_bond_historical_data(
                bond=bond, from_date=new_start, to_date=today,
                order='ascending', interval=interval)
            df.to_csv(path, mode='a', header=False)


def cor_bond(isReload=True):
    data = ['Japan 10Y', 'Switzerland 10Y', 'Australia 10Y',
            'Canada 10Y', 'U.S. 10Y', 'Germany 10Y',
            'New Zealand 10Y', 'U.K. 10Y']
    info = [[markets[3], 'united states', get_bonds]]*len(data)
    params = ['cor_bond', data, info, analysis_bond]
    make_market(params, isReload)


# ----------- get_currency_cross_historical_data ---------
def get_forex(quote, interval, country):
    quote_ = replace_specchar(quote, '/', '')
    path = currency_path + f'/{quote_}_{interval}.csv'
    if not check_data(currency_path, f'/{quote_}_{interval}.csv'):
        # check latest data
        df = iv.currency_crosses.get_currency_cross_historical_data(
            currency_cross=quote, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df = df.iloc[:, :-1]
        df.to_csv(path)
    else:
        new_start = append_preparing(path)
        if new_start is not None:
            df = iv.currency_crosses.get_currency_cross_historical_data(
                currency_cross=quote, from_date=new_start, to_date=today,
                order='ascending', interval=interval)
            df = df.iloc[:, :-1]
            df.to_csv(path, mode='a', header=False)


def compare_gold(isReload=True):
    data = ['XAU/USD', 'XAU/EUR', 'XAU/GBP', 'XAU/CAD',
            'XAU/CHF', 'XAU/JPY', 'XAU/AUD', 'XAU/NZD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['xaupair', data, info, analysis_currency]
    make_market(params, isReload)


def compare_silver(isReload=True):
    data = ['XAG/USD', 'XAG/EUR', 'XAG/GBP', 'XAG/CAD', 'XAG/CHF', 'XAG/AUD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['xagpair', data, info, analysis_currency]
    make_market(params, isReload)


# ----------------------------IMPORTANT- commondity---
# ------------- get_commodity_historical_data ---------------
def get_commodities(commodity, interval, country):
    path = commodity_path + f'/{commodity}_{interval}.csv'
    if not check_data(commodity_path, f'/{commodity}_{interval}.csv'):
        df = iv.commodities.get_commodity_historical_data(
            commodity=commodity, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df.to_csv(path)
    else:
        new_start = append_preparing(path)
        if new_start is not None:
            df = iv.commodities.get_commodity_historical_data(
                commodity=commodity, from_date=new_start, to_date=today,
                order='ascending', interval=interval)
            df.to_csv(path, mode='a', header=False)


def calculate_grains(isReload=True):
    # https://www.investing.com/commodities/grains
    data = ['Rough Rice', 'US Soybean Oil',
            'US Soybean Meal', 'US Soybeans',
            'US Wheat', 'US Corn', 'Oats', 'London Wheat']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['grain', data, info, analysis_commodity]
    make_market(params, isReload)


def calculate_softs(isReload=True):
    # https://www.investing.com/commodities/softs
    data = ['US Coffee C', 'US Cotton #2',
            'US Sugar #11', 'Orange Juice',
            'US Cocoa', 'Lumber', 'London Cocoa',
            'London Coffee', 'London Sugar']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['soft', data, info, analysis_commodity]
    make_market(params, isReload)


# shortcut: filename + dataset
def calculate_meats(isReload=True):
    # https://www.investing.com/commodities/meats
    data = ['Live Cattle', 'Lean Hogs', 'Feeder Cattle']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['meat', data, info, analysis_commodity]
    make_market(params, isReload)


def calculate_metals(isReload=True):
    # https://www.investing.com/commodities/metals
    data = ['Gold', 'Silver', 'Copper', 'Palladium', 'Platinum',
            'Aluminum', 'Zinc', 'Lead', 'Nickel', 'Tin']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['metal', data, info, analysis_commodity]
    make_market(params, isReload)


def calculate_energies(isReload=True):
    # https://www.investing.com/commodities/energy
    data = ['Brent Oil', 'Crude Oil WTI',
            'London Gas Oil', 'Natural Gas',
            'Heating Oil', 'Carbon Emissions',
            'Gasoline RBOB']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['energy', data, info, analysis_commodity]
    make_market(params, isReload)


# ----------------Commondity index-------------------------
# https://www.investing.com/indices/thomson-reuters---jefferies-crb
def get_crb(isReload=True):
    get_indices('TR/CC CRB', 'world')


# ----------------Correlation-------------------------
# -------------------------------------
# AUD vs NZD (correlation)
def cor_aunz(isReload=True):
    data = ['PHLX Australian Dollar', 'PHLX New Zealand Dollar',
            'Australia 10Y', 'New Zealand 10Y']
    info = [[markets[0], 'united states', get_indices]] * \
        2 + [[markets[3], 'united states', get_bonds]]*2
    params = ['cor_aunz', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------
# USD vs CAD (correlation)
def cor_usca(isReload=True):
    data = ['US Dollar Index', 'PHLX Canadian Dollar',
            'U.S. 10Y', 'Canada 10Y']
    info = [[markets[0], 'united states', get_indices]] * \
        2 + [[markets[3], 'united states', get_bonds]]*2
    params = ['cor_usca', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------
# JPY vs CHF (correlation)
def cor_jpsw(isReload=True):
    data = ['PHLX Yen', 'PHLX Swiss Franc', 'Japan 10Y', 'Switzerland 10Y']
    info = [[markets[0], 'united states', get_indices]] * \
        2 + [[markets[3], 'united states', get_bonds]]*2
    params = ['cor_jpsw', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------
# GBP vs EUR (correlation)
def cor_ukeu(isReload=True):
    data = ['PHLX British Pound', 'PHLX Euro', 'U.K. 10Y', 'Germany 10Y']
    info = [[markets[0], 'united states', get_indices]] * \
        2 + [[markets[3], 'united states', get_bonds]]*2
    params = ['cor_ukeu', data, info, analysis_intermarket]
    make_market(params, isReload)
# -------------------------------------------------------
# timeframe and Fibonacci
# Day? how much
# Week? how much
# Month? how much
# https://www.quora.com/Is-anyone-making-money-by-using-deep-learning-in-trading
# https://www.google.com/search?q=lstm+machine+learning&oq=LSTM&aqs=chrome.1.0i131i433j0i20i263j0l8.3356j0j4&sourceid=chrome&ie=UTF-8
# https://www.google.com/search?q=Deep+Q+Learning&oq=Deep+Q+Learning&aqs=chrome..69i57j69i65l2j69i60j69i61j69i60.365j0j7&sourceid=chrome&ie=UTF-8
# https://www.google.com/search?sxsrf=ALeKk02YjANRzQ9U67-s9QZOb2JB99YgdQ:1622172808386&q=Using+CNNs+to+analyze+trading+charts&spell=1&sa=X&ved=2ahUKEwi85YfQuOvwAhUVO3AKHS8iD0oQBSgAegQIARAw&biw=960&bih=915
# ----------------- T.B.D -----------------
# get last row date, check if is up to date-> read data, not write
# -------------------------------------------------------


def get_bond_quandl(currency, data, key):
    # ------------- quandl part-----------
    # get data and save, LACK Datetime range for data
    for value in data[key]:
        get_quandl_data(markets[3], key, currency, value)


def analysis_bond_quandl(params):
    # read saved data then analysis or return
    # need loop
    item = data[key][0]
    part = f'{currency_path}{currency}/{item}.csv'
    # ----------------------
    # read_data(part)

    # ----------------------
    # plot

    # ----------------------
    # predict

    # ----------------------
    # corr

    # ----------------------


# Currencies Heat Map
# https://www.investing.com/tools/currency-heatmap
def currenciesheatmap():
    # use Xy or smt???
    # output or ... bổ trợ cho cái khác ???
    pass


# Forex Volatility: -> calculte expected pips and most suitable pair
# https://www.investing.com/tools/forex-volatility-calculator
def forexvolatility(numofweeks, timeframe):
    # timeframe: x months after today time
    # numofweeks: slice of time in last timeframe
    # numofweeks càng nhỏ thì biến động càng lớn, ??? chọn bnhieu để
    # hợp vs day trading

    # definition:
    # volatility of a pair: standard deviation from the mean
    # higher volatility/ higher riskier
    # optimize trading strategy
    # which most volatile "pairs/ HOURS/ days/" week

    # Economic/ markets events
    markethours()
    economiccalendar()

    # rate

    # khác biệt cố hữu trong các động lực kinh tế của mỗi quốc gia
    # -> xu hướng biến động nhiều hơn
    # get_commodities / services (majors)
    # Most agricultural and commodities such as oil are priced in U.S. dollars
    # Try to draw a chart like this for 8 currencies
    # anti-U.S. dollar or pro-U.S. dollar (kháng/ hỗ Dollar)
    # https://www.babypips.com/learn/forex/crosses-present-more-trading-opportunities
    majors = ['GBP/USD', 'EUR/USD', 'USD/CHF', 'USD/JPY']
    commodity_pairs = ['AUD/USD', 'USD/CAD', 'NZD/USD']

    # cặp chéo
    # https://www.babypips.com/learn/forex/cleaner-trends-and-ranges
    # sometime it's more smoother, easier for trade
    majorcrosses = ['EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'GBP/JPY']
    minorcrosses = ['AUD/CHF', 'AUD/JPY', 'CAD/CHF', 'CAD/JPY',
                    'CHF/JPY', 'EUR/AUD', 'EUR/CAD', 'EUR/NZD',
                    'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD',
                    'NZD/CHF', 'NZD/JPY']
    # Hourly Volatility Pips/GMT Hours

    # Daily Volatility In Pips

    # Weekday Volatility In Pips

    # Monthweek Volatility In Pips

    # Yearmonth Volatility In Pips

    pass


# Fibonacci Calculator:
# https://www.investing.com/tools/fibonacci-calculator
def fibocalculator(start, end):
    # lack of interval
    start = datetime.datetime.strptime(start, "%d/%m/%Y")
    end = datetime.datetime.strptime(end, "%d/%m/%Y")
    # read data
    df = pd.read_csv('investpy/currenciesdata/EURGBP_Daily.csv')
    # convert date
    df['Date'] = pd.to_datetime(df['Date'])
    # get data range
    df = df[(df['Date'] >= start) & (df['Date'] <= end)]
    # define High/ Low/ Custom
    low = df['Low'].min()
    high = df['High'].max()
    isUptrend = True if (df.loc[df['High'] == high].index -
                         df.loc[df['Low'] == low].index > 0) else False
    inner_start = df.loc[df['High'] == high]['Date'].tolist()[0]
    inner_df = df[(df['Date'] > inner_start) & (df['Date'] <= end)]
    custom = inner_df['Low'].min()
    # print(low, high, custom)
    fiboret_level = (0.236, 0.382, 0.5,
                     0.618, 0.707, 0.786, 0.887)
    # T.B.D
    fiboexp_level = (-0.382, -0.236, 0, 0.236, 0.5,
                     0.618, 0.786, 1, 1.272, 1.618)
    if isUptrend:
        price_ret = [round((1-level)*(high-low) + low, 4)
                     for level in fiboret_level]
        price_ret.reverse()
    else:
        price_ret = [round(level*(high-low) + low, 4)
                     for level in fiboret_level]
    price_ret.append(high)
    price_ret.insert(0, low)
    return (price_ret, isUptrend)


# fibocalculator('07/05/2021', '12/05/2021')
# fibocalculator('05/04/2021', '14/04/2021')


# Pivot Point Calculator
# https://www.investing.com/tools/pivot-point-calculator
def pivotpointcalculator(pivotType, ohlc):
    pOpen, pHigh, pLow, pClose = ohlc
    # Classic
    if pivotType is 'Classic':
        pp = (pHigh + pLow + pClose) / 3
        S1 = pp*2 - pHigh
        S2 = pp - (pHigh-pLow)
        R1 = pp*2 - pLow
        R2 = pp + (pHigh-pLow)
        return [round(num, 2) for num in [pp, R1, R2, S1, S2]]
    # Fibonacci
    if pivotType is 'Fibonacci':
        pp = (pHigh + pLow + pClose) / 3

        R1 = pp + ((pHigh-pLow)*0.382)
        R2 = pp + ((pHigh-pLow)*0.618)
        R3 = pp + ((pHigh-pLow)*1)

        S1 = pp - ((pHigh-pLow)*0.382)
        S2 = pp - ((pHigh-pLow)*0.618)
        S3 = pp - ((pHigh-pLow)*1)
        return [round(num, 2) for num in [pp, R1, R2, R3, S1, S2, S3]]
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
        return [round(num, 2) for num in [pp, R1, R2, R3, R4, S1, S2, S3, S4]]
    # Woodie's
    if pivotType is 'Woodie':
        pp = (pHigh + pLow + 2*pClose) / 4

        R1 = 2*pp - pLow
        R2 = pp + pHigh - pLow

        S1 = 2*pp - pHigh
        S2 = pp - pHigh - pLow
        return [round(num, 2) for num in [pp, R1, R2, S1, S2]]
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
        return [round(num, 2) for num in [pp, R1, S1]]
    # print(pivotpointcalculator('DeMark', df.iloc[-1:, 1:5].
    # values.tolist()[0]))


def calculate_ohcl(ohlc):
    pctValues = {}
    pOpen, pHigh, pLow, pClose = ohlc
    # pct change
    pctValues['COO'] = round((pClose-pOpen)*100/pOpen, 5)
    # entire lenght
    pctValues['HLL'] = round((pHigh-pLow)*100/pLow, 5)
    # short edge
    pctValues['HCC'] = round((pHigh-pClose)*100/pClose, 5)
    # long edge
    pctValues['CLL'] = round((pClose-pLow)*100/pLow, 5)
    # bull/ bear domination all around
    pctValues['HOL'] = round((pHigh-pOpen)*100/pLow, 5)
    # bull/ bear Adj domination
    pctValues['CLO'] = round((pClose-pLow)*100/pOpen, 5)
    # real body
    pctValues['COL'] = round((pClose-pOpen)*100/pLow, 5)
    # strength volitality
    pctValues['HLO'] = round((pHigh-pLow)*100/pOpen, 5)
    return pctValues


def test():
    df = pd.read_csv('investpy/currenciesdata/XAUUSD_Daily.csv')
    # pct change
    df['COO'] = (df['Close']-df['Open'])/df['Open']*100
    # entire lenght
    df['HLL'] = (df['High']-df['Low'])/df['Low']*100
    # short edge
    df['HCC'] = (df['High']-df['Close'])/df['Close']*100
    # long edge
    df['CLL'] = (df['Close']-df['Low'])/df['Low']*100
    # bull/ bear domination all around
    df['HOL'] = (df['High']-df['Open'])/df['Low']*100
    # bull/ bear Adj domination
    df['CLO'] = (df['Close']-df['Low'])/df['Open']*100
    # real body
    df['COL'] = (df['Close']-df['Open'])/df['Low']*100
    # strength volitality
    df['HLO'] = (df['High']-df['Low'])/df['Open']*100
    # pct chage day previous close
    df['PCT'] = (df['Close']-df.shift()['Close'])/df['Close']*100
    df.drop(['Open', 'High', 'Low', 'Close'], axis=1, inplace=True)
    df.set_index('Date', inplace=True)
    print(df.tail())
    # ohlc = df[-1:].values.tolist()[0][1:5]


# test()
# 1. check file exist or not
# 2. download new
# -------------------------------------------------------------------


# financial-calendars
# https://www.investing.com/tools/financial-calendars
# ----------------------------------
# https://www.investing.com/tools/market-hours
def markethours():
    # Overlaps time: Overlapping trading hours contain
    # the highest volume of traders.

    # Phiên Á thì sao?? AUD, NZD

    # Phiên London

    # Phiên Mỹ

    pass


# ----------------------------------
# https://www.investing.com/economic-calendar/
def economiccalendar():
    # https://www.investing.com/central-banks/fed-rate-monitor
    # iv.news.economic_calendar()

    pass
