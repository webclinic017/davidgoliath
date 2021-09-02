# skewness python
# https://www.google.com/search?q=skewness+python&oq=Skewness+python&aqs=chrome.0.0l4j0i22i30l6.3988j0j4&sourceid=chrome&ie=UTF-8
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html
# https://www.geeksforgeeks.org/scipy-stats-skew-python/

''' Statistical functions
In simple words, skewness is the measure of how much the
probability distribution of a random variable deviates
from the normal distribution.
# https://www.investopedia.com/terms/s/skewness.asp

skewness = 0 : normally distributed.
skewness > 0 : more weight in the left tail of the distribution.
skewness < 0 : more weight in the right tail of the distribution.

'''
# part 1 ----------------------------------
import numpy as np
from scipy.stats import skew
import pandas as pd

arr = np.random.randint(1, 10, 10)
arr = list(arr)
# print(arr)
# # more weight in the right when skew>0,
# # determine skew close enough to zero
# print(skew(arr))
# print(skew([1, 2, 3, 4, 5]))

# part 2 ----------------------------------
# df = pd.read_csv('Data/nba.csv')
df = pd.read_csv('Data/XAUNZD_Daily.csv')

# print(df.tail())

# skewness along the index axis
print(df.skew(axis=0, skipna=True))

# skewness of the data over the column axis
# print(df.skew(axis=1, skipna=True))
