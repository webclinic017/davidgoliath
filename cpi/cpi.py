import pandas as pd
import quandl
import os
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'
tickers = {'USD': ['CPI_USA', 'INFLATION_USA'],
           'GBP': ['CPI_GBR', 'INFLATION_GBR'],
           'CHF': ['CPI_CHE', 'INFLATION_CHE'],
           'EUR': ['CPI_EUR', 'INFLATION_EUR'],
           'GER': ['CPI_DEU', 'INFLATION_DEU'],
           'NZD': ['CPI_NZL', 'INFLATION_NZL'],
           'JPY': ['CPI_JPN', 'INFLATION_JPN'],
           'CAD': ['CPI_CAN', 'INFLATION_CAN'],
           'AUD': ['CPI_AUS', 'INFLATION_AUS']
           }
cpi_path = 'data/cpi/'
inflation_path = 'data/inflation/'


def save_quote(path, item):
    if not os.path.exists(path):
        os.makedirs(path)

    df = quandl.get(f'RATEINF/{item}')
    df.to_csv(f'{path}{item}.csv')


for v in tickers.values():
    # for cpi
    save_quote(cpi_path, v[0])
    # for inflation
    save_quote(inflation_path, v[1])
