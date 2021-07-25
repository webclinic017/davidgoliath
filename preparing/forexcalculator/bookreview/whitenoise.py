'''
+ create white noise time series
- reference frame
- example plot
- statistical test
# create list gauss()
# draw gauss dist with mean 0 std 1
'''
import pandas as pd
from pandas.plotting import autocorrelation_plot
import random as rd
import matplotlib.pyplot as plt

# seed random number generator
rd.seed(1)

# create white noise series
series = [rd.gauss(0.0, 1.0) for i in range(1000)]
df = pd.DataFrame(series)

# summary stats: mean~0, std~1
print(df.describe())

# # line plot
# df.plot(color='red')
# # how to set legend and title
# plt.legend(title="Gauss df")
# plt.title("White noise summary")

# # histogram plot
# df.hist()

# autocorrelation
autocorrelation_plot(df)
plt.show()
