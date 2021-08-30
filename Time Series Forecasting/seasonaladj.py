import matplotlib.pyplot as plt
import pandas as pd

series = pd.read_csv('data/daily-min-temperatures.csv', header=0)
series['Date'] = pd.to_datetime(series['Date'])
series.set_index('Date', inplace=True)

'''
# ------ Deseasonalize dataset ------
diff = []
days_in_year = 365
for i in range(days_in_year, len(series)):
    diff.append(series.values[i] - series.values[i-days_in_year])
plt.plot(diff)
'''
# -------------------------------------------------------------
# ------ Handle offsets time problem (365 vs 366-leaf year) ----
'''
# + consider dataset probably stable in a period (few weeks)
# + consider a month all temperatures stable
# + subtract last year average temperature(same calendar month)
# + resampling dataset to monthly average minimum temperature
'''
# -------------------- Code --------------------
'''
resample = series.resample('M')
monthly_mean = resample.mean()
print(monthly_mean.head(13))
monthly_mean.plot()
'''
# -------------------- differencing Code --------------------
'''
diff = []
months_in_year = 12
# # notice that dataframe can't access by index
# # need using .values to convert to numpy.ndarray
# print(type(monthly_mean.values))
for i in range(months_in_year, len(monthly_mean)):
    diff.append(monthly_mean.values[i] - monthly_mean.values[i-months_in_year])
plt.plot(diff)
'''
# ---- deseasonalized dataset using monthly data ----
'''
# handle leaf year offset days
# average from one week same date in the previous year
# multiple scales time: Day level/ weeks/ month/ quarter or season
'''
diff = []
days_in_year = 365
for i in range(days_in_year, len(series)):
    month_str = str(series.index[i].year-1)+'-'+str(series.index[i].month)
    month_mean_last_year = series[month_str].mean()
    diff.append(series.values[i]-month_mean_last_year)
plt.plot(diff)
plt.show()
