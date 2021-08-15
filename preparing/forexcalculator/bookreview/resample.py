import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


# consider data source for apply parse date or not
def parser(x):
    return dt.datetime.strptime('190'+x, '%Y-%m')


df = pd.read_csv('data/shampoo.csv', header=0,
                 parse_dates=[0], index_col=0,
                 squeeze=True, date_parser=parser)
print(df.tail())
'''
fig = plt.figure(figsize=(12, 7))
layout = (2, 2)
plt.tight_layout()
'''
# ---------------------------- Code upsampling ----------------------------
'''
upsampled = df.resample('D').mean()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
# interpolated = upsampled.interpolate(method='linear')  # another method

# số hạng trong đa thức
interpolated = upsampled.interpolate(
    method='spline', order=2)  # polynomial: more curve
interpolated.plot()
plt.show()
'''

# ---------------------------- Code downsampling ----------------------------
'''
resample = df.resample('Q')
# resample = df.resample('Y')
quarterly_mean = resample.mean()
# print(quarterly_mean.tail())
quarterly_mean.plot()
plt.show()
'''
# ----------------------------
'''
resample = df.resample('A')
yearly_mean = resample.sum()
# resample = df.resample('Y')
# yearly_mean = resample.mean()
print(yearly_mean)
yearly_mean.plot()
plt.show()
'''
