from __future__ import print_function
import os
import quandl
import pandas as pd
import investpy as iv
import datamine as cme
from fredapi import Fred
from datetime import date
from forexflag import *

quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'
fred = Fred(api_key='fc9753be1dab36c5773160e0fdf05ba7')

# ---------- investpy items -----------
markets = ['indices', 'currencies', 'commodities',
           'rates-bonds', 'equities', 'etfs', 'crypto']
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
# --------- end investpy market folder path
# ---------- end investpy items -------
# ----------------------------------------------------------
# common function
# ----------------------------------------------------------


# Currencies Heat Map
# https://www.investing.com/tools/currency-heatmap
def currenciesheatmap():
    pass


# Forex Volatility:
# https://www.investing.com/tools/forex-volatility-calculator
def forexvolatility():
    pass


# Fibonacci Calculator:
# https://www.investing.com/tools/fibonacci-calculator
def fibocalculator():
    pass


# Pivot Point Calculator
# https://www.investing.com/tools/pivot-point-calculator
def pivotpointcalculator():
    pass


# financial-calendars
# https://www.investing.com/tools/financial-calendars
# ----------------------------------
# https://www.investing.com/tools/market-hours
def markethours():
    # Overlaps time: Overlapping trading hours contain
    # the highest volume of traders.
    pass


# ----------------------------------
# https://www.investing.com/economic-calendar/
def economiccalendar():
    pass


def analysis_currency(filename):
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
    check_folder(combine_path)
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
    pass


def check_folder(part):
    if not os.path.exists(part):
        os.makedirs(part)


def replace_specchar(obj, char, newchar):
    tmp = obj
    if char in obj:
        tmp = obj.replace(char, newchar)
    return tmp


# Fred part --------------------------------
def get_economic_fred(currency, item):
    economic_path = f'fred/{currency}/'
    check_folder(economic_path)
    df = fred.get_series(item,
                         observation_start=starttime, observation_end=today)
    print(df.tail())
    pass


# quandl part --------------------------------
def get_economic_quandl(currency, field, item):
    economic_path = f'quandl/{currency}/'
    check_folder(economic_path)
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    print(df.tail())
    # df.to_csv(economic_path + f'{item}.csv')


def get_quandl_data(market, field, currency, item):
    # need optimize folder name
    quandl_part = f'quandl/{market}data/{currency}/'
    # create folder
    check_folder(quandl_part)
    # request data then save to file, start_date, end_date
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    print(df.tail())
    # df.to_csv(quandl_part + f'{item}.csv')
    # return quandl_part + f'{item}.csv'


def get_investing_data():
    # Data Model: [date, open, high, low, close, volume, currency]
    # check types
    # use true get historical data function
    pass


def read_data(file):
    df = pd.read_csv(file)
    # return None


# --------------------- indices ----------------------------------
def get_indices(index, interval, country):
    check_folder(index_path)
    # check latest data
    df = iv.indices.get_index_historical_data(
        index=index, country=country, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    index = replace_specchar(index, '/', '_')
    # print(df.tail())
    df.to_csv(index_path + f'/{index}_{interval}.csv')


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
    check_folder(bond_path)
    # check latest data
    # ---------- historical_data ------------
    df = iv.bonds.get_bond_historical_data(
        bond=bond, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    # print(df.tail())
    df.to_csv(bond_path + f'/{bond}_{interval}.csv')


def cor_bond(isReload=True):
    data = ['Japan 10Y', 'Switzerland 10Y', 'Australia 10Y',
            'Canada 10Y', 'U.S. 10Y', 'Germany 10Y',
            'New Zealand 10Y', 'U.K. 10Y']
    info = [[markets[3], 'united states', get_bonds]]*len(data)
    params = ['cor_bond', data, info, analysis_bond]
    make_market(params, isReload)


# ----------- get_currency_cross_historical_data ---------
def get_forex(quote, interval, country):
    check_folder(currency_path)
    # check latest data
    df = iv.currency_crosses.get_currency_cross_historical_data(
        currency_cross=quote, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    df = df.iloc[:, :-1]
    quote = replace_specchar(quote, '/', '')
    # print(df.tail())
    df.to_csv(currency_path + f'/{quote}_{interval}.csv')


def compare_gold():
    data = ['XAU/USD', 'XAU/EUR', 'XAU/GBP', 'XAU/CAD',
            'XAU/CHF', 'XAU/JPY', 'XAU/AUD', 'XAU/NZD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['xaupair', data, info, analysis_currency]
    make_market(params, isReload)


def compare_silver():
    data = ['XAG/USD', 'XAG/EUR', 'XAG/GBP', 'XAG/CAD', 'XAG/CHF', 'XAG/AUD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['xagpair', data, info, analysis_currency]
    make_market(params, isReload)


# ----------------------------IMPORTANT- commondity---
# ------------- get_commodity_historical_data ---------------
def get_commodities(commodity, interval, country):
    check_folder(commodity_path)
    # check latest data
    df = iv.commodities.get_commodity_historical_data(
        commodity=commodity, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    # print(df.tail())
    df.to_csv(commodity_path + f'/{commodity}_{interval}.csv')


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
