import investpy
import datetime
import os
import pandas as pd
import pickle

pd.options.mode.chained_assignment = None
# no need to scrape data if you can list it through investing.com
# neu ma doc ten quotes tu file thi sao???

# https://www.investing.com/indices/indices-futures
stock_indices = []
# need save to pickle
bonds = ['Canada 10Y', 'U.S. 10Y', 'U.K. 10Y', 'Switzerland 10Y',
         'New Zealand 10Y', 'Australia 10Y', 'Japan 10Y', 'Germany 10Y']

# combination
main_cur = ['USD', 'EUR', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD']

pairs = ['XAU/USD', 'EUR/USD', 'GBP/USD', 'AUD/USD',
         'NZD/USD', 'USD/JPY', 'USD/CHF', 'USD/CAD']
commodities = ['Gold', 'Copper', 'Silver', 'Crude Oil WTI',
               'Brent Oil', 'Natural Gas', 'Platinum']
softs = []
meats = []
grains = []

bonds_path = 'Data/bond_dfs'
pairs_path = 'Data/fx_dfs'
commodities_path = 'Data/commo_dfs'


checklist = ['pairs', 'bonds', 'commodities']
# coins_path = ''
# to_date ~ up to date

# ###################-----Crypto------#########################
# ------------dump, load data-----------------------------------
# df = investpy.crypto.get_cryptos()
# df.drop(columns=['currency', 'name'], inplace=True)
# # df.set_index('symbol', inplace=True)
# tmp = df['symbol'].to_list()
# # print(df.head())
# with open("Data/crypto_list.pickle", "wb") as f:
#     pickle.dump(tmp, f)

# # get only top 100
# with open("Data/crypto_list.pickle", "rb") as f:
#     tickers = pickle.load(f)

# for ticker in tickers:
#     print(ticker)


# #### get_bond_historical_data improve : Weekly, Monthly ####


def get_bond_historical_data():
    if not os.path.exists(bonds_path):
        os.makedirs(bonds_path)
    for bond in bonds:
        print(bond)
        if not os.path.exists(bonds_path + '/{}.csv'.format(bond)):
            # datetime need const
            df = investpy.get_bond_historical_data(
                bond=bond, from_date='01/01/2010', to_date='15/05/2021')
            df.to_csv(bonds_path + '/{}.csv'.format(bond))
        else:
            print('Already have {}'.format(bond))

# ################ get forex historical_data ##################


def get_pair_historical_data():
    if not os.path.exists(pairs_path):
        os.makedirs(pairs_path)
    for pair in pairs:
        print(pair)
        # # consider below
        if '/' in pair:
            pair_name = pair.replace("/", "")
        if not os.path.exists(pairs_path + '/{}.csv'.format(pair_name)):
            df = investpy.get_currency_cross_historical_data(
                currency_cross=pair,
                from_date='01/01/2010', to_date='15/05/2021')
            df.to_csv(pairs_path + '/{}.csv'.format(pair_name))
        else:
            print('Already have {}'.format(pair_name))

# ################ get_commodity_historical_data ##################


def get_commodity_historical_data():
    if not os.path.exists(commodities_path):
        os.makedirs(commodities_path)
    for commodity in commodities:
        print(commodity)
        if not os.path.exists(commodities_path + '/{}.csv'.format(commodity)):
            df = investpy.commodities.get_commodity_historical_data(
                commodity=commodity,
                from_date='01/01/2010', to_date='15/05/2021')
            df.to_csv(commodities_path + '/{}.csv'.format(commodity))
        else:
            print('Already have {}'.format(commodity))

# ################ combine_data for analysis ##################


def process_bondyeilddata():
    # read bonds data from bonds_path

    # read GBPUSD data

    # combine them into a csv
    pass


def process_fxdata(filename, is_check_again=True):
    # filename = 'pairs_joined_closes'
    # re calculate divide data then write to file
    if is_check_again:
        df = pd.read_csv(pairs_path + '/{}.csv'.format(filename))
        df['EUR/USD'] = df['XAU/USD'] / df['EUR/USD']
        df['GBP/USD'] = df['XAU/USD'] / df['GBP/USD']
        df['AUD/USD'] = df['XAU/USD'] / df['AUD/USD']
        df['NZD/USD'] = df['XAU/USD'] / df['NZD/USD']
        df['USD/JPY'] = df['XAU/USD'] * df['USD/JPY']
        df['USD/CHF'] = df['XAU/USD'] * df['USD/CHF']
        df['USD/CAD'] = df['XAU/USD'] * df['USD/CAD']
        df.set_index('Date', inplace=True)
        df.to_csv(pairs_path + '/{}.csv'.format(filename))
    else:
        df = pd.read_csv(pairs_path + '/{}.csv'.format(filename))
        # # processing
        size = len(df.index)
        for i in range(1, size):
            for column in df:
                if(not isinstance(df[column].iloc[i], str)):
                    df[column].iloc[i] /= df[column].iloc[0]
                    df[column].iloc[i] *= 100
        for column in df:
            if '/' in column:
                df[column].iloc[0] = 100
        # rename column: dict
        df.rename(columns={'EUR/USD': 'XAU/EUR', 'GBP/USD': 'XAU/GBP',
                           'AUD/USD': 'XAU/AUD', 'NZD/USD': 'XAU/NZD',
                           'USD/JPY': 'XAU/JPY', 'USD/CHF': 'XAU/CHF',
                           'USD/CAD': 'XAU/CAD'}, inplace=True)
        df.set_index('Date', inplace=True)
        # write data
        df.to_csv(pairs_path + '/{}.csv'.format(filename))


# process_fxdata('pairs_joined_closes', False)


def plotting():
    df = pd.read_csv(pairs_path + '/{}.csv'.format(filename))

    pass
    # read combined data

    # tinh thuong so cua cap XAUUSD so vs Cac cap xxxUSD
    # tinh thuong so cua tat ca cac ngay tiep theo so voi Gold
    # ngay dau tien la 100%


# ################ combine_data for analysis ##################


# Refactor code: value is anything that you want list[bond, pair, ...]
# now it is all pair, all bond or all...
# example: value = [UK bond, US bond, GBPUSD]
# find the correlation

def combine_data(value):
    if value is 'pairs':
        xdata = [pairs, pairs_path, ['Open', 'High', 'Low', 'Currency']]
    elif value is 'bonds':
        xdata = [bonds, bonds_path, ['Open', 'High', 'Low']]
    else:
        xdata = [commodities, commodities_path, [
            'Open', 'High', 'Low', 'Volume', 'Currency']]
    main_df = pd.DataFrame()
    for count, item in enumerate(xdata[0]):
        tmp = item if '/' not in item else item.replace('/', '')
        df = pd.read_csv(xdata[1] + '/{}.csv'.format(tmp))
        df.set_index('Date', inplace=True)
        df.rename(columns={'Close': item}, inplace=True)
        # what purpose of 1
        df.drop(xdata[2], 1, inplace=True)
        main_df = df if main_df.empty else main_df.join(df, how='outer')
        print('{} and {}'.format(count, item))
    main_df.dropna(axis=0, how='any', inplace=True)
    main_df.to_csv(xdata[1] + '/' + value + '_joined_closes.csv')


# for itemlist in checklist:
#     combine_data(itemlist)
# ############## -----get_bond_spreads------ #################
# https://www.investing.com/rates-bonds/government-bond-spreads



# ############## -----trade balance------ #################


