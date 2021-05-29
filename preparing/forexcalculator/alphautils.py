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


# HUng refactor
def analysis_currency(filename):
    pass


# HUng refactor
def analysis_bond(filename):
    # processing data
    # https://pypi.org/project/nelson-siegel-svensson/0.1.0/
    # https://pypi.org/project/yield-curve-dynamics/
    pass


# HUng refactor
def analysis_index(filename):
    pass


def analysis_commodity(filename):
    pass


def combine_params(filename, params, interval):
    check_folder(combine_path)
    main_df = pd.DataFrame()
    for ticker, market in params.items():
        ticker = replace_specchar(ticker, '/', '')
        df = pd.read_csv(f'investpy/{market}data/{ticker}_{interval}.csv')
        df.set_index('Date', inplace=True)
        df.rename(columns={'Close': ticker}, inplace=True)
        df = df.filter([ticker])
        main_df = df if main_df.empty else main_df.join(df, how='outer')
        # fillna or dropna
    main_df.to_csv(combine_path + f'{filename}_{interval}.csv')


def norm_data():
    pass


def make_market(params, isReload=True):
    intervals = ['Daily', 'Weekly', 'Monthly']
    name, market, things, country, inputfunc, outputfunc = params
    markets = [market]*len(things)
    thing_pairs = dict(zip(things, markets))
    if isReload:
        dump_things(f'{name}{market}', thing_pairs, intervals,
                    country, inputfunc)
    else:
        outputfunc(combine_path + f'{name}{market}_{interval}.csv')
        pass


def dump_things(filename, things, intervals, country, func):
    for thing in things.keys():
        for interval in intervals:
            func(thing, interval, country)
    for interval in intervals:
        combine_params(filename, things, interval)


def lazy_loop():
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
    df = iv.indices.get_index_historical_data(
        index=index, country=country, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    index = replace_specchar(index, '/', '_')
    df.to_csv(index_path + f'/{index}_{interval}.csv')


def get_currency_indices(isReload=True):
    currency_indices = ['US Dollar Index', 'PHLX Euro',
                        'PHLX Australian Dollar', 'PHLX Canadian Dollar',
                        'PHLX Swiss Franc', 'PHLX British Pound',
                        'PHLX Yen', 'US Dollar Index']
    currency_params = ['currency', markets[0], currency_indices,
                       'united states', get_indices, analysis_index]
    make_market(currency_params, isReload)


# ------------------- bonds -----------------------------
def get_bonds(bond, interval, country):
    check_folder(bond_path)
    # ---------- historical_data ------------
    df = iv.bonds.get_bond_historical_data(
        bond=bond, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    df.to_csv(bond_path + f'/{bond}_{interval}.csv')


def get_bond_overview(country):
    df = iv.bonds.get_bonds_overview(country=country)
    pass


# ----------- get_currency_cross_historical_data ---------
def get_currency_cross(quote, interval, country):
    check_folder(currency_path)
    df = iv.currency_crosses.get_currency_cross_historical_data(
        currency_cross=quote, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    df = df.iloc[:, :-1]
    quote = replace_specchar(quote, '/', '')
    df.to_csv(currency_path + f'/{quote}_{interval}.csv')


def compare_gold():
    xaupairs = ['XAU/USD', 'XAU/EUR', 'XAU/GBP', 'XAU/CAD',
                'XAU/CHF', 'XAU/JPY', 'XAU/AUD', 'XAU/NZD']
    xaupair_params = ['xaupair', markets[1], xaupairs,
                      'united states', get_currency_cross, analysis_currency]
    make_market(xaupair_params, isReload)


def compare_silver():
    xagpairs = ['XAG/USD', 'XAG/EUR', 'XAG/GBP',
                'XAG/CAD', 'XAG/CHF', 'XAG/AUD']
    xagpair_params = ['xagpair', markets[1], xagpairs,
                      'united states', get_currency_cross, analysis_currency]
    make_market(xagpair_params, isReload)


# ----------------------------IMPORTANT- commondity---
# ------------- get_commodity_historical_data ---------------
def get_commodities(commodity, interval, country):
    check_folder(commodity_path)
    df = iv.commodities.get_commodity_historical_data(
        commodity=commodity, from_date=starttime, to_date=today,
        order='ascending', interval=interval)
    df.to_csv(commodity_path + f'/{commodity}_{interval}.csv')


def calculate_grains(isReload=True):
    # https://www.investing.com/commodities/grains
    grains = ['Rough Rice', 'US Soybean Oil',
              'US Soybean Meal', 'US Soybeans',
              'US Wheat', 'US Corn', 'Oats', 'London Wheat']
    grain_params = ['grain', markets[2], grains,
                    'united states', get_commodities, analysis_commodity]
    make_market(grain_params, isReload)


def calculate_softs(isReload=True):
    # https://www.investing.com/commodities/softs
    softs = ['US Coffee C', 'US Cotton #2',
             'US Sugar #11', 'Orange Juice',
             'US Cocoa', 'Lumber', 'London Cocoa',
             'London Coffee', 'London Sugar']
    soft_params = ['soft', markets[2], softs,
                   'united states', get_commodities, analysis_commodity]
    make_market(soft_params, isReload)


def calculate_meats(isReload=True):
    # https://www.investing.com/commodities/meats
    meats = ['Live Cattle', 'Lean Hogs', 'Feeder Cattle']
    meat_params = ['meat', markets[2], meats,
                   'united states', get_commodities, analysis_commodity]
    make_market(meat_params, isReload)


def calculate_metals(isReload=True):
    # https://www.investing.com/commodities/metals
    metals = ['Gold', 'Silver', 'Copper', 'Palladium', 'Platinum',
              'Aluminum', 'Zinc', 'Lead', 'Nickel', 'Tin']
    metal_params = ['metal', markets[2], metals,
                    'united states', get_commodities, analysis_commodity]
    make_market(metal_params, isReload)


def calculate_energies(isReload=True):
    # https://www.investing.com/commodities/energy
    energies = ['Brent Oil', 'Crude Oil WTI',
                'London Gas Oil', 'Natural Gas',
                'Heating Oil', 'Carbon Emissions',
                'Gasoline RBOB']
    energy_params = ['energy', markets[2], energies,
                     'united states', get_commodities, analysis_commodity]
    make_market(energy_params, isReload)


# ----------------Commondity index-------------------------
# https://www.investing.com/indices/thomson-reuters---jefferies-crb
def get_crb(isReload=True):
    get_indices('TR/CC CRB', 'world')


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
