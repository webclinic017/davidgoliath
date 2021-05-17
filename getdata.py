import bs4 as bs
import pickle
import requests
import os
import pandas as pd
import pandas_datareader as web
from enum import Enum
import datetime as dt


pairs = ['GBPUSD=X', 'EURUSD=X', 'AUDUSD=X', 'NZDUSD=X',
         'USDCHF=X', 'USDCAD=X', 'JPY=X', 'GC=F', 'CL=F']
indexs = ['DXY', 'US10Y']
bonds = ['AU10Y', 'CA10Y', 'DE10Y', 'GB10Y',
         'JP10Y', 'NZ10Y', 'SW10Y', 'US10Y']

tmp_path = 'Data/fx_dfs'
# def save_mywatchlist():
#     resp = requests.get('https://finance.yahoo.com/portfolio/p_0/view/v1')
#     # parse data
#     soup = bs.BeautifulSoup(resp.text, 'lxml')
#     with open('Webhtml.txt', mode='wt', encoding='utf-8') as file:
#         file.write(str(soup))
#     # table = soup.find('table', {'class': 'W(100%)'})
#     # print(table)


def get_data_from_yahoo(reload_mywatchlist=False):

    # if reload_mywatchlist:
    #     tickers = save_mywatchlist()
    # else:
    #     with open("Data/save_mywatchlist.pickle", "rb") as f:
    #         tickers = pickle.load(f)

    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2021, 5, 11)

    for ticker in pairs:
        print(ticker)
        # # consider below
        # if '.' in ticker:
        #     ticker = ticker.replace(".", "-")
        if not os.path.exists(tmp_path + '/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv(tmp_path + '/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


def combine_data():
    main_df = pd.DataFrame()
    for count, ticker in enumerate(pairs):
        df = pd.read_csv(tmp_path + '/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
        print('{} and {}'.format(count, ticker))
    main_df.dropna(axis=0, how='any', inplace=True)
    main_df.to_csv('Data/pairs_joined_closes.csv')


def visualize_data():
    df = pd.read_csv('Data/pairs_joined_closes.csv')
    df.set_index('Date', inplace=True)
    print(df.head())
    pass


# visualize_data()
combine_data()
# get_data_from_yahoo()
