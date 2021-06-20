# median statistics python
# https://www.google.com/search?q=median+statistics+python&oq=median+statistics+python&aqs=chrome..69i57j0i22i30l2.5214j0j4&sourceid=chrome&ie=UTF-8

'''
Mean, median, and mode are different measures of center
 in a numerical data set. They each try to summarize a
 dataset with a single number to represent a "typical" (điển hình)
 data point from the dataset.
'''

import numpy as np
from statistics import median

# sampling way 1
arr = np.random.randint(1, 10, 10)
print(np.median(arr))

arr = list(arr)
print(sorted(arr))
print(median(arr))
