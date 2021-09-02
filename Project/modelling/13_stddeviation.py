# standard deviation python
# https://www.google.com/search?q=standard+deviation+python&oq=Standard+deviation+python&aqs=chrome.0.0l10.1896j0j7&sourceid=chrome&ie=UTF-8

'''
Standard deviation measures the spread of a data distribution.
The more spread out a data distribution is, the greater its
standard deviation. Interestingly, standard deviation cannot be negative.
A standard deviation close to 0 indicates that the data points tend to
be close to the mean
'''

import numpy as np
from statistics import stdev

a = np.array([[1, 2], [3, 4]])
# print(np.std(a))
# print(np.std(a, ddof=1))
# print(np.std(a, axis=0))
# print(np.std(a, axis=1))

a = [14, 8, 11, 10, 7, 9, 10, 11, 10, 15, 5, 10]
# print(stdev(a))

a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
# print(a)
# print(np.std(a, dtype=np.float64))

a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
# print(np.std(a, ddof=1, dtype=np.float64))
