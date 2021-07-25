import investpy as iv
from datetime import date


quotes = {'amzn': 'united states',
          'tsla': 'united states',
          'aapl': 'united states'}
from_d = '01/01/2020'
to_d = date.today().strftime("%d/%m/%Y")


def dl_quotes(loc='data/'):
    for quote, country in quotes.items():
        # print(quote, country)
        df = iv.stocks.get_stock_historical_data(quote, country, from_d, to_d)
        df.to_csv(loc+f'{quote}.csv')


dl_quotes('10_arma/data/')
