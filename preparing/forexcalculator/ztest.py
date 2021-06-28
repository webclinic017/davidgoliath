# import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

# ------------------------------------------------------

# tmp = [1, 5, 6, 2, 3, 4]
# print(len(tmp[3:]))
# print(tmp[3:])

# --------------------------------------------------
'''
https://hvplot.holoviz.org/user_guide/Plotting.html
'''
import numpy as np
import hvplot.pandas  # noqa
import hvplot.dask  # noqa
from hvplot.sample_data import us_crime, airline_flights

crime = us_crime.read()
# print(type(crime))
# print(crime.head())
flights = airline_flights.to_dask().persist()
# print(type(flights))
# print(flights.head())
