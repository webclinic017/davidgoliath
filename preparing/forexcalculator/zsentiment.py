# -------------------- default template ------------------
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import schedule

style.use('fivethirtyeight')
# import scipy as sp

if __name__ == "__main__":
    df = pd.DataFrame({"B": [0, 1, 2, np.nan, 4]})
    # print(df)
    df = df.expanding()
    print(df.values)
    pass
# ------------------ end default template -----------------
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
