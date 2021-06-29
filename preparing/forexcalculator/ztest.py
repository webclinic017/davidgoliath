'''
# https://www.youtube.com/watch?v=GFSiL6zEZF0&ab_channel=NeuralNine
'''
import pandas as pd
import datetime as dt
import pandas_datareader as web

from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.layers import Dense, Dropout, LSTM
# from tensorflow.keras.models import Sequential

quote = 'USD'
base = 'BTC'

# start = dt.datetime(2016, 1, 1)
# end = dt.datetime.now()
# data = web.DataReader(f'{base}-{quote}', 'yahoo', start, end)
# data.to_csv(f'fred/data/{base}-{quote}.csv')

data = pd.read_csv(f'fred/data/{base}-{quote}.csv')
# print(data.tail())

# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
