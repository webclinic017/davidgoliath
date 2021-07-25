import os
import quandl
import pandas as pd
# from pandas.plotting import autocorrelation_plot
import investpy as iv
# import datamine as cme
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
# import yfinance as yf
# import seaborn as sns
# from inspect import getmembers

style.use('fivethirtyeight')

quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'
fred = Fred(api_key='fc9753be1dab36c5773160e0fdf05ba7')

# ---------- investpy items -----------
markets = ['indices', 'currencies', 'commodities',
           'rates-bonds', 'equities', 'etfs', 'crypto']
# global starttime
starttime = '01/01/2010'
today = date.today().strftime("%d/%m/%Y")

# --------- investpy market folder path
index_path = f'investpy/{markets[0]}data/'
currency_path = f'investpy/{markets[1]}data/'
commodity_path = f'investpy/{markets[2]}data/'
bond_path = f'investpy/{markets[3]}data/'
equity_path = f'investpy/{markets[4]}data/'
etf_path = f'investpy/{markets[5]}data/'
crypto_path = f'investpy/{markets[6]}data/'
combine_path = 'investpy/combinedata/'
analysis_path = 'investpy/analysisdata/'
# --------- end investpy market folder path
# ----------------------------------------------------------
# common function: for RAW DATA
# ----------------------------------------------------------
# if __name__ == "__main__":


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


