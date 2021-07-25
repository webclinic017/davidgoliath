import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.linear_model import LinearRegression
import numpy as np


def parser(x):
    return dt.datetime.strptime('190'+x, '%Y-%m')


df = pd.read_csv('data/shampoo.csv', header=0,
                 parse_dates=[0], index_col=0,
                 squeeze=True, date_parser=parser)

# ----------------------------------------------------------
'''
# This approach works well for data with a linear trend
# for quadratic trend -> need second level of differencing
diff = []
for i in range(1, len(df)):
    diff.append(df.values[i]-df.values[i-1])
# print(diff)
plt.plot(diff)
plt.show()
'''
# ----------------------------------------------------------
# fit linear model
X = [i for i in range(0, len(df))]
X = np.reshape(X, (len(X), 1))
y = df.values
model = LinearRegression()
model.fit(X, y)

# calc trend
trend = model.predict(X)

# plot trend
plt.plot(y, color='red')
plt.plot(trend, color='green')
# plt.show()

# detrend: original dataset subtract trend to get detrended data
detrend = [y[i]-trend[i] for i in range(0, len(df))]

# plot detrend
plt.plot(detrend, color='blue')
plt.show()
