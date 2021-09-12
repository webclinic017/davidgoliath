# Copyright 2021 Hung Nguyen, spideynolove @ GitHub
# See LICENSE for details.

__author__ = 'Hung Nguyen @spideynolove in GitHub'
__version__ = '0.0.1'

# mimic pro code
# from .technical import technical_indicators, moving_averages, pivot_points

import investpy as iv
import os
import numpy as np
import pandas as pd
import datetime
import re
from settings import *
from functools import reduce
from pprint import pprint
'''
# --------- investpy market folder path
equity_path = 'investpy/equitiesdata/'
crypto_path = 'investpy/cryptodata/'
'''
# today = datetime.date.today().strftime("%d/%m/%Y")
today = '19/08/2021'


def convert_date(date):
    return date.strftime("%d/%m/%Y")


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
    # print(quotes)
    # print(df)
    df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_stats.csv')


def calculate_one_stats():
    pass


def correlation_one(source=combine_path, periods=13,
                    quotes='cor_bond', interval='Daily'):
    # read data
    df = pd.read_csv(source+f'{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
    df = df.corr()
    # print(quotes, periods, interval)
    # print(df)
    # print()
    # print(df.corr())  # method='kendall' / 'spearman'
    df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_corr.csv')


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
            print(interval)
            infunc(thing, interval, country)
    for interval in intervals:
        combine_params(filename, things, interval)


def make_market(params, isReload=True):
    intervals = ['Daily', 'Weekly', 'Monthly']
    # filename, data, info, outfunc = params
    filename, data, info = params
    thing_pairs = dict(zip(data, info))
    if isReload:
        dump_things(filename, thing_pairs, intervals)
    # else:
    #     outfunc(combine_path + f'{filename}_{interval}.csv')
    #     # read data


def norm_data():
    # numpy processing
    pass


def append_preparing(path):
    df = pd.read_csv(path)
    cur_date = df[-1:]['Date'].tolist()[0]

    df = df[:-1]
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.to_csv(path)

    if cur_date == datetime.date.today().strftime('%Y-%m-%d'):
        return None
    else:
        dayRe = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
        mo = dayRe.search(cur_date)
        starttime = mo.group(3) + "/" + mo.group(2) + "/" + mo.group(1)
        return starttime


def check_data(folder_part, filename):
    # if os.path.exists(folder_part):
    #     # print(f'{folder_part} already exist!')
    #     if os.path.exists(folder_part+filename):
    #         print(f'{folder_part+filename} already exist!')
    #         return False
    #     else:
    #         return True
    # else:
    #     os.makedirs(folder_part)
    #     return False
    return False


def replace_specchar(obj, char, newchar):
    tmp = obj
    if char in obj:
        tmp = obj.replace(char, newchar)
    return tmp


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
# --------------------- indices ----------------------------------


def get_index(index, interval, country):
    index_ = replace_specchar(index, '/', '')
    path = f'investpy/indicesdata/{index_}_{interval}.csv'
    if not check_data('investpy/indicesdata/', f'{index_}_{interval}.csv'):
        df = iv.indices.get_index_historical_data(
            index=index, country=country, from_date=starttime,
            to_date=today, order='ascending', interval=interval)
        df.to_csv(path)
    # else:
    #     new_start = append_preparing(path)
    #     print(new_start, today)
    #     if new_start is not None:
    #         df = iv.indices.get_index_historical_data(
    #             index=index, country=country, from_date=new_start,
    #             to_date=today, order='ascending', interval=interval)
    #         df.to_csv(path, mode='a', header=False)


def get_indices(isReload=True):
    data = ['US Dollar Index', 'PHLX Euro',
            'PHLX Australian Dollar', 'PHLX Canadian Dollar',
            'PHLX Swiss Franc', 'PHLX British Pound',
            'PHLX Yen', 'PHLX New Zealand Dollar']
    info = [[markets[0], 'united states', get_index]]*len(data)
    # params = ['currencyindex', data, info, analysis_index]
    params = ['currencyindex', data, info]
    # make_market(params, isReload)


# ------------------- bonds -----------------------------
def get_bond(bond, interval, country):
    path = f'investpy/rates-bondsdata/{bond}_{interval}.csv'
    if not check_data('investpy/rates-bondsdata/', f'{bond}_{interval}.csv'):
        df = iv.bonds.get_bond_historical_data(
            bond=bond, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df.to_csv(path)
    # else:
    #     new_start = append_preparing(path)
    #     if new_start is not None:
    #         df = iv.bonds.get_bond_historical_data(
    #             bond=bond, from_date=new_start, to_date=today,
    #             order='ascending', interval=interval)
    #         df.to_csv(path, mode='a', header=False)


def get_bonds(isReload=True):
    data = ['U.S. 10Y', 'Canada 10Y',
            'Japan 10Y', 'Switzerland 10Y',
            'Australia 10Y', 'New Zealand 10Y',
            'Germany 10Y', 'U.K. 10Y']
    info = [[markets[3], 'united states', get_bond]]*len(data)
    # params = ['cor_bond', data, info, analysis_bond]
    params = ['cor_bond', data, info]
    # make_market(params, isReload)


def get_bond_spread(periods=6, name='cor_bond',
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


# ----------- get_currency_cross_historical_data ---------
def get_forex(quote, interval, country):
    quote_ = replace_specchar(quote, '/', '')
    path = f'investpy/currenciesdata/{quote_}_{interval}.csv'
    if not check_data('investpy/currenciesdata/', f'{quote_}_{interval}.csv'):
        # check latest data
        print("check_data True")
        df = iv.currency_crosses.get_currency_cross_historical_data(
            currency_cross=quote, from_date=starttime, to_date=today,
            order='ascending', interval=interval)
        df = df.iloc[:, :-1]
        df.to_csv(path)
    else:
        print("check_data False")
        new_start = append_preparing(path)
        print(new_start, today)
        if new_start is not None:
            df = iv.currency_crosses.get_currency_cross_historical_data(
                currency_cross=quote, from_date=new_start, to_date=today,
                order='ascending', interval=interval)
            df = df.iloc[:, :-1]
            df.to_csv(path, mode='a', header=False)


def get_goldpairs(isReload=True):
    data = ['XAU/USD', 'XAU/EUR', 'XAU/GBP', 'XAU/CAD',
            'XAU/CHF', 'XAU/JPY', 'XAU/AUD', 'XAU/NZD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    # params = ['xaupair', data, info, analysis_currency]
    params = ['xaupair', data, info]
    # make_market(params, isReload)


def get_silverpairs(isReload=True):
    data = ['XAG/USD', 'XAG/EUR', 'XAG/GBP',
            'XAG/CAD', 'XAG/CHF', 'XAG/AUD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    # params = ['xagpair', data, info, analysis_currency]
    params = ['xagpair', data, info]
    # make_market(params, isReload)
# ----------------------------IMPORTANT- commondity---
# ------------- get_commodity_historical_data ---------------


def get_commodities(commodity, interval, country):
    path = f'investpy/commoditiesdata/{commodity}_{interval}.csv'
    compath = 'investpy/commoditiesdata/'
    if not check_data(compath, f'{commodity}_{interval}.csv'):
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


def get_grains(isReload=True):
    # https://www.investing.com/commodities/grains
    data = ['Rough Rice', 'US Soybean Oil',
            'US Soybean Meal', 'US Soybeans',
            'US Wheat', 'US Corn', 'Oats', 'London Wheat']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    # params = ['grain', data, info, analysis_commodity]
    params = ['grain', data, info]
    # make_market(params, isReload)


def get_softs(isReload=True):
    # https://www.investing.com/commodities/softs
    data = ['US Coffee C', 'US Cotton #2',
            'US Sugar #11', 'Orange Juice',
            'US Cocoa', 'Lumber', 'London Cocoa',
            'London Coffee', 'London Sugar']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    # params = ['soft', data, info, analysis_commodity]
    params = ['soft', data, info]
    # make_market(params, isReload)

# shortcut: filename + dataset


def get_meats(isReload=True):
    # https://www.investing.com/commodities/meats
    data = ['Live Cattle', 'Lean Hogs', 'Feeder Cattle']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    # params = ['meat', data, info, analysis_commodity]
    params = ['meat', data, info]
    # make_market(params, isReload)


def get_metals(isReload=True):
    # https://www.investing.com/commodities/metals
    data = ['Gold', 'Silver', 'Copper', 'Palladium', 'Platinum',
            'Aluminum', 'Zinc', 'Lead', 'Nickel', 'Tin']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    # params = ['metal', data, info, analysis_commodity]
    params = ['metal', data, info]
    # make_market(params, isReload)


def get_energies(isReload=True):
    # https://www.investing.com/commodities/energy
    data = ['Brent Oil', 'Crude Oil WTI',
            'London Gas Oil', 'Natural Gas',
            'Heating Oil', 'Carbon Emissions',
            'Gasoline RBOB']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    # params = ['energy', data, info, analysis_commodity]
    params = ['energy', data, info]
    # make_market(params, isReload)

# ----------------Commondity index-------------------------
# https://www.investing.com/indices/thomson-reuters---jefferies-crb


def get_crb(isReload=True):
    intervals = ['Daily', 'Weekly', 'Monthly']
    for interval in intervals:
        get_index('TR/CC CRB', interval, 'world')
# ---------------- ETF -------------------------


def etf_percent():
    pass


def get_etf(etf, interval, country):
    path = f'investpy/etfsdata/{etf}_{interval}.csv'
    if not check_data('investpy/etfsdata/', f'{etf}_{interval}.csv'):
        df = iv.etfs.get_etf_historical_data(
            etf=etf, country=country, from_date=starttime,
            to_date=today, order='ascending', interval=interval)
        df.to_csv(path)
    # else:
    #     new_start = append_preparing(path)
    #     if new_start is not None:
    #         df = iv.etfs.get_etf_historical_data(
    #             etf=etf, country=country, from_date=new_start,
    #             to_date=today,
    #             order='ascending', interval=interval)
    #         df.to_csv(path, mode='a', header=False)
    # pass


def get_bondetfs(isReload=True):
    data = ['iShares Core US Aggregate Bond',
            'Vanguard Total Bond Market',
            'Vanguard Intermediate-Term Corporate Bond',
            'Vanguard Total International Bond',
            'Vanguard Short-Term Corporate Bond']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    # params = ['bondetfs', data, info, analysis_etf]
    params = ['bondetfs', data, info]
    # make_market(params, isReload)
    pass


def get_stocketfs(isReload=True):
    data = ['SPDR S&P 500', 'ishares S&P 500',
            'Vanguard Total Stock Market',
            'Vanguard S&P 500',
            'Invesco QQQ Trust Series 1']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    # params = ['stocketfs', data, info, analysis_etf]
    params = ['stocketfs', data, info]
    # make_market(params, isReload)
    pass


def get_goldetfs(isReload=True):
    data = ['SPDR Gold Shares', 'iShares Gold',
            'SPDR Gold MiniShares',
            'ETFS Physical Swiss Gold Shares',
            'GraniteShares Gold Trust']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    # params = ['goldetfs', data, info, analysis_etf]
    params = ['goldetfs', data, info]
    # make_market(params, isReload)


def get_silveretfs(isReload=True):
    # 'United States Copper' - not use
    data = ['iShares Silver', 'ETFS Physical Silver Shares',
            'ProShares Ultra Silver']
    info = [[markets[5], 'united states', get_etf]]*len(data)
    # params = ['silveretfs', data, info, analysis_etf]
    params = ['silveretfs', data, info]
    # make_market(params, isReload)
# ----------------Correlation-------------------------
# -------------------------------------
# AUD vs NZD (correlation)


def get_aunz(isReload=True):
    data = ['PHLX Australian Dollar', 'PHLX New Zealand Dollar',
            'Australia 10Y', 'New Zealand 10Y']
    info = [[markets[0], 'united states', get_index]] * \
        2 + [[markets[3], 'united states', get_bond]]*2
    # params = ['cor_aunz', data, info, analysis_intermarket]
    params = ['cor_aunz', data, info]
    make_market(params, isReload)

# -------------------------------------
# USD vs CAD (correlation)


def get_usca(isReload=True):
    data = ['US Dollar Index', 'PHLX Canadian Dollar',
            'U.S. 10Y', 'Canada 10Y']
    info = [[markets[0], 'united states', get_index]] * \
        2 + [[markets[3], 'united states', get_bond]]*2
    # params = ['cor_usca', data, info, analysis_intermarket]
    params = ['cor_usca', data, info]
    make_market(params, isReload)

# -------------------------------------
# JPY vs CHF (correlation)


def get_jpsw(isReload=True):
    data = ['PHLX Yen', 'PHLX Swiss Franc', 'Japan 10Y', 'Switzerland 10Y']
    info = [[markets[0], 'united states', get_index]] * \
        2 + [[markets[3], 'united states', get_bond]]*2
    # params = ['cor_jpsw', data, info, analysis_intermarket]
    params = ['cor_jpsw', data, info]
    make_market(params, isReload)

# -------------------------------------
# GBP vs EUR (correlation)


def get_ukeu(isReload=True):
    data = ['PHLX British Pound', 'PHLX Euro', 'U.K. 10Y', 'Germany 10Y']
    info = [[markets[0], 'united states', get_index]] * \
        2 + [[markets[3], 'united states', get_bond]]*2
    # params = ['cor_ukeu', data, info, analysis_intermarket]
    params = ['cor_ukeu', data, info]
    make_market(params, isReload)


# ----------------------------------
# https://www.investing.com/economic-calendar/


def get_economic_calendar():
    '''
    countries = ['united states', 'united kingdom', 'australia', 'canada',
                 'switzerland', 'germany', 'japan', 'new zealand', 'china']
    importances = ['high', 'medium']
    today = date.today()
    # get entire month (month have??? day)
    week_ago = (today + datetime.timedelta(days=6))
    # print(today, week_ago)
    df = iv.economic_calendar(time_zone='GMT +7:00', time_filter='time_only',
                              countries=countries, importances=importances,
                              categories=None, from_date=convert_date(today),
                              to_date=convert_date(week_ago))
    df.to_csv('investpy/calendar/economic_calendar.csv')
    '''
    df = pd.read_csv('investpy/calendar/economic_calendar.csv', index_col=0)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    print(df)
    pass


def csv_finder(foldername):
    paths = []
    for root, dirs, files in os.walk(foldername):
        for file in files:
            if file.endswith(".csv"):
                paths.append(os.path.abspath(os.path.join(root, file)))
    return paths


def read_data_vol():
    non_vols = []
    vols = []
    paths = csv_finder("investpy")
    for count, item in enumerate(paths, 1):
        df = pd.read_csv(item)
        if 'Volume' in df.columns and (df['Volume'] != 0).all():
            # planning correlation: GBP ~ Economic /
            # Volume commodity, stocks, indices, etfs
            # print(count, os.path.basename(item))
            vols.append(item)
        else:
            non_vols.append(item)
            # print(os.path.basename(item))
    return vols, non_vols


def get_all():
    get_bonds()

    get_metals()
    get_energies()
    get_meats()
    get_grains()
    get_softs()
    get_crb()

    get_indices()
    get_goldpairs()

    get_aunz()
    get_ukeu()
    get_usca()
    get_jpsw()


def correlation_new(path, periods):
    df = pd.read_csv(path)
    name, interval = os.path.basename(path).split('.')[0].rsplit('_', 1)
    # if 'Weekly' in path:
    #     periods = periods[:len(periods)-1]
    # elif 'Monthly' in path:
    #     periods = periods[:len(periods)-2]
    if 'Daily' in path:
        for period in periods:
            df = df.iloc[-period-1:]
            df = df.corr()
            # print(df.corr())  # method='kendall' / 'spearman'
            # df.to_csv(analysis_path + f'{name}_{period}_{interval}.csv')
            print(f'{name}_{period}_{interval}')
            print(df)
            # return None


def calculate_stats_new(source=combine_path, periods=13,
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
    # print(quotes)
    # print(df)
    # df.to_csv(analysis_path + f'{quotes}_{periods}_{interval}_stats.csv')


def corr_():
    compare = ['usmain', 'usbond', 'usindices', 'uspairs', 'usoil']
    # compare = ['eubond', 'eurmajor', 'eugold', 'euindex']
    # compare = ['corr_ukoil', 'ukindex', 'ukbond', 'gbpmajor']
    for item in csv_finder("investpy/combinedata"):
        for tmp in compare:
            if tmp in item:
                correlation_new(item, [13, 21, 34, 55, 89])
            pass


def label_data():
    df = pd.read_csv('data/Gold_Daily_fill.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low'], axis=1, inplace=True)

    # label own data
    df['status'] = 0
    for i in range(len(df)):
        df['status'].iloc[i] = 1 if df['pct_change'].iloc[i] > 0 else 0

    # open vs last date close

    # open vs ma param (historical mean data~in some windows)

    # close

    print(df.tail(10))
    pass


def data_to_corr(isReload=True):
    data = ['Gold', 'PHLX Canadian Dollar', 'PHLX Australian Dollar',
            'PHLX New Zealand Dollar', 'PHLX Yen', 'PHLX Swiss Franc',
            'PHLX Euro', 'PHLX British Pound']
    # info = [[markets[0], 'world', get_index]] + \
    #     [[markets[0], 'united states', get_index]] +\
    #     [[markets[3], 'united states', get_bond]] +\
    #     [[markets[2], 'united states', get_commodities]]*2
    # params = ['cbrcor_us', data, info]

    info = [[markets[2], 'united states', get_commodities]] +\
        [[markets[0], 'united states', get_index]]*7
    params = ['goldanother_xy', data, info]

    make_market(params, isReload)
    pass


def trick():
    values = {'vegetable': 'chard', 'fruit': 'nectarine'}
    print('I love %(vegetable)s and I love %(fruit)s.' % values)


# get_all()
# label_data()

# get_indices()
# data_to_corr()
# corr_()
# calculate_stats_new()

# vols, non_vols = read_data_vol()
# with open('../data/volAll.txt', 'w', encoding='utf-8') as f:
#     f.write(str(vols))
