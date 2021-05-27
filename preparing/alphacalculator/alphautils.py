import os
import quandl
import pandas as pd
import investpy as iv

from fredapi import Fred
from datetime import date
from alphasecrets import IEX_CLOUD_API_TOKEN

quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'
# fred = Fred(api_key='fc9753be1dab36c5773160e0fdf05ba7')

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
# --------- end investpy market folder path

# ---------- end investpy items -------
# ----------------------------------------------------------
# common function
# ----------------------------------------------------------


def check_folder(part):
    if not os.path.exists(part):
        os.makedirs(part)


def replace_specchar(obj, char, newchar):
    tmp = obj
    if char in obj:
        tmp = obj.replace(char, newchar)
    return tmp


# quandl part --------------------------------
def get_economic_quandl(currency, field, item):
    economic_path = f'quandl/{currency}/'
    check_folder(economic_path)
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    df.to_csv(economic_path + f'{item}.csv')
    pass


def get_quandl_data(market, field, currency, item):
    # need optimize folder name
    quandl_part = f'quandl/{market}data/{currency}/'
    # create folder
    check_folder(quandl_part)
    # request data then save to file, start_date, end_date
    df = quandl.get(f'{field}/{item}', start_date=starttime, end_date=today)
    df.to_csv(quandl_part + f'{item}.csv')
    # return quandl_part + f'{item}.csv'
    pass


def get_investing_data():
    # Data Model: [date, open, high, low, close, volume, currency]
    # check types

    # use true get historical data function
    pass


def get_fred_data():
    pass


def read_data(file):
    df = pd.read_csv(file)
    # return None
    pass


# -------------------------------------------------------
# get last row date, check if is up to date-> read data, not write
# -------------------------------------------------------
def get_bondyeild_quandl(currency, data, key):
    # ------------- quandl part-----------
    # get data and save, LACK Datetime range for data
    for value in data[key]:
        get_quandl_data(markets[3], key, currency, value)


def analysis_bondyeild_quandl(params):
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
    pass


# ------------- investpy part-----------
# def get_bondyeild_investpy(currency, quote):
#     get_bonds(quote)
#     pass


def analysis_bondyeild_investpy(params):
    print('not reload, process next')
    pass


# -------------------------------------------------------
def get_indices(index, country):
    check_folder(index_path)
    df = iv.indices.get_index_historical_data(
        index=index, country=country, from_date=starttime, to_date=today)
    index = replace_specchar(index, '/', '_')
    df.to_csv(index_path + f'/{index}.csv')
    pass


# -------------------------------------------------------
def get_commodities(commodity):
    check_folder(commodity_path)
    df = iv.commodities.get_commodity_historical_data(
        commodity=commodity, from_date=starttime, to_date=today)
    df.to_csv(commodity_path + f'/{commodity}.csv')
    pass


# -------------------------------------------------------
def get_bonds(bond):
    check_folder(bond_path)
    df = iv.bonds.get_bond_historical_data(
        bond=bond, from_date=starttime, to_date=today)
    df.to_csv(bond_path + f'/{bond}.csv')
    pass


# -------------------------------------------------------
def get_currency_cross(quote):
    check_folder(currency_path)
    df = iv.currency_crosses.get_currency_cross_historical_data(
        currency_cross=quote, from_date=starttime, to_date=today)
    df = df.iloc[:, :-1]
    # can we add pct change column
    quote = replace_specchar(quote, '/', '')
    df.to_csv(currency_path + f'/{quote}.csv')
    pass


# -------------------------------------------------------
# COMMON--------------------------------
def get_wti():
    get_commodities('Crude Oil WTI')
    pass


# COMMON--------------------------------
def get_brent():
    get_commodities('Brent Oil')
    pass


# -------------------------------------------------------
# COMMON--------------------------------
def get_goldprice():
    get_commodities('Gold')
    pass


# -------------------------------------------------------
# Chỉ số sợ hãi Volatility Index: JPY, CHF tăng giá
# dùng trong carry trade và stock predict
# < 20 -> ít sợ, > 40 -> sợ nhiều + các mô hình giá
# COMMON--------------------------------
def get_volatility():
    get_indices('S&P 500 VIX', 'united states')
    pass


# ----------------Commondity index-------------------------
# https://www.investing.com/indices/thomson-reuters---jefferies-crb
def get_crb():
    get_indices('TR/CC CRB', 'world')
    pass


# ----------------Copper-------------------------
def get_copper():
    get_commodities('Copper')
    pass


# ----------------Silver-------------------------
def get_silver():
    get_commodities('Silver')
    pass


# ----------------Natural Gas-------------------------
def get_gas():
    get_commodities('Natural Gas')
    pass


# ----------------Platinum-------------------------
def get_platinum():
    get_commodities('Platinum')
    pass


# ----------------Iron ore ---------------
#  https://www.investing.com/commodities/iron-ore-62-cfr-futures-streaming-chart
def get_ironore():
    # get_commodities('Iron ore')
    pass
