import pandas as pd
import quandl
import os
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
quandl.ApiConfig.api_key = 'isu4pbfFzpfUnowC-k-R'

# rate - yeild - tresure
tickers = {'RBA': ['AUD', 'F13_FOOIRATCR'],  # AUD
           'OECD': ['NZD', 'KEI_IR3TIB01_NZL_ST_Q'],  # NZD unoffical
           'BOC': ['CAD', 'CORRA'],  # CAD
           'BUNDESBANK': ['EUR', 'BBK01_SU0202'],  # EURO ZONE
           'FRED': ['USD', 'FEDFUNDS'],  # USD
           'BOE': ['GBP', 'IUDBEDR'],  # GBP
           'BCB': ['JPY', '17903'],  # JPY
           'SNB': ['CHF', 'SNBOFFZISA']  # CHF
           }

# example:
# quandl.get('RBA/A03_4', start_date='2023-05-12', end_date='2023-05-12')

rate_path = 'data/'


def save_quote(path, quote, name, item):
    if not os.path.exists(path):
        os.makedirs(path)
    print(quote + name)
    df = quandl.get(f'{quote}/{item}',
                    start_date="2001-12-31", end_date="2005-12-31")
    # print(df.head())
    df.to_csv(f'{path}{name}_rate.csv')


for k, v in tickers.items():
    # for rate
    save_quote(rate_path, k, v[0], v[1])
    # save_quote(inflation_path, v[1])
