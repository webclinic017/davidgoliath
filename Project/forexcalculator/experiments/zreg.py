import pandas as pd
import numpy as np
# import warnings
import matplotlib.pyplot as plt

from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, neighbors


from pickle import load, dump
from collections import Counter
from datetime import date

style.use('fivethirtyeight')

if __name__ == "__main__":
    tmp = [1, 2, 2, 3, 4, 5, 6, 7]
    print(tmp[:-2])  # shift df tuong tu
'''
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

# treated NaN as an outlier feature
df.fillna(value=-99999, inplace=True)

# drop columns
df.drop('Currency', axis=1, inplace=True)

# Make datetimeIndex
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# how to create create_dataset
'''