def calculate_stats(source=combine_path, periods=13,
                    quotes='cor_bond', interval='Daily'):
    df = pd.read_csv(source+f'{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]

    df['Mean'] = df.iloc[:, 1:5].mean(axis=1)
    df['Std'] = df.iloc[:, 1:5].std(axis=1)
    df['Skew'] = df.iloc[:, 1:5].skew(axis=1)
    df['Kurt'] = df.iloc[:, 1:5].kurtosis(axis=1)
    # error if not have Close columns
    df['Change%'] = df['Close'].pct_change()*100
    df['Mchange%'] = df['Mean'].pct_change()*100

    # consider drop or not
    df.drop(columns=['Open', 'High', 'Low'], inplace=True)
    df.set_index('Date', inplace=True)
    df = df[-periods:]
    print(quotes)
    print(df)
    # df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_stats.csv')

# calculate_stats(source=currency_path, periods=13,
#                 quotes='GBPUSD', interval='Daily')


def calculate_one_stats():
    pass


def correlation_one(source=combine_path, periods=13,
                    quotes='cor_bond', interval='Daily'):
    # read data
    df = pd.read_csv(source+f'{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
    df = df.corr()
    print(quotes, periods, interval)
    print(df)
    print()
    # print(df.corr())  # method='kendall' / 'spearman'
    # df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_corr.csv')
    # return None


def residuals_formula():
    pass


def correlation_two(periods=4, interval='Daily',
                    dicts={'currenciesdata': 'XAUUSD',
                           'rates-bondsdata': 'U.S. 10Y'}):
    sources = list(dicts.keys())
    quotes = list(dicts.values())
    df = pd.read_csv(
        f'investpy/{sources[0]}/{quotes[0]}_{interval}.csv')
    df = df.iloc[-periods-1:]
    df.reset_index(inplace=True)
    df1 = pd.read_csv(
        f'investpy/{sources[1]}/{quotes[1]}_{interval}.csv')
    df1 = df1.iloc[-periods-1:]
    df1.reset_index(inplace=True)
    df_ = list(df.corrwith(df1))
    df1_ = list(df.corrwith(df1, axis=1))
    return df_[-len(df_)+1:], df1_[-len(df1_)+1:]


def combine_params(filename, params, interval):
    check_data(combine_path, f'{filename}_{interval}.csv')
    main_df = pd.DataFrame()
    for ticker, info in params.items():
        if '/' in ticker:
            print(f'{ticker} have special /')
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
    # economic_path = f'fred/{currency}/'
    economic_path = f'quandl/{currency}/'
    # check_data(economic_path)
    df = fred.get_series(item, observation_start=starttime,
                         observation_end=today)
    df.to_csv(economic_path + f'{item}.csv')
    pass

# quandl part --------------------------------


def get_economic_quandl(currency, field, item):
    economic_path = f'quandl/{currency}/'
    check_data(economic_path, f'{item}.csv')
    df = quandl.get(f'{field}/{item}',
                    start_date=starttime, end_date=today)
    # print(df.tail())
    df.to_csv(economic_path + f'{item}.csv')


def get_quandl_data(market, field, currency, item):
    # need optimize folder name
    quandl_part = f'quandl/{market}data/{currency}/'
    # create folder
    check_data(quandl_part, f'{item}.csv')
    # request data then save to file, start_date, end_date
    df = quandl.get(f'{field}/{item}',
                    start_date=starttime, end_date=today)
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
    index_ = replace_specchar(index, '/', '')
    path = index_path + f'{index_}_{interval}.csv'
    if not check_data(index_path, f'{index_}_{interval}.csv'):
        df = iv.indices.get_index_historical_data(
            index=index, country=country, from_date=starttime,
            to_date=today, order='ascending', interval=interval)
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
    path = bond_path + f'{bond}_{interval}.csv'
    if not check_data(bond_path, f'{bond}_{interval}.csv'):
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
    data = ['U.S. 10Y', 'Canada 10Y',
            'Japan 10Y', 'Switzerland 10Y',
            'Australia 10Y', 'New Zealand 10Y',
            'Germany 10Y', 'U.K. 10Y']
    info = [[markets[3], 'united states', get_bonds]]*len(data)
    params = ['cor_bond', data, info, analysis_bond]
    make_market(params, isReload)


def bond_spread(periods=6, name='cor_bond',
                interval='Monthly', base='U.S. 10Y'):
    # https://pypi.org/project/nelson-siegel-svensson/0.1.0/
    # https://pypi.org/project/yield-curve-dynamics/

    # read data
    df = pd.read_csv(combine_path + f'{name}_{interval}.csv')

    # get a range value
    df = df.iloc[-periods-1:]

    # move base to the first columns
    first_column = df.pop(base)
    df.insert(1, base, first_column)

    # list(df)[1:] mean quotes list
    df.dropna(subset=list(df)[1:], how='any', inplace=True)

    # calculate spread by subtract to the base
    df.iloc[:, 1:9] = df.iloc[:, 1:9].sub(df[base], axis=0).pct_change()*100

    # drop zero base column
    df.drop(base, axis=1, inplace=True)

    # remove first empty row
    df = df[-len(df)+1:]

    # set Date as index
    df.set_index('Date', inplace=True)

    # write to file
    df.to_csv(analysis_path + f'{base}_spread_{periods}_{interval}.csv')


# bond_spread(base='Canada 10Y')

'''
# T.B.D
def bond_stats():
    # call function
    quotes = ['Japan 10Y', 'Switzerland 10Y', 'Australia 10Y',
              'Canada 10Y', 'U.S. 10Y', 'Germany 10Y',
              'New Zealand 10Y', 'U.K. 10Y']
    # quotes = ['New Zealand 10Y', 'U.S. 10Y']
    for quote in quotes:
        print(f'\nCheck_bonds: {quote} in {periods} {interval}')
        calculate_stats(periods=periods, quotes=quote, interval=interval)
    pass
'''
# ----------- get_currency_cross_historical_data ---------


def get_forex(quote, interval, country):
    quote_ = replace_specchar(quote, '/', '')
    path = currency_path + f'{quote_}_{interval}.csv'
    if not check_data(currency_path, f'{quote_}_{interval}.csv'):
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
    data = ['XAG/USD', 'XAG/EUR', 'XAG/GBP',
            'XAG/CAD', 'XAG/CHF', 'XAG/AUD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['xagpair', data, info, analysis_currency]
    make_market(params, isReload)

# ----------------------------IMPORTANT- commondity---
# ------------- get_commodity_historical_data ---------------


def get_commodities(commodity, interval, country):
    path = commodity_path + f'{commodity}_{interval}.csv'
    if not check_data(commodity_path, f'{commodity}_{interval}.csv'):
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
    # # test purpose
    # df = iv.indices.get_index_historical_data(
    #     index='TR/CC CRB', country='world', from_date=starttime,
    #     to_date=today, order='ascending', interval='Daily')
    # df.to_csv(index_path+'cbr_commondity.csv')

    # # test purpose 2
    # df = pd.read_csv(index_path+'cbr_commondity.csv')
    # close_ = df[-21:].Close
    # open_ = df[-21:].Open

    # fig = plt.figure(figsize=(8, 6))
    # ax = fig.add_subplot(111)
    # ax.plot(close_)

    # bx = fig.add_subplot(111)
    # bx.plot(open_)

    # plt.show()
    intervals = ['Daily', 'Weekly', 'Monthly']
    for interval in intervals:
        get_indices('TR/CC CRB', interval, 'world')


# ---------------- ETF -------------------------
def etf_percent():
    pass


def get_etf(etf, interval, country):
    '''
    # https://www.investing.com/etfs/major-etfs
    # df = iv.etfs.get_etf_countries()
    # df = iv.etfs.get_etfs('united states')
    # df.to_csv(etf_path + 'us_etfslist.csv')
    # df = iv.etfs.get_etfs_overview('united states')
    # df.to_csv(etf_path + 'us_etfsoverview.csv')
    # ------------------------------------------------
    # df = iv.etfs.get_etf_information('SPDR S&P 500', 'united states')
    # df = iv.etfs.get_etf_recent_data('SPDR S&P 500', 'united states')
    '''
    # print(f'ETF: {etf} - country: {country}')
    path = etf_path + f'{etf}_{interval}.csv'
    if not check_data(etf_path, f'{etf}_{interval}.csv'):
        df = iv.etfs.get_etf_historical_data(
            etf=etf, country=country, from_date=starttime,
            to_date=today, order='ascending', interval=interval)
        df.to_csv(path)
    else:
        new_start = append_preparing(path)
        if new_start is not None:
            df = iv.etfs.get_etf_historical_data(
                etf=etf, country=country, from_date=new_start,
                to_date=today,
                order='ascending', interval=interval)
            df.to_csv(path, mode='a', header=False)
    pass


def get_bondetfs(isReload=True):
    data = ['iShares Core US Aggregate Bond',
            'Vanguard Total Bond Market',
            'Vanguard Intermediate-Term Corporate Bond',
            'Vanguard Total International Bond',
            'Vanguard Short-Term Corporate Bond']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    params = ['bondetfs', data, info, analysis_etf]
    make_market(params, isReload)
    pass


def get_stocketfs(isReload=True):
    data = ['SPDR S&P 500', 'ishares S&P 500',
            'Vanguard Total Stock Market',
            'Vanguard S&P 500',
            'Invesco QQQ Trust Series 1']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    params = ['stocketfs', data, info, analysis_etf]
    make_market(params, isReload)
    pass


def get_goldetfs(isReload=True):
    data = ['SPDR Gold Shares', 'iShares Gold',
            'SPDR Gold MiniShares',
            'ETFS Physical Swiss Gold Shares',
            'GraniteShares Gold Trust']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    params = ['goldetfs', data, info, analysis_etf]
    make_market(params, isReload)


def get_silveretfs(isReload=True):
    # 'United States Copper' - not use
    data = ['iShares Silver', 'ETFS Physical Silver Shares',
            'ProShares Ultra Silver']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    params = ['silveretfs', data, info, analysis_etf]
    make_market(params, isReload)


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


def fibocalculator(source=currency_path, quotes='USDCHF',
                   interval='Monthly', periods=15):
    # read data
    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    # get data range
    df = df.iloc[-periods-1:]
    # get min/ max in data range
    low = df['Low'].min()
    high = df['High'].max()
    # get index
    last_pos = df.index.tolist()[len(df)-1]
    low_index, high_index = df.loc[df['Low'] ==
                                   low].index, df.loc[df['High'] == high].index
    # consider trend
    isUptrend = True if (high_index - low_index > 0) else False
    # fibo level
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


def pivotpointcalculator(pivotType='Fibonacci', source=currency_path,
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

def inner_volatility(source=currency_path, quotes='USDCHF',
                     interval='Monthly', periods=6):

    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
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
    df['PCT'] = (df['Close']-df['Open'])/df['Close']*100

    df = df[-periods:]
    df.drop(['Open', 'High', 'Low', 'Close'], axis=1, inplace=True)
    df.set_index('Date', inplace=True)
    df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_vols.csv')


# inner_volatility()
# -------------------------------------------------------------------

# financial-calendars
# https://www.investing.com/tools/financial-calendars
# ----------------------------------
# https://www.investing.com/tools/market-hours


def markethours():
    '''
    # Overlaps time: Overlapping trading hours contain
    # Volume increase in specific session
    '''
    sessions = ['AUS', 'ASIA', 'EU', 'US']
    now = datetime.datetime.now()

    # read api then check session time
    # print(now.year, now.month, now.day, now.hour, now.minute, now.second)

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


def get_all():
    # get_currency_indices()
    # cor_bond()
    # compare_gold()
    # compare_silver()
    # calculate_grains()
    # calculate_softs()
    # calculate_meats()
    # calculate_metals()
    # calculate_energies()
    # get_crb()
    # cor_aunz()
    # cor_usca()
    # cor_jpsw()
    # cor_ukeu()
    # get_goldetfs()
    # get_silveretfs()
    # get_stocketfs()
    # get_bondetfs()
    pass


# get_all()
